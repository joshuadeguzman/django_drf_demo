from ..models import Post
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer