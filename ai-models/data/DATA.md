# Water Potability Dataset

## 1. Thông tin chung

- Tên dataset: Water Potability
- Nguồn: Kaggle
- Tác giả dataset: Aditya Kadiwal
- Link Kaggle: https://www.kaggle.com/datasets/adityakadiwal/water-potability
- License: CC0 1.0 - Public Domain
- Loại bài toán: Binary Classification
- Số lượng mẫu: 3276
- Số lượng cột: 10
- Số lượng đặc trưng đầu vào: 9
- Biến mục tiêu: Potability

---

## 2. Mục tiêu bài toán

Dataset được sử dụng để xây dựng mô hình Machine Learning nhằm phân loại
khả năng uống được của nước dựa trên các thông số chất lượng nước.

Bài toán thuộc nhóm phân loại nhị phân (Binary Classification).

Biến mục tiêu:

- Potability = 0: Không uống được / Not Potable
- Potability = 1: Uống được / Potable

---

## 3. Các thuộc tính của dataset

| STT | Thuộc tính      | Kiểu dữ liệu | Ý nghĩa                                    |
| --- | --------------- | ------------ | ------------------------------------------ |
| 1   | ph              | Numeric      | Chỉ số pH của nước                         |
| 2   | Hardness        | Numeric      | Độ cứng của nước                           |
| 3   | Solids          | Numeric      | Tổng lượng chất rắn hòa tan                |
| 4   | Chloramines     | Numeric      | Hàm lượng Chloramine trong nước            |
| 5   | Sulfate         | Numeric      | Hàm lượng Sulfate                          |
| 6   | Conductivity    | Numeric      | Độ dẫn điện của nước                       |
| 7   | Organic_carbon  | Numeric      | Hàm lượng carbon hữu cơ                    |
| 8   | Trihalomethanes | Numeric      | Hàm lượng Trihalomethane                   |
| 9   | Turbidity       | Numeric      | Độ đục của nước                            |
| 10  | Potability      | Integer      | Nhãn phân loại khả năng uống được của nước |

---

## 4. Phân bố biến mục tiêu

Dataset có tổng cộng 3276 mẫu.

Phân bố biến Potability:

| Giá trị | Ý nghĩa     | Số lượng |
| ------- | ----------- | -------: |
| 0       | Not Potable |     1998 |
| 1       | Potable     |     1278 |

Có sự chênh lệch giữa hai lớp.

Việc đánh giá mức độ mất cân bằng và quyết định có cần xử lý hay không
sẽ được thực hiện trong giai đoạn EDA và tiền xử lý dữ liệu.

---

## 5. Missing Values

Dataset tồn tại giá trị thiếu ở ba thuộc tính:

| Thuộc tính      | Số lượng thiếu |
| --------------- | -------------: |
| ph              |            491 |
| Sulfate         |            781 |
| Trihalomethanes |            162 |

Các thuộc tính còn lại không có giá trị thiếu.

Ở giai đoạn này chưa thực hiện xóa hoặc điền giá trị thiếu.

Chiến lược xử lý missing values sẽ được quyết định trong bước
tiền xử lý dữ liệu nhằm tránh làm mất thông tin và tránh data leakage.

---

## 6. File dữ liệu

File dữ liệu gốc:

```text
water_potability.csv
```
