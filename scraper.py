import requests

def get_stats():
    # These headers make us look like a real browser visiting their dashboard
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://socialcounts.org/',
        'Origin': 'https://socialcounts.org'
    }
    
    stats = {"tiktok": "0", "insta": "0", "fb": "0"}
    
    # 1. TikTok (via SocialCounts API)
    try:
        r = requests.get("https://api.socialcounts.org/live/tiktok/luciferm0rn1ngstar", headers=headers, timeout=10)
        stats["tiktok"] = str(r.json().get("followers", 0))
    except Exception as e:
        print(f"TikTok Fail: {e}")

    # 2. Instagram (via SocialCounts API)
    try:
        r = requests.get("https://api.socialcounts.org/live/instagram/s666luc", headers=headers, timeout=10)
        stats["insta"] = str(r.json().get("followers", 0))
    except Exception as e:
        print(f"Insta Fail: {e}")

    # 3. Facebook (via SocialCounts API)
    try:
        r = requests.get("https://api.socialcounts.org/live/facebook/Lucifer.irl", headers=headers, timeout=10)
        stats["fb"] = str(r.json().get("followers", 0))
    except Exception as e:
        print(f"FB Fail: {e}")

    return stats

# Generate the HTML bridge
data = get_stats()
html_content = f"""<!DOCTYPE html><html><body>
<div id="tiktok">{data['tiktok']}</div>
<div id="insta">{data['insta']}</div>
<div id="fb">{data['fb']}</div>
</body></html>"""

with open("index.html", "w") as f:
    f.write(html_content)

print(f"SCRAPER RESULT: {data}")
