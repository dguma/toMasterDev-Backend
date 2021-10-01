from django.urls import path
from .views import PostsList, SubjectsList, UserList, CommentList
from .views import index

urlpatterns = [
    path('', index),
    path('api/', PostsList.as_view()),
    path('api/subjects/', SubjectsList.as_view()),
    path('api/users/', UserList.as_view()),
    path('api/comments/', CommentList.as_view())
]