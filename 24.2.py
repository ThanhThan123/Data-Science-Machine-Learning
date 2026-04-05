# Tips for choose Machine Learning model
    # Start with  a simple model
        # Choose the simplest model first
        # if it is good enough, you even do not need to try another model
    # Try differences model and shortlist the best one?
    # Do Hyperparameter Tuning for each models ?
        # GridSearchCV if the number of combinations is small
        # RandomizedSearchCV if the number of combination is large
    # Compare amongst the best models with the best hyperparameters to pick up the best one
# Underfitting and Overfitting
    # Xử lý Underfitting
        # Tăng độ phức tạp của mô hình

    # Xử lý Overfitting : Mô hình phức tạp quá so với dữ liệu
        # Kỹ thuật Regularization (Làm giảm độ phức tạp của mô hình)
            # Regularization
                # L1 Regularization : Có xu hướng ép 1 vài cái quest về 0 (tên gọi khác Lasso)
                    # Loss function + Regularization Term
                    # Nơi giao nhau giữa Loss function và  Regularization Term là điểm giao nhau giữa 2 cái này
                # L2 Regularization :  Có xu hướng ép 1 vài cái quest về số bé nhưng không về 0 (Ridge)
                    # Loss function + Regularization Term
                    # Nơi giao nhau giữa Loss function và  Regularization Term là điểm giao nhau giữa 2 cái này
                # L1 + L2 : (Elastic Net)
# Dimensionality Reduction ( Giảm số lượng features(cột))
    # Feature Selection :
        # Original Selection
            # Original features are maintained
        # Feature Extraction :
            # Features are transformed to a new space
# Khái niệm Singularity
# Khái niệm của curse of Dimensionality
    # Số chiều càng tăng thì bài toán càng phức tạp
    # Có 1 rule : Số lượng cột tăng theo cấp số cộng, tương đương với số lượng sample tăng cấp số nhân
    # Có 1 cách để xử lý curse of Dimensionality là giảm cột
    # Feature Selection : Đây dùng để giảm những cột
        # Thông thường đánh giá Correlation Coefficient:
            # ví dụ lấy 4 features có hệ số tương quan với target lớn nhất
            # Dựa vào đa cộng tuyến u
        # Sử dụng variance threshold
        # Sử dụng Lasso(L1)
        # Random-Forest có thuộc tính feature_important
# Khái niệm  Feature Extraction
    # Principle Component Analyst (quan trọng) sử dụng tốt cho bài toán Feature Extraction
        # Sử dụng hiệu quả với bộ dữ liệu nhiều chiều
            # Variance in data (Phương sai):
            # Covariance vs Correlation
                # Covariance: Mức độ phân tán giữa hai biến xung quanh mức độ trung bình của chúng
                # Correlation : Độ tuơng quan giữa chúng

