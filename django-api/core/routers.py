from rest_framework import routers
from core.post.viewsets import PostViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet

router = routers.SimpleRouter()

# Auth routes
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

# User routes
router.register(r"users", UserViewSet, basename="user")

# Post routes
router.register(r"posts", PostViewSet, basename="post")

urlpatterns = [
    *router.urls,
]
