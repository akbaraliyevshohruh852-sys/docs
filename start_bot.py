import subprocess
import os
import sys

def find_main_py(start_path):
    for root, dirs, files in os.walk(start_path):
        if 'main.py' in files and 'bot' in root:
            return os.path.join(root, 'main.py')
    return None

if __name__ == "__main__":
    current_dir = os.getcwd()
    main_path = find_main_py(current_dir)
    
    if main_path:
        # main.py turgan papkani PYTHONPATH ga qo'shamiz
        project_root = os.path.dirname(os.path.dirname(main_path))
        env = os.environ.copy()
        env['PYTHONPATH'] = project_root
        
        print(f"Fayl topildi: {main_path}")
        print(f"Ishga tushirilmoqda...")
        subprocess.run([sys.executable, main_path], env=env)
    else:
        print("XATO: main.py fayli topilmadi!")
        # Papka ichidagilarni ko'rsatish (diagnostika uchun)
        for root, dirs, files in os.walk(current_dir):
            print(f"Papkada: {root} -> {files}")
