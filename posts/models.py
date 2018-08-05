from django.db import models


class BlogConfig(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=1000)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

