import shlex
import subprocess
import sys
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
THIS_FILE = Path(__file__).resolve()


def discover_python_files() -> list[Path]:
    """Return python scripts under html_version except this Streamlit file."""
    scripts = []
    for file_path in BASE_DIR.rglob("*.py"):
        if file_path.resolve() == THIS_FILE:
            continue
        scripts.append(file_path)
    return sorted(scripts, key=lambda p: str(p.relative_to(BASE_DIR)).lower())


def run_script(script_path: Path, args: str) -> tuple[int, str]:
    cmd = [sys.executable, str(script_path)]
    if args.strip():
        cmd.extend(shlex.split(args))

    result = subprocess.run(
        cmd,
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    output_parts = []
    if result.stdout:
        output_parts.append("=== STDOUT ===\n" + result.stdout)
    if result.stderr:
        output_parts.append("=== STDERR ===\n" + result.stderr)
    if not output_parts:
        output_parts.append("(出力なし)")

    return result.returncode, "\n\n".join(output_parts)


def app() -> None:
    st.set_page_config(page_title="Python Script Launcher", layout="wide")
    st.title("Python Script Launcher")
    st.caption("html_version 内の Python スクリプトをブラウザから実行します。")

    scripts = discover_python_files()
    if not scripts:
        st.warning("実行可能な Python ファイルが見つかりませんでした。")
        return

    labels = [str(path.relative_to(BASE_DIR)) for path in scripts]
    selected_label = st.selectbox("実行するスクリプト", labels, index=0)
    selected_script = scripts[labels.index(selected_label)]

    st.code(f"{sys.executable} {selected_label} [args...]", language="bash")
    args = st.text_input("引数（任意）", value="", placeholder="例: --dry-run")
    auto_rebuild_catalog = st.checkbox(
        "実行後に update_catalog.py で通し番号とカタログを再構築する",
        value=False,
    )

    run_button = st.button("実行", type="primary", use_container_width=True)
    if run_button:
        with st.spinner("実行中..."):
            exit_code, output = run_script(selected_script, args)

        if exit_code == 0:
            st.success(f"終了コード: {exit_code}")
        else:
            st.error(f"終了コード: {exit_code}")
        st.text_area("実行ログ", output, height=400)

        should_run_rebuild = (
            auto_rebuild_catalog
            and selected_script.name != "update_catalog.py"
        )
        if should_run_rebuild:
            rebuild_script = BASE_DIR / "update_catalog.py"
            if rebuild_script.exists():
                with st.spinner("update_catalog.py を実行中..."):
                    rebuild_code, rebuild_output = run_script(rebuild_script, "")
                if rebuild_code == 0:
                    st.success("update_catalog.py の実行に成功しました。")
                else:
                    st.error(f"update_catalog.py の終了コード: {rebuild_code}")
                st.text_area("update_catalog.py 実行ログ", rebuild_output, height=280)
            else:
                st.warning("update_catalog.py が見つからないため再構築をスキップしました。")


if __name__ == "__main__":
    app()
