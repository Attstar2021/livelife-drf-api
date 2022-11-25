from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    image_filter_choices = [
        ('brightness', 'Brightness'),
        ('earlybird', 'Earlybird'),
        ('sparkle', 'Sparkle'),
        ('inkwell', 'Inkwell'),
        ('awesome', 'Awesome'),
        ('mystyle', 'MyStyle'),
        ('normal', 'Normal'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('strange', 'Strange'),
        ('beautiful', 'beautiful'),
        ('zest', 'zest')
    ]
    owner = models.ForeignKey(User, on_delete=models. CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_lxktru', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
