from django.contrib import admin

# Register your models here.
from bestshop.products.models import Product, Comment, Purchase, Ratings


class BestShopAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', )

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('user', 'text', )

class PurchaseAdmin(admin.ModelAdmin):
    model = Purchase
    list_display = ('user', 'purchase_date', )

class RatingsAdmin(admin.ModelAdmin):
    model = Ratings
    list_display = ('user', 'rating_price', 'rating_quality', 'rating_design',)
    list_filter = ('user', 'rating_price', 'rating_quality', 'rating_design',)

admin.site.register(Product, BestShopAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Ratings, RatingsAdmin)
