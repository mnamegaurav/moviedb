from rest_framework import serializers

from core.models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):
    details = serializers.JSONField()

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
