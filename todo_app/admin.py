from django.contrib import admin
from .models import TodoItem, Tag

admin.site.register(Tag)

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp', 'due_date')
    list_filter = ('status', 'tags')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'due_date', 'tags', 'status')}),
        ('Timestamps', {
            'fields': ('timestamp',),
            'classes': ('collapse',),
        }),
    )
