from django.db import models
from django.db.models import Model

# Create your models here.
class Tag(Model):
    caption=models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Author(Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email_field=models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Post(Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=300)
    image_name=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, db_index=True)
    content=models.TextField()
    author=models.ForeignKey(Author, on_delete=models.SET_NULL,related_name="posts",null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title