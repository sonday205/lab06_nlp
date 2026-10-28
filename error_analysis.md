# Error analysis

Ba token có attention trung bình cao nhất được lấy từ kết quả trong notebook.

| ID | Nhãn | Dự đoán | P positive | Token attention cao |
|---:|---|---|---:|---|
| 20 | Negative | Negative | 0,213 | bad, then, and |
| 1088 | Positive | Positive | 0,589 | naive, has, has |
| 466 | Negative | Negative | 0,468 | neo, neo, and |
| 748 | Negative | Positive | 0,522 | and, and, and |
| 315 | Negative | Positive | 0,556 | and, and, and |
| 106 | Negative | Positive | 0,569 | and, and, lives |

- Mẫu 20: `bad` nhận attention cao và phù hợp với nhãn negative; dự đoán đúng.
- Mẫu 1088: attention cao ở `naive` và `has`; dự đoán đúng, nhưng các token này chưa đủ giải thích kết quả.
- Mẫu 466: attention cao ở `neo` và `and`; dự đoán đúng với xác suất gần ngưỡng.
- Mẫu 748, 315 và 106: attention trung bình cao ở `and`, không phải từ thể hiện sentiment rõ. Đây là giả thuyết liên quan đến lỗi, chưa chứng minh nguyên nhân.
- Cả sáu review dài hơn 120 token. Truncation có thể làm mất thông tin sentiment; cần thử tăng giới hạn và so sánh lại để kiểm chứng.

## Ba câu ứng dụng

- “I do not like this movie.”: dự đoán negative, phù hợp sentiment negative.
- “I like this movie.”: dự đoán negative, sai so với sentiment positive. Đây là câu ngắn khác phân phối review dài; domain shift là một giả thuyết cần kiểm tra thêm.
- “I thought this movie would be bad, but it was actually excellent.”: dự đoán negative, sai so với sentiment positive. Từ `bad` và sự chuyển ý có thể gây khó khăn; cần thí nghiệm đối chứng để xác nhận.
