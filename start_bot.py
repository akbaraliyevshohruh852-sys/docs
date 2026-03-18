import subprocess
import os
import sys

# Hozirgi papka manzilini avtomatik aniqlash (Linux uchun moslashadi)
current_dir = os.path.dirname(os.path.abspath(__file__))
env = os.environ.copy()

# PYTHONPATH ga asosiy papkani qo'shish (core papkasini topishi uchun)
env['PYTHONPATH'] = current_dir

# Botni yurgizuvchi main.py manzili
main_path = os.path.join(current_dir, 'bot', 'main.py')

if __name__ == "__main__":
    print(f"Botingiz ishga tushmoqda: {main_path}")
    # Render-da 'python' o'rniga 'sys.executable' ishlatish ishonchliroq
    subprocess.run([sys.executable, main_path], env=env)
