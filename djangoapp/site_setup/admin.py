from django.contrib import admin
from django.http import HttpRequest
from site_setup.models import MenuLink, SiteSetup

# Using this class a new tab apper

# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = "id", "text", "url_or_path"
#     list_display_links = "id", "text", "url_or_path"
#     search_fields = "id", "text", "url_or_path"


# Using inline you can add multiple menu links and put it in the same page
class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1


# Site config using admin account on django admin
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = "tittle", "description"
    inlines = (MenuLinkInline,)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
