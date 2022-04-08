from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from .forms import CreatePostForm
from .models import Post

class BlogListView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        context = {
            'posts': posts
        }
        return render(request, 'main_blog.html', context)

class CreatePostView(View):

    def get(self, request, *args, **kwargs):
        form = CreatePostForm()
        context = {
            'form': form
        }
        return render(request, 'create_post.html', context)

    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            form = CreatePostForm(request.POST)
            if form.is_valid():
                temp_title = form.cleaned_data.get('title')
                temp_content = form.cleaned_data.get('content')
            
            p, created = Post.objects.get_or_create(title = temp_title, content = temp_content)
            p.save()

            return redirect('main_home')

        context = {}
        return render(request, 'create_post.html', context)

class PostDetailView(View):

    def get(self, request, pk, *args, **kwargs):

        post = get_object_or_404(Post, pk = pk)

        context = {
            'post': post
        }
        return render(request, 'detail_blog.html', context)

class PostUpdateView(UpdateView):

    model = Post
    fields = ['title','content']
    template_name = 'update_post.html'

    def get_success_url(self):

        pk = self.kwargs['pk']
        
        return reverse_lazy('blog:detail', kwargs = {'pk':pk})

class PostDeleteView(DeleteView):

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home')