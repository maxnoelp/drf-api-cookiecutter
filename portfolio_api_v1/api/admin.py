from django.contrib import admin

from portfolio_api_v1.api.models import Projects
from portfolio_api_v1.api.models import Skill

admin.site.register(Projects)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "teaser",
        "coding_language",
        "coding_lang_icon",
        "description",
        "images",
        "created_at",
        "updated_at",
        "published",
    )
    list_filter = ("created_at", "updated_at", "published")
    search_fields = ("title", "description")
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Skill)
