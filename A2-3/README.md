# A2-3 – Thiết kế test với AI cho Giỏ hàng & Checkout, so benchmark coverage

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục A2-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 3 | Day 15 | 210' | demo 15' + thực hành & nộp 195' | Mentor | Review A2-3 (Day 16) – bổ sung condition còn thiếu so benchmark |

**Mục tiêu:** Áp dụng ≥ 4/5 kỹ thuật (EP, BVA, decision table, state transition, pairwise) với AI; đo coverage theo quy tắc 1.3; loại trùng.

**Bài học tiên quyết:** A2-1, A2-2

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| A1-4 | `A1-4/A1_Review_Log.csv` | **Bắt buộc** | Review log ĐÃ FIX COMMENT: mâu thuẫn/mơ hồ đã làm rõ (vd ngưỡng free ship REQ-SF-15) quyết định condition và expected. |
| A1-4 | `A1-4/Test_Plan.md` | Khuyến nghị | Ưu tiên/độ sâu theo rủi ro → chọn kỹ thuật và mức Cao cho REQ. |
| F2-3 | `prompts/PROMPT_LIBRARY.md` | Khuyến nghị | Tái dùng khung prompt sinh condition JSON (PR-F2-02) làm gốc cho prompt theo từng kỹ thuật. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py A2-3 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 02_SRS_Storefront.md mục 3–4
- Benchmark 30 condition (trainer phát SAU khi nộp v1)
- PICT (pairwise)

## Các bước (tóm tắt)
1. Prompt theo từng kỹ thuật (1 prompt/kỹ thuật, có version) cho Giỏ hàng & Checkout.
2. Review: loại trùng (duplicate rule), loại hallucination, gắn REQ + ưu tiên; ghi giữ/sửa/loại.
3. Nộp v1 → trainer phát benchmark 30 condition.
4. Đối chiếu Match/Partial/Miss theo quy tắc 1.3, tính coverage, liệt kê thiếu/thừa.
5. Cải tiến prompt v2 cho phần thiếu, chạy lại, đo coverage v2. Bấm giờ vào time_log.csv.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `A2-3/A2_Test_Design_Coverage.csv` | Condition v1 + v2 (cột version), REQ, kỹ thuật, quyết định, benchmark_id, match_type | **Bắt buộc** | ≥ 1 dòng |
| `A2-3/coverage_summary.md` | Bảng coverage v1, v2 + condition thiếu/thừa | **Bắt buộc** | – |
| `A2-3/prompt_record.md` | 1 prompt/kỹ thuật có version + quyết định | **Bắt buộc** | – |
| `A2-3/time_log.csv` | Design time (đầu vào KPI A6-3) | **Bắt buộc** | ≥ 1 dòng |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py A2-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| A3-2 | `A2-3/A2_Test_Design_Coverage.csv` | **Bắt buộc** | Test condition A2-3 BẢN ĐÃ FIX COMMENT (đã bổ sung condition thiếu so benchmark) – mỗi TC phải trỏ về condition_id. |
| A6-3 | `A2-3/time_log.csv` | **Bắt buộc** | KPI design time. |
| A6-3 | `A2-3/coverage_summary.md` | **Bắt buộc** | KPI benchmark coverage (v2). |

Dùng lại ngoài lab: G3 / RP / đồ án: chuẩn coverage ≥ 90%.

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Áp dụng đúng kỹ thuật (≥ 4/5; đúng loại yêu cầu) — **35**
- [ ] Coverage v2: ≥ 90% = 30; 80–89% = 25; 70–79% = 20; < 70% = 0 — **30**
- [ ] Loại trùng đúng rule — **15**
- [ ] Bằng chứng AI & quyết định giữ/sửa/loại — **20**

**Điều kiện bắt buộc:** Coverage v2 ≥ 70% benchmark; Mọi REQ ưu tiên Cao trong phạm vi có ≥ 1 condition

**Critical fail (dừng chấm):** Bằng chứng giả

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
