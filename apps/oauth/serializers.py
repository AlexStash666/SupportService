from django.template.defaulttags import now
from rest_framework import serializers
from apps.oauth.models import AuthUser, SocialLink


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serialization registration and creation of a new user.
    """
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = AuthUser
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return AuthUser.objects.create_user(**validated_data)


class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SocialLink
        fields = ('id', 'link')


class UserSerializer(serializers.ModelSerializer):
    """
    User detail serializer.
    """

    class Meta:
        social_links = SocialLinkSerializer(many=True)
        ref_name = "my_user"
        model = AuthUser
        fields = ('id', 'email', 'avatar', 'username', 'is_staff', 'tickets', 'answers', 'social_links')


