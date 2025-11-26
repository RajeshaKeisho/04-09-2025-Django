from django.urls import path
from .views import AuthorListCreateView, AuthorRetrieveView, BookListCreateView, BookRetrieveView

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view(), name='author-list-create'),
    path("authors/<int:pk>", AuthorRetrieveView.as_view(), name='author-detail'),
    path("books/", BookListCreateView.as_view(), name='book-list-create'),
    path("books/<int:pk>", BookRetrieveView.as_view(), name='book-detail'),

]
