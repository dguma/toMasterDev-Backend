# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PostsSerializer, SubjectsSerializer, UserSerializer, CommentSerializer
from .models import Posts, Subjects, User, Comment
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'pg_app_frontend/index.html')

class PostList(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class SubjectList(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentList(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
