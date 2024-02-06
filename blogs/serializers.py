# posts/serializers.py
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "id",
        "title",
        "description",
        "status",
        "created_by",
        "created_date"
        "modified_date"
)
model = Post