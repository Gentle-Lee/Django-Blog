# -*- coding: UTF-8 -*-  
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Article(models.Model):
    FILTER_VAR = (
        ('M','MAJOR'),
        ('L','LIFE'),
        )
    author = models.ForeignKey('auth.User')
    title = models.CharField('题目',max_length=200, blank=False, null=False )
    abstract =RichTextField('摘要', max_length=200, blank=True, null=True, 
                                help_text="可选，如若为空将摘取正文的前200个字符")
    # text = models.TextField('正文',null=True, blank=True)
    text =  RichTextField('正文',null=True, blank=True)
    filter_var = models.CharField('文章类型',max_length = 1,choices = FILTER_VAR,null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    category = models.CharField('类名', max_length=20,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title.encode('utf-8')
     
    def save(self, *args, **kwargs):    
        # 如果没有填写摘要
        if not self.abstract:
            # 从文本摘取前 54 个字符赋给 excerpt
            self.abstract = self.text[:100]
        # 调用父类的 save 方法将数据保存到数据库中
        super(Article, self).save(*args, **kwargs)

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'article_id': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
