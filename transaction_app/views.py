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
from auth_app.models import Person, MmInvestment
from django.db.models.fields.related import ManyToManyField

def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
        else:
            data[f.name] = f.value_from_object(instance)
    return data

#@login_required(login_url = 'sign_in' )
def dashboard(request):
    person=Person.objects.filter(user__id=request.user.id)[0]
    invested=person.money_invested.through.objects.all()
    data=[]
    for i in invested:
        json_data=to_dict(i)
        data.append(json_data)
    return render(request, 'dashboard.html',{'data':data,'person':person})

def home(request, cat_name,page_num=1):
    if cat_name.lower() == 'home':
        posts = Post.objects.all().order_by('id').reverse()
    else:
        posts = Post.objects.all().filter(category__name=cat_name).order_by('id').reverse()
    category=Category.objects.all()
    return render(request, 'listing.html',{'posts':posts, 'category':category})



def blog_search(request):
    data = request.GET
    page_num=1
    cat_name='search'
    keyword = data["keyword"]
    tagval = keyword.strip()
    tagval = str(tagval).split(" ")
    entry_query = get_query(keyword.strip(), ['category__name','title','body'])
    posts = Post.objects.filter(entry_query).distinct().order_by('id').reverse()
    return render(request, 'blog/blog/index.html') 

@csrf_exempt
def investments(request,slug):
    amount=int(request.POST['amount'])
    if request.user.is_authenticated():
        user=User.objects.filter(email=request.user.email)[0]
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
