from django.contrib import admin
from .models import Record

# Register your models here.


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('rid', 'name', 'phone_number', 'address', 'created')
    list_filter = ('created', )
    search_fields = ('rid', 'name', 'phone_number', 'address')
