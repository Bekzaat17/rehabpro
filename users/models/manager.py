# users/models/manager.py
from django.contrib.auth.models import BaseUserManager
from .enums import UserRole

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role=UserRole.CONSULTANT, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, role=UserRole.ADMIN, **extra_fields)