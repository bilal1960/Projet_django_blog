from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from blog.models import Article
from blog.forms import ArticleForm

def dashboard(request):
    return render(request,'db.html')

@login_required
def user_articles(request):
    has_perm= False
    if request.user.has_perm("blog.delete_article"):
         has_perm = True

    list_articles = Article.objects.filter(user=request.user)
    return render(request, 'my-articles.html',{'list_articles':list_articles,'has_perm':has_perm})

class addArticle(LoginRequiredMixin,CreateView):
    model = Article
    form_class = ArticleForm
    template_name ="add-article.html"
    success_url = "my-articles"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class UpdateArticle(LoginRequiredMixin,UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app_admin/article_form.html'
    success_url = '/my-admin/my-articles'  

class DeleteArticle(LoginRequiredMixin,DeleteView):
    model = Article
    success_url = "/my-admin/my-articles"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.has_perm('blog.delete_article'):
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
         

