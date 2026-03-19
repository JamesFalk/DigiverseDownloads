# Digiverse Downloads - GitHub Pages

## Deploy Steps
1. Create a new GitHub repo (e.g. `digiversedownloads`)
2. Upload all files maintaining the folder structure
3. Go to repo Settings → Pages → Source: main branch / root
4. Your site will be live at `https://yourusername.github.io/digiversedownloads/`

## Missing Assets (add these to complete the site)
- `_nav_icons_/ContactMe.jpg` — contact button icon (not in backup)
- `slideshow/` folder — slideshow subpage
- `digitube/` folder — DigiTube subpage
- `PicRoll/` folder — images for GridEx slideshow widget
  - After adding images, update the `imageArray` in GridEx.html

## Changes Made from Bluehost Version
- All `https://digiversedownloads.com/` internal links → relative paths
- `blog_SWIRLstars.gif` → `.webp` (matches uploaded file)
- `index_DigiverseDownloads.gif` → `.webp` (matches uploaded file)
- `/_nav_icons_/` absolute paths → relative `_nav_icons_/`
- `getimages.php` removed — replaced with JS imageArray in GridEx.html
- Removed https-redirect scripts (GitHub Pages is always https)
