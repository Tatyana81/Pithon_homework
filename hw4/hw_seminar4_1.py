# 1.Вычислить число c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141,  10^{-1} ≤ d ≤10^{-10}
import math
d = 0.0001
d1 = str(d)
count = abs(d1.find('.') - len(d1)) - 1
print(f'Резульатат округления числа Пи {math.pi} с точностью {d} равен {round((math.pi),count)}')
