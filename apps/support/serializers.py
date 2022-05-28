from rest_framework import serializers
from ..support.models.answer import Answer
from ..support.models.ticket import Ticket
from ..oauth.serializers import UserSerializer as my_user


class FilterAnswerListSerializer(serializers.ListSerializer):
    """
    Output only parent responses
    """

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """
    Recursive output of child responses
    """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        # serializer = AnswerSerializer(value, context=self.context)
        return serializer.data


class AnswerListSerializer(serializers.ModelSerializer):
    """
    Answer serializer
    """
    children = RecursiveSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    #  user = my_user(read_only=True)
    ticket = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        list_serializer_class = FilterAnswerListSerializer
        model = Answer
        fields = ('id', 'user', 'ticket', 'text', 'children', 'create_at')


class TicketDetailSerializer(serializers.ModelSerializer):
    """
    Ticket detail info
    """
    answers = AnswerListSerializer(many=True, read_only=True, required=False)
    # user = my_user(read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'user', 'title', 'status', 'text', 'screenshot', 'create_at', 'answers')


class AnswerDetailSerializer(serializers.ModelSerializer):
    """
    Answer detail serializer
    """
    children = RecursiveSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    ticket = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        list_serializer_class = FilterAnswerListSerializer
        model = Answer
        fields = ('id', 'user', 'ticket', 'text', 'children', 'screenshot', 'create_at')


class TicketListSerializer(serializers.ModelSerializer):
    """
    List of requests
    """
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    answers = AnswerListSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Ticket
        fields = ('id', 'user', 'title', 'status', 'text', 'answers')
