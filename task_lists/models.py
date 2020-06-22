from django.db import models
from datetime import datetime

# Create your models here.
class Task_List(models.Model):

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'

    name = models.CharField(max_length=254, default='')
    TYPECHOICES = (
        ('Normal', 'Normal'),
        ('Group', 'Group')
    )
    type = models.CharField(max_length=254, choices=TYPECHOICES, default='')
    parent_list = models.IntegerField(blank=True, null=True)
    SORTCHOICES = (
        ('Ascending', 'Ascending'),
        ('Descending', 'Descending')
    )
    sort_by = models.CharField(max_length=254, choices=SORTCHOICES, default='Ascending')
    list_owner = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    list = models.ForeignKey(Task_List, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=254, default='')
    description = models.TextField(default='', blank=True)
    due_date = models.DateField(default=datetime.now)
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    importance = models.CharField(max_length=25, choices=YESNOCHOICES, default='No')
    completed = models.CharField(max_length=25, choices=YESNOCHOICES, default='No')
    assigned_to = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Task_List_Users(models.Model):

    class Meta:
        verbose_name = 'Task List User'
        verbose_name_plural = 'Task List Users'

    list_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    perm_view = models.CharField(max_length=25, choices=YESNOCHOICES, default='No')
    perm_add = models.CharField(max_length=25, choices=YESNOCHOICES, default='No')
    perm_edit = models.CharField(max_length=25, choices=YESNOCHOICES, default='No')
    perm_delete = models.CharField(max_length=25, choices=YESNOCHOICES, default='No')
