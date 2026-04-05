# Mối quan hệ giữa các variables(features, target)
    # Correlation ( Hệ số tương quan) : Chỉ áp dụng cho thuộc tính dạng số
        # Mức độ 2 hay nhiều variables quan hệ tuyến tính với nhau
        # Hệ số tương quan: [-1,1]
            # Càng gần 1 hoặc -1 thì hệ số tuyến tính mạnh
                # Nếu gần 1 thì a tăng b cũng tăng
                # Nếu gần -1 thì a tăng b thì giảm và ngược lại
                # Nếu 2 hệ số bằng 0 thì 2 biến không có quan hệ tuyến tính với nhau
                    # Quan hệ tuyến tính: hệ số bậc 1 vd y = ax +b
                    # Nhưng nó không lên 2 hệ số này độc lập với nhau
        # Correlation does not imply causation
    # Mỗi cột là feature (Input)(Independen rival)
    # Cột cuối là Target (Output)(Dependen rival)
from statistics import correlation

# Mối quan hệ giữa các features
    # Multi collinearity
        # Mức độ 2 hay nhiều features quan hệ tuyến tính với nhau
        # Thông thường hệ số tương quan > 0.7 hoặc < -0.7 biểu thị rằng
        # 2 hay nhiều features có hiện tượng (đa) cộng tuyến tính với nhau
        # Nếu mối quan hệ tuyến tính giữa các features cao là không mong muốn
            # Ví dụ như 2 người làm 1 việc gây ảnh hưởng đến target tương tự nhau
        # Nếu chủ đích sử dụng mô hình tuyến tính chủ động loại bỏ mối quan hệ đa cộng tuyến
    # No multicollinearity
# Step 3.5: Balance data : Cân bằng dữ liệu (chỉ áp dụng cho bài toán classfication)
# làm cho dữ liệu bớt cân bằng hơn
    # Over-sampling (Tạo thêm sample cho class thiểu số) (Ưu chuộng hơn)
        # Decision fuction of LogisticRegresstion
            # Without resampling (bản gốc)
            # Using RandomOverSampler (Thuật toán Random)
                # Mô hình tiếp xúc với class thiểu số thường xuyên hơn nhưng không đa dạng hơn
            # Sử dụng thuật toán
                # SMOTE
    # Under-sampling (Thường dùng bỏ bớt class đa số)

# Step 4 Trực quan hóa dữ liệu
    # Sử dụng 2 thư viện chủ yếu:
        # matplotlib

        # seaborn: Gọi hàm của matplot và thể hiện nhiều dạng sơ đồ
    # Dạng biểu đồ
        # Biều đồ đơn biến
            # Biểu đồ Histogram (rời rạc hóa): Phân bố cơ bản của dữ liệu (dùng trong dạng number)
            # Biểu đồ Density Plot (liên tục hóa):
                # import pandas as pd
                # import matplotlib.pyplot as plt
                #
                # data = read_csv("data_name")
                # data.plot(kind="density", subplots=True, layout=(3,3), sharex=False)
                # plt.show()
            # Biểu đồ Box Plot
        # Biểu đồ đa biến
            # Correlation matrix plot
                # correlations = data.corr()
                # Sử dụng biểu đồ heatmap cùa seaborn
                    # sn.heatmap(data.corr(),)
            # Scatter Matrix Plot (ít dùng)
                # Chỉ quan tâm điềm có nó tại truc hoành (ở dưới) và trục tung ở trên)
    # Data visualization with matplotlib
        # Figure : 1 Figure (1 khung lớn)
            # 1 đĩa
        # Axes: Khung con ( có 1 hoặc nhiều khung con)
            # Trục hoành
                # Label
                # Name
                # Stick
                # Legend
                # Grid
            # Trục tung
                # Label
                # Name
                # Stick
                # Legend
                # Grid




