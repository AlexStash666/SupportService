from rest_framework import routers
from apps.oauth.api import SocialLinkViewSet

oauth_router = routers.SimpleRouter()
oauth_router.register(r'social_links', SocialLinkViewSet, basename='social_link'),

urlpatterns = oauth_router.urls
