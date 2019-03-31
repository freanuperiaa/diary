from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone


from .models import Post, Tag
from users.models import CustomUser
from django.views.generic import  DetailView, ListView, TemplateView
from django.views.generic.edit import FormView
from .forms import EntryForm, EntryModelForm
# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        queryset = None
        if self.request.user.is_authenticated:
            queryset = Post.objects.filter(author =
            self.request.user).order_by('-id')[:5]
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['number'] = Post.objects.filter(author=self.request.user).count()
        return context



class EntryCreateView(FormView):
    template_name = 'add_entry.html'
    #form_class = EntryForm

    # def form_valid(self, form):
    #     #this is what I was talking about in Freanu's notes, sir.
    #     #I couldn't find another way for doing this. Perhaps there's
    #     #another way to do this that I do not know - yet.
    #     new_title = form.cleaned_data['title']
    #     new_pub_date = timezone.now()
    #     new_author = self.request.user
    #     new_content = form.cleaned_data['content']
    #     tags = form.cleaned_data['tags']
    #     new_post = Post(
    #         title = new_title, pub_date = new_pub_date,
    #                 author = new_author, content = new_content
    #     )
    #     new_post.save()

    #     #add tags that are not in the database
    #     if form.cleaned_data['more_tags']:
    #         unsaved_tags = form.cleaned_data['more_tags']
    #         unsaved_tags.replace(' ','')
    #         list_tags = unsaved_tags.split(',')
    #         tags_in_db = Tag.objects.all()
    #         for item in list_tags:
    #             if item not in tags_in_db:
    #                 new_tag = Tag(title = item)
    #                 new_tag.save()
    #                 new_post.tags.add(new_tag)
            
    #     tags_list = Tag.objects.filter(pk__in=tags)
    #     for item in tags_list:
    #         new_post.tags.add(item)
    #     return redirect(new_post.get_absolute_url())
    

    #changed method since the form is changed to ModelForm
    form_class = EntryModelForm
    def form_valid(self, form):
        new_title = form.cleaned_data['title']
        new_pub_date = timezone.now()
        new_author = self.request.user
        new_content = form.cleaned_data['content']
        new_tags = form.cleaned_data['tags']
        new_post = Post(
            title = new_title,
            pub_date = new_pub_date,
            author = new_author,
            content = new_content,
        )
        new_post.save()

        tags = Tag.objects.filter(pk__in=new_tags)
        for tag in tags:
            new_post.tags.add(tag)

        return redirect(new_post.get_absolute_url())



class EntryDetailView(DetailView):
    template_name = 'detail_entry.html'
    model = Post

    def get_object(self, **kwargs):
        post_object = get_object_or_404(Post, id = self.kwargs['pk'])
        if post_object.author != self.request.user:
            return None
        else:
            return post_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id = self.kwargs['pk'])
        context['tags'] = post.tags.all()
        return context


# class TimelineView(ListView):
#     template_name = 'timeline.html'
    
#     def get_queryset(self):
#         queryset = Post.objects.filter(author =
#         self.request.user).order_by('-id')[:5]
#         return queryset


class ArchiveView(ListView):
    template_name = 'archive.html'

    def get_queryset(self):
        queryset = Post.objects.filter(author = 
                self.request.user).order_by('-id')
        return queryset

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
