# Phiếu ghi chú F1-1 – 5 khái niệm + ví dụ QA SM-WEB

> Nguồn: ô ghi chú đầu notebook Colab "DatNM7_sm-web-aat" – chép nguyên văn (chỉ thêm ngắt dòng markdown).

5 khái niệm:  
1. Token (đơn vị văn bản model xử lý): Token (đơn vị văn bản mà model xử lý) không phải là “từ”. Quá trình tokenization (tách văn bản thành token) cắt văn bản thành các mảnh: có thể là một từ, một phần của từ, một dấu câu hoặc khoảng trắng. Model chỉ “nhìn thấy” chuỗi token, không nhìn thấy ký tự như con người.  
Ví dụ QA trên SM-WEB:  
Question: Hãy liệt kê 5 phương thức thanh toán được hỗ trợ trên SM-WEB.  
Expected Answer:  
1. Bank Transfer.  
2. Cash on Delivery.  
3. Credit Card.  
4. Buy Now Pay Later.  
5. Gift Card.  
Ý nghĩa QA: Kiểm tra AI có đọc và xử lý đầy đủ thông tin trong SRS hay không, đặc biệt khi nội dung có nhiều trường dữ liệu và thuật ngữ tiếng Anh.  
  
2. Context window (cửa sổ ngữ cảnh) là tổng số token tối đa model xử lý được trong một lần gọi, gồm input + output. Mọi thông tin model “biết” trong lần gọi đó nằm trong cửa sổ này; ngoài cửa sổ, model không có trí nhớ về cuộc trò chuyện trước (các ứng dụng chat tạo cảm giác “nhớ” bằng cách gửi lại lịch sử trong mỗi lần gọi).  
Ví dụ QA trên SM-WEB:  
Question: Theo bảng ánh xạ SRS ↔ UAT đã cung cấp, phí vận chuyển, SAOMAI10 và điểm thưởng đã có trên UAT chưa?  
Expected Answer: Chưa có trên UAT. Các nội dung này cần được kiểm thử ở mức thiết kế/review (A2, CR-01).  
  
Ý nghĩa QA: Kiểm tra AI có duy trì và truy xuất đúng thông tin từ SRS đã cung cấp trong suốt cuộc hội thoại hay không.  
  
3.  
- Temperature (nhiệt độ – tham số điều chỉnh mức ngẫu nhiên): làm phân phối “nhọn” hơn hoặc “phẳng” hơn. Temperature thấp → token có xác suất cao gần như luôn được chọn → output ổn định, ít sáng tạo. Temperature cao → token ít khả năng cũng có cơ hội → output đa dạng hơn, dễ lệch hơn. Temperature = 0 về lý thuyết tương đương greedy decoding (luôn chọn token xác suất cao nhất).  
  
- Top-p  
Top-p (nucleus sampling – lấy mẫu theo nhóm xác suất tích lũy): chỉ xét nhóm token nhỏ nhất có tổng xác suất đạt p (ví dụ 0,95), loại phần “đuôi” xác suất thấp, rồi lấy mẫu trong nhóm đó.  
Ví dụ QA trên SM-WEB:  
Đặt cùng một câu hỏi ở hai cấu hình khác nhau:  
Question: SM-WEB hỗ trợ những phương thức thanh toán nào?  
Expected Answer: Cả hai cấu hình đều phải liệt kê đúng 5 phương thức:  
1. Bank Transfer.  
2. Cash on Delivery.  
3. Credit Card.  
4. Buy Now Pay Later.  
5. Gift Card.  
Ý nghĩa QA: Kiểm tra khi thay đổi Temperature hoặc Top-p, AI có thể thay đổi cách diễn đạt nhưng không được làm sai dữ liệu nghiệp vụ trong SRS.  
  
4. Non-determinism (tính không tất định – cùng input nhưng output có thể khác giữa các lần chạy) là đặc tính tester phải chấp nhận và quản lý.  
Ví dụ QA trên SM-WEB:  
Thực hiện cùng một câu hỏi 3 lần:  
- Question: Địa chỉ thanh toán trên SM-WEB gồm những thông tin gì?  
- Expected Answer: AI phải xác định đúng trường thông tin theo SRS là Billing address (5 trường).  
Ví dụ kết quả:  
Câu trả lời của lần hỏi 1: Địa chỉ thanh toán gồm 5 trường thông tin.  
Câu trả lời của lần hỏi 2: Billing address có 5 trường.  
Câu trả lời của lần hỏi 3: SRS quy định 5 trường cho địa chỉ thanh toán.  
Ý nghĩa QA: Câu trả lời có thể khác nhau về cách diễn đạt nhưng thông tin cốt lõi phải nhất quán, không tự ý thay đổi số lượng trường.  
  
5. Hallucination (ảo giác – AI bịa thông tin) là khi model sinh nội dung nghe hợp lý nhưng không đúng sự thật hoặc không có căn cứ trong nguồn được cung cấp.  
Ví dụ QA trên SM-WEB:  
- Question: Phí vận chuyển của SM-WEB trên UAT là bao nhiêu? Mã giảm giá SAOMAI10 được áp dụng như thế nào?  
- Expected Answer:  
Theo SRS được cung cấp, phí vận chuyển và SAOMAI10 chưa có trên UAT. Các nội dung này cần được kiểm thử ở mức thiết kế/review (A2, CR-01). Tài liệu hiện tại không cung cấp số tiền phí vận chuyển hoặc quy tắc áp dụng mã giảm giá.  
- Câu trả lời sai (Hallucination):  
AI tự đưa ra mức phí vận chuyển 30.000 VNĐ và khẳng định mã SAOMAI10 giảm 10% cho đơn hàng.  
Ý nghĩa QA: Kiểm tra AI có tự bịa ra dữ liệu nghiệp vụ khi SRS không cung cấp thông tin hay không.  
  
2. Các nguyên nhân khiến output AI sai trong tác vụ kiểm thử:  
1. Thiếu hoặc sai ngữ cảnh: không đưa SRS, đưa nhầm phiên bản, đưa quá dài khiến model bỏ sót.  
2. Prompt mơ hồ: không nói rõ phạm vi, kỹ thuật thiết kế test, định dạng output – model tự chọn theo cách của nó.  
3. Giới hạn kiến thức của model: model không biết tài liệu nội bộ/hư cấu, không biết thay đổi sau thời điểm huấn luyện.  
4. Sampling ngẫu nhiên và non-determinism: lần chạy này đúng, lần sau thiếu biên.  
5. Output bị cắt do max_tokens quá nhỏ → JSON hỏng, thiếu condition.  
6. Điểm yếu về tính toán, đếm, logic nhiều bước: tính sai thành tiền, đếm sai số chữ số.  
7. Chỉ dẫn độc hại nằm trong dữ liệu (prompt injection – học ở F2-2): tài liệu đầu vào chứa câu “bỏ qua yêu cầu trước đó…”.  
  
3.  
- LLM thuần:  
+ Khi nào dùng (QA): Giải thích khái niệm, gợi ý kỹ thuật, viết lại văn bản khi đủ dữ liệu  
+ Rủi ro chính: Hallucination, kiến thức lỗi thời, không biết tài liệu hư cấu/nội bộ  
+ Cách kiểm chứng: Đối chiếu nguồn chính thức; không dùng làm oracle  
  
- RAG:  
+ Khi nào dùng (QA): Hỏi đáp/sinh test bám bộ tài liệu SRS, KB  
+ Rủi ro chính: Nguồn sai/lỗi thời, truy xuất sai đoạn, injection gián tiếp  
+ Cách kiểm chứng: Bắt trích dẫn nguồn; kiểm tra version kho; thử câu hỏi ngoài tài liệu  
  
- Tool calling:  
+ Khi nào dùng (QA): Lấy dữ liệu thật từ API, validate schema, tra cứu CI  
+ Rủi ro chính: Sai tool/tham số, quyền công cụ quá rộng  
+ Cách kiểm chứng: Log mọi lần gọi; quyền tối thiểu; xác nhận hành động ghi/xóa  
  
- AI agent:  
+ Khi nào dùng (QA): Tác vụ nhiều bước: khám phá UI, phân tích log, nháp PR  
+ Rủi ro chính: Hành động ngoài phạm vi, lỗi cộng dồn, khó tái lập  
+ Cách kiểm chứng: Giới hạn phạm vi/quyền; human-in-the-loop; lưu trace; kiểm tra độc lập  
