from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from core.api.serializers import (
    MovieSerializer,
    CommentSerializer
)

from core.models import Comment
# Create your views here.


class MoviesAPIView(GenericAPIView):
    serializer_class = MovieSerializer

    def get(self, request, format=None):
        return Response({'m get': 1})

    def post(self, request, format=None):
        return Response({'m post': 1})


class CommentsAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
