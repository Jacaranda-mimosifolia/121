temperature = [-1, 2, 6, 12, 22, 28, 31, 32, 26, 23, 15, 2]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def HeatingCarbonEmissions(t):  # 制热
    dt = 18 - t
    q = dt * (0.3 * 37 / 0.3 + 1.6 * 5 / 0.3 + 0.2 * 12 / 0.3 + 0.25 * 12)
    w = q / 3.5 * 0.001
    c_e = w * 0.28
    return c_e


def CoolingCarbonEmissions(t):  # 制冷
    dt = t - 26
    q = dt * (0.3 * 37 / 0.3 + 1.6 * 5 / 0.3 + 0.2 * 12 / 0.3 + 0.25 * 12)
    w = q / 2.7 * 0.001
    c_e = w * 0.28
    return c_e


carbonemissions = []

for i in range(12):
    t = temperature[i]
    d = days[i]
    value = 0
    if t < 18:
        value = HeatingCarbonEmissions(t)
    elif t > 26:
        value = CoolingCarbonEmissions(t)
    value = value * d
    carbonemissions.append(value)

print(carbonemissions)
print('总和：', sum(carbonemissions))
