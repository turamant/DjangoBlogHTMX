from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)