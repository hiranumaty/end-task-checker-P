from django.urls import path
from . import views
# ExStateにアクセスするためには認証情報をヘッダーに付与して送信する必要がある
urlpatterns = [
     # 一覧取得
     path('ExState/', views.ExStateListAPIView.as_view()),
     #idで指定した詳細の取得 更新
     path('ExState/<uuid:id>/detail/',
          views.ExStateRetriveAPIView.as_view()),
     path('ExState/<uuid:id>/update/',
          views.ExStateUpDateAPIView.as_view()),
     #TargetMonthでの絞り込み
     path('ExState/<str:TargetMonth>/list/',
          views.ExStateListMonthAPIView.as_view()),
     path('GetTaskMaster/',
          views.GetTasksMaster.as_view()),
     path('GetDeptsMaster/',
          views.GetDeptsMaster.as_view()),
]
