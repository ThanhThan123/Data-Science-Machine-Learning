    # Chỉ số Gini trong Decision Tree
        #  Gini = 1 - i=1Mc(pi)^2
            # Gini Impurity (Độ tạp của chỉ số)
                # Chỉ số này lớn nhất là 0.5
                # Chỉ số này càng nhỏ càng tốt
                # Phân chia đến khi nào các nốt nó lệch thì chọn nốt đó
                # Dựa vào độ sâu, đội sample, độ lệch của nốt lá
            # Nhược điểm : 1 vài thay đổi nhỏ nó sẽ ảnh hưởng đến cả kiến trúc ảnh hưởng
# Ensemble method
    # Bagging
        # Mô hình sẽ chạy song song với nhau
        # Gộp kết quả lại thành kết quả mới
        # Random Forest
            # Kết hợp nhiều decision tree
            # Bao gồm:
                # S1.Các tập training data từ 1,2,...n
                # S2.Các Decision Tree từ 1,2...n
                # S3.Voting
                # AS.
            # Tại sao không dùng toàn bộ dữ liệu vì nó mất đi sự đa dạng của kết quả

    # Boosting
        # Mô hình chạy nối tiếp
        # Mô hình 2 chạy tập trung vào lỗi của mô hình 1 chạy
        # và tiếp tục tiếp diễn
    # Stacking