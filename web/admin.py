from django.contrib import admin
from web.models import *


# Register your models here.
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['Gmodel', 'brand', 'unit', 'type', 'price', 'min_price', 'meno','user','date' ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','date']


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','date']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','date']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id','name','tel','contact','phone','date']
