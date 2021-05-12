from django.urls import path
from . import views
#ここはMASTERDATAを管理するためのURL
urlpatterns =[
    path('getDepts/<str:pk>/detail/',
        views.GetDeptsRetriveAPIView.as_view()),
    path('getDepts/<str:pk>/update/',
        views.ChangeDeptsAPIView.as_view()),
    path('getDepts/create/',
        views.CreateDeptsAPIView.as_view()),
    path('getDepts/checkValid/<str:TargetDay>/',
        views.CheckDeptsValidAPIView.as_view()),
    path('getTasks/<str:pk>/detail/',
        views.GetTasksRetriveAPIView.as_view()),
    path('getTasks/<str:pk>/update/',
        views.ChangeTasksAPIView.as_view()),
    path('getTasks/create/',
        views.CreateTasksAPIView.as_view()),
    path('getTasks/checkValid/<str:TargetDay>/',
        views.CheckTasksValidAPIView.as_view())
]