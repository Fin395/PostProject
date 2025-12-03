from rest_framework.routers import DefaultRouter

from post.apps import PostConfig
from post.views import CommentaryViewSet, PostViewSet

app_name = PostConfig.name

router = DefaultRouter()
router.register(r"post", PostViewSet, basename="post")
router.register(r"commentary", CommentaryViewSet, basename="commentary")

urlpatterns = [] + router.urls
