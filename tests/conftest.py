import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.oauth.models import AuthUser


@pytest.fixture
def api_client():
    return APIClient


@pytest.mark.django_db
@pytest.fixture
def admin_user():
    return AuthUser.objects.create_superuser(
        username="questioner",
        email="admin@questioner.com",
        password='password',
    )


@pytest.mark.django_db
@pytest.fixture
def user1():
    return get_user_model().objects.create(
        username="user1", email="user1@questioner.com", is_staff=False
    )
