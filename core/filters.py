import django_filters as filters

from core.models import Comment


class CommentFilter(filters.FilterSet):
    text__contains = filters.CharFilter(
        field_name='text', lookup_expr='contains')

    class Meta:
        model = Comment
        fields = ('movie',)
