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
    list_filter = ['is_active']
    actions = ['publish', 'hidden']

    def publish(self, request, queryset):
        queryset.update(is_active=True)

    publish.short_description = "Опубликовать новость"

    def hidden(self, request, queryset):
        queryset.update(is_active=False)

    hidden.short_description = "Скрыть новость"

    class Meta:
        model = Price


class TeachersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Teachers._meta.fields]
    search_fields = [search.name for search in Teachers._meta.fields]
    list_filter = ['is_active']

    class Meta:
        model = Teachers


class ContactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contacts._meta.fields]
    search_fields = [search.name for search in Contacts._meta.fields]

    class Meta:
        model = Contacts


class OrdersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Orders._meta.fields]
    search_fields = [search.name for search in Orders._meta.fields]
    list_filter = ['is_processed']
    actions = ['processed']

    def processed(self, request, queryset):
        queryset.update(is_processed=True)

    processed.short_description = "Изменить состояние"

    class Meta:
        model = Orders


admin.site.register(Branches, BranchesAdmin)
admin.site.register(Tagline)
admin.site.register(Price, PricesAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Contacts,ContactsAdmin)
admin.site.register(Orders,OrdersAdmin)
