# Host on GitHub Pages

Follow these steps to put your site live.

## 1. Build the site (if you changed data or code)

```powershell
cd "c:\Users\Yad\Desktop\zhena web"
.\venv\Scripts\Activate.ps1
python build.py
```

## 2. Create a new repository on GitHub

1. Go to [github.com](https://github.com) and sign in.
2. Click **"+"** → **"New repository"**.
3. Name it (e.g. `zhena-web` or `doctor-products`).
4. Choose **Public**, leave "Add a README" **unchecked**.
5. Click **"Create repository"**.

## 3. Push your project to GitHub

In PowerShell, from your project folder:

```powershell
cd "c:\Users\Yad\Desktop\zhena web"

# If you haven't committed yet:
git add .
git commit -m "Initial commit - static site for GitHub Pages"

# Replace YOUR_USERNAME and YOUR_REPO with your GitHub username and repo name:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

## 4. Turn on GitHub Pages

1. Open your repo on GitHub.
2. Go to **Settings** → **Pages** (left sidebar).
3. Under **"Build and deployment"**:
   - **Source:** Deploy from a branch
   - **Branch:** `main` (or `master`)
   - **Folder:** `/docs`
4. Click **Save**.

After a minute or two, your site will be at:

**https://YOUR_USERNAME.github.io/YOUR_REPO/**

## Updating the site later

1. Edit files in `data/`, `templates/`, or `static/`.
2. Run `python build.py`.
3. Commit and push:

   ```powershell
   git add .
   git commit -m "Update products"
   git push
   ```

GitHub Pages will automatically serve the updated `docs/` folder.
