# Một vài câu hỏi về precision và recall
    # Tìm bệnh nhân ung thư
        # Positive: Ung thư
            # Lỗi loại 1 những người thường bị dự đoán là ung thư
        # Negative: Không bị ung thư
            # Lỗi loại 2 những người ung thư bị dự đoán là không bị
        # Giải trong y tế người ta tập trung vào recall
            # Thà nhầm 1 negative còn hơn để sót positive
    # Tuyển dụng người phù hợp với vị trí công việc
        # Positive: Người phù hợp
        # Negative: Chưa phù hợp
            # Vị trí cấp thấp : Tập trung vào Recall
            # Vị trí cấp cao : Tập trung vào Precision
    # Ứng dụng Ai vào lĩnh vực luật pháp
        # Có tội : Positive
            # Bỏ tù nhầm 1 người vô tội
        # Không có tội : Negative
            # Thả nhầm 1 người có tội
        # Giải nên tập trung vào Precision: Không bắt nhầm người vô tội
    # Nếu có 3 class thì sao ví dụ gà, chó, mèo
        # Lấy class quan trọng ví dụ chó
        # còn gà với mèo là negative

# Một vài classification matrics nâng cao
    # True Positive Rate (= Recall) (tăng cùng tăng hoặc giảm cùng giảm với False P R) (Hoành độ)
        # TP/(TP + FN)
            # Tỷ lệ đoán đúng
    # False Positive Rate (Tung độ)
        # FP/(FP+TN)
            # Tỷ lệ người khoẻ bị đoán thành ung thư
    # Thuộc tính ROC (Receiver Operating Characteristic curve)
        # Là 1 cái đường để xem và đánh giá thường thì khó đánh giá
    # Thuộc tính AUC (Area under the  ROC curve)
        # Là diện tích của đường đó để đánh giá performance cao thấp của ROC)

# Regesstion : Tính độ sai lệch (sai số) giữa thực tế với dự đoán
    # Mean absoulute error
        # Tính giá trị tuyệt đối
    # Root Mean Squared Error(RMSE)

# Machine Learning pipeline
    # Step 1 : Data collection
        # Thu thập dữ liệu
            # Đánh nhãn dữ liệu
    # Step 2: Statistics (2, 3, 4 có thể đảo thứ tự thực hiện)
        # Hiện dữ liệu qua thống kê
    # Step 3: Data preprocessing
        # Tiền xử lý dữ liệu
            # Đưa về dạng dữ liệu máy móc hiểu
            # Xử lý dữ liệu thành dạng dễ học cho máy
    # Step 4: Data visualization
        # Trực quan hoá dữ liệu
            # Làm cầu nối để giải thích với những người chưa hiểu về Data scient
            # Thường dạng biểu đồ hoặc hình ảnh
    # Step 5: Model building
        # Xây dựng và huấn luyện mô hình
    # Step 6: Model evaluation
        # Đánh giá mô hình
    # Step 7: Model deployment
        # Triển khai mô hình

"""
    # Ex1: Write a program to count positive and negative numbers in a list
    data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

    # Ex2: Given a list, extract all elements whose frequency is greater than k.
    data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
    k = 3

    # Ex3: find the strongest neighbour. Given an array of N positive integers.
    # The task is to find the maximum for every adjacent pair in the array.
    data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

    # Ex4: print all Possible Combinations from the three Digits
    data4 = [1, 2, 3]

    # Ex5: Given two matrices (2 nested lists), the task is to write a Python program
    # to add elements to each row from initial matrix.
    # For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
    # Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
    data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
    data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

    # Ex6:  Write a program which will find all such numbers which are divisible by 7
    # but are not a multiple of 5, between 2000 and 3200 (both included).
    # The numbers obtained should be printed in a comma-separated sequence on a single line.

    # Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
    # The numbers obtained should be printed in a comma-separated sequence on a single line.

    # Ex8: Let user type 2 words in English as input. Print out the output
    # which is the shortest chain according to the following rules:
    # - Each word in the chain has at least 3 letters
    # - The 2 input words from user will be used as the first and the last words of the chain
    # - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
    # - All the words are from the file wordsEn.txt
    # - If there are multiple shortest chains, return any of them is sufficient
"""

# Ex1: Write a program to count positive and negative numbers in a list
# data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
#
# count_data = []
# count_data1 =[]
# for num in data1:
#     if num < 0:
#         count_data.append(num)
#         print(count_data, "is a negative number")
#     else:
#         count_data1.append(num)
#         print(count_data1, "is a positive number")

# Ex2: Given a list, extract all elements whose frequency is greater than k.
# data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k = 3
#
# better_number = []
# def greater_k (data2, k):
#    for num in data2:
#        if data2.count(num) > k and num not in better_number:
#            better_number.append(num)
#    return better_number
# print(greater_k(data2, k))

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
# data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
#
# def maximum_adjacent(data3) :
#     adjacent = []
#     for number in range(len(data3) - 1) :
#        if data3[number] > data3[number + 1]:
#            adjacent.append(data3[number])
#        else:
#            adjacent.append(data3[number + 1])
#     return adjacent
#
# print(maximum_adjacent(data3))

# Ex4: print all Possible Combinations from the three Digits
#
# from random import randint
# data4 = [1, 2, 3]
# combin = []
# def print_combinations(data4):
#     for  i in range(len(data4)):
#         for j in range(len(data4)):
#             for k in range(len(data4)):
#                 if i != j and j !=k and i != k:
#                     number = str(data4[i]) + str(data4[j]) + str(data4[k])
#                     combin.append(number)
#     return combin

# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], o[1, 2, 3], [3, 7, 4]],
# test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
# data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
# data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

# def count_matrix (data5_list1, data5_list2):
#     result = []
#     for i in range(len(data5_list1)):
#             if data5_list1[i] :
#                 new_row = data5_list1[i] + data5_list2[i]
#                 result.append(new_row)
#     return result
#
# print(count_matrix(data5_list1, data5_list2))

# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# 2002 , 2009, 2016, 2023,

def divisible_number():
    result = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result

print(divisible_number())