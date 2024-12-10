from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'departments', DepartmentViewSet, basename='apidepartment')

urlpatterns = [
    path('', include(router.urls)),
]
