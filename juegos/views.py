from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from .forms import JuegoForm
from .models import Juego

# Create your views here.


class JuegoListView(ListView):
    model = Juego
    template_name = 'juegos/juego_list.html'
    context_object_name = 'juegos'
    ordering = ['titulo']
    paginate_by = 5

class JuegoDetailView(DetailView):
    model = Juego
    template_name = 'juegos/juego_detail.html'
    context_object_name = 'juegos'


class JuegoCreateView(CreateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'juegos/juego_form.html'
    success_url = reverse_lazy('juego_list')

    def form_valid(self, form):
        messages.success(self.request, 'Juego creado correctamente')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'crear'
        return context


class JuegoUpdateView(UpdateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'juegos/juego_form.html'
    success_url = reverse_lazy('juego_list')

    def get_queryset(self):
        return Juego.objects.filter(usuario=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Juego actualizado correctamente')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'editar'
        return context


class JuegoDeleteView(DeleteView):
    model = Juego
    template_name = 'juegos/juego_confirm_delete.html'
    success_url = reverse_lazy('juego_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Juego eliminado correctamente')
        return super().delete(request, *args, **kwargs)