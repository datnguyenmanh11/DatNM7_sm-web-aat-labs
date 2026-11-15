# F2-3 – Chuỗi prompt yêu cầu → test condition (JSON schema), self-check, kiểm thử injection + đo thời gian

> File này được sinh từ `lab_chain.json` bằng `scripts/generate_lab_docs.py` – không sửa tay. Đề đầy đủ: `05_Lab_Guides.md` mục F2-3.

| Tuần | Day | Thời lượng | Hình thức | Người chấm | Review & fix comment |
|---|---|---|---|---|---|
| 1 | Day 5 | 135' | demo 15' + thực hành & nộp 120' | Trainer (chữa trong CK1-1) | CK1-1 (Day 6) + Review lab nền tảng (Day 8) |

**Mục tiêu:** Xây chuỗi prompt có version sinh test condition đúng schema, truy vết req ID, phát hiện hallucination, kiểm thử injection, tái lập được.

**Bài học tiên quyết:** F2-1, F2-2

## ⬅️ Đầu vào từ lab trước
| Từ | File | Mức | Dùng để làm gì |
|---|---|---|---|
| F1-3 | `F1-3/conclusion.md` | Khuyến nghị | Bài học F1-3 (biến thiên, hallucination khi thiếu ngữ cảnh) → luôn đưa đoạn SRS vào prompt, cố định config để tái lập. |
| F2-1 | `prompts/PROMPT_LIBRARY.md` | Khuyến nghị | 2 prompt có version + change log từ bài F2-1 (PR-F2-001 v1.0 → v1.1) là điểm xuất phát. |

Kiểm tra trước khi bắt đầu: `python scripts/check_lab_chain.py F2-3 --mode start`

**Đầu vào khác (bộ tài liệu khóa):**
- 10_Starter_Kit/f2_fixtures/ (tc_condition.schema.json, fixture_srs_cart_checkout.md, fixture_srs_injection.md)
- 10_Starter_Kit/common/F2_prompt_chain.py
- KHÔNG dùng Toolshop bản có lỗi

## ▶️ Chạy notebook (Colab) – output ghi thẳng vào thư mục lab
- Script: `F2-3/notebook/F2_prompt_chain.py (bản học viên chép từ 10_Starter_Kit/common rồi sửa prompt)` · `LAB_OUT=<repo>/F2-3` · biến: `LLM_MODEL`, `F2_FIXTURES`
- Ghi ra: `F2-3/raw_ai_output/<batch>_<prompt-id>_<tag>.txt`; `F2-3/injection_cases.csv (tín hiệu tự động)`; `F2-3/f2_results.json (config tái lập + kết quả)`; `F2-3/f2_llm_calls.csv`
- Cách đặt Secrets, clone repo, commit: [colab/COLAB_SETUP.md](../colab/COLAB_SETUP.md)

## Các bước (tóm tắt)
1. Prompt 1 PR-F2-01 v1.0: trích {req_id, mô tả, giá trị/quy tắc} từ fixture.
2. Prompt 2 PR-F2-02 v1.0: sinh condition JSON theo tc_condition.schema.json, req_id phải thuộc danh sách prompt 1.
3. Prompt 3 PR-F2-03 v1.0: self-check (req_id lạ, giá trị không có trong SRS, biên còn thiếu).
4. Validate bằng jsonschema; req_id ngoài whitelist → đánh dấu hallucination, loại.
5. Chạy trên fixture_srs_injection.md (3 ca: bỏ qua schema, REQ-SF-99, lộ system prompt) → ghi injection_cases.csv.
6. Chạy lại toàn chuỗi 2 lần cùng config, so số condition và req_id phủ.
7. Bấm giờ 5 condition thủ công vs chuỗi prompt (gồm review) → time_measurement.csv.
8. Lưu prompt có version vào prompts/PROMPT_LIBRARY.md (v1).

## 📦 Sản phẩm nộp (trong thư mục này / repo)
| File | Nội dung | Mức | Tối thiểu |
|---|---|---|---|
| `prompts/PROMPT_LIBRARY.md` | Prompt library v1: PR-F2-01/02/03 có version + change log | **Bắt buộc** | – |
| `F2-3/notebook/F2_prompt_chain.py` | Chuỗi prompt của học viên (chép từ starter, sửa prompt + version); F6-2 chạy lại đúng file này | **Bắt buộc** | – |
| `F2-3/AI_Output_Evaluation.md` | Đánh giá: schema, traceability, hallucination, tái lập, 3 ca injection | **Bắt buộc** | – |
| `F2-3/injection_cases.csv` | ≥ 3 ca injection: hành vi model + kiểm soát phát hiện | **Bắt buộc** | ≥ 3 dòng |
| `F2-3/time_measurement.csv` | Bảng đo thời gian thủ công vs chuỗi prompt | **Bắt buộc** | ≥ 2 dòng |
| `F2-3/raw_ai_output/*` | Raw output 2 lần chạy + bản injection | **Bắt buộc** | – |
| `F2-3/f2_results.json` | Config tái lập + kết quả 2 lần chạy + injection (notebook tự ghi) | **Bắt buộc** | – |

Kiểm tra trước khi nộp: `python scripts/check_lab_chain.py F2-3 --mode submit` → nộp **link commit** qua form + cập nhật `evidence/EVIDENCE_INDEX.md`.

## ➡️ Đầu ra được dùng ở lab sau
| Lab sau | File của lab này | Mức | Dùng để làm gì |
|---|---|---|---|
| F6-2 | `F2-3/notebook/F2_prompt_chain.py` | **Bắt buộc** | F6_cost_guardrail.py nạp đúng file này (biến F2_CHAIN): 1 task = 1 lần chạy chuỗi F2-3 của chính học viên, cùng prompt version, cùng input. |
| F6-2 | `prompts/PROMPT_LIBRARY.md` | **Bắt buộc** | Ghi đúng prompt ID + version dùng để đo trên 2 model. |
| F6-2 | `F2-3/AI_Output_Evaluation.md` | Khuyến nghị | Cách chấm schema/coverage/hallucination của F2-3 dùng lại cho điểm chất lượng. |
| F6-2 | `F2-3/f2_results.json` | Khuyến nghị | Số condition / req_id phủ / hallucination của F2-3 làm mốc so chất lượng 2 model. |
| A2-3 | `prompts/PROMPT_LIBRARY.md` | Khuyến nghị | Tái dùng khung prompt sinh condition JSON (PR-F2-02) làm gốc cho prompt theo từng kỹ thuật. |
| A6-3 | `prompts/PROMPT_LIBRARY.md` | **Bắt buộc** | Prompt library v1 → nâng lên v2. |

Dùng lại ngoài lab: G1 (đánh giá lại rubric); WS #1 (prompt library v1).

> ⚠️ Lab sau dùng **bản đã fix comment** – sửa xong theo nhận xét review rồi mới chuyển sang lab tiếp theo.

## ✅ Tự kiểm theo rubric (100 điểm, đạt ≥ 70)
- [ ] JSON hợp lệ theo schema — **15**
- [ ] Condition truy vết tới req ID; coverage ≥ 70% benchmark fixture (quy ước 1.3) — **30**
- [ ] Phát hiện & loại hallucination — **20**
- [ ] ≥ 3 ca injection được ghi nhận (hành vi + kiểm soát phát hiện) — **15**
- [ ] Config/version đủ để tái lập (2 lần chạy lại) — **10**
- [ ] Bảng đo thời gian — **10**

**Điều kiện bắt buộc:** Coverage ≥ 70% benchmark fixture; ≥ 3 ca injection

**Critical fail (dừng chấm):** Dữ liệu thật/secret trong prompt

Quy tắc chung: insufficient evidence → 0 điểm tiêu chí; mọi dùng AI có dữ liệu cần cân nhắc → ghi `F3_AI_Usage_Escalation_Log.csv`.
