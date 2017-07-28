# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,render_to_response
from django.utils import timezone
from comments.forms import CommentForm
from .models import Article

def article_list(request):
    articles = Article.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/main.html', {'articles': articles})

def programming_list(request):
    articles = Article.objects.filter(created_date__lte=timezone.now(),filter_var = 'M').order_by('-created_date')
    return render(request, 'blog/main.html', {'articles': articles})

def jotting_list(request):
    articles = Article.objects.filter(created_date__lte=timezone.now(),filter_var = 'L').order_by('-created_date')
    return render(request, 'blog/main.html', {'articles': articles})    

def homepage(request):
	return render(request,'blog/index.html')

def article_detail(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
     # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = article.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'article' : article,
               'form': form,
               'comment_list': comment_list,
               }
    return render(request, 'blog/article.html', context=context)

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    articles = Article.objects.filter(title__icontains=q)
    if not articles:
    	articles = Article.objects.filter(category__icontains=q)
    if not articles:
        error_msg = '搜索不到该关键字'
        return render(request, 'blog/result.html', {'error_msg': error_msg})
    return render(request, 'blog/result.html', {'error_msg': error_msg,
                                               'articles': articles})
