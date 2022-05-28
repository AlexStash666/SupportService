from model_bakery import baker
import factory
import json
import pytest

from apps.oauth.models import AuthUser
from apps.support.models import Answer, Ticket
from tests.tests_app_support.factories import TicketFactory

pytestmark = pytest.mark.django_db


class TestTicketsEndpoints:
    endpoint = '/api/v1/tickets/'

    def test_list(self, api_client, admin_user):
        api_client().force_authenticate(user=admin_user)
        baker.make(Ticket, user=admin_user)
        response = api_client().get(path=self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_create(self, api_client, admin_user):
        ticket = baker.prepare(Ticket, user=admin_user)
        expected_json = {
            'title': ticket.title,
            'status': ticket.status,
            'text': ticket.text,
        }

        response = api_client().post(
            self.endpoint,
            data=expected_json,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json
