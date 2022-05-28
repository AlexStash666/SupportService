from django.core.validators import FileExtensionValidator
from django.db import models
from apps.base.services import get_path_upload_screenshot, validate_size_image, delete_old_file
from apps.oauth.models import AuthUser


class Ticket(models.Model):
    """
    Support Request Model
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=80)

    class Status(models.TextChoices):
        Solved = 'solved',
        Unresolved = 'unresolved',
        Frozen = 'frozen'

    status = models.CharField(choices=Status.choices, default='Unresolved', max_length=100)
    text = models.TextField(max_length=1000)
    screenshot = models.ImageField(
        upload_to=get_path_upload_screenshot,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image, delete_old_file]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.title} - {self.status}'

    def get_answer(self):
        return self.answers_set.filter(parent__isnull=True)
