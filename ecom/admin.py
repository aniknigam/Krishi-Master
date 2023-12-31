from django.contrib import admin
from .models import ProductListing,buyproduct
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
      list_display = ("title", "slug", "status", "created_on")
      list_filter = ("status", "created_on")
      search_fields = ["title", "content"]
      prepopulated_fields = {"slug": ("title",)}


admin.site.register(ProductListing,ProductAdmin)

@admin.register(buyproduct)
class BuyedAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "product", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)