import os
import zipfile
import subprocess
import sys
import time

def unzip_project():
    zip_name = 'jonlitaxi_deploy.zip'
    if os.path.exists(zip_name):
        print(f"--- {zip_name} ochilmoqda... ---")
        try:
            with zipfile.ZipFile(zip_name, 'r') as zip_ref:
                zip_ref.extractall('.')
            print("--- Fayllar chiqarildi! ---")
            return True
        except Exception as e:
            print(f"--- ZIP ochishda xato: {e} ---")
            return False
    else:
        print(f"--- XATO: {zip_name} topilmadi! ---")
        return False

if __name__ == "__main__":
    # 1. ZIP-ni ochish
    if unzip_project():
        # 2. PYTHONPATH sozlash (loyihani ko'rishi uchun)
        current_dir = os.getcwd()
        env = os.environ.copy()
        env['PYTHONPATH'] = current_dir
        
        # 3. main.py manzilini aniqlash
        # Eslatma: ZIP ichida 'bot' papkasi va uning ichida 'main.py' bor deb hisoblaymiz
        main_path = os.path.join(current_dir, 'bot', 'main.py')
        
        if os.path.exists(main_path):
            print(f"--- Bot ishga tushmoqda: {main_path} ---")
            # subprocess.run o'rniga Popen ishlatamiz (Render port kutib qolmasligi uchun)
            subprocess.run([sys.executable, main_path], env=env)
        else:
            print(f"--- XATO: {main_path} topilmadi! ZIP ichini tekshiring. ---")
            print(f"Papkadagi fayllar: {os.listdir(current_dir)}")
    
    # Render o'chirib yubormasligi uchun vaqtinchalik kutish
    time.sleep(10)
