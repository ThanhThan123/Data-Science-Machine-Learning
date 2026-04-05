# Thực hiện bài toán Dự đoán Student Score
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder # OrdinalEncoder, OneHotEncoder is New
from ydata_profiling import ProfileReport
from sklearn.pipeline import Pipeline # New
from sklearn.impute import SimpleImputer # New
from sklearn.compose import ColumnTransformer # New
from ex18 import x_train

# Đọc file
data = pd.read_csv("StudentScore.xls")
# profile = ProfileReport(data, title="Score Report", explorative=True)
# profile.to_file("score.html")

# # In ra hệ số tương quan
# print(data[["math score", "reading score", "writing score"]].corr())
# # Kiểm tra cột có bao nhiêu giá trị (kiểm tra là lớp hay trường)
print(data["lunch"].unique())
# Mỗi cột có 2 loại norminal (không có thứ bậc) và ordinal có thứ bậc
# print(data["race/ethnicity"].unique()) # Không có thứ bậc
# print(data["parental level of education"].unique())# Có thứ bậc
# some high school, high school, some college, bachelor's degree,associate's degree,master's degree

target  = 'writing score'

x = data.drop(target, axis=1)
y = data[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Có 3 loại dữ liệu Num , Ordi, Nom
# Dùng Pipeline để kết hợp các bước cần fit_transform lại thành 1 khối (khong co thu bac Num)
num_transformer = Pipeline(steps=[
# Điền vào dữ liệu bị khuyết (nếu muốn thay đổi dữ liệu nên dùng = nodepad)
    ('imputer', SimpleImputer(missing_values=-1, strategy='median')),
    ('scaler', StandardScaler())
])

# Co thu bac is OrdinalEncoder (Loại này tiết kiệm dữ liệu tiếc kiệm bộ nhớ)(loại dữ liệu)
education_values = ["some high school", "high school", "some college", "associate's degree","bachelor's degree",
                    "master's degree"]
lunch = x_train["lunch"].unique()
test_values = x_train["test preparation course"].unique()
gender_values = ["male", "female"]
ord_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('scaler', OrdinalEncoder(categories=[education_values, gender_values, lunch,test_values]))
])
# 3 cach OneHot for Nom cũng là có thứ bậc(Mất nhiều dữ liệu bộ nhớ)
nom_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('scaler', OneHotEncoder(sparse_output=False))
])

preprocessor = ColumnTransformer(transformers =[
    ("num_feature", num_transformer, ["reading score", "math score"]),
    ("ord_feature", ord_transformer, ["parental level of education","gender", "lunch", "test preparation course" ]),
    ("nom_feature", nom_transformer, ["race/ethnicity"])
])

reg = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

reg.fit(x_train, y_train)
y_predict = reg.predict(x_test)
for i, j in zip(y_predict, y_test):
    print("Predicted value: {}. Actual value: {}".format(i, j))