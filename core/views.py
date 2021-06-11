from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import filters, status

from core.models import Comment, Movie
from core.filters import CommentFilter
from core.api.serializers import (
    MovieSerializer,
    CommentSerializer
)
from core.utils import get_movie_data
# Create your views here.


class MoviesAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = (
        'details__Year', 'details__Released', 'details__Runtime',
        'details__Runtime', 'details__Country', 'details__imdbRating',
        'details__imdbVotes',
    )
    search_fields = ('details__Title',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # check if movie title is already available in db
        if queryset.count() == 0:
            # if not then search from omdbapi
            # save the results from omdb to db
            search_query = request.query_params.get('search')
            movie_datas = get_movie_data(title=search_query)
            serializer = self.serializer_class(
                data={"details": movie_datas}, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # response = Response(serializer.data,
                #                     status=status.HTTP_201_CREATED)

            queryset = self.filter_queryset(self.get_queryset())

        return super().list(request, *args, **kwargs)


class CommentsAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filterset_class = CommentFilter
