import os
import subprocess

# الدليل الذي يحتوي على المستودعات
repos_dir = '/path/to/your/repos'  # استبدل هذا بالمسار الصحيح

# الدالة لتنسيق الكود
def format_code(repo_path):
    try:
        # تنسيق الكود باستخدام Prettier لـ JavaScript
        subprocess.run(['npx', 'prettier', '--write', '.'], cwd=repo_path, check=True)
        print(f"Formatted code in {repo_path}")
    except Exception as e:
        print(f"Error formatting code in {repo_path}: {e}")

# الدالة لتحديث المستودع
def update_repo(repo_path):
    try:
        subprocess.run(['git', 'pull'], cwd=repo_path, check=True)
        print(f"Updated repository {repo_path}")
    except Exception as e:
        print(f"Error updating repository {repo_path}: {e}")

# تنقل إلى كل مستودع
def process_repositories():
    for repo in os.listdir(repos_dir):
        repo_path = os.path.join(repos_dir, repo)
        
        if os.path.isdir(repo_path):
            format_code(repo_path)  # تنسيق الكود
            update_repo(repo_path)   # تحديث المستودع

if __name__ == "__main__":
    process_repositories()
