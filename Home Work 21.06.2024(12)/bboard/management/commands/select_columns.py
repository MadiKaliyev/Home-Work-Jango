from django.core.management.base import BaseCommand
from bboard.models import Task 

class Command(BaseCommand):
    help = 'Selects specific columns from the Task table'

    def handle(self, *args, **kwargs):
        selected_columns = Task.objects.values('description')

        for task in selected_columns:
            print(task)
