from django.contrib import admin
from blog.models import Tag, Categories, Page, Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "name",
        "slug",
    )
    list_per_page = 10
    ordering = ("-id",)
    list_filter = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "name",
        "slug",
    )
    list_per_page = 10
    ordering = ("-id",)
    list_filter = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = (
        "id",
        "title",
        "slug",
        "is_published",
    )
    list_display_links = ("title",)
    search_fields = (
        "id",
        "title",
        "slug",
        "is_published",
    )
    list_per_page = 50
    ordering = ("-id",)
    list_filter = ("title", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_editable = ("is_published",)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = (
        "id",
        "title",
        "slug",
        "is_published",
        "created_by",
    )
    list_display_links = ("title",)
    search_fields = (
        "id",
        "title",
        "slug",
        "created_by",
        "content",
        "excerpt",
        "is_published",
    )
    list_per_page = 50
    ordering = ("-id",)
    list_filter = ("categories", "title", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ("categories", "tags")
    list_editable = ("is_published",)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
