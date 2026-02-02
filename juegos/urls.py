from django.urls import path
from . import views

urlpatterns = [
    path('',views.JuegoListView.as_view(), name='juego_list'),
    path('detalle/<int:pk>/',views.JuegoDetailView.as_view(), name='juego_detail'),
    path('crear/',views.JuegoCreateView.as_view(), name='juego_create'),
    path('editar/<int:pk>/',views.JuegoUpdateView.as_view(), name='juego_update'),
    path('eliminar/<int:pk>/',views.JuegoDeleteView.as_view(), name='juego_delete'),
]