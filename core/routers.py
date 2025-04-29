from rest_framework_nested import routers

from core.post.viewsets import PostViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.comment.viewsets import CommentViewSet

router = routers.SimpleRouter()

# Auth routes
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

# User routes
router.register(r"users", UserViewSet, basename="user")

# Post routes
router.register(r"posts", PostViewSet, basename="post")

posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")

# Comment routes
posts_router.register(r"comments", CommentViewSet, basename="post-comment")

urlpatterns = [
    *router.urls,
    *posts_router.urls,
]
