from .models import Blog
from rest_framework import serializers
class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.login_id')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'created_at', 'user', 'body']
