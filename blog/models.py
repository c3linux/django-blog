from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1,"Publish")   
)
class Post(models.Model):
    image = models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # class Meta:
    #     ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.TextField(max_length=140, default='')
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')

    class Meta:
        verbose_name='comment'
        verbose_name_plural='comments'

    def __str__(self):
        return 'Comment'