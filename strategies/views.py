# strategies/views.py
from django.shortcuts import render, redirect

from core.core_functions import calculate_profit_rate
from .models import StrategyIdea
# 导入核心功能函数
import sys

sys.path.append('..')  # 关联根目录的core_functions.py


def strategy_list(request):
    """策略列表页：展示所有策略+计算收益率"""
    # 从SQLite中查询所有策略
    strategies = StrategyIdea.objects.all()
    # 为每个策略计算收益率
    strategy_data = []
    for s in strategies:
        profit_rate = calculate_profit_rate(
            principal=float(s.principal),
            profit=float(s.expected_profit)
        )
        strategy_data.append({
            'id': s.id,
            'name': s.name,
            'principal': s.principal,
            'expected_profit': s.expected_profit,
            'profit_rate': profit_rate,
            'description': s.description,
            'create_time': s.create_time
        })
    return render(request, 'strategies/index.html', {'strategies': strategy_data})


def add_strategy(request):
    """添加新策略"""
    if request.method == 'POST':
        # 获取表单数据
        name = request.POST.get('name')
        principal = request.POST.get('principal')
        expected_profit = request.POST.get('expected_profit')
        description = request.POST.get('description')
        # 保存到SQLite数据库
        StrategyIdea.objects.create(
            name=name,
            principal=principal,
            expected_profit=expected_profit,
            description=description
        )
        # 重定向到列表页
        return redirect('strategy_list')
    # GET请求返回添加页面
    return render(request, 'strategies/add.html')
