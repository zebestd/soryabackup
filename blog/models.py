from django.db import models
from django.utils.text import slugify


from django.conf import settings

from django.db.models.signals import pre_save
from django.utils import timezone

class Category(models.Model):
    isim = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.isim 

class Post(models.Model):
    isim = models.CharField(max_length=200, null=True)
    soru = models.CharField(max_length=255, null=True)
    slug = models.SlugField(null=True)
    kategori = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    aciklama = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    isim = models.CharField(max_length=255)
    yanit = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


def create_slug(instance, new_slug=None):
    slug = slugify(instance.isim)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)