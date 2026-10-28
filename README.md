# LAB 06 — Attention Mechanism

Nguyễn Huy Sơn — 23001922

- `attention_numpy.py`: scaled dot-product attention và softmax ổn định.
- `self_attention.ipynb`: thí nghiệm, hình và đánh giá.
- `results.csv`, `attention_heatmap.png`, `confusion_matrix.png`: kết quả chạy notebook.
- `prediction.md`, `error_analysis.md`, `reflection.md`: câu trả lời và nhận xét ngắn.
- `calculations.pdf`: bài tính viết tay.

Dữ liệu so sánh là NLTK movie_reviews (2.000 review), không phải IMDb của LAB 05. Hai mô hình được huấn luyện trên cùng dữ liệu, cùng split; kết quả chỉ là thí nghiệm nhỏ. Ma trận ngẫu nhiên ở phần minh họa không phải attention của mô hình đã huấn luyện.

Chạy: `python -c "import nltk; nltk.download('movie_reviews')"`, sau đó mở và chạy `self_attention.ipynb`. Cần NumPy, pandas, matplotlib, scikit-learn, NLTK, PyTorch và Jupyter.

## AI assistance statement

- Tool: OpenAI Codex.
- Purpose: tạo mã, notebook, biểu đồ.
- Generated: `attention_numpy.py`, notebook, README.
- Verified: xem output notebook và kết quả thực thi thực tế; sinh viên cần tự kiểm tra và hoàn thiện phần cá nhân theo quy định của môn học.
