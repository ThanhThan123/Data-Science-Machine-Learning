# chỉ có 2 bộ train với test của bài toán classification
import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
# Giả sử bạn có DataFrame 'data'
data = pd.read_csv("diabetes.csv")
# Step 2 & Step 4
# tách dữ liệu và
target = "Outcome"
# Tách theo chiều dọc
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Step 3 : Tiền xử lý dữ liệu
# Standard Scaler :Biến đổi giá trị theo kỳ vọng
# Gồm 3 thuộc tính
    # scaler.fit(): Để đo kỳ vọng độ lệch chuẩn,
    # scaler.transform(): Biến đổi dữ liệu,
    # scaler.fit_transform(): bằng fit + transform
    # Chỉ được phép biến đổi khi đã có bộ phân chia rồi vd : x_test, x_train
    # Bộ train fit để lưu số đo còn test kế thừa nó nên không được sử dụng fit ở bộ test
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Sử dụng bài toán SVC của classification (Chọn model)
model = SVC()

# Huấn luyện model được chọn
model.fit(x_train, y_train)

# predict-proba
y_predict = model.predict(x_test)

# Đem mô hình đi dự đoán (mặc định)
# for i, j in zip(y_predict, y_test.values):
#     print("Predicted value: {}. Actual value: {}".format(i, j))

# Dự đoán kết hợp metrics (Đưa vào dữ liệu thực tế trước, dự đoán sau)
print("Precision: {}".format(precision_score(y_test, y_predict)))
print("Accuracy : {}".format(accuracy_score(y_test, y_predict)))
print("Recall: {}".format(recall_score(y_test, y_predict)))
print("F1: {}".format(f1_score(y_test, y_predict)))
print(confusion_matrix(y_test, y_predict))

# [[82 17] # 82 sample dự đoán đúng người ta bình thường
#  [24 31]] # 31 người bị bệnh thật . 24 người bị bệnh dự đoán là khoẻ

# # Tạo báo cáo
# profile = ProfileReport(data, title="Diabetes report", explorative=True)
# # Xuất báo cáo ra file HTML
# profile.to_file("diabetes_report.html")

# stats = data.corr()

#random_state : Thuộc tính phân chia bộ text một cách ngẫu nhiên nhưng phải cố định
# data.head(10)
# data.info()
# data.describe()
# data.corr()
# Thư viện ydata_profiling