# Unsupervised # Không thể trả ra kết quả bạn kỳ vọng
    # Để tăng khả năng đúng kỳ vọng ta gán Label một số data làm chuẩn
    # K-nearest classi
        # Thuật toán kết thúc khi data point chạy nữa nhưng thuật toán đó không đổi
            #

# Natural language Processing ( Xử lý ngôn ngữ tự nhiên) (NLP)
    # Có 3 loại chính :
        # Rule Base: Xây dựng mô hình dựa trên quy tắc
            # Ví dụ dựa vào 10 số là biết số điện thoại
        # Classical NLP
            # Text File -> Language Detection -> Pre-processing -> Modeling -> Output
        # Deep Learning
            # Text File -> Dense Embedding -> Hidden Layer -> Output Units -> Output
    # Khái niệm NLP
        # Cách 1 Bag of words
            # Cho biết một từ xuất hiện bao nhiêu lần
                # Nhược điểm mất đi thứ tự của từ đó
            # Tập hợp đoạn từ thường được đặt là corpus
            # Bag of words (Đưa nó về cùng độ dài)
                # Corpus -> Make vocabulary -> Score assignment
            # Trong sklearn có thư viện CountVectorizer
            # Các tiền dữ liệu dạng text (Text preprocessing)
                # Step 1: Remove punctuations: Xoá bỏ các dấu không ảnh hưởng đến câu vd: .,!,?,(),%,@
                # Step 2: Lower text: Go và go nên được xem là một mẫu duy nhất
                # Step 3: Tokenization: Chia tài liệu trong từ và câu (Khó ở ngôn ngữ Vn)
                # Step 4: Remove stopwords : Loại bỏ những từ xuất hiện nhiều nhưng không có giá trị như : I, You, is
                # Step 5.1: Stemming : Send = Sent = Sending ->learning -> learn cool -> cool machine -> machin
                # Step 5.2: Lemmatization
                
           # N-grams: Trong thực tế người ta thường dùng kết hợp vd: Uni-Gram và Bi-Gram. Thường lấy n từ 1 - 5
                # Uni-Gram: 1 từ liên tiếp
                # Bi-Gram: 2 từ liên tiếp
                # Tri-Gram: 3 từ liên tiếp
                # Thư viện: CountVectorizer trong sklearn
           # TFIDF (dùng khi text dài và có nhiều giá trị khác nhau (chữ))
                # Term Frequency (TF) (Không xuất hiện trong document
                    # Tần số xuất hiện của 1 word in 1 document
                    # TF = 1 từ khoá X  / số từ trong document hiện tại
                # Inverse Document Frequency(IDF) # bằng 0 nghĩa là ở đâu cũng xuất hiện)
                    # Mức độ phổ biến/hiếm của 1 word trong toàn bộ các documents
                    # TF = log(số document hiện tại trong corpus / Số document nơi mà từ khoá X xuất hiện)
                        # Ví dụ số document = 4, Số document nơi mà từ khoá X xuất hiện = 2 => log(4%2) = 1
                # TF IDF = TF * IDF # Điểm càng cao càng tốt
                # Thư viện TfidfVectorizer