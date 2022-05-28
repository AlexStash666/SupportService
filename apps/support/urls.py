from rest_framework import routers
from ..support.api import TicketViewSet, AnswerViewSet

router = routers.SimpleRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'answers', AnswerViewSet, basename='answer')
urlpatterns = router.urls
