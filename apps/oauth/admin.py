from django.contrib import admin
from apps.oauth.models import AuthUser, SocialLink


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'avatar', 'is_staff')
    list_display_links = ('email', 'username')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'link')
