from django.shortcuts import redirect
from django.views.generic import  DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post


class HomePageView(TemplateView):
    template_name = 'diary/home.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            kwargs['number'] = Post.objects.filter(
                author=self.request.user).count()
            kwargs['post_list'] = Post.objects.filter(
                author=self.request.user
            ).order_by('-id')[:5]
        return super(). get_context_data(**kwargs)


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        new_post.save()
        return redirect(new_post.get_absolute_url())


class EntryDetailView(DetailView):
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class ArchiveView(ListView):
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-id')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
