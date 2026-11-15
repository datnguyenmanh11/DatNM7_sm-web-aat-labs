#!/usr/bin/env python3
"""Kiểm tra chuỗi lab SM-WEB theo lab_chain.json.

  python scripts/check_lab_chain.py A3-2 --mode start    # đủ đầu vào từ lab trước chưa?
  python scripts/check_lab_chain.py A3-2 --mode submit   # đủ sản phẩm nộp chưa?
  python scripts/check_lab_chain.py --all                # bảng trạng thái cả chuỗi
  python scripts/check_lab_chain.py --secrets            # quét API key/token bị commit (critical fail)

Trạng thái file: OK | TEMPLATE (chưa điền) | THIẾU DÒNG | THIẾU.
Chỉ kiểm tra sự tồn tại/độ đầy đủ – KHÔNG thay mentor chấm nội dung.
"""
import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK = "<!-- TEMPLATE:"
IGNORE = {".gitkeep"}
SECRET_PATTERNS = {
    "Google/Gemini API key": re.compile(r"AIza[0-9A-Za-z_\-]{35}"),
    "Groq API key": re.compile(r"gsk_[0-9A-Za-z]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}"),
    "OpenAI-style key": re.compile(r"sk-[0-9A-Za-z_\-]{32,}"),
    "Bearer/JWT": re.compile(r"eyJ[0-9A-Za-z_\-]{10,}\.eyJ[0-9A-Za-z_\-]{10,}\.[0-9A-Za-z_\-]{10,}"),
}
SCAN_EXT = {".py", ".ts", ".js", ".json", ".md", ".csv", ".txt", ".ipynb", ".yml", ".yaml", ".env", ".log"}


def load():
    return json.loads((ROOT / "lab_chain.json").read_text(encoding="utf-8"))["labs"]


def csv_rows(p: Path) -> int:
    with p.open(encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.reader(f) if any(c.strip() for c in r)]
    return max(len(rows) - 1, 0)


def status(rel: str, min_rows=None):
    """Trả (mã, mô tả)."""
    if "*" in rel:
        hits = [p for p in ROOT.glob(rel) if p.is_file() and p.name not in IGNORE and not p.name.startswith("_TEMPLATE")]
        if not hits:
            return "MISSING", "chưa có file"
        return "OK", f"{len(hits)} file"
    p = ROOT / rel
    if not p.exists():
        return "MISSING", "chưa có file"
    if p.suffix == ".csv":
        n = csv_rows(p)
        need = min_rows or 1
        if n == 0:
            return "TEMPLATE", "mới có header"
        if n < need:
            return "SHORT", f"{n}/{need} dòng"
        return "OK", f"{n} dòng"
    text = p.read_text(encoding="utf-8", errors="ignore")
    if MARK in text:
        return "TEMPLATE", "còn dòng TEMPLATE"
    if not text.strip():
        return "TEMPLATE", "file rỗng"
    return "OK", "đã điền"


ICON = {"OK": "✅", "TEMPLATE": "📝", "SHORT": "⚠️", "MISSING": "❌"}


def check(lab, mode):
    items = lab["upstream"] if mode == "start" else lab["outputs"]
    title = "ĐẦU VÀO từ lab trước" if mode == "start" else "SẢN PHẨM NỘP"
    out = [f"### {lab['id']} – {title}", "", "| | File | Mức | Trạng thái |", "|---|---|---|---|"]
    blocking = 0
    for it in items:
        code, msg = status(it["path"], it.get("min_rows"))
        src = f" (từ {it['from']})" if mode == "start" else ""
        lvl = "Bắt buộc" if it["required"] else "Khuyến nghị"
        out.append(f"| {ICON[code]} | `{it['path']}`{src} | {lvl} | {msg} |")
        if it["required"] and code != "OK":
            blocking += 1
    if not items:
        out.append("| ✅ | – | – | Lab đầu chuỗi, không phụ thuộc lab trước |")
    out.append("")
    if blocking:
        hint = ("Hoàn thành / fix comment lab trước rồi mới bắt đầu." if mode == "start"
                else "Bổ sung trước khi nộp – thiếu bằng chứng = 0 điểm tiêu chí (mục 1.2).")
        out.append(f"**{blocking} mục bắt buộc chưa đạt.** {hint}")
    else:
        out.append("**Đủ điều kiện** " + ("bắt đầu lab." if mode == "start" else "để nộp (mentor vẫn chấm nội dung theo rubric)."))
    return "\n".join(out), blocking


def overview(labs):
    out = ["### Trạng thái chuỗi lab", "", "| Lab | Tuần · Day | Đầu vào bắt buộc | Sản phẩm bắt buộc |", "|---|---|---|---|"]
    for lab in labs:
        def frac(items):
            req = [i for i in items if i["required"]]
            ok = sum(1 for i in req if status(i["path"], i.get("min_rows"))[0] == "OK")
            return f"{ok}/{len(req)}" if req else "–"
        out.append(f"| {lab['id']} | T{lab['week']} · {lab['day']} | {frac(lab['upstream'])} | {frac(lab['outputs'])} |")
    return "\n".join(out)


def scan_secrets():
    found = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts or "node_modules" in p.parts:
            continue
        if p.suffix not in SCAN_EXT and p.name != ".env":
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for name, rx in SECRET_PATTERNS.items():
            if rx.search(text):
                found.append(f"- `{p.relative_to(ROOT)}`: nghi {name}")
    if found:
        return "### ❌ Nghi lộ secret (critical fail)\n\n" + "\n".join(found) + \
               "\n\nXóa khỏi file, **thu hồi (rotate) key**, dùng Colab/GitHub Secrets. Xóa khỏi lịch sử git không đủ – key đã lộ phải đổi.", 1
    return "### ✅ Không phát hiện mẫu secret", 0


def emit(md):
    print(md)
    s = os.environ.get("GITHUB_STEP_SUMMARY")
    if s:
        with open(s, "a", encoding="utf-8") as f:
            f.write(md + "\n\n")


def main():
    labs = load()
    by_id = {l["id"]: l for l in labs}
    ap = argparse.ArgumentParser()
    ap.add_argument("lab", nargs="?", help="Mã lab, vd A3-2")
    ap.add_argument("--mode", choices=["start", "submit"], default="submit")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--secrets", action="store_true")
    a = ap.parse_args()

    rc = 0
    if a.secrets:
        md, r = scan_secrets()
        emit(md)
        rc |= r
    if a.all:
        emit(overview(labs))
    if a.lab:
        lab = by_id.get(a.lab.upper())
        if not lab:
            sys.exit(f"Không có lab '{a.lab}'. Hợp lệ: {', '.join(by_id)}")
        md, blocking = check(lab, a.mode)
        emit(md)
        rc |= 1 if blocking else 0
    if not (a.secrets or a.all or a.lab):
        ap.print_help()
    sys.exit(rc)


if __name__ == "__main__":
    main()
