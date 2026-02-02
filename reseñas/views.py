from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Resena
from .forms import ResenaForm

# Create your views here.
class ResenaListView(ListView):
    model = Resena
    template_name = 'reseñas/reseña_list.html'
    context_object_name = 'resenas'
    ordering = ['usuario_username']
    paginate_by = 5


class ResenaDetailView(DetailView):
    model = Resena
    template_name = 'reseñas/reseña_detail.html'
    context_object_name = 'resena'


class ResenaCreatView(LoginRequiredMixin,CreateView):
    model = Resena
    form_class = ResenaForm
    template_name = 'reseñas/reseña_form.html'
    success_url = reverse_lazy('resenas_list')

    def form_valid(self, form):
        messages.success(self.request, 'Reseña creada correctamente')
        form.instance.usuario_username = self.request.user.username
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'crear'
        return context


class ResenaUpdateView(LoginRequiredMixin,UpdateView):
    model = Resena
    form_class = ResenaForm
    template_name = 'reseñas/reseña_form.html'
    success_url = reverse_lazy('resenas_list')

    def get_queryset(self):
        return Resena.objects.filter(usuario_username=self.request.user.username)

    def form_valid(self, form):
        messages.success(self.request, 'Reseña actualizada correctamente')
        form.instance.usuario_username = self.request.user.username
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'editar'
        return context


class ResenaDeleteView(LoginRequiredMixin,DeleteView):
    model = Resena
    template_name = 'reseñas/reseña_confirm_delete.html'
    success_url = reverse_lazy('resenas_list')

    def get_queryset(self):
        return Resena.objects.filter(usuario_username=self.request.user.username)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Reseña eliminada correctamente')
        return super().delete(request, *args, **kwargs)