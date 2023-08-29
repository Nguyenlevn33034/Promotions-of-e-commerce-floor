import pandas as pd
import numpy as np
df = pd.read_csv("D:/DATA ANALYST/Mind X/I. Data for everyone/Project/E-commerce Dataset.csv")

#Xoá bỏ các dữ liệu bị trống
df.dropna(inplace= True)


#Tách cột Time ra Hour 
df['Hour'] = df['Time'].str.split(':').str[0]

#Tạo ra cột Delivered_Date từ cột Order_Date và Aging 
# Chuyển đổi cột "Order_Date" thành kiểu dữ liệu datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
# Tạo cột mới "Delivered_Date" bằng cách cộng cột "Order_Date" với cột "Aging"
df['Delivered_Date'] = df['Order_Date'] + pd.to_timedelta(df['Aging'], unit='D')


#Vẽ biểu đồ tổng đơn hàng theo giờ
import matplotlib.pyplot as plt
order_count_by_hour = df['Hour'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(order_count_by_hour.index, order_count_by_hour.values, color='lightcoral')
plt.xlabel('Hour')
plt.ylabel('Customer_Id')
plt.title('Total Orders by Hour')
plt.xticks(order_count_by_hour.index)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#Vẽ biểu đồ tổng đơn hàng theo giờ và phân loại theo giới tính
import matplotlib.pyplot as plt
order_count_by_gender_hour = df.groupby(['Hour', 'Gender']).size().unstack(fill_value=0)
# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
plt.bar(order_count_by_gender_hour.index, order_count_by_gender_hour['Female'], label='Female', color='lightcoral')
plt.bar(order_count_by_gender_hour.index, order_count_by_gender_hour['Male'], bottom=order_count_by_gender_hour['Female'], label='Male', color='lightblue')
plt.xlabel('Hour')
plt.ylabel('Customer_Id')
plt.title('Total Orders by Gender and Hour')
plt.xticks(order_count_by_gender_hour.index)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#Vẽ biểu đồ các sản phẩm mà phụ nữ mua nhiều nhất
import matplotlib.pyplot as plt
female_customers = df[df['Gender'] == 'Male']
order_count_by_category = female_customers['Product'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(order_count_by_category.index, order_count_by_category.values, color='lightcoral')
plt.xlabel('Product')
plt.ylabel('Total Orders')
plt.title('Total Orders by Product Category for Female Customers')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#Vẽ biểu đồ top 5 sản phẩm mà phụ nữ mua nhiều nhất
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Code của bạn để lấy top 5 sản phẩm đã đúng

top_5_products = df[df['Gender'] == 'Female']['Product'].value_counts().nlargest(5)

# Chỉnh màu của cột
custom_color = (64/255, 111/255, 147/255)  # Chuyển từ RGB (0-255) sang dạng chuẩn (0-1)
plt.bar(top_5_products.index, top_5_products.values, color=custom_color)

plt.xlabel('Product')
plt.ylabel('Count of Product')
plt.title('Top 5 Products Purchased by Female Customers')
plt.xticks(rotation=45, fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(top_5_products.values):
    plt.text(i, v, str(v), ha='center', va='bottom')
plt.show()




