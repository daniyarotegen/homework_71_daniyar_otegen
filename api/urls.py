from django.urls import path
from api.views.likes import LikeListView, LikeDetailView
from api.views.posts import PostListView, PostDetailView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_api'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail_api'),
    path('posts/<int:post_id>/add_like/', LikeDetailView.as_view(), name='add_like'),
    path('likes/', LikeListView.as_view(), name='likes_api'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like_detail_api'),

]