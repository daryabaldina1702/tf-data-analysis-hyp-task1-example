import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.05
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    se = ((p1*(1-p1))/x_cnt + (p2*(1-p2))/y_cnt)**0.5
    z = (p1 - p2) / se
    critical_value = abs(norm.ppf(alpha/2))
    return abs(z) > critical_value
