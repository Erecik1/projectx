from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from projectx.forms import PostForm, PostSearchForm
from django.db.models import Q
from post.models import Post

def post_list(request):
    return render(request,
                  template_name='blog/post_list.html')
def Posts(request):
    title = author = text = ""
    form = PostSearchForm()
    if request.POST:
        form = PostSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title", "")
            author = form.cleaned_data.get("author", "")
            text = form.cleaned_data.get("text", "")

    post_list1 = Post.objects.filter(Q(title__icontains=title)
                                    &Q(text__icontains=text)
                                    &Q(author__username__icontains=author))

    return render(request,
                  template_name="posts.html",
                  context={"Posts": post_list1,
                           "form": form})

def Post1(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,
                  template_name="post.html",
                  context={"Post": post})

def post_create(request):
    form = PostForm()
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('post-list'))
    return render(request, template_name='post_create.html', context={'form':form},)



def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(reverse_lazy("post-list"))