from django.core.validators import FileExtensionValidator
from django.db import models
from apps.base.services import get_path_upload_screenshot, validate_size_image, delete_old_file
from apps.oauth.models import AuthUser
from apps.support.models.ticket import Ticket


class Answer(models.Model):
    """
    Request response model
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='users_answers')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='answers', verbose_name='Запрос')
    text = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    user_of_likes = models.ManyToManyField(AuthUser, related_name='likes_of_tickets', blank=True)
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.SET_NULL, blank=True, null=True,
    )
    screenshot = models.ImageField(
        blank=True,
        null=True,
        upload_to=get_path_upload_screenshot,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image, delete_old_file]
    )

    def __str__(self):
        return f'{self.ticket} - {self.user}'
