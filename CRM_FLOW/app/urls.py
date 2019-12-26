from django.urls import path, re_path
from app import views

app_name='app'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('addbook/', views.addbook, name='addbook'),
    path('<int:id>/delete/', views.delbook, name='delbook'),
    path('<int:id>/change/', views.changebook, name='changebook'),
    path('query/', views.query, name='query'),
    path('test/', views.test, name='test')
]
