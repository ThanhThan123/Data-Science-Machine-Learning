# Lý thuyết của Time series forecasting và  Error in Machine Learning
# Time series forecasting
    # Các kiểu dữ liệu cơ bản
        # Time series data
            # Time series + exogenous variable (biến ngoại sinh)
                # Ví dụ : Thời tiết + Độ ẩm
    # Các bài toán của Time series forecasting
        # Recursive multi-step Time series Forecasting
            # Loại phần tử
                # Observed value
                # Predicted value
                # Predictors (lags)
                # Model trained to predict step+1
            # Nhược điểm
                # Dự đoán dữ liệu trong tương lai theo kiểu dời từng ô
                # Nếu dự đoán T+1 sai thì càng dời ô càng sai
        # Direct multi-step Time series Forecasting
            # Sử dụng n số mô hình
                # Các mô hình chuyên biệt
                    # Ví dụ có một mô hình chuyên dự đoán T+1, mô hình khác chuyên dự đoán T+2,...
            # Loại phần tử
                # Observed value
                # Predicted value
                # Predictors (lags)
                # Model trained to predict step+1
                # Model trained to predict step+2,...
            # Ưu điểm
                # Không sử dụng dữ liệu chưa xảy ra
            # Nhược điểm
                # Tốn memory
            # Lưu ý : Các mô hình liên quan đến tự nhiên thì dễ dự đoán hơn và còn liên quan đến con người thì khó
# Error in Machine Learning
    # Có 2 lỗi chính trong Machine Learning
        # Lỗi có thể giảm thiều (Reducible Error)
            # Machine Learning Errors -> Reducible Error -> Bias (bậc 1)
             # Bias :
                # Sai lệch giữa prediction(dự đoán mô hình) và actual label (giá trị thật tế)
                # Cho ta biết khả năng dự đoán chính xác của mô hình
                # Bias càng bé càng tốt (bai ếch)
                # High bias means:
                    # Over-simplified model
                    # Under-fitting
                    # High error on both train và test sets
            # Machine Learning Errors -> Reducible Error -> Variance (bậc 2)
                # Mức độ thay đổi của độ chính xác của prediction nếu input thay đổi
                # Cho ta biết khả năng tổng quát hoá mô hình
                # Variance càng bé càng tốt
                # High variance means:
                    # Overly-complex model
                    # Over-fitting
                    # Low error on training set but high error in test set
            # Muốn giảm Variance thì Bias tăng và ngược lại
            # Trong thực tế ta thường giải các mô hình gặp high bias và low variance và high variance và low bias
          # Choose Machine Learning model based on data
            # Low bias + high variance
                # Decision tree
                # Random Forest
                # K-nearest neighbours
                # Kernel SVM
                # -> Phù hợp khi có nhiều data và ít features
            # High bias + low variance
                # Linear Regesstion
                # Logistic regesstion
                # Linear SVM
                # -> Phù hợp khi có ít data và nhiều features
            # Extra
                # Khi có nhiều data và nhiều features
                    # Giảm chiều dữ liệu (e.g.PCA)
                    # Sử dụng Neural network
        # Lỗi không thể giảm thiểu (Irreducible Error)
            # Machine Learning Errors -> Irreducible Error
    # Choose Machine Learning model based on business domain (cần quan tâm khi đi làm)
        # Which matric is important?
            # Accuracy, precision, recall,F1,...
        # What is the priority?
            # Speed: self-driving car app need to be realtime -> fast
            # Memory: Model deployed in embedded device needs to be small (ip)
            # Accuracy: In medical field, accuracy is the most important factor
        # Interpretability ?
            # Do you need to explain result ?
            # Do you need to find out which features are important ?