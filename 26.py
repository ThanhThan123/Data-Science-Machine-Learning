# Kiểm định giả thuyết
    # Bao gồm những bước
        # Đầu tiên đưa ra giả thuyết (tập đối tượng lớn)(Population)
        # Lấy mẫu (Sample)
        # Suy luận
        # Đưa ra dự đoán quay về tập mẫu
    # Các khái niệm
        # Hypothesis (Giả thuyết)
            # 1 mệnh đề được đưa ra, cần phải kiểm định đúng sai
        # Statistical hypothesis ( Giả thuyết thống kê)
            # Là giả thuyết về 1 biến ngẫu nhiên.Có 2 loại chính
            # Tham số (phổ biến hơn):
                # Giả thuyết về tham số của biến ngẫu nhiên (kỳ vọng, phuơng sai, xác suất)
            # Phi tham số:
                # Giả thuyết về phân phối hoặc tính chất của biến ngẫu nhiên
            #H0: Giả thuyết gốc/cơ bản/không ( H0 luôn phải có dấu )
                # H0  : 0 = 0o
                # H1/H: 0 != 0o

                # H0: 0=0o(0<=0o)
                # H1/Ha: 0 > 0o

                #H0: 0=0o(0>=0o)
                # H1/Ha : 0 < 0o
            #H1/HA: Giả thuyết đối/ đối thuyết (H1 phải xung khắc H0)
        # Hypothesis (Kiểm định giả thuyết)
            # Kểm định tính đúng sai của 1 giả thuyết nào đó
    # Các quyết định và sai lầm P1
        # Đưa ra kết luận bác bỏ H0
        # Không đủ cơ sở để bác bỏ H0
    # Phân phối chuẩn
        # Expectation
        # Variance
        # Quy tắc 3 síchma: Nếu biến ngẫu nhiên X có phân phối
    # Định lý giới hạn trung tâm (Central Limit theorem)
        # Chọn 1 tập mẫu kích thước n đủ lớn thì giá trị trung bình của tập mẫu này
        # sẽ sấp xỉ giá trị trung bình tổng thể
        # Phân phối của giá trị trung bình của tập mẫu này sẽ tiệm cận phân phối chuẩn
        # Ví dụ
    # Nguyên lý xác suất nhỏ ( The principle of small probability)
        # xác suất bé tuỳ vào ngữ cảnh (không có số nhất định)
        # Nếu một biến ngẫu nhiên có xác suất rất nhỏ thì thực tế có thể cho rằng trong
        # một phép thử biến đó sẽ không xẩy ra
    # Phương pháp phản chứng
        # Để chứng minh mệnh đề A là đúng: Giả sử A không đúng từ đó suy ra 1 điều vô lý/ mâu thuẫn với thực tế

    # Các quyết định và sai lầm P2 (alpha: mức ý nghĩa), 1 - Beta: Lực lượng kiểm định
        # Thực tế / quyết định      |H0 đúng                                    | H0 sai
        # Bác bỏ H0                 |Sai lầm loại 1 (xác suất bằng alpha)       | Quyết định đúng (xác suất bằng 1-Beta)
        # Không bác bỏ H0           |Quyết định đúng (xác xuất bằng 1 - alpha)  | Sai lầm loại 2 : (Xác xuất bằng Beta)

        # Ví dụ sai lầm loại 1: Máy bay không rơi nhưng bạn không đi, loại 2 : Máy bay rơi
        # Thông thường phải làm giảm sai lầm loại 2

    # Các bước tiến thành kiểm định giả thuyết
        # Bước 1: Thành lập cặp giả thuyết H0 và H1
            # H0 : Null Hypothesis
            # H1 : Alternative Hypothesis
        # Bước 2: Chọn 1 thống kế Z có liên quan đến biến X
            # Tỷ lệ hỏng của 1 lô hàng <= 1%        => X: TRạng thái của 1 món hàng
            # Chú ý : 1 trong 2 điều kiện sau phải được thoả mãn:
                # X(tập mẫu) có phân phối chuẩn
                # n > 30 (Tập mẫu có kích thước n)
            # Ngoài ra: X1, X2,..., độc lập với nhau
        # Bước 3 : Xác định miền bác bỏ  (rejected area) giả thuyết H0
            # Miền bác bỏ Walpha với mức ý nghĩa là alpha
            # Có 3 loại
                # Dựa vào dấu của H1:
                    # One-Tailed Test (left) khi dấu bé ở H1,
                    # Two-Tailed Test khi dấu != ở H1,
                    # One-Tailed Test (right) khi dấu lớn ở H1
        # Bước 4: Xác định giá trị quan sát của tiểu chuẩn kiểm định Z

        # Bước 5: So sánh giá trị quan sát và giá trị tới hạn

# Bài tập kiểm định giả thuyết
    #