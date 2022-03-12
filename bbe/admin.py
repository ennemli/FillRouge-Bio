from django.contrib import admin
from bbe.models import Client, Product,ProductImage

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass

class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)