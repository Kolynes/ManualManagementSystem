from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class LecturerModelManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('Email must be set!')
        else:
            user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class LecturerModel(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256, unique=True)
    phone = models.CharField(max_length=15)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FILEDS = ["first_name", "last_name", "phone"]

    objects = LecturerModelManager()

    @property
    def dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "id": self.id
        }

