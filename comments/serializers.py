
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('post', 'author', 'text', 'created_at','approved_comment')

        model = Comment