# A7-3 – API suite ≥ 15 logical test case cho Giỏ hàng & Checkout, chạy CI

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục A7-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 5 | Day 25 | 225' | demo 10' + thực hành & nộp 215' | Mentor | Review A7-3 (Day 26) + CK4-2 |

**Mục tiêu:** Thiết kế và tự động hóa API suite ≥ 15 logical TC (contract/schema, auth, negative, data-driven); chạy CI trên bản chuẩn và target lỗi.

**Bài học tiên quyết:** A7-1, A7-2, F0-TS

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| A4-3 | `A4-3/stability_runs.csv` | **Bắt buộc** | API suite đưa vào CI CÙNG suite UI của A4-3 – workflow CI phải đang chạy ổn định. |
| A3-2 | `A3-2/A3_Traceability_Matrix.csv` | Khuyến nghị | Điền cột automated_api_id cho REQ-API/REQ-SF-31 để traceability phủ cả API. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py A7-3 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 02_SRS_Storefront.md mục 4 (REQ-API-01…04) + REQ-SF-31
- Swagger Toolshop
- Target lỗi: api-with-bugs hoặc aat-api-mutant-proxy (trainer chọn)

## Các bước (tóm tắt)
1. Đọc Swagger, chọn endpoint giỏ hàng, hóa đơn, đăng nhập (tên chính xác theo Swagger).
2. AI gợi ý case; kiểm chứng từng case với Swagger/SRS → A7_API_AI_Evidence.csv.
3. Viết ≥ 15 logical TC (API-TC-01…), oracle status + schema + body; phủ contract (API-01), auth 401/403 (API-02, 04; oracle 403 theo 1.6), negative 4xx không 5xx (API-03), ≥ 1 data-driven.
4. Đưa vào CI cùng suite UI; chạy trên bản chuẩn (xanh) và target lỗi (case tương ứng fail) → ci_runs.md.
5. Token/mật khẩu lấy từ Secrets, không ghi trong code.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `A7-3/api_tc_list.csv` | ≥ 15 logical TC (API-TC-xx) với oracle status + schema + body | **Bắt buộc** | ≥ 15 dòng |
| `A7-3/A7_API_AI_Evidence.csv` | Case ID, prompt, nguồn kiểm chứng, giữ/sửa/loại + lý do | **Bắt buộc** | ≥ 1 dòng |
| `A7-3/ci_runs.md` | Link CI run bản chuẩn (xanh) + target lỗi (fail đúng case) | **Bắt buộc** | – |
| `A7-3/time_log.csv` | Thời gian thiết kế + tự động hóa API (tùy chọn cho A6-3) | Khuyến nghị | ≥ 1 dòng |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py A7-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| A5-3 | `A7-3/api_tc_list.csv` | **Bắt buộc** | Chạy suite API của A7-3; request/response làm bằng chứng RCA. |
| A6-3 | `A7-3/time_log.csv` | Khuyến nghị | Bổ sung (tùy chọn) dữ liệu automation API. |

Dùng lại ngoài lab: Đồ án cuối khóa (automation API chạy CI).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Thiết kế case & oracle đúng (ID, oracle status + schema + body) — **30**
- [ ] Phủ contract/schema, auth, negative — **20**
- [ ] Data-driven & chạy CI — **15**
- [ ] Phát hiện lỗi cài sẵn trên target lỗi — **20**
- [ ] Bằng chứng AI-augmented (prompt, nguồn kiểm chứng, quyết định) — **15**

**Điều kiện bắt buộc:** ≥ 15 logical TC; Suite xanh trên bản chuẩn; Bắt được ≥ 1 lỗi cài sẵn

**Critical fail (dừng chấm):** Lộ token/secret

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
