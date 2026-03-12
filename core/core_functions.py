# core_functions.py - 量化策略核心计算函数
def calculate_profit_rate(principal, profit, risk_rate=0.02):
    """
    计算量化策略的预期收益率（带风险调整）
    :param principal: 本金
    :param profit: 预期收益
    :param risk_rate: 风险调整系数（默认2%）
    :return: 调整后的收益率（百分比，保留2位小数）
    """
    if principal <= 0:
        return 0.0
    # 核心计算公式：(收益/本金 - 风险系数) * 100
    profit_rate = ((profit / principal) - risk_rate) * 100
    return round(profit_rate, 2)