from django.utils import timezone
from django.db import models


class Post(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    """DjangoAdmin Models"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    document = models.ImageField(
        upload_to='documents/%m/%d/%Y/',
        height_field=None, width_field=None, max_length=100, blank=True, null=True)

    def publish(self):
        """Publish"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
