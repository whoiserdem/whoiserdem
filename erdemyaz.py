import os
import subprocess
from datetime import datetime, timedelta

# GitHub Grid (0=Pazar, 6=Cumartesi)
# (Satır, Hafta_Geriye)
points = [
    # E
    (1,12), (2,12), (3,12), (4,12), (5,12), (1,11), (1,10), (3,11), (3,10), (5,11), (5,10),
    # R
    (1,8), (2,8), (3,8), (4,8), (5,8), (1,7), (1,6), (2,6), (3,7), (4,6), (5,6),
    # D
    (1,4), (2,4), (3,4), (4,4), (5,4), (1,3), (1,2), (5,3), (5,2),
    # E
    (1,0), (2,0), (3,0), (4,0), (5,0), (1,-1), (1,-2), (3,-1), (3,-2), (5,-1), (5,-2),
    # M
    (1,-4), (2,-4), (3,-4), (4,-4), (5,-4), (2,-5), (3,-6), (2,-7), (1,-8), (2,-8), (3,-8), (4,-8), (5,-8)
]

def commit_on_date(days_back):
    date = (datetime.now() - timedelta(days=days_back)).isoformat()
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_DATE"] = date
    subprocess.run(['git', 'commit', '--allow-empty', '-m', 'art', '--date', date], env=env, shell=True)

print("Yazı enjekte ediliyor...")
today_idx = (datetime.now().weekday() + 1) % 7

for row, week in points:
    days_back = ((week + 10) * 7) + (today_idx - row)
    if days_back > 0:
        commit_on_date(days_back)