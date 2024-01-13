from django.contrib import admin
from products.models import Products,Contact,Address,ProductImage
# Register your models here.
# ADD a search field

class PictureInline(admin.StackedInline):
    model =  ProductImage
    search_fields=("name",)
# for Multiple images
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInline]
admin.site.register(Products, ProductAdmin)


class ContactAdmin(admin.ModelAdmin):
    search_fields=("name",)
admin.site.register(Contact,ContactAdmin)

class AddressAdmin(admin.ModelAdmin):
    search_fields=(["name","city"])
admin.site.register(Address)



# Admin Setting
admin.site.site_header="Eco_Select Admin Pannnel"
admin.site.site_index="Welcome to EcoSelect"

# End Admin Pannel