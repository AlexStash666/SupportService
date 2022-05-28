from django.contrib import admin
from apps.support.models import Ticket, Answer


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'title')
    list_display_links = ('user',)
    list_filter = ('status',)
    search_fields = ('title', 'status')


@admin.register(Answer)
class TicketAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ticket')
    list_display_links = ('user',)
