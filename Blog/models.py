from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name

class Post(models.Model):
    image =models.ImageField(upload_to='blog/',default='blog/default.jpeg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return "{} - {}".format(self.title, self.id)

    # def snippets(self):
    #     return self.content[]
