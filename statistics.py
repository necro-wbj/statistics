#!python3
import math
data = [30, 36, 47, 50, 52, 52, 56, 60, 63, 70, 70, 110]  # [這裡放數值用逗號隔開]


# 中位數
def Median(data):
    list.sort(data)
    length = len(data)
    if length % 2 == 0:
        if length == 2:
            return sum(data) / 2
        else:
            return (data[length // 2 - 1] + data[length // 2]) / 2
    else:
        return data[length // 2]


# 平均數
def Mean(data):
    length = len(data)
    return sum(data) / length


# 眾數
def Mode(data):
    result = list()
    times = [0, 0]
    for i in set(data):
        times[0] = data.count(i)
        if times[0] > times[1]:
            times[1] = times[0]
            result = list([i])
        elif times[0] == times[1]:
            result.append(i)
    return result


# 四分位數
def Quartile(data):
    list.sort(data)
    length = len(data)
    Q = [0, 0, 0]
    Q[1] = Median(data)
    if length % 2 == 0:
        Q[0] = Median(data[:length // 2])
        Q[2] = Median(data[length // 2:])
    else:
        index = data.index(Q[1])
        Q[0] = Median(data[:index])
        Q[2] = Median(data[index + 1:])
    return Q


# 變異數
def Variance(data):
    length = len(data)
    return sum(map(lambda x: (x - Mean(data))**2, data)) / length


list.sort(data)
print("資料：", *data)
print("平均數：", Mean(data))
print("眾數：", *Mode(data))
Quartile = Quartile(data)
print("第1四分位數：", Quartile[0])
print("第2四分位數：", Quartile[1])
print("第3四分位數：", Quartile[2])
print("IQR：", Quartile[2] - Quartile[0])
print("1.5倍IQR：", 1.5 * (Quartile[2] - Quartile[0]))
print("變異數：", Variance(data))
print("標準差", math.sqrt(Variance(data)))
