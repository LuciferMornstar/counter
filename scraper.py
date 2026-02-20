import requests
import re
import os

def get_stats():
    stats = {"tiktok": "0", "insta": "0", "fb": "0"}
    
    # 1. TikTok (Livesubs)
    try:
        r = requests.get("https://livesubs.io/api/tiktok/luciferm0rn1ngstar", timeout=10)
        stats["tiktok"] = str(r.json().get("followers", 0))
    except: pass

    # 2. Instagram (Blastup)
    try:
        r = requests.post("https://blastup.com/api/instagram/follower-count", 
                          json={"username": "s666luc"}, timeout=10)
        stats["insta"] = str(r.json().get("count", 0))
    except: pass

    # 3. Facebook (Livecounts)
    try:
        r = requests.get("https://api.livecounts.nl/facebook-live-follower-count/search/Lucifer.irl", timeout=10)
        stats["fb"] = str(r.json().get("followerCount", 0))
    except: pass

    return stats

def update_html(stats):
    with open("index.html", "w") as f:
        f.write(f"""<!DOCTYPE html>
<html>
<body>
  <div id="tiktok">{stats['tiktok']}</div>
  <div id="insta">{stats['insta']}</div>
  <div id="fb">{stats['fb']}</div>
</body>
</html>""")

if __name__ == "__main__":
    data = get_stats()
    update_html(data)
    print(f"Updated with: {data}")