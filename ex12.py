# Mô hình Supervised Learning
    # Labeled data ( dữ liệu có nhãn)
        # Tabular data (dữ liệu dạng bảng) (excel và csv)
            # Cột (feature) : Đặc trưng hoặc thuộc tính
            # label (target) : Cột trả ra kết quả
            # Hàng (temple hoặc item)
                # feature vector  -> corresponstring (out put) # 1 dòng
                # feature matrix -> label/ target vector (out put) # lấy tất cả hàng
    # Model Training (Huấn luyện mô hình)
        # Input : feature vector (1 hàng)
        # Model:
        # Output: prediction and label
        # feature vector -> Model -> loss(Thể hiện sự chênh lệch giữa bài toán và thực tế
        # gồm (prediction >< label)

        # Input : feature matrix (cả vector)
        # Model:
        # Output: prediction and label
        # feature vector -> Model -> loss -> update Model(Thể hiện sự chênh lệch giữa bài toán
        # và thực tế gồm (prediction >< label)

        # Epoch: Số lần cả bộ dữ liệu được xử lý qua
    # Loss function (Hàm mất mát)
        # L1 loss Bài toán mọi example đều được chú ý
            # Loss = Σ|yprediction -yactual|
            # Các gọi tên
                # Least Absolute Deviations (LAD)
                # Absolute Error
                # Mean of these Absolute Error
        # L2 loss (Dùng để tối thiểu hoá quy trình) Focus vào các  sai số lớn ( Loại bỏ outdier)
            # Loss = Σ(yprediction -yactual) ^ 2
            # Các gọi tên
                # Least Square Error (LS)
                # Squared Error
                # Mean of these Squared Error
    # Phân chia dataset
        # Training set
            # Được dùng để huấn luyện mô hình
        # Validation set
            # Không được dùng để huần luyện mô hình (Đánh giá xem mô hình có đi đúng hướng hay không)
            # Có bị overating hay không
        # Test set
            # Sẽ chỉ được dùng khi quá trình huấn luyện đã kết thúc
            # Dùng để đánh giá lần cuối. Để đưa ra performance của mô hình đó so với các mô h khác
        # K-fold cross validation (sử dụng khi bộ dữ liệu nhỏ)
            # Mọi sample sẽ được tham gia vào quá trình validation
    # Các bài toán trong supervised learning
        # Mô hình Classfication ( phân loại)
            # Binary Classfication
                # one thing or another
            # Multiclass classification
                # more than one thing or another
            # Multilabel classfication
                # Một example có 1 hoặc nhiều hơn 1 labels
        # Số liệu phân loại (Classfication metrics) (ma trận 2 x 2) (dùng để đánh giá performance)
            # TP: true positive (true là so sánh giữa nhãn và dự đoán) (positive dự đoán của thuật toán)
            # FP: false positive
            # FN: false negative
            # TN: true negative
            # Tính độ chính xác
                # Accuracy: (TP+TN)/All : Độ chính xác tổng quát
                # Precision: TP/(TP+FP) : Tính độ chính xác đối với class +
                    # Ý nghĩa mẫu số: Tổng số Positive thực sự
                    # Chọn những example quan trọng nhất mới cho vào:
                        # Ví dụ chọn những quán ăn thực sự rất ngon
                        # Ví dụ 2: Tăng nhiều vòng kiểm tra vào
                    # Cố gắng tăng Precision thì Recall sẽ giảm
                # Recall: TP/(TP+FN): Độ bao phủ đối với các dự đoán về class +
                    # Ý nghĩa mẫu số: Số lượng example positive thực sự
                    # Muốn có recall cao thì cho tất cả các example bạn biết vào
                    # Tăng recall precision sẽ giảm
                # F1 Score: (2*Pre*Re)/(Pre+Re): Trung bình điều hoà giữa Precision và Recall
                    # Khi cùng cực lắm mới dùng F1 thường dùng trong môi trường hàng lâm
        # Ví dụ: Mô hình dự đoán covid : Người bị covid: Positive, Người thường: negative
            # Tập trung vào Recall : Có thể bắt nhầm người sai
            # Nhưng không thể để lọt người bị