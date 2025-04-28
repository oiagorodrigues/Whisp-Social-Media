from rest_framework import routers
from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()

# User routes

router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
]
