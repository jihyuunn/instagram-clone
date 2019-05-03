from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length = 50, default = 'haribo')
    content = models.TextField()
    img = models.ImageField(null=True)

    def __str__(self):
        return self.content[:11]

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')