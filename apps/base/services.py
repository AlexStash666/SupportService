import os

from rest_framework.exceptions import ValidationError
from django.core.mail import send_mail


def get_path_upload_avatar(instance, file):
    """
    Building a path to file media/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def get_path_upload_screenshot(instance, file):
    """
    Building a path to media/screenshot/ticket_id/screen.png
    """
    return f'screenshot/ticket_{instance.id}/{file}'


def validate_size_image(file_obj):
    """
    Checking file size
    """
    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:
        raise ValidationError(f"Max image size {mb_limit}MB")


def delete_old_file(path_file):
    """
    Deleting an old file
    """
    if os.path.exists(str(path_file)):
        os.remove(str(path_file))


def send(user_email, topic, message):
    """
     Sending a message to the mail
    """
    send_mail(
        f'{topic}',
        f'{message}',
        'alexoskarrrr@gmail.com',
        [user_email],
        fail_silently=False,
    )
