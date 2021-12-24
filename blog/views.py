from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.db.models import Q
def PostList(request):
    search = request.GET.get('search')
    posts = Post.objects.order_by('-id')
    if search:
        posts = posts.filter(
            Q(title__icontains=search) 
        ).distinct()
    return render(request, 'index.html', context={
        'posts' : posts,
        
    })

def PostDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        add_comment_form = CommentForm(data=request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.username = request.POST.get("username", "")
            comment.post = post
            comment.save()
    add_comment_form = CommentForm()
    
    return render(request, 'post_detail.html', context={
        'post' : post,
        'comments' : comments,
        'add_comment_form': add_comment_form
    })

