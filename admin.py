from django.contrib import admin
from todo.models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_complete')  # Change 'is_completed' to 'is_complete'

admin.site.register(Todo, TodoAdmin)
