from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import PostSerializer
from instaclone.models import Post


class PostListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Post.objects.all()
        serializer = PostSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        issue = self.get_object(pk)
        serializer = PostSerializer(issue)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        issue = self.get_object(pk)
        serializer = PostSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        issue = self.get_object(pk)
        issue.delete()
        return Response(f"You just deleted post #{pk}", status=status.HTTP_204_NO_CONTENT)


