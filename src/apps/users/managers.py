from typing import TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager


if TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **kwargs: dict) -> "User":
        if not email:
            raise ValueError("Email must be set")

        normalized_email = self.normalize_email(email)

        user: User = self.model(email=normalized_email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **kwargs: dict) -> "User":
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Admin must have staff=True")

        if kwargs.get("is_superuser") is not True:
            raise ValueError("Admin must have admin=True")

        return self.create_user(email, password, **kwargs)
