from rest_framework import viewsets

from portfolio_api_v1.api.models import Projects
from portfolio_api_v1.api.models import Skill
from portfolio_api_v1.api.permissions import IsOwnerOrReadOnly
from portfolio_api_v1.api.serializers import ProjectsSerializer
from portfolio_api_v1.api.serializers import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsOwnerOrReadOnly]
