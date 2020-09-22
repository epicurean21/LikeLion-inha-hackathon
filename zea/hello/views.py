from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator   
from .models import Blog
from .models import StuApply


# Create your views here.
def main(request):
    return render (request, 'main.html')

def home(request):
    posts = Blog.objects.all().order_by('-id')
    paginator = Paginator(posts,6) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'home.html',{'page_posts':page_posts}) 

def category1(request):
    category = request.GET.get("category")
    
    posts = Blog.objects.filter(category="디자인").order_by('-id')    
    paginator = Paginator(posts,6) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'category1.html',{'page_posts':page_posts}) 

def category2(request):
    category = request.GET.get("category")
    
    posts = Blog.objects.filter(category="영상 및 사진").order_by('-id')    
    paginator = Paginator(posts,6) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'category1.html',{'page_posts':page_posts})

def category3(request):
    category = request.GET.get("category")
    
    posts = Blog.objects.filter(category="컨설팅").order_by('-id')    
    paginator = Paginator(posts,6) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'category1.html',{'page_posts':page_posts})

def category4(request):
    category = request.GET.get("category")
    
    posts = Blog.objects.filter(category="IT 및 프로그래밍").order_by('-id')    
    paginator = Paginator(posts,6) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'category1.html',{'page_posts':page_posts})



def postnew(request):
    return render(request, 'postnew.html')
 
def postcreate(request):
    print(request.method)
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.name = request.POST['name']
        post.spot = request.POST['spot']
 
        post.date = request.POST['date']
        post.pay = request.POST['pay']
        post.save()
    return redirect('home')

def detail(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render (request, 'detail.html', {'onepost':onepost})

def detail2(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render (request, 'detail2.html', {'onepost':onepost})

def detail3(request,post_id):
    onepost=get_object_or_404(StuApply,pk=post_id)
    return render (request, 'detail3.html', {'onepost':onepost})
 
def postedit(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'postedit.html',{'onepost':onepost})
    
def postupdate(request,post_id):
    editpost=get_object_or_404(Blog,pk=post_id)
    editpost.title = request.POST['title']
    editpost.body = request.POST['body']
    editpost.name = request.POST['name']
    editpost.spot = request.POST['spot']
  
    editpost.date = request.POST['date']
    editpost.pay = request.POST['pay']
    editpost.save()
    return redirect('/detail/'+str(post_id))

def postdelete(request,post_id):
    deletepost=get_object_or_404(Blog,pk=post_id)
    deletepost.delete()
    return redirect('/')

def apply1(request):
    return render (request, 'apply.html')


def mypost(request):
    if not request.user.is_authenticated: 
        return render(request, 'login.html')
    else:
        your_category= request.GET.get("your_category")
        posts = Blog.objects.filter(category="대학생").order_by('-id')    
        paginator = Paginator(posts,6) 
        page = request.GET.get('page')
        page_posts = paginator.get_page(page)
        return render(request,'mypost.html',{'page_posts':page_posts})

def mypost01(request):
    if not request.user.is_authenticated: 
        return render(request, 'login.html')
    else:
        category2 = request.GET.get("category2")
        posts = Blog.objects.filter(category2="업체").order_by('-id')    
        paginator = Paginator(posts,6) 
        page = request.GET.get('page')
        page_posts = paginator.get_page(page)
        return render(request,'mypost01.html',{'page_posts':page_posts})


def mypost02(request):
    if not request.user.is_authenticated: 
        return render(request, 'login.html')
    else:
        category = request.GET.get("category")
        posts = StuApply.objects.filter(category="학생").order_by('-id')    
        paginator = Paginator(posts,6) 
        page = request.GET.get('page')
        page_posts = paginator.get_page(page)
        return render(request,'mypost02.html',{'page_posts':page_posts})
