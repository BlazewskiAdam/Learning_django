import os
import django
from myapp.models import ToDoList, Item

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()


# Create a ToDoList object
to_do_list = ToDoList(name='Daily Tasks')
to_do_list.save()

# Create some Item objects and associate them with the ToDoList
item1 = Item(to_do_list=to_do_list, name='Buy groceries', description='Milk, Bread, Eggs', completed=False)
item1.save()

item2 = Item(to_do_list=to_do_list, name='Read a book', description='Read 30 pages of a novel', completed=False)
item2.save()

item3 = Item(to_do_list=to_do_list, name='Exercise', description='30 minutes of running', completed=False)
item3.save()

items = Item.objects.all()

for i in items:
    print(f'Item: {i.name}, Description: {i.description}, Completed: {i.completed}')