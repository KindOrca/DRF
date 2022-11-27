from blog.models import Blog
from blog.serializers import BlogSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class BlogList(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request): # 오버라이딩 한거라 이름 바꾸면 안됨
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):
    def object(self, Primary_Key):
        try:
            return Blog.objects.get(pk=Primary_Key)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, Primary_Key, format=None):
        blog = self.object(Primary_Key)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, Primary_Key, format=None):
        blog = self.object(Primary_Key)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Primary_Key, format=None):
        blog = self.get_object(Primary_Key)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  