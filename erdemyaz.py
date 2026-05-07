import os
import subprocess
from datetime import datetime, timedelta

# 2026 Ocak ayının 1'inden 28'ine kadar her güne 3 commit atar.
# Bu takvimde düz, kalın ve temiz bir yeşil blok oluşturur.
def commit_simple(day):
    date = f"2026-01-{day:02d} 12:00:00"
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_DATE"] = date
    # Her güne 3 commit (koyu yeşil olması için)
    for _ in range(3):
        subprocess.run(['git', 'commit', '--allow-empty', '-m', 'update', '--date', date], env=env, shell=True)

print("Sistem blokları işleniyor...")
for d in range(1, 29):
    commit_simple(d)

print("Bitti! Şimdi README ile birlikte gönderiyoruz.")