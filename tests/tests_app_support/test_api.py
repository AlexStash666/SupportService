# import json
# import pytest
# from django_mock_queries.mocks import MockSet
# from model_bakery import baker
# from apps.oauth.models import AuthUser
# from apps.support.api import TicketViewSet
# from apps.support.models import Ticket
# # from tests.tests_app_support.factories import TicketFactory
#
# pytestmark = [pytest.mark.urls('config.urls'), pytest.mark.unit, pytest.mark.django_db]
#
#
# class TestTicketViewSet:
#     def test_list(self, mocker, rf, api_client):
#         # Arrange
#         url = '/api/v1/tickets/'
#         request = rf.get(url)
#         user = baker.make(AuthUser)
#         api_client().force_authenticate(user=user)
#         qs = MockSet(
#             baker.prepare(Ticket, _save_kwargs={'user_id': user.id}, _quantity=3)
#         )
#         view = TicketViewSet.as_view(
#             {'get': 'list'}
#         )
#         # Mocking
#         mocker.patch.object(
#             TicketViewSet, 'get_queryset', return_value=qs
#         )
#         # Act
#         response = view(request).render()
#         # Assert
#         assert response.status_code == 200
#         assert len(json.loads(response.content)) == 3
