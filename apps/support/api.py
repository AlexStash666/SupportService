from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

from apps.base.permissions import IsAuthorOrAdmin
from apps.support.models.answer import Answer
from apps.support.models.ticket import Ticket
from apps.support.tasks import send_new_ticket_email, send_update_ticket_email, send_new_answer_email
from ..support.serializers import (
    TicketListSerializer,
    TicketDetailSerializer,
    AnswerListSerializer,
    AnswerDetailSerializer,
)


class TicketViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    A viewset that provides `CRUD` actions.
    The user sees only his own topics, but admin sees all.
    """
    permission_classes = (IsAuthorOrAdmin, AllowAny)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        send_new_ticket_email.delay('alexanderstashinski@gmail.com', serializer.data)

    def list(self, request, *args, **kwargs):
        if request.user.is_staff:
            queryset = Ticket.objects.all()
        else:
            queryset = Ticket.objects.filter(user=self.request.user)
        serializer = TicketListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        if request.user.is_staff:
            queryset = Ticket.objects.all()
        else:
            queryset = Ticket.objects.filter(user=self.request.user)
        ticket = get_object_or_404(queryset, pk=pk)
        serializer = TicketDetailSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(title=self.request.data['title'])
        send_update_ticket_email.delay('alexanderstashinski@gmail.com', str(ticket))

    def get_serializer_class(self):
        return TicketDetailSerializer

    def get_queryset(self):
        return Ticket.objects.all()

    @action(methods=('post',), detail=True, permission_classes=(IsAuthorOrAdmin,))
    def create_answer(self, request, pk=None):
        serializer = AnswerDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user, ticket_id=pk)
        headers = self.get_success_headers(serializer.data)
        send_new_answer_email.delay('alexanderstashinski@gmail.com', str(request.data))
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AnswerViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    A viewset that provides retrieve, update, destroy, list actions.
    """
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        return AnswerDetailSerializer

    def get_queryset(self):
        return Answer.objects.all()

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
        queryset = Answer.objects.all()
        serializer = AnswerListSerializer(queryset, many=True)
        return Response(serializer.data)
