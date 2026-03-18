import os
import zipfile
import subprocess
import sys

def run_bot():
    current_dir = os.getcwd()
    zip_name = 'jonlitaxi_deploy.zip'

    # ZIP-ni ochish
    if os.path.exists(zip_name):
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(current_dir)
        print("--- Fayllar chiqarildi! ---")

    # PYTHONPATH sozlash (xuddi .bat dagi kabi)
    env = os.environ.copy()
    env['PYTHONPATH'] = current_dir

    # Botni ishga tushirish
    bot_path = os.path.join(current_dir, 'bot', 'main.py')

    if os.path.exists(bot_path):
        print(f"Botingiz ishga tushmoqda...")
        subprocess.run([sys.executable, bot_path], env=env)
    else:
        print(f"XATO: {bot_path} topilmadi!")

if __name__ == "__main__":
    run_bot()
