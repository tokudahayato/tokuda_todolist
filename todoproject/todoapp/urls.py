from django.urls import path
from . import views
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,TaskListLoginView,RegisterTodoApp
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",TaskList.as_view(),name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(),name = "task"),
    path("create_task/", TaskCreate.as_view(),name = "create_task"),
    path("edit_task/<int:pk>/", TaskUpdate.as_view(),name = "edit_task"),
    path("delete_task/<int:pk>/", TaskDelete.as_view(),name = "delete_task"),
    path("login/", TaskListLoginView.as_view(),name = "login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterTodoApp.as_view(), name="register"),

]
