import pandas as pd
from lazypredict.Supervised import LazyClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ydata_profiling import ProfileReport

from ex18 import x_test

data = pd.read_csv('csgo.csv')

# # Tạo báo cáo
# profile = ProfileReport(data, title="Csgo report", explorative=True)
# # Xuất báo cáo ra file HTML
# profile.to_file("csgo_report.html")


target = "result"

drop_cols = [
    "day", "month", "year", "date",
    "wait_time_s", "match_time_s",
    "team_a_rounds", "team_b_rounds"
]

x = data.drop(columns=drop_cols + [target], errors="ignore")
y = data[target]

# Xử lý missing values
x = x.dropna()
y = y.loc[x.index]

# Encode cột dạng category/string, ví dụ map
x = pd.get_dummies(x, drop_first=True)

# Chia train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Scale dữ liệu
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Train nhiều model
clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(x_train, x_test, y_train, y_test)

print(models)