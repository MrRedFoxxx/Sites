import multiprocessing
import subprocess
import os
import time

def run_artel_prod():
    """Запуск сайта Artel-Prod"""
    os.chdir("Artel-Prod")
    subprocess.run(["python3", "api/main.py"])

def run_rank_ai():
    """Запуск сайта Rank-AI"""
    os.chdir("Rank_AI")
    subprocess.run(["python3", "main.py"])

if __name__ == '__main__':
    # Создаем процессы для каждого приложения
    p1 = multiprocessing.Process(target=run_artel_prod)
    p2 = multiprocessing.Process(target=run_rank_ai)

    # Запускаем процессы
    p1.start()
    p2.start()
    
    print("Оба сайта запущены:")
    print(f"- Artel-Prod работает на порту 8000")
    print(f"- Rank-AI работает на порту 8001")
    print("Для остановки нажмите Ctrl+C")
    
    try:
        # Бесконечный цикл для поддержания работы скрипта
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nОстановка сайтов...")
        p1.terminate()
        p2.terminate()
        p1.join()
        p2.join()
        print("Сайты остановлены")