# from rest_framework import viewsets, parsers, permissions
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# from oauth import serializers
# from oauth.base.permissions import IsAuthorOrAdmin
from apps.oauth.serializers import RegistrationSerializer


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


# class UserView(viewsets.ModelViewSet):
#     """
#     CRUD user
#     """
#     parsers_classes = (parsers.MultiPartParser,)
#     serializer_class = serializers.UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return self.request.user
#
#     def get_object(self):
#         return self.get_queryset()
#
#
# class SocialLinkView(viewsets.ModelViewSet):
#     """
#     CRUD social links
#     """
#     serializer_class = serializers.SocialLinkSerializer
#     permission_classes = [IsAuthorOrAdmin]
#
#     def get_queryset(self):
#         return self.request.user.social_links.all()
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
