from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserProjectListView

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')

project_create = ProjectViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('',include(router.urls)),
    path('clients/<int:client_pk>/projects/', project_create, name='create-client-project'),
    path('projects/', UserProjectListView.as_view(), name='user-projects'),
]