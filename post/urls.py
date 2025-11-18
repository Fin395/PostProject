from django.urls import path
from rest_framework.routers import DefaultRouter
from post.apps import PostConfig
from post.views import PostViewSet

# from materials.views import (
#     CourseViewSet,
#     LessonCreateAPIView,
#     LessonDestroyAPIView,
#     LessonListAPIView,
#     LessonRetrieveAPIView,
#     LessonUpdateAPIView,
#     SubscriptionAPIView,
# )

app_name = PostConfig.name

router = DefaultRouter()
router.register(r"post", PostViewSet, basename="post")
urlpatterns = [
    # path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    # path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    # path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    # path(
    #     "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"
    # ),
    # path(
    #     "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"
    # ),
    # path("subs/create/", SubscriptionAPIView.as_view(), name="subs-create"),
] + router.urls
