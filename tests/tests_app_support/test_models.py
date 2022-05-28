import pytest
from model_bakery import baker

from apps.oauth.models import AuthUser
from apps.support.models import Answer
from tests.tests_app_support.factories import TicketFactory


@pytest.mark.django_db()
def test_create_ticket():
    user = baker.make(AuthUser)
    ticket = TicketFactory.build(user=user)
    assert ticket.title == 'ticket0'


@pytest.mark.django_db()
def test_create_answer(user1):
    answer = baker.make(Answer, user=user1)
    assert answer.user_id == user1.id


@pytest.mark.django_db()
def test_create_user(user1):
    assert user1.username == "user1"


@pytest.mark.django_db()
def test_create_admin_user(admin_user):
    assert admin_user.username == "questioner"
