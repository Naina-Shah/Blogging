from django.shortcuts import render, redirect  # redirect bhi import karo
from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from django.contrib.auth.decorators import login_required

    
@login_required
def post_list(request):
    if request.method == 'POST':
        blog.objects.create(
            
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.POST['author'],

        )
        return redirect('/blog/')  # redirect karo same page pe
    
    blogs = blog.objects.all()
    return render(request, 'post_list.html', {'blogs': blogs})

@login_required
def blog_detail(request, id):
    single_blog = get_object_or_404(blog, id=id)
    return render(request, 'blog_detail.html', {'blog': single_blog})
@login_required
def blog_edit(request, id):
    single_blog= get_object_or_404(blog,id=id)
    if request.method == 'POST':
        single_blog.title =request.POST['title'],
        single_blog.content=request.POST['content'],
        single_blog.author=request.POST['author'],
        single_blog.save(   )
        return redirect('/blog/')
        
    return render(request, 'blog_edit.html', {'blog': single_blog})
@login_required
def blog_delete(request, id):
    single_blog= get_object_or_404(blog, id=id)
    if request.method== 'POST':
        
        single_blog.delete()
        return redirect('/blog/')
    return render(request, 'blog_delete.html', {'blog': single_blog})

def home(request):
    
    blogs = blog.objects.all().order_by('-id')
    return render(request, 'home.html', {'blogs': blogs})
def blog_detail(request, id):
    single_blog = get_object_or_404(blog, id=id)
    return render(request, 'blog_detail.html', {'blog': single_blog})

    