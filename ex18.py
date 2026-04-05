
import pandas as pd
from lazypredict.Supervised import LazyClassifier
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import os


# data = pd.read_csv("diabetes.csv")

data = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__name__)), "diabetes.csv"))

target = "Outcome"
# Tách theo chiều dọc
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Hyper paramete
# model = RandomForestClassifier(n_estimators=200,criterion="gini", random_state=100)
# model.fit(x_train, y_train)
#
# y_predict = model.predict(x_test)
# print(classification_report(y_test, y_predict))

# params = {
#     "n_estimators": [100, 200, 300],
#     "criterion": ["gini", "entropy", "log_loss"]
# }

# Dùng GirdSearch để tìm xem bộ hyper parameters tốt nhất
# grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=100), param_grid=params,scoring="recall", cv=4, verbose=2)
# grid_search.fit(x_train, y_train)
# print(grid_search.best_params_)
# print(grid_search.best_score_)
# print(grid_search.best_estimator_)
# y_predict = grid_search.predict(x_test)
# print(classification_report(y_test, y_predict))

# Sử dụng thư viện lazypredict để tìm xem nào có bộ performance tốt nhất
clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(x_train, x_test, y_train, y_test)




