from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    RegisterView,
    TaskViewSet
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegisterView.as_view(), name='register'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Tasks
    path("tasks/", TaskViewSet.as_view({"post": "create", "get": "list"})),
    path("tasks/<int:pk>", TaskViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]
