from django.shortcuts import render,redirect
from blog.models import Article

def dashboard(request):
    return render(request,'db.html')

def user_articles(request):
    if not  request.user.is_authenticated:
       return redirect('home')

    list_articles = Article.objects.filter(user=request.user)
    return render(request, 'my-articles.html',{'list_articles':list_articles})
