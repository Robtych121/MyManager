from django.contrib import admin
from .models import Task, Task_List, Task_List_Users

# Register your models here.


class TaskListUsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'list_id', 'perm_view', 'perm_add', 'perm_edit', 'perm_delete')


admin.site.register(Task)
admin.site.register(Task_List)
admin.site.register(Task_List_Users, TaskListUsersAdmin)