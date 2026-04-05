# Ma trận và biến đổi dữ liệu
# PCA visualization (thuật toán sử dụng nhiều) 
    # step 1: Standardize the dataset
    # step 2: Calculate the covariance matrix (tính hiệp phương sai)
    # step 3: Calculate eigenvector(vector riêng) and eigenvalue (trị riêng)
        # A.v = lâmdah.v
            # A maxtrix
            # v :Eigenvector : khi nhân nó không thay đổi phương và khác vector 0
            # lâmda: Eigenvalue
        #Một ma trận cấp n có vô số eigenvector và có đúng n eigenvalue
        # Các phép biến đổi trên vector
            # Phép co dữ liệu
            # Phép phản chiếu dữ liệu (reflection)
            # Phép làm méo dữ liệu (Shear)
    # Step 4: Sort eigenvalues & corresponding eigenvectors
    # Step 5: Pick k eigenvalues and forms matrix
    # Step 6: Transform feature metric

# Recommendation systems
    # Types of recommendation systems
        # Popularity-based recommendation system (dựa vào độ nổi bật)
            # Ưu điểm
                # Đơn giản
            # Nhược điểm
                # Không có tính cá nhân hoá
        # Content-based filtering (Dựa vào nội dung người dùng tương tác)
            # Nhược điểm
                # Không đa dạng (cứ xem gì nó cứ gợi ý mãi).
                # Không giúp người dùng khám phá ra những thứ người dùng có thể thích
        # Collaborative filtering
            # Dựa vào thông tin người dùng tương tự để gợi ý
            # Ưu điểm
                # Giúp người dùng khám phá những thứ người dùng có thể thích mà chưa biết
            # Nhược điểm
                # Phức tạp
        # Hybrid Recommendations
            # Utility Matrix
                # Dữ liệu bị lệch về mẫu
                # Long tail: 

