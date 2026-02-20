import requests
import json

def get_stats():
    # We use a real browser "User-Agent" to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    stats = {"tiktok": "0", "insta": "0", "fb": "0"}
    
    # 1. TikTok (Livesubs)
    try:
        r = requests.get("https://livesubs.io/api/tiktok/luciferm0rn1ngstar", headers=headers, timeout=10)
        stats["tiktok"] = str(r.json().get("followers", 0))
    except Exception as e:
        print(f"TikTok Error: {e}")

    # 2. Instagram (Blastup)
    try:
        r = requests.post("https://blastup.com/api/instagram/follower-count", 
                          json={"username": "s666luc"}, headers=headers, timeout=10)
        stats["insta"] = str(r.json().get("count", 0))
    except Exception as e:
        print(f"Insta Error: {e}")

    # 3. Facebook (Livecounts)
    try:
        # Note: Livecounts often requires a specific search first, but this API is usually open
        r = requests.get("https://api.livecounts.nl/facebook-live-follower-count/search/Lucifer.irl", headers=headers, timeout=10)
        stats["fb"] = str(r.json().get("followerCount", r.json().get("count", 0)))
    except Exception as e:
        print(f"FB Error: {e}")

    return stats

def update_html(stats):
    # This format is easy for Google Script to RegEx
    html_content = f"""<!DOCTYPE html>
<html>
<head><title>Social Stats Bridge</title></head>
<body>
  <div id="tiktok">{stats['tiktok']}</div>
  <div id="insta">{stats['insta']}</div>
  <div id="fb">{stats['fb']}</div>
</body>
</html>"""
    
    with open("index.html", "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    data = get_stats()
    update_html(data)
    print(f"Successfully updated index.html with: {data}")
