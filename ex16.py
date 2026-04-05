# Superivised Learning algorithms
    # Bài toán Regresstion (hồi quy)
        # Linear Regresstion (Hồi quy tuyến tính)
            # Không có tỷ lệ bao nhiêu % và thằng này thuộc Regress còn (Logic) thuộc (Class) (So sánh với Logic Regre)
            # Mô hình này sẽ được thiết kế để phù hợp với phần lớn mọi người (đường thẳng đi qua trung tâm dữ liệu)
            # 1 trong số các thuật toán cơ bản và đơn giản nhất trong Supervised Learning
            # Simple linear regression: 1 input feature
            # Multiple linear regression: 2 input features trở lên
            # Phù hợp hơn với các linear dataset
            # Lấy dữ liệu tham B0, B1 để triển khai. Còn dữ liệu thì không cần nữa
            # Y = B0 + B1X1 + B2X2+...+BPXP + E
                # Y: dependent variable, response
                # x : x-variable, independent variable
                # B: coeffect
                # E : is random error, "noise" (sai số)
            # ƯU ĐIỂM
                # - Ít bị quá khớp nhưng có thể bị quá khớp trong các tập dữ liệu có chiều cao.
                # - Hiệu quả khi tập dữ liệu có các đặc trưng
                # có thể phân tách tuyến tính.
                # - Dễ triển khai và hiệu quả trong huấn luyện.
            # NHƯỢC ĐIỂM
                # - Không nên sử dụng khi số lượng quan sát ít hơn số lượng đặc trưng.
                # - Giả định về tính tuyến tính, điều này hiếm khi xảy ra trong thực tế.
                # - Chỉ có thể được sử dụng để dự đoán các hàm rời rạc.
        # Polynomial Regresstion ( Đa thức hồi quy) (ít khi sử dụng) (Không cần dữ liệu khi đã triển khai)
            # Đa thức : ví dụ hàm bậc 2, bậc 3,..
            # Phù hợp với bộ dữ liệu không có feature nào liên quan đến target
            # Không phải mô hình bậc 1: là phi tuyến
        # * Could also be used here
    # Bài toán Classification(Phân loại)
        # Logistic Regression
            # Biến đổi mô hình Linear Regression sao cho phù hợp với bài toán Classification
                # Lúc đầu Linear Regression kết hợp với hàm sích môi : síchmoi(z) = 1 / (1+e-z)
            # Có tỷ lệ chắc chắn bao nhiêu %
            # Kết hợp giữa hàm tuyến tính và phi tuyến
            # Giảm ngưỡng tăng Recall
            # Tăng ngưỡng tăng Precision
            # ƯU ĐIỂM
                # - Ít bị quá khớp nhưng có thể bị quá khớp trong các tập dữ liệu có chiều cao.
                # - Hiệu quả khi tập dữ liệu có các đặc trưng
                # có thể phân tách tuyến tính.
                # - Dễ triển khai và hiệu quả trong huấn luyện.
            # NHƯỢC ĐIỂM
                # - Không nên sử dụng khi số lượng quan sát ít hơn số lượng đặc trưng.
                # - Giả định về tính tuyến tính, điều này hiếm khi xảy ra trong thực tế.
                # - Chỉ có thể được sử dụng để dự đoán các hàm rời rạc.
        # Support Vector Machine (Rất hay) Phi tuyến -> Tạo chiều mới dựa vào các hàm phi tuyến
            # Ví dụ phân loại dữ liệu hình tròn và dữ liệu hình thoi
            # Hyperplane: Siêu phẳng: Trong không gian 2 chiều nó gọi là đường thẳng
                # Chọn điểm cách đều 2 điểm gần nhất thuộc 2 class
                # Maximised margin 2 class này (Tối đa khoảng cách giữa 2 class này)
                # Đủ 2 đk suy ra đó là Optimal Hyperplane
            # Support vector:
                # những dữ liệu ảnh hưởng đến Hyperplane
                # Dựa vào những sample dễ nhầm nhất giữa 2 class
            # Trong không gian 3 chiều Hyperplane là 1 mặt phẳng
                # Những trường hợp đường thẳng không làm được mà mặt phẳng làm được
                # z = f(x,y)
        # K-nearest neighbors* (Thuật toán không có tham số)
            # Dùng khi không có nhiều dữ liệu
            # Có điểm dữ liệu mới tìm đến k điểm gần nó nhất
                # Thông thường chọn k là số lẻ
            # ví dụ : nó gần 2 điểm a và 1 điểm b thì nó điểm mới đó là điểm a
            # Không có quá trình training (Khác với tất cả các mô hình khác)
            # Mất nhiều thời gian triển khai (Khác với các cái khác
        # Naive Bayes
        # Decision Tree*
            # Độ chính xác khi đứng 1 mình rất thấp và dễ overrating
            # Phân chia càng lệch càng làm root tốt
            # Định nghĩa độ sâu
            # Input: Should i accept a new job offer?
            # Root node: salary at least: $50.000
            # decision nodes: Nơi ra cái so sánh đánh giá
            # leaf nodes : Đưa ra quyết định nhận hay không nhận
