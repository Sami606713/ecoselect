from django.contrib import admin
from products.models import Products,ProductImage,Contact,Address,Order
# Register your models here.
# ADD a search field

class PictureInline(admin.StackedInline):
    model =  ProductImage
    max_num = 4  # Set the maximum number of forms to 1
    can_delete = False
    search_fields=("name",)
# for Multiple images
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInline]
admin.site.register(Products, ProductAdmin)


class ContactAdmin(admin.ModelAdmin):
    search_fields=("name",)
admin.site.register(Contact,ContactAdmin)


class OrderInline(admin.StackedInline):
    model=Order
    max_num = 1  # Set the maximum number of forms to 1
    can_delete = False  # Prevent deletion of existing Order objects


class AddressAdmin(admin.ModelAdmin):
    search_fields=["name","city"]
    inlines=[OrderInline]
admin.site.register(Address,AddressAdmin)

# Admin Setting
admin.site.site_header="Eco_Select Admin Pannnel"
admin.site.site_index="Welcome to EcoSelect"

# End Admin Pannel