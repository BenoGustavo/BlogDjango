from django.contrib.auth.models import User
from django.db import models
from utils.rands import create_slug
from utils.images import resize_image
from django_summernote.models import AbstractAttachment


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs) -> str:
        # Get the current favicon name
        current_file_name = str(self.file.name)

        super_save = super().save(*args, **kwargs)

        file_changed = False

        # If has a file and the current file name is different from the new file name
        if self.file:
            file_changed = current_file_name != str(self.file.name)

        # If the file has changed, resize it
        if file_changed:
            resize_image(self.file, new_width=900)

        return super_save


class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=50
    )

    def save(self, *args, **kwargs) -> str:
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

    def save(self, *args, **kwargs) -> str:
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

    def save(self, *args, **kwargs) -> str:
        if not self.slug:
            self.slug = create_slug(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    title = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=50
    )
    excerpt = models.CharField(max_length=150)
    content = models.TextField()
    is_published = models.BooleanField(default=False, help_text="Publish this post?")
    cover = models.ImageField(upload_to="posts/%Y/%m/", default="", blank=True)
    cover_in_post_content = models.BooleanField(
        default=True, help_text="Show cover in post content?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_created_by",
    )

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_updated_by",
    )

    categories = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    tags = models.ManyToManyField(Tag, blank=True, default="")

    def save(self, *args, **kwargs) -> str:
        if not self.slug:
            self.slug = create_slug(self.title)

        # Get the current favicon name
        current_cover_name = str(self.cover.name)

        super_save = super().save(*args, **kwargs)

        cover_changed = False

        # If has a cover and the current cover name is different from the new cover name
        if self.cover:
            cover_changed = current_cover_name != str(self.cover.name)

        # If the cover has changed, resize it
        if cover_changed:
            resize_image(self.cover, new_width=900)

        return super_save

    def __str__(self) -> str:
        return self.title
