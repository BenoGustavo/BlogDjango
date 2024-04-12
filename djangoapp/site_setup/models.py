from django.db import models
from utils.model_validator import validate_png
from utils.images import resize_image


class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name_plural = "Menu Links"

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    site_setup = models.ForeignKey(
        "SiteSetup",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.text


class SiteSetup(models.Model):
    class Meta:
        verbose_name = "Setup"
        verbose_name_plural = "Setup"

    tittle = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    favicon = models.ImageField(
        upload_to="assets/favicon/%Y/%m/",
        default="",
        blank=True,
        null=True,
        validators=[validate_png],
    )

    def save(self, *args, **kwargs):
        # Check if the favicon has changed

        # Get the current favicon name
        current_favicon_name = str(self.favicon.name)

        super().save(*args, **kwargs)

        favicon_changed = False

        # If has a favicon and the current favicon name is different from the new favicon name
        if self.favicon:
            favicon_changed = current_favicon_name != str(self.favicon.name)

        # If the favicon has changed, resize it
        if favicon_changed:
            resize_image(self.favicon, new_width=32)

    def __str__(self):
        return self.tittle
