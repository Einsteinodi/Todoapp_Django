from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from Todos_app.models import list

# Create your views here.
def list_display(request):
    context={'todo_list' : list.objects.all()}
    return render(request,'todos.html',context)



def insert_todo_item(request: HttpRequest):
    todo = list(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')



def delete_todo_item(request,todo_id):
    todo_to_delete = list.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')









