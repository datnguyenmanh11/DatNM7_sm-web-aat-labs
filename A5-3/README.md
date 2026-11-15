# A5-3 – RCA 5 lỗi Giỏ hàng & Checkout trên SM-WEB bản có lỗi + báo cáo

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục A5-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 6 | Day 28 | 135' | demo 10' + thực hành & nộp 125' | Mentor | Review A5-3 (Day 29) + CK4-2 |

**Mục tiêu:** Dùng AI hỗ trợ RCA nhưng kết luận dựa trên bằng chứng; viết bug report + test summary tiếng Anh; ghi defect analysis time.

**Bài học tiên quyết:** A5-1, A5-2

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| A4-3 | `A4-3/automated_tc.csv` | **Bắt buộc** | Chạy suite UI của A4-3 trên bản with-bugs để phát hiện lỗi. |
| A7-3 | `A7-3/api_tc_list.csv` | **Bắt buộc** | Chạy suite API của A7-3; request/response làm bằng chứng RCA. |
| A3-2 | `A3-2/A3_Traceability_Matrix.csv` | Khuyến nghị | Gắn bug với REQ/TC (điền cột bug_id) để test summary nêu được phạm vi ảnh hưởng. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py A5-3 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- https://with-bugs.practicesoftwaretesting.com (so với bản chuẩn)
- Template A5_RCA_Worksheet.md, T03_Bug_Report_EN.md, T04_Test_Summary_EN.md

## Các bước (tóm tắt)
1. Chạy suite UI/API trên with-bugs; so sánh cùng thao tác trên bản chuẩn.
2. Chọn 5 lỗi (≥ 4 thuộc Giỏ hàng & Checkout); bấm giờ defect analysis time từng lỗi.
3. RCA theo worksheet; giả thuyết AI sai phải loại có lý do + bằng chứng.
4. Bug report EN (T03) + test summary EN (T04).
5. Cập nhật evidence/EVIDENCE_INDEX.md + prompt_record.md; điền bug_id vào traceability.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `A5-3/bug_reports/BUG-*.md` | 5 bug report tiếng Anh (T03) | **Bắt buộc** | – |
| `A5-3/RCA_Worksheet.md` | Triệu chứng → giả thuyết → bằng chứng → nguyên nhân gốc → hành động | **Bắt buộc** | – |
| `A5-3/Test_Summary_EN.md` | Test summary tiếng Anh (T04) cho khách hàng | **Bắt buộc** | – |
| `A5-3/defect_analysis_time.csv` | Defect analysis time 5 lỗi (đầu vào KPI A6-3) | **Bắt buộc** | ≥ 5 dòng |
| `A5-3/prompt_record.md` | Prompt + giả thuyết AI giữ/loại | **Bắt buộc** | – |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py A5-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| A6-3 | `A5-3/defect_analysis_time.csv` | **Bắt buộc** | KPI defect analysis time. |

Dùng lại ngoài lab: Đồ án cuối khóa (5 bug report + RCA, test summary EN).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Tái hiện & bug report đúng chuẩn (bước, expected/actual, severity, evidence) — **25**
- [ ] RCA có bằng chứng, nguyên nhân hợp lý, giả thuyết AI sai được loại có lý do — **30**
- [ ] Test summary EN rõ cho khách hàng — **15**
- [ ] Evidence index + prompt record — **20**
- [ ] Defect analysis time từng lỗi — **10**

**Điều kiện bắt buộc:** ≥ 4/5 lỗi tái hiện được kèm bằng chứng

**Critical fail (dừng chấm):** Bằng chứng giả/sao chép

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
