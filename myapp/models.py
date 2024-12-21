from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)  # Zmieniono ToDoList na to_do_list
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    

