from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    content = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('diary:entry', args=[self.id])
