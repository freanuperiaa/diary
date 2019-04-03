from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import  DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView

from .models import Post
from apps.users.models import CustomUser
from .forms import EntryModelForm


class HomePageView(ListView):
    template_name = 'diary/home.html'

    def get_queryset(self):
        queryset = None
        if self.request.user.is_authenticated:
            queryset = Post.objects.filter(author =
            self.request.user).order_by('-id')[:5]
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['number'] = Post.objects.filter(author =
                                self.request.user).count()
        return context

class EntryCreateView(CreateView):
    template_name = 'diary/add_entry.html'
    form_class = EntryModelForm
   
    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        new_post.pub_date = timezone.now()
        new_post.save()
        return redirect(new_post.get_absolute_url())

class EntryDetailView(DetailView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author =
                       self.request.user)


class ArchiveView(ListView):
    
    def get_queryset(self):
        return Post.objects.filter(author = self.request.user).order_by('-id')

