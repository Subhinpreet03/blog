from django.urls import path, re_path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, login, signup, test_token

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    re_path(r'^login/', login),
    re_path(r'^signup/', signup),
    re_path(r'^test_token/', test_token),
]
