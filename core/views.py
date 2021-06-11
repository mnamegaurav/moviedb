from django.db.models import Q

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import filters, status

from core.models import Comment, Movie
from core.filters import CommentFilter
from core.api.serializers import (
    MovieSerializer,
    MovieTitleSerializer,
    CommentSerializer,
)
from core.utils import get_movie_data
# Create your views here.


class MoviesAPIView(ListCreateAPIView):
    serializer_class = MovieTitleSerializer
    movie_serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = (
        'details__Year', 'details__Released', 'details__Runtime',
        'details__Runtime', 'details__Country', 'details__imdbRating',
        'details__imdbVotes',
    )

    def get(self, request, format=None):
        serializer = self.movie_serializer_class(
            self.get_queryset(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        search_title = request.data.get('title', '')

        # check if movie title is already available in db
        queryset = self.get_queryset().filter(
            Q(details__has_key='Title') & Q(title__icontains=search_title)
        )

        # if not then search from omdbapi
        if queryset.count() == 0:
            movie_data = get_movie_data(title=search_title)
            # save the results from omdb to current db
            serializer = self.movie_serializer_class(
                data={'details': movie_data},
            )
            if serializer.is_valid(raise_exception=True):
                # save all the new movies
                serializer.save()
        else:
            serializer = self.movie_serializer_class(queryset, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class CommentsAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filterset_class = CommentFilter
