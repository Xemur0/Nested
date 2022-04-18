from django.urls import path

from api import views

urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    path('comments/', views.CommentListView.as_view()),
    path('comments/<int:pk>', views.CommentNestedView.as_view())
]