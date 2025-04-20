from rest_framework import serializers

from portfolio_api_v1.api.models import Projects
from portfolio_api_v1.api.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "bs_icon", "image"]


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = [
            "title",
            "teaser",
            "coding_language",
            "coding_lang_icon",
            "description",
            "images",
            "created_at",
            "updated_at",
            "published",
        ]
