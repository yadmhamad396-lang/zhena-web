# Doctor Products – Static Site

A **static** website with three parts: **About the Doctor**, **Product categories**, and **Products**. When someone wants to buy, they click "Order via WhatsApp" and the product details are sent to the doctor's WhatsApp—no server or paid hosting needed. Ideal for **GitHub Pages**.

## Why static?

- **GitHub Pages** only hosts static files (HTML, CSS, JS). No backend = no server costs.
- "Buy" is handled by a **WhatsApp link** (`wa.me`) with a pre-filled message containing the product info. No database or server required.

## Setup

### 1. Python environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (CMD):
.\venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Edit your content

- **`data/doctor.yaml`** – Name, title, bio, **WhatsApp phone** (with country code, no + or spaces), email.
- **`data/categories.yaml`** – Product categories (id, name, description).
- **`data/products.yaml`** – Products (id, name, category id, price, description).

### 3. Build the site

```bash
python build.py
```

This generates the static site in the **`docs/`** folder.

### 4. GitHub Pages

1. Push the repo to GitHub.
2. In the repo: **Settings → Pages**.
3. Under "Build and deployment", set **Source** to **Deploy from a branch**.
4. Branch: e.g. `main`, Folder: **`/docs`**.
5. Save. Your site will be at `https://<username>.github.io/<repo>/`.

## Project structure

```
├── data/
│   ├── doctor.yaml      # Doctor/person info + WhatsApp number
│   ├── categories.yaml  # Product categories
│   └── products.yaml    # Products (each has a category)
├── templates/
│   └── index.html       # Page template
├── static/
│   └── style.css        # Styles
├── docs/                # Generated output (for GitHub Pages)
├── build.py             # Build script
├── requirements.txt
└── README.md
```

## Adding products

Edit `data/products.yaml` and use an existing `category` id from `data/categories.yaml`. Then run `python build.py` again and push the updated `docs/` to GitHub.
