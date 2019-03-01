from rest_framework.routers import DefaultRouter
from proapp.views import ReportViewSet
from django.conf.urls import url

router=DefaultRouter()
router.register(prefix='reportcard',viewset=ReportViewSet)
urlpatterns=router.urls