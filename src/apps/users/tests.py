from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.test import TestCase


if TYPE_CHECKING:
    from .models import User


class UserManagersTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.user_model: type[User] = get_user_model()

    def test_create_user(self) -> None:
        user: User = self.user_model.objects.create_user(email="user@user.com", password="password")

        self.assertEqual("user@user.com", user.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            self.user_model.objects.create_user()

        with self.assertRaises(TypeError):
            self.user_model.objects.create_user(email="")

        with self.assertRaises(ValueError):
            self.user_model.objects.create_user(email="", password="password")

    def test_create_admin(self) -> None:
        admin: User = self.user_model.objects.create_superuser(email="admin@user.com", password="password")

        self.assertEqual("admin@user.com", admin.email)
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

        with self.assertRaises(ValueError):
            self.user_model.objects.create_superuser(email="admin@user.com", password="password", is_superuser=False)
