from django import template
from ..models import Article

register = template.Library()


@register.simple_tag
def get_context_of_news_lenta():
    """view for random article context"""
    articles = Article.objects.filter(lenta=True).order_by('?', '-date')[0:10]
    return articles


@register.simple_tag
def get_context_of_news_upd():
    """view for special posts"""
    articles = Article.objects.filter(upd=True).order_by('-date')[0:9]
    return articles


@register.simple_tag
def get_context_of_news_simple():
    """view for simple posts"""
    articles = Article.objects.filter(simple=True).order_by('-date')[0:6]
    return articles


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """view for parameters replacing"""
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.filter(name='range')
def range_(num_s, num_e):
    """view for showing paginator`s numbers"""
    page_list = []
    for i in range(num_s, num_s + 6):
        print(page_list)
        page_list.append(i)
        if num_e in page_list:
            break
    return page_list


@register.filter(name='range_s')
def range_s(num):
    """one more view for showing paginator`s numbers"""
    page_list = []
    for i in reversed(range(num - 6, num)):
        if i == 0:
            break
        page_list.append(i)
    return list(reversed(page_list))


@register.filter(name='index')
def list_index(list, index):
    """one more view for showing paginator`s numbers"""
    print(list[index])
    return list[index]
