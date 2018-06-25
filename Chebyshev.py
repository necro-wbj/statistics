#! python3
import statistics
import math
data = [1, 2, 3, 4]  # [這裡輸入資料，用逗號隔開]


def Chebyshew(data, k):
    Standard_Deviation = math.sqrt(statistics.Variance(data))
    k = (statistics.Mean(data) - k) / Standard_Deviation
    result = len(data) * 1 / k**2 * 100 / 100
    return result


print("----------------------------------------")
print("切比雪夫結果(數目) :", Chebyshew(data, 2))  # (,這裡修改需要的數字)
