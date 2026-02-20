import requests

def get_stats():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    stats = {"tiktok": "0", "insta": "0", "fb": "0"}
    
    # TikTok
    try:
        r = requests.get("https://livesubs.io/api/tiktok/luciferm0rn1ngstar", headers=headers, timeout=15)
        stats["tiktok"] = str(r.json().get("followers", 0))
    except Exception as e:
        print(f"TikTok Fail: {e}")

    # Instagram
    try:
        r = requests.post("https://blastup.com/api/instagram/follower-count", 
                          json={"username": "s666luc"}, headers=headers, timeout=15)
        stats["insta"] = str(r.json().get("count", 0))
    except Exception as e:
        print(f"Insta Fail: {e}")

    # Facebook
    try:
        r = requests.get("https://api.livecounts.nl/facebook-live-follower-count/search/Lucifer.irl", headers=headers, timeout=15)
        stats["fb"] = str(r.json().get("followerCount", 0))
    except Exception as e:
        print(f"FB Fail: {e}")

    return stats

# Generate the HTML
data = get_stats()
html_template = f"""<!DOCTYPE html><html><body>
<div id="tiktok">{data['tiktok']}</div>
<div id="insta">{data['insta']}</div>
<div id="fb">{data['fb']}</div>
</body></html>"""

with open("index.html", "w") as f:
    f.write(html_template)
print("Done!")
