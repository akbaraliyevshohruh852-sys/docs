import os
import zipfile
import subprocess
import sys

def run_server():
    current_dir = os.getcwd()
    zip_name = 'jonlitaxi_deploy.zip'

    # 1. ZIP-ni ochish (Fayllarni tayyorlash)
    if os.path.exists(zip_name):
        print("--- Fayllar ZIP-dan chiqarilmoqda... ---")
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(current_dir)

    # 2. PYTHONPATH sozlash (Xuddi .bat-dagi kabi)
    env = os.environ.copy()
    env['PYTHONPATH'] = current_dir

    # 3. Botni ishga tushirish (Logingizdagi bot\main.py buyrug'i)
    bot_path = os.path.join(current_dir, 'bot', 'main.py')

    if os.path.exists(bot_path):
        print(f"--- Bot ishga tushmoqda: {bot_path} ---")
        # Loglarda ko'ringan botni yurgizish jarayoni
        subprocess.run([sys.executable, bot_path], env=env)
    else:
        print(f"XATO: {bot_path} topilmadi!")
        print(f"Mavjud fayllar: {os.listdir(current_dir)}")

if __name__ == "__main__":
    run_server()
