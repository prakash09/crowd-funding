from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import datetime
from auth_app.models import Person
# Create your models here.


class Category(models.Model):
    name = models.SlugField(null=True, blank=True, editable=False)
    description = models.CharField(max_length=255,verbose_name="Category Name")
    def __unicode__(self):
        return self.description
    def save(self,*args,**kwargs):
        self.name=slugify(self.description)
        super(Category,self).save(*args,**kwargs)


class Post(models.Model):
    category = models.ForeignKey(Category)
    featured_image=models.ImageField(upload_to='images/',null=True, blank=True)
    author_name=models.ForeignKey(Person, related_name="posts")
    interest_rate=models.FloatField(default=0.0,null=True, blank=True ) #automatic
    title = models.CharField(max_length=255)
    body=RichTextField()
    amount_requested=models.FloatField(default=0)
    amount_received=models.FloatField(default=0) #automatic
    tenure=models.IntegerField(null=True, blank=True) #automatic 10 12 15 20
    slug=models.SlugField(editable=False) #automatic
    date = models.DateField(auto_now_add=True) #automatic
    is_active=models.BooleanField(default=False) #automatic
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title+str(self.author_name))
        if self.author_name.profile_category==1:
            self.interest_rate=6
            self.tenure=10
        elif self.author_name.profile_category==2:
            self.interest_rate=9
            self.tenure=12
        elif self.author_name.profile_category==3:
            self.tenure=15
            self.interest_rate=12
        else:
            self.tenure=20
            self.interest_rate=12.5
        super(Post,self).save(*args,**kwargs)
    def __unicode__(self):
        return self.title
    def created_on(self):
        return self.date.strftime('%Y-%m-%d')
    created_on.short_description = 'Created on'

    def article_category(self):
        return format_html('<span style="color: red;">{0}</span>', self.category)
    article_category.short_description = 'Category'
    article_category.allow_tags = True
    article_category.admin_order_field = 'category'
    type = property(article_category)
