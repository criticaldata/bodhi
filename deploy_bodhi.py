"""
BODHI GitHub Pages Deployment Script
Upload the 4 files (index.html, styles.css, script.js, README.md) to Colab first,
then run this script
"""

from google.colab import userdata, files
import os
import shutil

print("="*60)
print("BODHI GitHub Pages Deployment")
print("="*60)

# Step 1: Upload files
print("\nStep 1: Upload your website files")
print("Please upload: index.html, styles.css, script.js, README.md")
print("Click the upload button below...\n")

uploaded = files.upload()

if len(uploaded) < 4:
    print(f"\n⚠ Warning: Only {len(uploaded)} files uploaded. Expected 4 files.")
    print("Continuing anyway...")

print(f"\n✓ {len(uploaded)} files uploaded")

# Step 2: Get Git token
try:
    git_token = userdata.get('Git')
    print("✓ Git token loaded")
except Exception as e:
    print(f"✗ Error loading Git token: {e}")
    exit(1)

# Step 3: Configure Git
os.system('git config --global user.name "maximinl"')
os.system('git config --global user.email "maximinl@users.noreply.github.com"')
print("✓ Git configured")

# Step 4: Clean up and clone
if os.path.exists('/content/bodhi_deploy'):
    shutil.rmtree('/content/bodhi_deploy')

print("\nCloning repository...")
clone_result = os.system(f'git clone https://{git_token}@github.com/criticaldata/bodhi.github.io.git /content/bodhi_deploy 2>&1')

if clone_result != 0:
    print("✗ Failed to clone repository")
    exit(1)

print("✓ Repository cloned")

# Step 5: Copy uploaded files to repo
os.chdir('/content/bodhi_deploy')

for filename in uploaded.keys():
    shutil.copy(f'/content/{filename}', filename)
    print(f"✓ Copied {filename}")

# Step 6: Show files
print("\nFiles in repository:")
os.system('ls -lh *.html *.css *.js *.md 2>/dev/null')

# Step 7: Commit and push
print("\nStaging files...")
os.system('git add .')

print("\nCommitting...")
os.system('git commit -m "Deploy BODHI Framework website"')

print("\nPushing to GitHub...")
push_result = os.system('git push origin main')

if push_result == 0:
    print("\n" + "="*60)
    print("✓ SUCCESS! Site deployed to GitHub")
    print("="*60)
    print("\nYour site: https://criticaldata.github.io/bodhi.github.io/")
    print("\nEnable GitHub Pages:")
    print("https://github.com/criticaldata/bodhi.github.io/settings/pages")
    print("Select 'main' branch and Save")
else:
    print("\n✗ Push failed")
