import os
import zipfile
import subprocess
import sys

def run_bot():
    current_dir = os.getcwd()
    zip_name = 'jonlitaxi_deploy.zip'

    # 1. ZIP faylni ochish (agar u mavjud bo'lsa)
    if os.path.exists(zip_name):
        print(f"--- {zip_name} ochilmoqda... ---")
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(current_dir)
        print("--- Fayllar chiqarildi! ---")

    # 2. PYTHONPATH sozlash (Xuddi .bat faylingizdagidek)
    env = os.environ.copy()
    env['PYTHONPATH'] = current_dir

    # 3. Botni ishga tushirish (Linux formatidagi yo'l bilan)
    # Windows'dagi 'bot\main.py' Linux'da 'bot/main.py' bo'ladi
    main_path = os.path.join(current_dir, 'bot', 'main.py')

    if os.path.exists(main_path):
        print(f"Botingiz ishga tushmoqda: {main_path}")
        subprocess.run([sys.executable, main_path], env=env)
    else:
        print(f"XATO: {main_path} topilmadi!")
        print(f"Papkadagi mavjud fayllar: {os.listdir(current_dir)}")

if __name__ == "__main__":
    run_bot()
