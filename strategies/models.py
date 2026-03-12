# strategies/models.py - 策略想法模型（关联SQLite）
from django.db import models

class StrategyIdea(models.Model):
    """量化策略想法模型"""
    # 策略名称
    name = models.CharField(max_length=100, verbose_name="策略名称")
    # 本金
    principal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="本金")
    # 预期收益
    expected_profit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="预期收益")
    # 策略描述
    description = models.TextField(blank=True, verbose_name="策略描述")
    # 创建时间（自动生成）
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "策略想法"
        verbose_name_plural = "策略想法"
        db_table = "strategy_idea"  # SQLite中的表名

    def __str__(self):
        return self.name