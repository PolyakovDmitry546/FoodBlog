from typing import Any

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Comment, Post
from blog.forms import CommentForm


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self) -> str:
        return self.object.post.get_absolute_url()

    def form_valid(self, form) -> HttpResponse:
        form.instance.post_id = self.kwargs.get('id')
        return super().form_valid(form)
