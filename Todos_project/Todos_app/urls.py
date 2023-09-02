from django.urls import path
from Todos_app import views


app_name='Todos_app'


urlpatterns = [
    path('list/',views.list_display ),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
]
