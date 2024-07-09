from rest_framework.serializers import ModelSerializer

from content.models import Blog


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'auther', 'created']

