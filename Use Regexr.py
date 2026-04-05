# ví dụ Mô hình giúp extract ra email, phone,...
import re
text = "My phone number is +49 1748048234. My brother's one is 01233035715"
result = re.findall("\+?\d+\s?\d+", text)
print (result)

text1 = ("My email is nguyenthanhthan@gmail.com I have another email,which is than@gmail.com")

result1 = re.findall("\w{2,}\@\w+.\w+", text1)
print (result1)