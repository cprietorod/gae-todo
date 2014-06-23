import endpoints
from google.appengine.ext import ndb
from protorpc import messages
from protorpc import message_types
from protorpc import remote


class TodoModel(ndb.Model):
  title = ndb.StringProperty()
  completed = ndb.BooleanProperty()


class Todo(messages.Message):
  title = messages.StringField(1)
  completed = messages.BooleanField(2)


class TodoList(messages.Message):
  items = messages.MessageField(Todo, 1, repeated=True)


@endpoints.api(name='todos', version='1',
               description='API for Task Management')
class TodoApi(remote.Service):

  @endpoints.method(Todo, Todo,
                    name='todo.insert',
                    path='todo',
                    http_method='POST')
  def insert_todo(self, request):
    todoModel = TodoModel()
    todoModel.title = request.title
    if request.completed:
        todoModel.completed = request.completed
    else:
        todoModel.completed = False
    todoModel.put()
    return request

  @endpoints.method(message_types.VoidMessage, TodoList,
                    name='todo.list',
                    path='todos',
                    http_method='GET')
  def list_todos(self, unused_request):
    todos = []
    for todo in TodoModel.query():
      todos.append(Todo(title=todo.title, completed=todo.completed))
    return TodoList(items=todos)


application = endpoints.api_server([TodoApi])
