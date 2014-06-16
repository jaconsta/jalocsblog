#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class MainCategoriesManager(models.Manager):
    def get_queryset(self):
        return super(MainCategoriesManager, self).get_queryset().\
            filter(display=True, dependency__name='root').\
            exclude(name__exact='root')

class Categories(models.Model):
    name = models.CharField('Name', max_length = 75)
    dependency = models.ForeignKey('self', verbose_name = 'Parent', default = 1, null = True, blank = True) #Set to not null
    display = models.BooleanField('Show in page', default = True)
    color = models.CharField('Color', max_length = 16)

    #Managers
    objects = models.Manager()
    main_objects = MainCategoriesManager()
    
    def __unicode__(self):
        return self.name

class RecentPostManager(models.Manager):
    def RecentPost(self, cat):
        return super(RecentPostManager, self).get_queryset().\
            filter(category=cat, private = False)

class Post(models.Model):
    category = models.ForeignKey('Categories', verbose_name="Categoría del post")
    title = models.CharField('Título', max_length = 140)
    headimg = models.ImageField('Header Image', upload_to = '/static/img/posts/', null = True, blank = True)
    resume = models.CharField('Resume text', max_length = 250, null = True, blank = True)
    body = models.TextField('Post body')
    author = models.ForeignKey(User)
    newdate = models.DateTimeField('Creation date', auto_now_add = True)
    postdate = models.DateTimeField('Publish date', auto_now_add = True)
    update = models.DateTimeField('Last modification date', auto_now = True)
    publish = models.BooleanField('Publish and display', default = False)
    private = models.BooleanField('Private post', default = False)

    #Managers
    objects = RecentPostManager() #models.Manager()
#    recent_objects = RecentPostManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['publish', ]
