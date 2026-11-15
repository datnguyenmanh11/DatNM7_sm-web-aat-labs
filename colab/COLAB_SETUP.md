# Chạy notebook lab trên Colab và ghi kết quả thẳng vào repo (F1-3, F2-3, F6-2)

Notebook mẫu nằm ở `10_Starter_Kit/common/` (bản v1.1). Biến `LAB_OUT` cho script biết thư mục lab trong repo, nên mọi CSV, raw output và log ghi thẳng vào đó. Không cần chép tay từ `/content` (thư mục này mất khi phiên Colab kết thúc).

## Cell 1 – Secrets (một lần cho mỗi notebook)
Trong Colab, mở 🔑 **Secrets** và thêm: `GEMINI_API_KEY`, `LLM_MODEL` (F6-2 thêm `LLM_MODEL_A`, `LLM_MODEL_B`). Nếu muốn push từ Colab thì thêm `GH_TOKEN` (token chỉ có quyền ghi repo cá nhân).
```python
import os
from google.colab import userdata
for k in ["GEMINI_API_KEY", "LLM_MODEL", "LLM_MODEL_A", "LLM_MODEL_B", "GH_TOKEN"]:
    try: os.environ[k] = userdata.get(k)
    except Exception: pass          # secret chưa đặt -> bỏ qua
# KHÔNG print(os.environ[...]); KHÔNG dán key vào cell. Lộ key = critical fail.
```

## Cell 2 – Lấy repo cá nhân + starter kit
```python
HV = "HV001"                                   # mã học viên
REPO = f"/content/sm-web-aat-{HV}"
!git clone https://$GH_TOKEN@<github-nội-bộ>/<org>/sm-web-aat-{HV}.git {REPO}
!git clone <URL repo bộ tài liệu khóa> /content/aat-course    # chứa 10_Starter_Kit/
!pip -q install openai jsonschema pandas
import sys; sys.path.insert(0, "/content/aat-course/10_Starter_Kit/common")
os.environ["F2_FIXTURES"] = "/content/aat-course/10_Starter_Kit/f2_fixtures"
```
Không có `GH_TOKEN` thì clone qua HTTPS và đăng nhập khi được hỏi, hoặc làm theo cách B ở cuối trang.

## Cell 3 – Chạy lab (chỉ chạy ô của lab đang làm)
```python
# F1-3
os.environ["LAB_OUT"] = f"{REPO}/F1-3"
%run /content/aat-course/10_Starter_Kit/common/F1_variability.py

# F2-3 – chép notebook mẫu vào repo một lần, sau đó SỬA PROMPT TRONG BẢN CỦA MÌNH (tăng version + change log)
os.environ["LAB_OUT"] = f"{REPO}/F2-3"
!mkdir -p {REPO}/F2-3/notebook && cp -n /content/aat-course/10_Starter_Kit/common/F2_prompt_chain.py {REPO}/F2-3/notebook/
%run {REPO}/F2-3/notebook/F2_prompt_chain.py

# F6-2 – đo đúng chuỗi F2-3 của mình trên 2 model
os.environ["LAB_OUT"] = f"{REPO}/F6-2"
os.environ["F2_CHAIN"] = f"{REPO}/F2-3/notebook/F2_prompt_chain.py"
%run /content/aat-course/10_Starter_Kit/common/F6_cost_guardrail.py
```
Nếu model "thinking" trả output rỗng (log có `finish_reason=length`), đặt `os.environ["LLM_REASONING_EFFORT"]="low"` hoặc tăng `max_tokens`. **Ghi thay đổi này vào biến cố định**, không sửa raw output.

## Cell 4 – Kiểm tra rồi commit
```python
%cd {REPO}
!python scripts/check_lab_chain.py --secrets
!python scripts/check_lab_chain.py F1-3 --mode submit      # đổi mã lab
!git add -A && git -c user.name="{HV}" -c user.email="{HV}@example.com" commit -m "F1-3: 8 lần chạy [submit F1-3]" && git push
```
Script sinh sẵn dữ liệu và tín hiệu tự động. Học viên vẫn phải **tự điền** các cột đánh giá (`correct_vs_SRS`, `hallucination`, `model_followed_instruction`, `quality_score`…) sau khi đọc raw output.

### Cách B – không push từ Colab
Chạy cell 3, tải thư mục lab về bằng `!zip -r f13.zip {REPO}/F1-3` rồi `files.download("f13.zip")`. Giải nén vào repo trên máy và commit như bình thường.
