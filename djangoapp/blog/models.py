from django.db import models
from utils.rands import create_slug


class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=50
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Categories(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=50
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(
        max_length=50,
    )
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=50
    )
    is_published = models.BooleanField(default=False, help_text="Publish this page?")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
