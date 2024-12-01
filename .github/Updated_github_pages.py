import os
import subprocess

# إعدادات المستودع
repo_url = 'https://github.com/your-username/your-repo.git'  # استبدل بهذا برابط مستودعك
local_repo_dir = '/path/to/your/local/repo'  # استبدل بالمسار المحلي للمستودع

# دالة لتحديث Pages
def update_github_pages():
    if not os.path.exists(local_repo_dir):
        print(f"Cloning repository from {repo_url}...")
        subprocess.run(['git', 'clone', repo_url, local_repo_dir], check=True)
    
    print(f"Navigating to {local_repo_dir}...")
    os.chdir(local_repo_dir)

    print("Pulling latest changes...")
    subprocess.run(['git', 'pull'], check=True)

    # يمكنك إضافة أي أوامر أخرى هنا (مثل بناء المشروع إذا كان مطلوبًا)

    print("Pushing changes to GitHub...")
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Update GitHub Pages'], check=True)
    subprocess.run(['git', 'push'], check=True)

if __name__ == "__main__":
    update_github_pages()
