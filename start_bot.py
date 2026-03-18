import os
import zipfile
import subprocess
import sys

def run_server_bot():
    zip_name = 'jonlitaxi_deploy.zip'
    current_dir = os.getcwd()

    # 1. ZIP-ni ochish (Windows-dagi fayllarni tayyorlash)
    if os.path.exists(zip_name):
        print(f"--- {zip_name} ochilmoqda... ---")
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(current_dir)
        print("--- Fayllar chiqarildi! ---")
    else:
        print(f"--- XATO: {zip_name} topilmadi! ---")
        # Agar ZIP bo'lmasa, papkani o'zini tekshiramiz
        print(f"Hozirgi papkadagi fayllar: {os.listdir(current_dir)}")

    # 2. PYTHONPATH sozlash (Xuddi .bat ichidagi 'set PYTHONPATH' kabi)
    env = os.environ.copy()
    env['PYTHONPATH'] = current_dir

    # 3. Botni ishga tushirish (Xuddi .bat ichidagi 'python bot\\main.py' kabi)
    # Linux-da slash / ko'rinishida bo'ladi
    bot_path = os.path.join(current_dir, 'bot', 'main.py')

    if os.path.exists(bot_path):
        print(f"--- Bot topildi: {bot_path} ---")
        print("--- Ishga tushirilmoqda... ---")
        # subprocess.run bot o'chmaguncha kodni ushlab turadi
        subprocess.run([sys.executable, bot_path], env=env)
    else:
        print(f"--- XATO: {bot_path} topilmadi! ---")
        # Diagnostika uchun ichki papkalarni ko'ramiz
        if os.path.exists('bot'):
            print(f"'bot' papkasi ichidagilar: {os.listdir('bot')}")

if __name__ == "__main__":
    run_server_bot()
