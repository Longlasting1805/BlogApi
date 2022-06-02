
import view
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from myBlog.models import Blog
from myBlog.serializers import BlogSerializer


class BlogView(APIView):
    def get(self, request):
        articles = Blog.objects.all()
        serializer = BlogSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

