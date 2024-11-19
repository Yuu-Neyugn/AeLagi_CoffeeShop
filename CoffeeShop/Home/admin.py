from django.contrib import admin
from .models import AboutUs, OurTeam

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "image")
    list_display_links = ("id", "title", "content", "image")
admin.site.register(AboutUs)

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ("id", "memberName", "position", "avatar")
    list_display_links = ("id", "memberName", "position", "avatar")
admin.site.register(OurTeam)