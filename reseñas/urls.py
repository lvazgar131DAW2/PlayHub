from django.urls import path

from reseñas.views import ResenaUpdateView, ResenaDeleteView, ResenaDetailView, ResenaListView, ResenaCreatView

urlpatterns = [
    path('',ResenaListView.as_view(), name='resenas_list'),
    path('detalle/<int:pk>/',ResenaDetailView.as_view(), name='resena_detail'),
    path('crear/',ResenaCreatView.as_view(), name='resena_create'),
    path('editar/<int:pk>/',ResenaUpdateView.as_view(), name='resena_update'),
    path('eliminar/<int:pk>/',ResenaDeleteView.as_view(), name='resena_delete'),
]