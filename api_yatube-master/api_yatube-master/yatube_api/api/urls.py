from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()
router.register('posts', PostViewSet,
                basename='posts')
router.register('groups', GroupViewSet,
                basename='groups')
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view(
             {'get': 'list',
              'post': 'create'}),
         name='post-comments'),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view(
             {'get': 'retrieve',
              'put': 'update',
              'patch': 'partial_update',
              'delete': 'destroy'}),
         name='post-comment-detail'),
]
