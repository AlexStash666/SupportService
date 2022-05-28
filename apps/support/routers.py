from rest_framework import routers
from apps.support.api import TicketViewSet, AnswerViewSet

support_router = routers.SimpleRouter()
support_router.register(r'tickets', TicketViewSet, basename='ticket')
support_router.register(r'answers', AnswerViewSet, basename='answer')

urlpatterns = support_router.urls
