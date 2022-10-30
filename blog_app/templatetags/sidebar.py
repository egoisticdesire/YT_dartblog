from django import template
from blog_app.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog_app/inc/_sidebar_popular_posts.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('blog_app/inc/_sidebar_tags.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
