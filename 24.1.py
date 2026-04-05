# Thực hiện Time Series forecasting ( Mô hình Direct multi-step Time series Forecasting )và   Error in Machine Learning
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_absolute_error, \
    mean_squared_error, r2_score


def create_ts_data(data, window_size=5, target_size=3):
    i = 1
    while i < window_size:
        data["co2_{}".format(i)] = data["co2"].shift(-i)
        i += 1
    i = 0
    while i < target_size:
        data["target_{}".format(i+1)] = data["co2"].shift(-i-window_size)
        i += 1
    data = data.dropna(axis=0)
    return data

data = pd.read_csv("co2.csv") # Đọc dữ liệu
data["time"] = pd.to_datetime(data["time"]) # convert dạng date time
data["co2"] = data["co2"].interpolate() # sử dụng hàm nội suy để thêm vào data bị None

window_size = 5
target_size = 3
data = create_ts_data(data, window_size, target_size)

targets = ["target_{}".format(i+1) for i in range(target_size)]
x = data.drop(["time"] + targets , axis=1)
y = data[targets]

train_ratio= 0.8
num_samples = len(x)

# Tách theo 1 chuỗi liên tục
x_train = x[:int(num_samples*train_ratio)]
y_train = y[:int(num_samples*train_ratio)]
x_test = x[int(num_samples*train_ratio):]
y_test = y[int(num_samples*train_ratio):]



regs = [LinearRegression() for _ in range(target_size)]
for i,reg in enumerate(regs):
    reg.fit(x_train, y_train["target_{}".format(i+1)])

r2 = []
mse = []
mae =[]
for i, reg in enumerate(regs):
    prediction = reg.predict(x_test)

    y_predict = reg.predict(x_test) # là mảng 2 chiều
    mae.append(mean_absolute_error(y_test["target_{}".format(i+1)], y_predict))
    mse.append(mean_squared_error(y_test["target_{}".format(i+1)], y_predict))
    r2.append(r2_score(y_test["target_{}".format(i+1)], y_predict))

print("R2 {}".format(r2))
print("MAE {}".format(mae))
print("MSE {}".format(mse))

# Visualization
# fig, ax = plt.subplots()
# ax.plot(data["time"][:int(num_samples*train_ratio)], data["co2"][:int(num_samples*train_ratio)], label="train"),
# ax.plot(data["time"][int(num_samples*train_ratio):], data["co2"][int(num_samples*train_ratio):], label="test"),
# ax.plot(data["time"][int(num_samples*train_ratio):], y_predict, label="prediction"),
# ax.set_xlabel("Year")
# ax.set_ylabel("CO2")
# ax.legend()
# ax.grid()
# plt.show()