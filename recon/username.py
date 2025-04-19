import requests

def username_recon(username, verbose=True):
    results = []

    platforms = {
        "GitHub": f"https://github.com/{username}",
        "X (Twitter)": f"https://x.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Linktree": f"https://linktr.ee/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Dev.to": f"https://dev.to/{username}",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (AI-OSINT-Crawler)"
    }

    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                msg = f"[✓] Found on {platform}: {url}"
            elif response.status_code == 302:
                msg = f"[✓] Possibly found on {platform} (Redirect): {url}"
            elif response.status_code == 404:
                msg = f"[✗] Not found on {platform}"
            else:
                msg = f"[~] Unexpected response from {platform}: HTTP {response.status_code}"
        except requests.RequestException as e:
            msg = f"[!] Error connecting to {platform}: {e}"

        results.append(msg)
        if verbose:
            print(msg)

    return results  # ← ✅ Mission-critical line
