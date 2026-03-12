from django.urls import path
from . import views

urlpatterns = [
    path('', views.strategy_list, name='strategy_list'),  # 策略列表页
    path('add.html/', views.add_strategy, name='add_strategy'), # 添加策略页
]