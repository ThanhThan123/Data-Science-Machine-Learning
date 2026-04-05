# Data-Science-Machine-Learning

## Mô tả dự án
Dự án **Data-Science-Machine-Learning** tập trung vào việc áp dụng các phương pháp học máy và xử lý dữ liệu để giải quyết các bài toán thực tế. Dự án sử dụng các mô hình học máy từ cơ bản đến nâng cao, từ phân loại, hồi quy, cho đến phân tích chuỗi thời gian. Các mô hình được huấn luyện và đánh giá với các bộ dữ liệu khác nhau, sử dụng các kỹ thuật tiền xử lý dữ liệu, chọn lựa mô hình và tối ưu hóa siêu tham số.

## Các bài toán đã giải quyết
### 1. **Dự báo điểm số học sinh (Student Score Prediction)**:
   - **Mô tả**: Áp dụng mô hình **Linear Regression** để dự đoán điểm số học sinh dựa trên các yếu tố như điểm thi môn toán, đọc và viết.
   - **Kỹ thuật**: Tiền xử lý dữ liệu, chuẩn hóa dữ liệu, huấn luyện mô hình **SVC** và **Random Forest** để đánh giá và dự đoán điểm số.
   - **Đánh giá mô hình**: Sử dụng các chỉ số như **Precision**, **Recall**, **F1-score** và **Accuracy** để đánh giá hiệu quả mô hình.
   
### 2. **Phân loại bệnh tiểu đường (Diabetes Classification)**:
   - **Mô tả**: Phân loại bệnh nhân có nguy cơ mắc bệnh tiểu đường sử dụng mô hình **SVC** và **Random Forest**.
   - **Kỹ thuật**: Tiền xử lý dữ liệu bao gồm chuẩn hóa dữ liệu và sử dụng **GridSearchCV** để tối ưu hóa siêu tham số.
   - **Đánh giá mô hình**: Đánh giá hiệu suất mô hình sử dụng các chỉ số như **Confusion Matrix**, **Precision**, **Recall**.

### 3. **Dự báo CO2 (CO2 Emission Prediction)**:
   - **Mô tả**: Dự đoán mức độ phát thải CO2 dựa trên dữ liệu lịch sử với các mô hình **Linear Regression** và **RandomForestRegressor**.
   - **Kỹ thuật**: Sử dụng **Recursive multi-step** và **Direct multi-step Time Series Forecasting** để dự báo chuỗi thời gian.
   - **Đánh giá mô hình**: Sử dụng **MAE**, **MSE**, và **R2-score** để đánh giá hiệu quả mô hình dự báo.

### 4. **Hệ thống gợi ý phim (Movie Recommendation System)**:
   - **Mô tả**: Triển khai hệ thống gợi ý phim sử dụng các phương pháp **Content-based Filtering** và **Collaborative Filtering**.
   - **Kỹ thuật**: Sử dụng **Cosine Similarity** để tính toán mức độ tương đồng giữa các bộ phim và đề xuất phim cho người dùng.
   - **Đánh giá mô hình**: Đánh giá mô hình với **Precision** và **Recall**.

### 5. **Kiểm định giả thuyết (Hypothesis Testing)**:
   - **Mô tả**: Áp dụng các phương pháp kiểm định giả thuyết để phân tích dữ liệu và đưa ra các quyết định thống kê.
   - **Kỹ thuật**: Sử dụng các khái niệm như **Bias**, **Variance**, và **L1 Regularization** để xử lý **Underfitting** và **Overfitting**.
   - **Quy trình**: Thành lập giả thuyết **H0** và **H1**, chọn thống kê kiểm định **Z** và xác định miền bác bỏ.

### 6. **Dự báo chuỗi thời gian (Time Series Forecasting)**:
   - **Mô tả**: Dự báo dữ liệu chuỗi thời gian như lượng CO2 sử dụng các mô hình **Recursive multi-step** và **Direct multi-step**.
   - **Kỹ thuật**: Tạo dữ liệu chuỗi thời gian, tiền xử lý và huấn luyện mô hình dự báo.
   - **Đánh giá mô hình**: Đánh giá mô hình với các chỉ số **MAE**, **MSE**, và **R2**.

## Các tính năng chính
1. **Xử lý và Tiền xử lý Dữ liệu:**
   - Đọc và xử lý dữ liệu từ các file CSV/Excel.
   - Tiền xử lý dữ liệu như chuẩn hóa, xử lý giá trị thiếu, mã hóa các đặc trưng.
   - Phân chia dữ liệu thành tập huấn luyện và kiểm tra.
   - Sử dụng `StandardScaler` và các công cụ khác để chuẩn hóa và làm sạch dữ liệu.

2. **Các mô hình học máy:**
   - **Phân loại**: Sử dụng các mô hình như `SVC`, `RandomForestClassifier`, và thư viện `LazyClassifier` để phân loại dữ liệu.
   - **Hồi quy**: Áp dụng mô hình `LinearRegression` và `RandomForestRegressor` cho bài toán dự báo.
   - **Dự báo chuỗi thời gian**: Sử dụng các phương pháp như **Recursive multi-step** hoặc **Direct multi-step** Time Series Forecasting.
   - **Kỹ thuật tối ưu hóa mô hình**: Sử dụng `GridSearchCV` và `RandomizedSearchCV` để tối ưu hóa các siêu tham số.

3. **Phân tích và Đánh giá mô hình:**
   - Sử dụng các chỉ số đánh giá như **Precision**, **Recall**, **F1-score**, **Accuracy**, và **Confusion Matrix** để đánh giá mô hình phân loại.
   - Áp dụng các phương pháp như **Cross-Validation** và **Hyperparameter Tuning** để tìm ra mô hình tốt nhất.

4. **Các thuật toán và lý thuyết học máy:**
   - **Lý thuyết về kiểm định giả thuyết** và các phương pháp thống kê.
   - **Dimensionality Reduction** (Giảm số chiều) sử dụng **PCA** và các phương pháp chọn đặc trưng.
   - **Regularization** (L1, L2, Elastic Net) để giảm thiểu Overfitting.
   - **Feature Extraction** và **Feature Selection** để cải thiện hiệu suất mô hình.

5. **Hệ thống gợi ý (Recommendation Systems):**
   - Triển khai các loại hệ thống gợi ý như **Popularity-based**, **Content-based Filtering**, **Collaborative Filtering**, và **Hybrid Recommendations**.

6. **Xử lý ngôn ngữ tự nhiên (NLP):**
   - Áp dụng các kỹ thuật như **Bag of Words**, **TF-IDF**, **N-grams**, và **Lemmatization** để xử lý văn bản.

## Các tính năng chính
1. **Xử lý và Tiền xử lý Dữ liệu:**
   - Đọc và xử lý dữ liệu từ các file CSV/Excel.
   - Tiền xử lý dữ liệu như chuẩn hóa, xử lý giá trị thiếu, mã hóa đặc trưng.
   - Phân chia dữ liệu thành tập huấn luyện và kiểm tra.
   - Sử dụng `StandardScaler` và các công cụ khác để chuẩn hóa và làm sạch dữ liệu.

2. **Các mô hình học máy:**
   - **Phân loại**: Sử dụng các mô hình như `SVC`, `RandomForestClassifier`, và thư viện `LazyClassifier` để phân loại dữ liệu.
   - **Hồi quy**: Áp dụng mô hình `LinearRegression` và `RandomForestRegressor` cho bài toán dự báo.
   - **Dự báo chuỗi thời gian**: Sử dụng các phương pháp như **Recursive multi-step** và **Direct multi-step** Time Series Forecasting.
   - **Kỹ thuật tối ưu hóa mô hình**: Sử dụng `GridSearchCV` và `RandomizedSearchCV` để tối ưu hóa các siêu tham số.

3. **Phân tích và Đánh giá mô hình:**
   - Sử dụng các chỉ số đánh giá như **Precision**, **Recall**, **F1-score**, **Accuracy**, và **Confusion Matrix** để đánh giá mô hình phân loại.
   - Áp dụng các phương pháp như **Cross-Validation** và **Hyperparameter Tuning** để tìm ra mô hình tốt nhất.

4. **Các thuật toán và lý thuyết học máy:**
   - **Lý thuyết về kiểm định giả thuyết** và các phương pháp thống kê.
   - **Dimensionality Reduction** (Giảm số chiều) sử dụng **PCA** và các phương pháp chọn đặc trưng.
   - **Regularization** (L1, L2, Elastic Net) để giảm thiểu Overfitting.
   - **Feature Extraction** và **Feature Selection** để cải thiện hiệu suất mô hình.

5. **Hệ thống gợi ý (Recommendation Systems):**
   - Triển khai các loại hệ thống gợi ý như **Popularity-based**, **Content-based Filtering**, **Collaborative Filtering**, và **Hybrid Recommendations**.

6. **Xử lý ngôn ngữ tự nhiên (NLP):**
   - Áp dụng các kỹ thuật như **Bag of Words**, **TF-IDF**, **N-grams**, và **Lemmatization** để xử lý văn bản.

## Cách sử dụng
1. **Chuẩn bị dữ liệu**:
   - Đảm bảo rằng bạn có các file dữ liệu như `diabetes.csv` hoặc `movies.csv` trong thư mục chính của dự án.
   - Dữ liệu sẽ được xử lý bằng cách loại bỏ các giá trị thiếu, mã hóa các cột kiểu category và chuẩn hóa các đặc trưng.

2. **Huấn luyện mô hình**:
   - Chạy các tập lệnh để huấn luyện các mô hình phân loại hoặc hồi quy tùy thuộc vào bài toán bạn muốn giải quyết.
   - Ví dụ, sử dụng `SVC` cho bài toán phân loại hoặc `RandomForestRegressor` cho bài toán hồi quy.

3. **Đánh giá mô hình**:
   - Các mô hình sẽ được đánh giá bằng các chỉ số như **Accuracy**, **Precision**, **Recall**, **F1-score** và **Confusion Matrix**.
   - Có thể thực hiện tối ưu hóa siêu tham số bằng cách sử dụng `GridSearchCV` hoặc `RandomizedSearchCV`.

4. **Dự báo chuỗi thời gian**:
   - Nếu bạn muốn dự báo chuỗi thời gian, hãy sử dụng các mô hình **Recursive multi-step** hoặc **Direct multi-step** cho các bài toán dự báo như **CO2 emission**.
   
## Cài đặt
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
