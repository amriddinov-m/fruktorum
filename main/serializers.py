from rest_framework import serializers
from .models import Bookmark, Collection
from .open_graph import load_data_from_url


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
        read_only_fields = 'title', 'description', 'link_type', 'preview_image'

    def create(self, validated_data):
        url = validated_data.get('url')

        if not url:
            raise serializers.ValidationError({'url': 'URL-адрес обязателен.'})
        bookmark_info = load_data_from_url(url)
        if bookmark_info:
            validated_data.update({
                'title': bookmark_info.get('title'),
                'description': bookmark_info.get('description'),
                'preview_image': bookmark_info.get('image_url'),
            })

        return super().create(validated_data)


class CollectionSerializer(serializers.ModelSerializer):
    bookmarks = BookmarkSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'
