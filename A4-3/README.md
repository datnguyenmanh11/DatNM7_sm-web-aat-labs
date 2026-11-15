# A4-3 – Tự động hóa 10 TC UI của Giỏ hàng & Checkout từ mẫu khởi tạo, chạy CI

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục A4-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 4 | Day 21 | 255' | demo 15' + thực hành & nộp 240' | Mentor | Review A4-3 (Day 22) + CK3-2 |

**Mục tiêu:** Tự động hóa 10 TC UI (chọn từ A3-2) trên starter có POM, fixture, workflow CI; review code AI; đạt chuẩn ổn định 1.5.

**Bài học tiên quyết:** A4-1, A4-2, F0-TS

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| A3-2 | `A3-2/reviewed/T02_Test_Case.csv` | **Bắt buộc** | Chọn 10 TC ưu tiên cao đã review; tên test bắt đầu bằng TC ID (vd TC-SF04-01) để truy vết. |
| A3-2 | `A3-2/A3_Traceability_Matrix.csv` | Khuyến nghị | Điền cột automated_ui_id cho 10 TC được tự động hóa. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py A4-3 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- Starter aat-playwright-starter (pages/, fixtures, stability-10x.yml)
- vars.BASE_URL = Toolshop bản chuẩn

## Các bước (tóm tắt)
1. Đặt biến repo vars.BASE_URL = Toolshop bản chuẩn.
2. Mở rộng pages/ProductPage.ts, pages/CheckoutPage.ts; locator theo role/label/data-test (xác nhận bằng codegen/Inspector).
3. AI gợi ý code theo mẫu; review từng đoạn trước khi commit; ghi phần đã sửa vào prompt_record.md.
4. Chạy local, sửa flaky bằng web-first assertion (không waitForTimeout, không retry).
5. Chạy workflow stability-10x.yml (10 lần toàn suite, retries = 0) → ghi stability_runs.csv; đạt khi ≥ 9/10.
6. Ghi flaky_notes.md; cập nhật cột automated_ui_id trong A3-2/A3_Traceability_Matrix.csv.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `A4-3/automated_tc.csv` | 10 TC đã tự động hóa: TC ID ↔ file spec ↔ test title | **Bắt buộc** | ≥ 10 dòng |
| `A4-3/stability_runs.csv` | 10 lần chạy toàn suite (link run stability-10x), ≥ 9/10 đúng, retries = 0 | **Bắt buộc** | ≥ 10 dòng |
| `A4-3/flaky_notes.md` | Lần fail, nguyên nhân, cách sửa | **Bắt buộc** | – |
| `A4-3/prompt_record.md` | Prompt + phần code AI đã sửa | **Bắt buộc** | – |
| `A4-3/time_log.csv` | Automation time (đầu vào KPI A6-3) | **Bắt buộc** | ≥ 1 dòng |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py A4-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| A7-3 | `A4-3/stability_runs.csv` | **Bắt buộc** | API suite đưa vào CI CÙNG suite UI của A4-3 – workflow CI phải đang chạy ổn định. |
| A5-3 | `A4-3/automated_tc.csv` | **Bắt buộc** | Chạy suite UI của A4-3 trên bản with-bugs để phát hiện lỗi. |
| A6-3 | `A4-3/time_log.csv` | **Bắt buộc** | KPI automation time (10 TC đạt chuẩn ổn định). |

Dùng lại ngoài lab: Đồ án cuối khóa (automation UI chạy CI).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] 10 TC đúng expected, assertion có ý nghĩa — **35**
- [ ] POM/fixture đúng mẫu — **20**
- [ ] Locator bền vững (role/label/test-id) — **15**
- [ ] CI đạt chuẩn ổn định (10 lần toàn suite, ≥ 9/10, retries = 0) — **20**
- [ ] Bằng chứng AI (prompt, phần code AI đã sửa) — **10**

**Điều kiện bắt buộc:** Chuẩn ổn định 1.5: ≥ 9/10 lần chạy toàn suite, retries = 0

**Critical fail (dừng chấm):** Dùng retry/self-healing/skip để che lỗi; Lộ secret

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
