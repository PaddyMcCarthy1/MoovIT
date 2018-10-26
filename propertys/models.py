from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=100, default=None, blank=False, null=True)
    address1 = models.CharField(max_length=100, default=None, blank=False, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, default=None, blank=False, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    eircode = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default=None, blank=False, null=True)
    description = models.TextField(default=None, blank=False, null=True)
    key1 = models.CharField(max_length=100, default=None, blank=False, null=True)
    key2 = models.CharField(max_length=100, default=None, blank=False, null=True)
    key3 = models.CharField(max_length=100, default=None, blank=False, null=True)
    key4 = models.CharField(max_length=100, default=None, blank=False, null=True)
    key5 = models.CharField(max_length=100, default=None, blank=False, null=True)
    video = EmbedVideoField(default=None, blank=True, null=True)
    mapping = models.CharField(max_length=500, default=None, blank=False, null=True)
    floorplan = models.ImageField(default=None, blank=True, null=True)
    price = models.CharField(max_length=50, default=None, blank=False, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    publish_date = models.DateField(auto_created=True, blank=True, null=True)

    class Meta:
        ordering = ['-publish_date']

    def get_absolute_url_(self):
        return reverse('property_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

