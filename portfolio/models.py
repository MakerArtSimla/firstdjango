from django.db import models
from django.utils import timezone
# Create your models here.

#23/11/2017 BF fist model is Project
#copied and adapted from djangogirls tutorial (for a blog app)

class Project(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE  )
    title = models.CharField(max_length=200)
    description = models.TextField()
    reflection = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
