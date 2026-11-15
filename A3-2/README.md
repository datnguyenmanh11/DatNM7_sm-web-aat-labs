# A3-2 – Sinh và review TC + test data cho Giỏ hàng & Checkout

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục A3-2.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 3 | Day 17 (phần 1, 135') + Day 18 (phần 2, 75') | 210' | Phần 1: thực hành 135' · Phần 2: demo 10' + thực hành & nộp 65' | Mentor (chấm 1 lần sau phần 2) | Review A3-2 (Day 18) + CK3-2 |

**Mục tiêu:** Sinh bằng AI và review ≥ 30 TC + test data giả, lập traceability, đưa vào GitHub Projects, tính acceptance rate.

**Bài học tiên quyết:** A3-1

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| A2-3 | `A2-3/A2_Test_Design_Coverage.csv` | **Bắt buộc** | Test condition A2-3 BẢN ĐÃ FIX COMMENT (đã bổ sung condition thiếu so benchmark) – mỗi TC phải trỏ về condition_id. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py A3-2 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 02_SRS_Storefront.md
- Template T02_Test_Case.csv, A3_Traceability_Matrix.csv, A3_Review_Decision_Log.csv, A3_GitHub_Projects_Import.csv
- scripts/import_tc_to_project.sh (starter)

## Các bước (tóm tắt)
1. [Phần 1] Sinh TC (T02) từ condition A2-3 bằng AI, ưu tiên REQ Cao/Trung bình; lưu raw output.
2. [Phần 1] Review từng TC: giữ/sửa nhỏ/sửa lớn/loại → A3_Review_Decision_Log.csv kèm lý do.
3. [Phần 1] Lưu bản sau review vào reviewed/T02_Test_Case.csv (≥ 30 TC); tạo test data giả. Commit cuối buổi.
4. [Phần 2] Lập traceability REQ ↔ condition ↔ TC.
5. [Phần 2] Tạo project "SM-WEB Test Cases" (TC ID, REQ, Priority, Status), import bằng script hoặc thủ công; chụp ảnh vào evidence/.
6. [Phần 2] Tính acceptance rate = (giữ + sửa nhỏ) / tổng TC AI sinh × 100%.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `A3-2/raw_ai_output/*` | Output AI nguyên bản | **Bắt buộc** | – |
| `A3-2/reviewed/T02_Test_Case.csv` | ≥ 30 TC sau review (có condition_id) | **Bắt buộc** | ≥ 30 dòng |
| `A3-2/A3_Review_Decision_Log.csv` | Giữ / sửa nhỏ / sửa lớn / loại + lý do | **Bắt buộc** | ≥ 30 dòng |
| `A3-2/test_data/test_data.csv` | Data giả (@example.com, thẻ test công khai, địa chỉ hư cấu) | **Bắt buộc** | ≥ 1 dòng |
| `A3-2/A3_Traceability_Matrix.csv` | REQ ↔ condition ↔ TC (các lab sau bổ sung cột automation/bug) | **Bắt buộc** | ≥ 30 dòng |
| `A3-2/A3_GitHub_Projects_Import.csv` | File import GitHub Projects | **Bắt buộc** | ≥ 30 dòng |
| `A3-2/acceptance_rate.md` | Acceptance rate theo định nghĩa 1.4 | **Bắt buộc** | – |
| `A3-2/evidence/*` | Ảnh GitHub Projects | **Bắt buộc** | – |
| `A3-2/time_log.csv` | Thời gian sinh + review TC (tham khảo cho A6-3) | Khuyến nghị | ≥ 1 dòng |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py A3-2 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| A4-3 | `A3-2/reviewed/T02_Test_Case.csv` | **Bắt buộc** | Chọn 10 TC ưu tiên cao đã review; tên test bắt đầu bằng TC ID (vd TC-SF04-01) để truy vết. |
| A4-3 | `A3-2/A3_Traceability_Matrix.csv` | Khuyến nghị | Điền cột automated_ui_id cho 10 TC được tự động hóa. |
| A7-3 | `A3-2/A3_Traceability_Matrix.csv` | Khuyến nghị | Điền cột automated_api_id cho REQ-API/REQ-SF-31 để traceability phủ cả API. |
| A5-3 | `A3-2/A3_Traceability_Matrix.csv` | Khuyến nghị | Gắn bug với REQ/TC (điền cột bug_id) để test summary nêu được phạm vi ảnh hưởng. |
| A6-3 | `A3-2/A3_Review_Decision_Log.csv` | **Bắt buộc** | KPI acceptance rate (định nghĩa 1.4). |

Dùng lại ngoài lab: Đồ án cuối khóa (bổ sung đủ ≥ 50 TC).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Chất lượng TC (đúng nghiệp vụ, bước rõ, expected kiểm chứng được, thực thi được trên Toolshop) — **30**
- [ ] Traceability đầy đủ REQ ↔ condition ↔ TC — **20**
- [ ] Test data đúng & không PII thật — **15**
- [ ] Review decision log + acceptance rate đúng định nghĩa — **20**
- [ ] Đưa vào GitHub Projects theo template — **15**

**Điều kiện bắt buộc:** ≥ 30 TC sau review

**Critical fail (dừng chấm):** PII thật trong data

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
