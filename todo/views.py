from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem
from django.views.generic import ListView
# Create your views here.

class  todoListView(ListView):
    model=TodoItem
    context_object_name='all_items'
    paginate_by=3
    template_name='todo.html'

def addTodo(request):
    content=request.POST['content']
    new_item=TodoItem.objects.create(content=content)
    new_item.save()
    return redirect('todoListView')
def deleteTodo(request, todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()

    return redirect('todoListView')
