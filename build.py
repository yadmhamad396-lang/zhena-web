"""
Build the static website from data and templates.
Output goes to docs/ for GitHub Pages.
Run: python build.py
"""
import json
import re
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE / "data"
TEMPLATES_DIR = BASE / "templates"
OUTPUT_DIR = BASE / "docs"


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_doctor():
    return load_yaml(DATA_DIR / "doctor.yaml")


def load_categories():
    return load_yaml(DATA_DIR / "categories.yaml")


def load_products():
    return load_yaml(DATA_DIR / "products.yaml")


def phone_digits(phone: str) -> str:
    """WhatsApp wa.me needs digits only (country code, no + or spaces)."""
    return re.sub(r"\D", "", phone or "")


def build():
    doctor = load_doctor()
    categories = load_categories()
    products = load_products()

    doctor_phone = phone_digits(doctor.get("phone", ""))
    doctor["phone_digits"] = doctor_phone

    # JSON for client-side (categories, products)
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("index.html")
    html = template.render(
        doctor=doctor,
        categories=categories,
        products=products,
        categories_json=json.dumps(categories),
        products_json=json.dumps(products),
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")

    # Copy static assets if we have any
    static_src = BASE / "static"
    static_dst = OUTPUT_DIR / "static"
    if static_src.exists():
        import shutil
        if static_dst.exists():
            shutil.rmtree(static_dst)
        shutil.copytree(static_src, static_dst)

    print("Built static site in docs/")


if __name__ == "__main__":
    build()
