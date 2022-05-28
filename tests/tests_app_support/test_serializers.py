import pytest
import factory

from apps.support.serializers import TicketListSerializer, TicketDetailSerializer
from tests.tests_app_support.factories import TicketFactory


pytestmark = [pytest.mark.unit, pytest.mark.django_db]


class TestTicketListSerializer:
    def test_serialize_model(self):
        ticket = TicketFactory.build()
        serializer = TicketListSerializer(ticket)

        assert serializer.data

    def test_serialized_data(self, admin_user):
        valid_serialized_data = factory.build(
            dict,
            user=admin_user,
            FACTORY_CLASS=TicketFactory
        )

        serializer = TicketListSerializer(data=valid_serialized_data)
        assert serializer.is_valid(raise_exception=True)
        assert serializer.errors == {}


class TestTicketDetailSerializer:
    def test_serialize_model(self):
        ticket = TicketFactory.build()
        serializer = TicketDetailSerializer(ticket)

        assert serializer.data

    def test_serialized_data(self, mocker, admin_user):
        valid_serialized_data = factory.build(
            dict,
            user=admin_user,
            FACTORY_CLASS=TicketFactory
        )

        serializer = TicketDetailSerializer(data=valid_serialized_data)
        assert serializer.is_valid(raise_exception=True)
        assert serializer.errors == {}
