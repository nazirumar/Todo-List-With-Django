
from . views import TaskCreate, TaskDelete, TaskDetail, TaskList, TaskUpdate, CustomLoginVew, RegisterPage
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('login/',  CustomLoginVew.as_view(), name="login" ),
    path('logout/',  LogoutView.as_view(next_page='login'), name="logout"),
    path('register/',  RegisterPage.as_view(), name="register"),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),


]
