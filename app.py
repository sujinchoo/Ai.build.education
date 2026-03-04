from __future__ import annotations

from pathlib import Path
from subprocess import run

from flask import Flask, render_template, send_from_directory

ROOT = Path(__file__).parent
app = Flask(__name__, template_folder=".")


def ensure_built_assets() -> None:
    manifest = ROOT / "built" / "manifest.json"
    if manifest.exists():
        return
    run(["python", "build_curriculum.py"], cwd=ROOT, check=True)


@app.route("/")
def index() -> str:
    ensure_built_assets()
    return render_template("index.html")


@app.route("/built/<path:filename>")
def built_assets(filename: str):
    ensure_built_assets()
    return send_from_directory(ROOT / "built", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
