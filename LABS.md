# SM-WEB – Khung bài tập lab AAT (10 lab, nối thành chuỗi)

Khung này được chép vào repo cá nhân `sm-web-aat-<mã HV>` (tạo từ `10_Starter_Kit/aat-playwright-starter`). Mỗi lab trong `05_Lab_Guides.md` có một thư mục riêng, gồm đề tóm tắt, template sản phẩm nộp, và chỉ rõ **file nào lấy từ lab trước** và **file nào lab sau sẽ dùng**.

- Nguồn chuẩn: Syllabus AAT v1.4 → `05_Lab_Guides.md`, `04_Backlog_xuyen_suot.md`. Nếu có khác biệt thì theo syllabus và báo training lead.
- Sơ đồ và bảng nối: **[LAB_CHAIN.md](LAB_CHAIN.md)**
- Dữ liệu chuỗi (máy đọc được): `lab_chain.json`, là nguồn để sinh README từng lab và để script kiểm tra.

## 1. Cài vào repo cá nhân (làm 1 lần, Tuần 0 / A1-1)
```bash
# trong repo sm-web-aat-<mã HV> đã tạo từ starter
cp -rn <thư-mục-khung>/. .              # -n: không ghi đè file sẵn có của starter
python scripts/generate_lab_docs.py --init   # tạo template còn thiếu, sinh README lab
cat >> .gitignore <<'EOF'
.env
*.key
colab_secrets*
EOF
git add . && git commit -m "chore: thêm khung lab SM-WEB"
```
Workflow `lab-chain-check.yml` có tên riêng nên không đụng các workflow `stability-10x.yml` hoặc CI của starter.

## 2. Thứ tự lab và mạch nối
| # | Lab | Tuần · Day | Phút | Nhận đầu vào chính từ | Chuyển giao chính cho |
|---|---|---|---|---|---|
| 1 | [F1-3](F1-3/README.md) | T1 · Day 2 | 60 | SRS REQ-SF-03 | F2-3 (bài học về hallucination và tái lập) |
| 2 | [F2-3](F2-3/README.md) | T1 · Day 5 | 135 | Fixture F2, F1-3 | F6-2 (task đo chi phí), A2-3 (khung prompt), A6-3 (prompt library v1) |
| 3 | [F6-2](F6-2/README.md) | T2 · Day 8 | 60 | **F2-3** (chuỗi prompt + prompt library) | Model đã chọn + guardrail cho các lab A (khuyến nghị) |
| 4 | [A1-4](A1-4/README.md) | T2 · Day 11 | 120 | SRS 12 REQ + KB-02 | **A2-3** (review log đã fix) |
| 5 | [A2-3](A2-3/README.md) | T3 · Day 15 | 210 | **A1-4** | **A3-2** (condition đã fix), A6-3 (coverage, design time) |
| 6 | [A3-2](A3-2/README.md) | T3 · Day 17 + T4 · Day 18 | 135 + 75 | **A2-3** | **A4-3** (10 TC), A6-3 (acceptance rate), traceability cho A4/A7/A5 |
| 7 | [A4-3](A4-3/README.md) | T4 · Day 21 | 255 | **A3-2** | **A7-3** (CI chung), **A5-3** (suite UI), A6-3 (automation time) |
| 8 | [A7-3](A7-3/README.md) | T5 · Day 25 | 225 | Swagger + **A4-3** (CI) | **A5-3** (suite API) |
| 9 | [A5-3](A5-3/README.md) | T6 · Day 28 | 135 | **A4-3**, **A7-3** | A6-3 (defect analysis time) |
| 10 | [A6-3](A6-3/README.md) | T6 · Day 30 | 60 | **A2-3, A3-2, A4-3, A5-3**, F2-3 | Đồ án cuối khóa (5 KPI), prompt library v2 |

Chữ **đậm** là phụ thuộc bắt buộc. Sau các lab, cả chuỗi đổ vào **G3 → RP (Tuần 7) → đồ án cuối khóa (Tuần 8)**.

## 3. Vòng làm một lab
```
check start ─► làm lab ─► check submit ─► commit "[submit <lab>]" ─► nộp link commit qua form
     ▲                                                                      │
     └──── lab sau ◄── commit "fix comment" ◄── review lab & fix comment ◄──┘
```
1. `python scripts/check_lab_chain.py <lab> --mode start` kiểm tra lab trước đã có đủ đầu vào (bản đã fix comment) chưa.
2. Làm theo `<lab>/README.md`, đề đầy đủ ở `05_Lab_Guides.md`.
3. `python scripts/check_lab_chain.py <lab> --mode submit` kiểm tra đủ sản phẩm nộp và đủ số dòng tối thiểu (≥ 8 lần chạy, ≥ 30 TC, ≥ 15 API TC, 10 CI run, 5 lỗi, 5 KPI).
4. Commit với message chứa `[submit <lab>]` (vd `[submit A3-2]`). CI chạy lại kiểm tra và báo đỏ nếu thiếu mục bắt buộc.
5. Nộp link commit qua form của khóa trên LevelUp, rồi ghi vào `evidence/EVIDENCE_INDEX.md`.
6. Sau buổi review: sửa, commit `fix comment <lab>`, ghi commit đó vào EVIDENCE_INDEX. **Lab sau dùng bản đã fix.**

> Script chỉ kiểm tra file có tồn tại và đã được điền hay chưa. Nội dung vẫn do trainer/mentor chấm theo rubric.

## 4. Cấu trúc repo
```
LABS.md                         # file này
LAB_CHAIN.md                    # sơ đồ + bảng nối (sinh tự động)
lab_chain.json                  # dữ liệu chuỗi lab
evidence/EVIDENCE_INDEX.md      # mục lục bằng chứng + checklist A1-1
F3_AI_Usage_Escalation_Log.csv  # dùng suốt khóa (mở từ F3-1)
prompts/PROMPT_LIBRARY.md       # v1 (F2-3) → v2 (A6-3)
scripts/check_lab_chain.py      # kiểm tra start/submit/secrets
scripts/generate_lab_docs.py    # sinh README lab + LAB_CHAIN.md; --init tạo template
.github/workflows/lab-chain-check.yml
<mã lab>/                       # F1-3 … A6-3
  README.md                     # đề tóm tắt + đầu vào ⬅️ / đầu ra ➡️ + tự kiểm rubric
  prompt_record.md              # mẫu mục 1.7
  raw_ai_output/                # output AI nguyên bản, KHÔNG sửa: <ngày>_<prompt-id>_<lần>.txt/json
  reviewed/  evidence/          # bản sau review / ảnh, link CI, request-response, log
  ...                           # template sản phẩm nộp của lab
```
Code Playwright đặt theo cấu trúc của starter (`pages/`, `tests/…`, `tests/api/`). Thư mục `A4-3/` và `A7-3/` chỉ chứa bảng ánh xạ TC ↔ spec, CI run và ghi chú.

## 5. Ba sợi nối xuyên chuỗi
- **Traceability**: `A3-2/A3_Traceability_Matrix.csv` do A3-2 lập. Sau đó A4-3 điền `automated_ui_id`, A7-3 điền `automated_api_id`, A5-3 điền `bug_id`. Đồ án dùng lại ma trận này.
- **Đo thời gian (KPI)**: `time_log.csv` của A2-3, A3-2, A4-3 (và A7-3) cùng `A5-3/defect_analysis_time.csv` là dữ liệu cho A6-3. Ghi giờ ngay trong lúc làm, không ghi bù.
- **Prompt library**: F2-3 tạo v1. Các lab A thêm prompt mới có version. A6-3 nâng lên v2.

## 6. Quy tắc bắt buộc (mục 1.2 Lab Guide)
- Rubric 100 điểm, đạt khi **≥ 70**, đủ mọi điều kiện bắt buộc, và không có critical fail.
- **Critical fail**: dữ liệu thật/PII thật; lộ secret/API key/token (CI tự quét bằng `--secrets`); bằng chứng giả hoặc sao chép; dùng retry/self-healing/skip để che lỗi ở A4.
- Tiêu chí không có bằng chứng truy được thì được **0 điểm**.

## 7. Dành cho trainer
Khi syllabus đổi (thời lượng, ngưỡng, file chuyển giao), chỉ cần sửa `lab_chain.json` rồi chạy `python scripts/generate_lab_docs.py`. README của từng lab và LAB_CHAIN.md sẽ được sinh lại cho khớp.
