# Step 2: Statistics (Thống kê)
    # Loại dữ liệu
        # Tất cả các features và target đều là numerical data
        # Có 2 feature là float còn lại là int
    # Thường sử dụng thư viện pandas (statistical of Data)
        # from pandas import read_csv
        # data = read_csv("name_file")
            # mean: Giá trị kỳ vọng
            # std: standard deviation ( Độ lệch chuẩn)
            # Median: Trung vị: Phần tử ở giữa sau khi đã sắp xếp
                # 25% : First Quartile
                # 50% : Second Quartile
                # 75% : Thirst Quartile
    #Category Distribution (Loại đóng góp)
        # 0 : 500 người thường
        # 1 : 268 bệnh nhân
# Step 3: Handle missing or invalid values
    # Handle missing or invalid value : Xử lý dữ liệu bị thiếu hoặc sai
        # Nếu tỷ lệ bị khuyết dưới 5% -> Drop dữ liệu
        # Nếu hơn 5% và đó là dữ liệu quan trọng
    # Remove outliers: Loại bỏ outliers (những thành phần khác biệt với những thành phần còn lại)
        # Thành phần đó không phản ánh đa số
        # Có những bài toán chúng ta cần lấy outliers
            # Ví dụ mô hình dự đoán bệnh ung thư
    # Data Transformation : Biến đổi dữ liệu
        # Tiền xử lý Numerical features
            # MinMaxScaler
                # Tác dụng:
                    # Nó giúp ta biến đổi giá trị từ 0 -1
                # Ưu điểm: Đơn giản
                # Nhược điểm bị ảnh hưởng rất nặng bởi outdiers
            # Standard Scaler
                # Tính ra kỳ vọng và độ lệch chuẩn
                # Ảnh hưởng nhẹ hơn bởi outdiers
                # Nằm trong khoảng từ -3 - 3
                # Công thức : z = (x - u) / s
                    # x: giá trị ban đầu
                    # u : giá trị kỳ vọng
                    # s :  standard deviation (Độ lệch chuẩn)
            # RobustScaler
        # Tiền xử lý Ordinal features (Đặc điểm thứ tự)
            # Đưa về dạng số 0 - 4
            # 2 mục đích :
                # Giúp mô hình nhận định giá trị này khác giá trị kia
                # Dạy cho mô hình giữa các giá trị này có thứ bậc
                    # ví dụ: Tăng dần, Giảm dần, Tốt dần
        #  Các cách mã hoá nominal features (Đặc điểm định danh)
            # One-hot encoding (vector)
            # Không có thứ bậc và gần gũi giữa các vector (từ)
                # Hệ trực chuẩn
                    #  Red -> 1, 0, 0, 0
                    #  Blue -> 0, 1, 0, 0
                    #  Green -> 0, 0, 1, 0
                    #  Black -> 0, 0, 0, 1
                # Advantage
                    # Simple
                # Disadvantage
                    # Sparse Data (Dữ liệu thưa thớt)
            # Hash encoding (băm) (vector)
                # Giúp phân biệt giữa mô hình này với mô hình kia
                # Không có thứ bậc giữa các giá trị
                # Hệ
                    # USA -> 1, 0, 0
                    # UK -> 0, 0, 1
                    # Korea -> 0, 1, 0
                    # Russia -> 1, 0, 0
                # Advantage
                    # Simple
                    # Less sparse
                # Disadvantage
                    # Collision (Khả năng đụng độ với các giá trị khác)
                    # No inverse-mapping (Không có ánh xạ ngược)
            # Word Embedding
                # Mã hoá các vector khác nhau và thể hiện sự gần gũi giữa 2 vector (cấp bậc)
                # Thể hiện dưới cái góc được tạo bởi các vector
                # Phải có rất nhiều data để huấn luyện mô hình này
                # Cosine Simaliti
                    # Dog -> 0.27,-0.31,-0.35
                    # Lion -> -0.7, 0.61, 0.42
                    # Tiger -> -0.71, 0.6, 0.38
                    # Mouse -> 0.31,-0.34,0.76
                #Advantage
                    # Memory efficient: Không sử dụng tài nguyên lưu số 0 vô nghĩa
                    # Relationship learn : Thể hiện mức độ gần gũi giữa 2 vector khác nhau
                # Disadvantage
                    # Word2vec: model nedded
                    # Maybe many demension needed (Cần rất nhiều chiều)
    # Remove multicollinearity: Loại bỏ đa cộng tuyến