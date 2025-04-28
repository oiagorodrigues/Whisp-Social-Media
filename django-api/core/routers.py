from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet

router = routers.SimpleRouter()

# Auth routes
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")

# User routes
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
]
