# A6-3 – Đo 5 KPI + hoàn thiện prompt library v2

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục A6-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 6 | Day 30 | 60' | thực hành & nộp 60' | Mentor | Review A6-3 (Day 30) + CK4-2 |

**Mục tiêu:** Tổng hợp 5 KPI theo protocol (05b mục A6-1) từ dữ liệu lab A2–A5; nâng prompt library lên v2; ghi escalation.

**Bài học tiên quyết:** A6-1, A6-2

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| A2-3 | `A2-3/time_log.csv` | **Bắt buộc** | KPI design time. |
| A2-3 | `A2-3/coverage_summary.md` | **Bắt buộc** | KPI benchmark coverage (v2). |
| A3-2 | `A3-2/A3_Review_Decision_Log.csv` | **Bắt buộc** | KPI acceptance rate (định nghĩa 1.4). |
| A4-3 | `A4-3/time_log.csv` | **Bắt buộc** | KPI automation time (10 TC đạt chuẩn ổn định). |
| A5-3 | `A5-3/defect_analysis_time.csv` | **Bắt buộc** | KPI defect analysis time. |
| A7-3 | `A7-3/time_log.csv` | Khuyến nghị | Bổ sung (tùy chọn) dữ liệu automation API. |
| F2-3 | `prompts/PROMPT_LIBRARY.md` | **Bắt buộc** | Prompt library v1 → nâng lên v2. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py A6-3 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- Template T06_KPI_AAT.csv, T05_Prompt_Library.md
- Protocol KPI 05b mục A6-1

## Các bước (tóm tắt)
1. Điền T06: design time, automation time, defect analysis time, benchmark coverage, acceptance rate – mỗi số có link file/commit nguồn.
2. Diễn giải: xu hướng, sai lệch đo (cherry-pick, tác vụ không tương đương).
3. Nâng prompt library v1 → v2: metadata, version, người review, trạng thái, bằng chứng chất lượng.
4. Ghi escalation (nếu có) vào F3_AI_Usage_Escalation_Log.csv.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `A6-3/T06_KPI_AAT.csv` | Đủ 5 KPI, mỗi số có nguồn (file/commit) | **Bắt buộc** | ≥ 5 dòng |
| `A6-3/kpi_interpretation.md` | Diễn giải xu hướng + sai lệch đo | **Bắt buộc** | – |
| `prompts/PROMPT_LIBRARY.md` | Prompt library v2 (metadata, version, reviewer, trạng thái, bằng chứng) | **Bắt buộc** | – |
| `F3_AI_Usage_Escalation_Log.csv` | Log escalation (nếu có) | Khuyến nghị | ≥ 1 dòng |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py A6-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
_Không có lab sau dùng trực tiếp._

Dùng lại ngoài lab: Đồ án cuối khóa (5 KPI); RP (protocol Baseline/After).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Đủ 5 KPI, công thức đúng — **40**
- [ ] Nguồn dữ liệu truy vết được — **20**
- [ ] Diễn giải hợp lý (có nêu sai lệch đo) — **15**
- [ ] Prompt library v2 đủ metadata — **25**

**Điều kiện bắt buộc:** Đủ 5 KPI

**Critical fail (dừng chấm):** Số liệu bịa/không có nguồn

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
