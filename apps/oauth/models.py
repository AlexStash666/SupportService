from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.base.services import (
    get_path_upload_avatar,
    validate_size_image,
    delete_old_file
)


class AuthUserManager(BaseUserManager):
    """
    Manager for a custom user
    """
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class AuthUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image, delete_old_file]
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AuthUserManager()

    def __str__(self):
        return f'{self.email} {self.username} - staff {self.is_staff}'


class SocialLink(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=150)

    def __str__(self):
        return f'{self.user}'
