from django.contrib import admin
from .models import *

# Register your models here.


class BranchesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Branches._meta.fields]
    search_fields = [search.name for search in Branches._meta.fields]

    class Meta:
        model = Branches


class PricesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Price._meta.fields]
    search_fields = [search.name for search in Price._meta.fields]

    class Meta:
        model = Price


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]
    search_fields = [search.name for search in News._meta.fields]

    class Meta:
        model = Price


class TeachersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Teachers._meta.fields]
    search_fields = [search.name for search in Teachers._meta.fields]

    class Meta:
        model = Teachers


admin.site.register(Branches, BranchesAdmin)
admin.site.register(Tagline)
admin.site.register(Price, PricesAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Teachers, TeachersAdmin)
