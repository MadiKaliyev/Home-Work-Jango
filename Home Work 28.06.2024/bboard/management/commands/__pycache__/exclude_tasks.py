from django.core.management.base import BaseCommand
from bboard.models import Task 

class Command(BaseCommand):
    help = 'Excludes tasks with a specific condition'

    def handle(self, *args, **kwargs):
        excluded_tasks = Task.objects.exclude(description__icontains='ЗАПИСЬ')

        for task in excluded_tasks:
            print(task.description, task.deadline)
