from ..models import Post, Category
from django import template

register = template.Library()


# 最近发表
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


# 归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类
@register.simple_tag
def get_categories():
    return Category.objects.all()
