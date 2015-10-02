# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from markdown import markdown
from collections import Counter
import datetime
import json
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Post, Category
from django.template.defaultfilters import slugify
from .utils import get_query
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.urlresolvers import reverse
"""""""""""""""""""""""""""
view functions
"""""""""""""""""""""""""""

#@login_required(login_url = 'sign_in' )
def home(request, cat_name,page_num=1):
    """
    Home page
    """
    if cat_name.lower() == 'home':
        posts = Post.objects.all().order_by('id').reverse()
    else:
        posts = Post.objects.all().filter(category__name=cat_name).order_by('id').reverse()
    mark_down(posts)
    posts = paginate(posts, page_num)
    return render(request, 'transaction_app/index.html',
                  fill_page_with(posts=posts, nav_name='blog', active_category=cat_name))

@login_required(login_url = 'sign_in' )
def article(request, article_id):
    """
    article details page
    """
    posts = Post.objects.filter(slug=article_id)
    if posts.count() == 0:
        return render(request, 'blog/blog/article.html')

    post = posts[0]
    post.body = markdown(post.body)

    return render(request, 'blog/blog/article.html',
                  fill_page_with(post=post, active_category=post.category.name, nav_name='blog'))

def fill_page_with(**kwargs):
    base_dict = \
        {
            'categories': article_count_per_category(),
        }
    base_dict.update(kwargs)
    return base_dict


def mark_down(posts):
    for post in posts:
        post.body = markdown(post.body)


def paginate(posts, page_num=1):
    paginator = Paginator(posts, 5)
    try:
        page = int(page_num)
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return posts

def get_categories():
    categories = Category.objects.values('name', 'description')
    return categories


def article_count_per_category():
    return Counter(post.category for post in Post.objects.all()).iteritems()


def about(request):
    return render(request, 'blog/blog/about.html',
                  fill_page_with(nav_name='about'))


def contact(request):
    return render(request, 'blog/blog/contact.html',
                  fill_page_with(nav_name='contact'))


def blog_search(request):
    data = request.GET
    page_num=1
    cat_name='search'
    keyword = data["keyword"]
    tagval = keyword.strip()
    tagval = str(tagval).split(" ")
    entry_query = get_query(keyword.strip(), ['category__name','title','body'])
    posts = Post.objects.filter(entry_query).distinct().order_by('id').reverse()
    mark_down(posts)
    posts = paginate(posts, page_num)
    return render(request, 'blog/blog/index.html',
                  fill_page_with(posts=posts, nav_name='blog',active_category=cat_name)) 

@csrf_exempt
def investments(request,slug):
    amount=int(request.POST['amount'])
    if request.user.is_authenticated():
        user=User.objects.filter(email=request.user.email)[0]
        import pdb; pdb.set_trace()
        author=user.authors
        if int(author.credits_available) >= int(amount):
            author.credits_spent=author.credits_spent+amount  #two users one with slug and other with email
            author.credits_available=author.credits_available- amount
            post=Post.objects.filter(slug=slug)[0]
            post.amount_received=post.amount_received+amount
            author.money_invested.add(post.author_name)
            author.save()
            post.save()
        else:
            return HttpResponse("You have less amount than required")
    return HttpResponse("done")

