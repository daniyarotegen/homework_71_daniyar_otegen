from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import LikeSerializer
from instaclone.models import Like, Post


class LikeListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Like.objects.all()
        serializer = LikeSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeDetailView(APIView):
    def get_object(self, pk):
        try:
            return Like.objects.get(pk=pk)
        except Like.DoesNotExist:
            raise Http404

    def get(self, request, post_id=None, pk=None, format=None):
        if post_id is not None:
            return self.post(request, post_id)
        else:
            issue = self.get_object(pk)
            serializer = LikeSerializer(issue)
            return Response(serializer.data)

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        like = Like(user=user, post=post)
        like.save()
        return Response({"detail": "Like added successfully."}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        like = self.get_object(pk)
        post = like.post
        like.delete()
        post.likes_count -= 1
        post.save()
        return Response({"detail": f"You just deleted like with id {pk}"}, status=status.HTTP_204_NO_CONTENT)
