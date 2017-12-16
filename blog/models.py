from django.db import models
from django.utils.dateformat import format
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    publishDate = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    text= models.TextField()
    image = models.ImageField(null=True, blank=True,
        validators=[FileExtensionValidator(['jpg','jpeg','png'])],
    upload_to='blog/images/post%Y%m%d')
    altImage = models.CharField(max_length=50, default='blog post image')

    def __str__(self):
        return self.title + ' (' + self.publishDate.strftime('%d-%m-%Y') +')'

    def publishDateShort(self):
        return self.publishDate.strftime('%d %b %Y')

    def summary(self):
        return self.text[:100]
