from django.db import models


class Blog(models.Model):
    theme = models.CharField(max_length=30)

class Recording(models.Model):
    header = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)






# Create your models here.
