# Thực hiện Time Series forecasting ( Mô hình Recursive multi-step Time series Forecasting )và   Error in Machine Learning
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_absolute_error, \
    mean_squared_error, r2_score


def create_ts_data(data, window_size=5):
    i = 1
    while i < window_size:
        data["co2_{}".format(i)] = data["co2"].shift(-i)
        i += 1
    data["target"]  = data["co2"].shift(-i)
    data = data.dropna(axis=0)
    return data

data = pd.read_csv("co2.csv") # Đọc dữ liệu
data["time"] = pd.to_datetime(data["time"]) # convert dạng date time
data["co2"] = data["co2"].interpolate() # sử dụng hàm nội suy để thêm vào data bị None

data = create_ts_data(data)

# fig, ax = plt.subplots()
# ax.plot(data["time"], data["co2"])
# ax.set_xlabel("Year")
# ax.set_ylabel("CO2")
# plt.show()

x = data.drop(["time", "target"], axis=1)
y = data["target"]

train_ratio= 0.8
num_samples = len(x)

# Tách theo 1 chuỗi liên tục
x_train = x[:int(num_samples*train_ratio)]
y_train = y[:int(num_samples*train_ratio)]
x_test = x[int(num_samples*train_ratio):]
y_test = y[int(num_samples*train_ratio):]

# Train model
reg = LinearRegression()
reg.fit(x_train, y_train)

# Test Model
# y_predict = reg.predict(x_test) # là mảng 2 chiều
# print("MAE: {}".format(mean_absolute_error(y_test, y_predict)))
# print("MSE: {}".format(mean_squared_error(y_test, y_predict)))
# print("R2: {}".format(r2_score(y_test, y_predict)))
# # Linear Regresstion (nó có khả năng đưa ra dự đoán chưa thấy bao giờ)
# # MAE: 0.3605603788359235
# # MSE: 0.2204494736034648
# # R2: 0.9907505918201437 (từ một góc mà ra nên hệ số tương quan cao)
# # RandomForestRegressor (đưa ra dự đoán nằm trong khoảng đã từng thấy trong bộ train)
# # MAE: 5.69921271929813
# # MSE: 50.723843787278966
# # R2: -1.1282225263269545
#
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

# Deployment
current_data = [380.5, 390, 390.2, 390.4, 393]
for i in range(10):
    print("Input {}".format(current_data))
    prediction = reg.predict([current_data])[0]
    print("CO2 in week {} is {}".format(i+1, prediction))
    current_data = current_data[1:] + [prediction]
    print("----------------------------")