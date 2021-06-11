from rest_framework import serializers

from core.models import Movie, Comment


class MovieTitleSerializer(serializers.Serializer):
    title = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    details = serializers.JSONField()

    class Meta:
        model = Movie
        fields = ('details',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
