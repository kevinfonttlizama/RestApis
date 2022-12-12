from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """manager para perfiles de usuario """

    def create_user(self, email, name, password=None):
        """crear nuevo user profile """
        if not email:
            raise ValueError('Usuario debe tener un Email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


    





class userProfile(AbstractBaseUser,PermissionsMixin):
    """ Modelo Base de Datos para usarlo en el sistema """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """obtener nombre completo del usuario"""
        return self.name


    def get_short_name(self):
        """obtener nombre corto del usuario """
        return self.name


    def __str__(self):
        ''' retornar cadena representando nuestro usuario '''
        return self.email


class ProfileFeedItem(models.Model):
    """perfil de estatus update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.status_text

