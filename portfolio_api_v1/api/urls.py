from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from portfolio_api_v1.api.views import ProjectsViewSet
from portfolio_api_v1.api.views import SkillViewSet

router = DefaultRouter()
router.register("skills", SkillViewSet)
router.register("projects", ProjectsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
