import numpy as np

# 月份天数
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 两地温度
monthly_avg_temps_1 = np.array([9, 11, 15, 17, 20, 22, 21, 20, 18, 16, 13, 10])
monthly_avg_temps_2 = np.array([-1, 2, 6, 12, 22, 28, 31, 32, 26, 23, 15, 2])

# 热导系数
wall_conductivity = 0.3
roof_conductivity = 0.2
window_conductivity = 1.6
floor_conductivity = 0.25

# 热传导面积
wall_area = 2 * (4 + 3) * 3 - 5
roof_area = 4 * 3
window_area = 5
floor_area = 4 * 3

# 性能系数
COP = 3.5
EER = 2.7


def calculate_carbon_emission(monthly_avg_temp):
    for i in days:

        if monthly_avg_temp < 18:
            temp_diff = 18 - monthly_avg_temp
            heat_loss = (wall_area * wall_conductivity / 0.3 + roof_area * roof_conductivity / 0.3 +
                         window_area * window_conductivity / 1 + floor_area * floor_conductivity / 0.3) * temp_diff
            electricity_consumption = heat_loss / COP * 0.001
        elif monthly_avg_temp > 26:
            temp_diff = monthly_avg_temp - 26
            heat_gain = (wall_area * wall_conductivity / 0.3 + roof_area * roof_conductivity / 0.3 +
                         window_area * window_conductivity / 1 + floor_area * floor_conductivity / 0.3) * temp_diff
            electricity_consumption = heat_gain / EER * 0.001
        else:
            electricity_consumption = 0

        carbon_emission = electricity_consumption * 0.28 * i
        return carbon_emission


total_carbon_emission_1 = sum([calculate_carbon_emission(temp) for temp in monthly_avg_temps_1])
total_carbon_emission_2 = sum([calculate_carbon_emission(temp) for temp in monthly_avg_temps_2])
print("Total yearly carbon emission_1:", total_carbon_emission_1, "kg")
print("Total yearly carbon emission_2:", total_carbon_emission_2, "kg")
