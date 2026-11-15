# A1-4 – Review đặc tả Giỏ hàng & Checkout (có lỗi cài sẵn) + test plan theo rủi ro

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục A1-4.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 2 | Day 11 | 120' | demo 10' + thực hành & nộp 110' | Mentor | Review A1-4 (Day 12) + CK2-2 |

**Mục tiêu:** Dùng AI rà soát đặc tả, kiểm chứng từng phát hiện, ghi review log có trích dẫn; lập test plan theo rủi ro.

**Bài học tiên quyết:** A1-1, A1-2, A1-3

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| F6-2 | `F6-2/F6_Model_Quality_Cost.csv` | Khuyến nghị | Gợi ý (không bắt buộc theo lab guide): dùng model đã chọn ở F6-2 và giữ guardrail cho các lab A. |
| A1-1 | `evidence/EVIDENCE_INDEX.md` | Khuyến nghị | Checklist truy cập UAT/API/Swagger (A1-1) đã hoàn thành; repo cá nhân đã tạo. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py A1-4 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 02_SRS_Storefront.md – REQ-SF-01…07 (3.1) + REQ-SF-10, 11, 12, 15, 16 (3.2)
- KB/KB-02_Van_chuyen.md
- Template A1_Review_Log.csv, T01_Test_Plan.md

## Các bước (tóm tắt)
1. Prompt có cấu trúc rà soát theo checklist: thiếu, mâu thuẫn, mơ hồ, không kiểm thử được (kèm trích dẫn câu SRS).
2. Kiểm chứng từng phát hiện với SRS/KB → giữ/sửa/loại; phát hiện AI bịa → "Loại – AI bịa" + lý do.
3. Viết câu hỏi làm rõ gửi BA (mentor đóng vai) cho mỗi lỗi giữ lại.
4. Lập test plan T01: ma trận rủi ro, ưu tiên/độ sâu, entry/exit, môi trường Toolshop + giả định ánh xạ.
5. Lưu prompt + raw output + quyết định vào prompt_record.md.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `A1-4/A1_Review_Log.csv` | Review log có trích dẫn SRS, quyết định giữ/sửa/loại, câu hỏi làm rõ | **Bắt buộc** | ≥ 1 dòng |
| `A1-4/Test_Plan.md` | Test plan T01: ma trận likelihood × impact, ưu tiên/độ sâu, entry/exit | **Bắt buộc** | – |
| `A1-4/prompt_record.md` | Prompt + raw output + quyết định | **Bắt buộc** | – |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py A1-4 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| A2-3 | `A1-4/A1_Review_Log.csv` | **Bắt buộc** | Review log ĐÃ FIX COMMENT: mâu thuẫn/mơ hồ đã làm rõ (vd ngưỡng free ship REQ-SF-15) quyết định condition và expected. |
| A2-3 | `A1-4/Test_Plan.md` | Khuyến nghị | Ưu tiên/độ sâu theo rủi ro → chọn kỹ thuật và mức Cao cho REQ. |

Dùng lại ngoài lab: Đồ án cuối khóa (test plan).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Phát hiện lỗi cài sẵn trong đặc tả (theo key) — **25**
- [ ] Review log có trích dẫn yêu cầu, không ghi phát hiện AI bịa — **15**
- [ ] Nhận diện rủi ro & đánh giá likelihood × impact — **25**
- [ ] Phạm vi/ưu tiên/độ sâu kiểm thử, entry/exit criteria theo rủi ro — **20**
- [ ] Bằng chứng AI (prompt, raw output, quyết định giữ/sửa/loại) — **15**

**Điều kiện bắt buộc:** Phát hiện ≥ 1 lỗi critical cài sẵn

**Critical fail (dừng chấm):** Dữ liệu thật; Bằng chứng giả

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
