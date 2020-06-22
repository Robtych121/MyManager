from .models import Task_List, Task_List_Users


def get_task_lists(request):
    task_lists = Task_List.objects.exclude(parent_list__isnull=False).order_by('name')
    task_list_users = Task_List_Users.objects.filter(user_id=request.user.id)
    return { 'nav_task_lists': task_lists, 'task_list_users': task_list_users}


def get_sub_task_lists(request):
    sub_task_lists = Task_List.objects.exclude(parent_list__isnull=True).order_by('name')
    return { 'sub_task_lists': sub_task_lists}