from django.contrib import admin

from . models import Category, Product, Discount



class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_object', 'amount', 'date_begin', 'date_end')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price')
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
