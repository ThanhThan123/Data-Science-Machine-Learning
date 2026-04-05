# Thử các matric  R2 cho regresstion

# Thực hiện bài toán Dự đoán Student Score
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score # New
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV # new
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder # OrdinalEncoder, OneHotEncoder is New
from ydata_profiling import ProfileReport
from sklearn.pipeline import Pipeline # New
from sklearn.impute import SimpleImputer # New
from sklearn.compose import ColumnTransformer # New
from lazypredict.Supervised import  LazyRegressor
from ex18 import x_train

# Đọc file
data = pd.read_csv("StudentScore.xls")
# profile = ProfileReport(data, title="Score Report", explorative=True)
# profile.to_file("score.html")

# # Kiểm tra cột có bao nhiêu giá trị (kiểm tra là lớp hay trường)
print(data["lunch"].unique())

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
# 3 cach OneHot for Nom cũng là có thứ bậc(Mất nhiều dữ liệu bộ nhớ)  (cho chuỗi string có ít loại dữ liệu hơn tfidf)
nom_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('scaler', OneHotEncoder(sparse_output=False))
])

preprocessor = ColumnTransformer(transformers =[
    ("num_feature", num_transformer, ["reading score", "math score"]),
    ("ord_feature", ord_transformer, ["parental level of education","gender", "lunch", "test preparation course" ]),
    ("nom_feature", nom_transformer, ["race/ethnicity"])
])

# reg = Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('model', RandomForestRegressor())
# ])

reg = LazyRegressor(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = reg.fit(x_train, x_test, y_train, y_test)
# Khi số lượng options muổn thử quá lớn
# params = {
#     "preprocessor__num_feature__imputer__strategy": ["median", "mean"],
#     "model__n_estimators": [100, 200, 300],
#     "model__criterion": ["poisson", "absolute_error", "squared_error"],
#     "model__max_depth": [None, 2, 5]
# }
#
# grid_search = RandomizedSearchCV(estimator=reg, param_distributions=params,scoring="r2",n_iter=20, cv=5, verbose=2, n_jobs=3)
# grid_search.fit(x_train, y_train)
# print(grid_search.best_score_)
# print(grid_search.best_params_)
# reg.fit(x_train, y_train)
# y_predict = grid_search.predict(x_test)
# for i, j in zip(y_predict, y_test):
#     print("Predicted value: {}. Actual value: {}".format(i, j))
# print("MAE: {}".format(mean_absolute_error(y_test, y_predict)))
# print("MSE: {}".format(mean_squared_error(y_test, y_predict)))
# print("R2: {}".format(r2_score(y_test, y_predict)))