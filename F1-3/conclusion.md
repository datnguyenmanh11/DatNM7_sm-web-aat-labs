# F1-3 – Kết luận (≤ 5 câu, dựa trên số đo)

1. Ở temperature 0, ba lần chạy E1 (batch 21:33) cho ba output khác nhau (3 sha1 khác nhau, cùng giá trị SL = 0/5/11 nhưng khác diễn đạt), và ở batch 21:32 một lần temperature 0 còn trả "Không có trong tài liệu" dù có đủ SRS, nên temperature 0 chỉ giảm chứ không loại bỏ biến thiên.
2. Temperature 1 cũng không làm output luôn khác (run 6 ở temperature 1 trùng hệt run 1 ở temperature 0, sha1 4f28bd717b), nên biến thiên mang tính xác suất và 3 lần chạy mỗi mức chưa đủ để kết luận định lượng.
3. Cả 6 output E1 đều thiếu hai biên SL = 1 và SL = 10 của REQ-SF-03, nên không dùng thẳng output AI làm bộ condition hay test oracle mà phải đối chiếu SRS theo BVA.
4. Ở E2, có SRS thì model trả lời đúng (tối đa 10, vượt giới hạn thì không chấp nhận và hiển thị thông báo), không có SRS thì model từ chối thay vì bịa giới hạn do system prompt yêu cầu từ chối, nên thí nghiệm này không tái hiện được hallucination và không được suy ra rằng model không hallucinate.
5. Hệ quả cho test oracle: expected result phải lấy từ SRS, và mỗi lần chạy phải cố định, ghi lại config cùng raw output và sha1 để truy vết, tái lập.

_Nguồn số đo:_ `F1-3/F1_Experiment_Log.csv` (batch 21:33, 8 lần chạy) · `F1-3/raw_ai_output/` · `F1-3/evidence/batch_2132_notebook_output.txt` (batch 21:32).
