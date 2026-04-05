
import re
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer # new Lib
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline # New
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.feature_selection import SelectKBest, chi2, SelectPercentile # New
from imblearn.over_sampling import RandomOverSampler # New
# New Sử dụng regexr để lấy mã bang của cột location
def filter_location(location):
    result = re.findall(r",\s[A-Z]{2}$", location)
    if len(result) != 0:
        return result[0][2:]
    else:
        return location

data = pd.read_excel("final_project.ods", engine="odf", dtype=str) # dtype vs engine is new
data = data.dropna(axis=0) # Drop 1 ô dư
data["location"] = data["location"].apply(filter_location) # New
target="career_level"

# Xẻ dữ liệu theo chiều dọc và chiều ngang
x = data.drop(target, axis=1)
y = data[target]
x_train, x_test, y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=100, stratify=y) # stra is new

# Balance Data (over sample) #new
# ros = RandomOverSampler(random_state=0, sampling_strategy={
#     "director_business_unit_leader": 500,
#     "specialist": 500,
#     "managing_director_small_medium_company":500,
#     "bereichsleiter": 1000
# }) # New sử dụng Balance data
# x_train, y_train = ros.fit_resample(x_train, y_train)


# Chỉ ra cách chúng ta tiền xử lý dữ liệu
preprocessor = ColumnTransformer(transformers=[
    ("title_ft", TfidfVectorizer(stop_words="english", ngram_range=(1, 1)), "title"),
    ("location_ft", OneHotEncoder(handle_unknown="ignore"), ["location"]),
    ("des_ft", TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=0.01, max_df=0.95), "description"),
    ("function_ft", OneHotEncoder(handle_unknown="ignore"),["function"]),
    ("industry_ft", TfidfVectorizer(stop_words="english",ngram_range=(1, 1)), "industry")
])

# Xây dựng Pipeline
cls = Pipeline(steps=[
    ("preprocessor", preprocessor),
    # ("feature_selector", SelectKBest(chi2, k=300)), # làm việc với 300 features
    ("feature_selector", SelectPercentile(chi2, percentile=5)), # Phải biết có tổng bao nhiêu số feature
    ('model', RandomForestClassifier()),
])

# Sử dụng GridSearch
params={
    # "n_estimators": [100, 200, 300],
    "model__criterion": ["gini", "entropy","log_loss"],
    "feature_selector__percentile": [1, 5, 10]
}
grid_search = GridSearchCV(estimator=cls, param_grid=params,scoring="recall_weighted", cv=4, verbose=2)
grid_search.fit(x_train, y_train)
# print(grid_search.best_params_)
# print(grid_search.best_score_)
# print(grid_search.best_estimator_)
y_predicted = grid_search.predict(x_test)
print(classification_report(y_test, y_predicted))

# Cách biết có bao nhiêu feature
# results = cls.fit_transform(x_train, y_train)
# print(results.shape)

# Huẩn luyện dữ liệu
cls.fit(x_train, y_train)
y_predicted = cls.predict(x_test)

# Đem mô hình đi dự đoán
print(classification_report(y_test, y_predicted))

# Câu lệnh check xem bộ dữ liệu có bị thiếu không
# print(data.isna().sum()) # New
# Dùng để can thiệp vào sự quan trọng của mô hình tfidf  min_df=0.01, max_df=0.95 (New)

# không min_đf và max_df.
#  accuracy                           0.68      1615
#  macro avg      0.46      0.26      0.25      1615
#weighted avg       0.64      0.68      0.62      1615
# có min_đf và max_df có, không có SelectKBest với 850k features
#                               accuracy                           0.74      1615
#                              macro avg       0.51      0.29      0.29      1615
#                           weighted avg       0.72      0.74      0.69      1615
#   có min_đf và max_df có,  có SelectKBest với 300 features
#                               accuracy                           0.76      1615
#                              macro avg       0.52      0.32      0.33      1615
#                           weighted avg       0.75      0.76      0.74      1615

# Quy tắc chia dữ liệu 1 sample chỉ có thể nằm trong 1 bộ test hoặc train không thể chung