from django.contrib import admin
from django.urls import path
from genres.views import genre_create_list_view, genre_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', genre_create_list_view, name='genre_create_list'),
    path('genre/<int:pk>/', genre_detail_view, name='detail_list')
]
