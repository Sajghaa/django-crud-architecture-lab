from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms  import PostForm

class PostListView(ListView):
    model =  Post
    template_name = "blog_basic/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog_basic/post_detail.html"

class PostCreateView(CreateView):
    model =  Post
    form_class = PostForm
    template_name = "blog_basic/post_form.html"

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name= "blog_basic/post_form.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name= "blog_basic/post_confirm_delete.html"
    success_url = reverse_lazy("blog_basic:post_list")