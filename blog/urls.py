from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('noticias/<int:pk>/', views.post_detail, name='post_detail'),
    path('noticias/no/<int:num>/', views.noticias, name='noticias'),
    path('galerias/<int:num>/', views.galerias, name='galerias'),
    path('galeria/<int:pk>/', views.galeria, name='galeria'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
