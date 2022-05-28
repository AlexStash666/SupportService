from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.base.permissions import IsAuthorOrAdmin
from apps.oauth.serializers import RegistrationSerializer, SocialLinkSerializer


class RegistrationAPIView(APIView):
    """
    Allow all users (authenticated and not) to access this endpoint.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        auth_user = request.data.get('authUser', {})
        serializer = self.serializer_class(data=auth_user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SocialLinkViewSet(viewsets.ModelViewSet):
    """
    CRUD social links
    """
    serializer_class = SocialLinkSerializer
    permission_classes = (IsAuthorOrAdmin,)

    def get_queryset(self):
        return self.request.user.social_links.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
