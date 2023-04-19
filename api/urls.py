from django.urls import path
from api.views import PostListView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_api'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail_api'),

]