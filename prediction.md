# Prediction

Prediction được thực hiện trước thí nghiệm.

| Câu | Prediction | Reason | Confidence |
|---|---|---|---|
| 1 | Key có dot product lớn nhất nhận weight lớn nhất. | Softmax giữ thứ tự của các score. | Cao |
| 2 | Bốn weight bằng nhau, mỗi weight là 0,25. | Các score bằng nhau. | Cao |
| 3 | Attention tập trung gần như toàn bộ vào token thứ ba. | Score thứ ba lớn hơn nhiều. | Cao |
| 4 | Với full self-attention, ma trận tăng từ 100 lên 1.000.000 phần tử. | Số phần tử tăng theo bình phương số token. | Cao |
| 5 | Không. | Attention phụ thuộc query, dữ liệu và tham số đã học. | Cao |
