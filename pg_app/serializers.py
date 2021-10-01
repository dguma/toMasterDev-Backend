from rest_framework import serializers
from .models import Posts, Subjects, User, Comment

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'name', 'title', 'description')

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('id', 'focusDefinition', 'focusContent', 'focusLinks', 'focusImages', 'focus')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstName', 'lastName', 'email', 'password')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'date',)