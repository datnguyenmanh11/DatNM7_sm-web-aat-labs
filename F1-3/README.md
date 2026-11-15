# F1-3 – Thí nghiệm biến thiên output và hallucination (có kiểm soát biến)

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục F1-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 1 | Day 2 | 60' | demo 10' + thực hành & nộp 50' | Trainer (chữa trong CK1-1) | CK1-1 (Day 6) + Review lab nền tảng (Day 8) |

**Mục tiêu:** Đo ảnh hưởng của một biến tới output LLM khi giữ cố định các biến khác; rút kết luận dựa trên số đo.

**Bài học tiên quyết:** F1-1, F1-2, F3-1

## ⬅️ Đầu vào từ lab trước
_Lab đầu chuỗi – không phụ thuộc lab trước._

**Đầu vào khác (bộ tài liệu khóa):**
- 02_Requirements/02_SRS_Storefront.md – REQ-SF-03 (số lượng 1–10)
- 10_Starter_Kit/common/F1_variability.py (Colab)

## ▶️ Chạy notebook (Colab) – output ghi thẳng vào thư mục lab
- Script: `10_Starter_Kit/common/F1_variability.py` · `LAB_OUT=<repo>/F1-3` · biến: `LLM_MODEL`
- Ghi ra: `F1-3/F1_Experiment_Log.csv (đúng cột template)`; `F1-3/raw_ai_output/<batch>_PR-F1-001_<lần>_*.txt`; `F1-3/f1_llm_calls.csv`
- Cách đặt Secrets, clone repo, commit: [colab/COLAB_SETUP.md](../colab/COLAB_SETUP.md)

## Các bước (tóm tắt)
1. Đặt GEMINI_API_KEY, LLM_MODEL trong Colab Secrets (không dán key vào notebook).
2. Ghi biến cố định: model + version, prompt PR-F1-001 v1.0, input, max_tokens, top_p, ngày giờ chạy.
3. E1 – chỉ đổi temperature: temp 0 × 3 lần, temp 1 × 3 lần.
4. E2 – chỉ đổi ngữ cảnh: câu hỏi dễ hallucination, 1 lần có đoạn SRS, 1 lần không (temp 0).
5. Điền F1_Experiment_Log.csv (mỗi dòng 1 lần chạy), lưu raw output vào raw_ai_output/.
6. Viết conclusion.md: biến thiên, khi nào hallucination, hệ quả cho test oracle. Không khẳng định temp 0 là deterministic.

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `F1-3/F1_Experiment_Log.csv` | Config + 8 lần chạy (E1: 3×temp 0, 3×temp 1; E2: có/không SRS) | **Bắt buộc** | ≥ 8 dòng |
| `F1-3/conclusion.md` | Kết luận ≤ 5 câu dựa trên số đo | **Bắt buộc** | – |
| `F1-3/F1-1_notes.md` | Phiếu ghi chú F1-1 (5 khái niệm + ví dụ QA SM-WEB) | **Bắt buộc** | – |
| `F1-3/raw_ai_output/*` | Raw output 8 lần chạy, không sửa | **Bắt buộc** | – |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py F1-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| F2-3 | `F1-3/conclusion.md` | Khuyến nghị | Bài học F1-3 (biến thiên, hallucination khi thiếu ngữ cảnh) → luôn đưa đoạn SRS vào prompt, cố định config để tái lập. |

Dùng lại ngoài lab: G1 (đánh giá lại rubric).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] Ghi đủ biến cố định / biến thay đổi cho từng thí nghiệm — **30**
- [ ] Đủ raw output của 8 lần chạy (không sửa) — **30**
- [ ] Kết luận đúng, dựa trên số đo; không khẳng định temperature 0 là deterministic — **30**
- [ ] Tuân thủ dữ liệu (chỉ dữ liệu SM-WEB/giả; ghi F3 log nếu có tình huống) — **10**

**Critical fail (dừng chấm):** Dùng dữ liệu thật/secret trong prompt; Commit API key

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
