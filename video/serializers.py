from rest_framework import serializers

from categories.serializers import CategorySerializer
from video.models import Video


class VideoSerializer(serializers.ModelSerializer):
    tag = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'tag')
