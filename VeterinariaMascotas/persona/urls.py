from django.urls import path
from . import views
#from django.contrib.auth import views as vista
from django.conf import settings
from django.conf.urls.static import static
from .views import mi_vista

app_name = "blog"

urlpatterns = [
    path('',views.lista_personas, name='lista_personas'),
    path('persona/<int:pk>/',views.detalle_persona, name='detalle_persona'),
    path('persona/new', views.persona_new, name='persona_new'),
    path('persona/<int:pk>/edit/', views.persona_edit, name='persona_edit'),
    path('persona/<int:pk>/delete/', views.persona_delete, name='persona_delete'),
    path('animal/',views.lista_animales, name="lista_animales"),
    path('animal/new', views.animal_new, name='animal_new'),
    path('animal/<int:pk>/',views.detalle_animal, name="detalle_animal"),
    path('animal/<int:pk>/edit/', views.animal_edit, name="animal_edit"),
    path('animal/<int:pk>/delete/', views.animal_delete, name="animal_delete"),
    path('consulta/', views.lista_consultas, name="lista_consultas"),
    path('consulta/new', views.consulta_new, name="consulta_new"),
    path('consulta/<int:pk>/', views.detalle_consulta, name='detalle_consulta'),
    path('consulta/<int:pk>/edit/', views.consulta_edit, name="consulta_edit"),
    path('consulta/<int:pk>/delete/', views.consulta_delete, name="consulta_delete"),
    path('registro/', views.register, name='registro' ),
    path('mi-vista/', mi_vista, name='mi_vista'),


    ##ACA PONDRE LOS REST FRAMEWORK, desde la ppt los copio, pego y cambio nomrbe de objeto del modelo que manejare
    ## Despues me voy al del proyecto validando que estan lo de las url
    path('postsapi/', views.posts_list, name='posts-list'),
    path('postsapi/<int:pk>/', views.posts_detail, name='posts-detail'),
    ##URL PARA TOKENS
    path('postsapi/obtener-token/', views.obtener_token, name='obtener-token'), 
]




