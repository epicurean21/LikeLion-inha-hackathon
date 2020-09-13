from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
# Create your views here.
def main(request):
    return render (request, 'main.html')

def home(request):
    blogs = Blog.objects
    return render (request, 'home.html', {'blogs':blogs})

def postnew(request):
    return render(request, 'postnew.html')
 
def postcreate(request):
    print(request.method)
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')

def detail(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render (request, 'detail.html', {'onepost':onepost})

def postedit(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'postedit.html',{'onepost':onepost})
    
def postupdate(request,post_id):
    editpost=get_object_or_404(Blog,pk=post_id)
    editpost.title=request.POST['title']
    editpost.body=request.POST['body']
    editpost.save()
    return redirect('/detail/'+str(post_id))

def postdelete(request,post_id):
    deletepost=get_object_or_404(Blog,pk=post_id)
    deletepost.delete()
    return redirect('home')