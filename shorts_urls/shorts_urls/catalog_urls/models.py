from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Catalog_Urls(models.Model):
    long_link = models.CharField(max_length=256)
    short_link = models.CharField(max_length=265)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('short_u', kwargs={'short_u': self.short_link})
