from django.urls import path
from . import views
# ExStateにアクセスするためには認証情報をヘッダーに付与して送信する必要がある
urlpatterns = [
    # 一覧取得
    path('ExState/', views.ExStateListAPIView.as_view()),
    #このパターンで分岐しないのは何故
    path(r'^ExState/Detail/<pk>/$',
         views.ExStateRetriveAPIView.as_view())
    # 選択したモデルの変更
]
