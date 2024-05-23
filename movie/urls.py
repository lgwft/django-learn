from django.urls import path
from . import views

urlpatterns = [
    path('list', views.movie_list),
    path('detail/<int:movie_id>', views.movie_detail)
]