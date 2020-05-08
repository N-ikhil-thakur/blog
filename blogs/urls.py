from django.urls import path

from .views import BlogPostsList  , BlogDetailView


urlpatterns = [
    path('' , BlogPostsList.as_view() , name = 'home'),
    path('post/<int:pk>/' ,BlogDetailView.as_view() , name = 'post_detail' ),
]