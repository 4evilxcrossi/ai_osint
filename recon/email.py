import requests

def email_recon(email, verbose=True):
    results = []

    headers = {
        "User-Agent": "Mozilla/5.0 (AI-OSINT-Crawler)"
    }

    # Define the sources and their validation method
    sources = {
        # Email check and breach sites
        "HaveIBeenPwned": f"https://haveibeenpwned.com/unifiedsearch/{email}",
        "Hunter (Email Discovery)": f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=YOUR_HUNTER_API_KEY",
        "EmailRep": f"https://emailrep.io/{email}",
        "Gravatar": f"https://en.gravatar.com/{email}.json",
        "IntelX": f"https://intelx.io/?s={email}",
        "LeakCheck.io": f"https://leakcheck.io/search?email={email}",

        # Social media platforms
        "Facebook": f"https://www.facebook.com/{email}",
        "LinkedIn": f"https://www.linkedin.com/search/results/people/?keywords={email}",
        "Twitter (X)": f"https://twitter.com/search?q={email}",
        "Instagram": f"https://www.instagram.com/{email}",
        "Pinterest": f"https://www.pinterest.com/search/pins/?q={email}",
        "GitHub": f"https://github.com/{email}",
        "Reddit": f"https://www.reddit.com/user/{email}",
        "TikTok": f"https://www.tiktok.com/@{email}",
    }

    # Define a simple validation function to check for relevant content
    def validate_content(source, response):
        """Helper function to validate if the page content is relevant to the email search."""
        if source == "HaveIBeenPwned":
            if "pwned" in response.text:
                return True
        elif source == "Hunter (Email Discovery)":
            if "email" in response.text:  # Check for email validation data
                return True
        elif source == "EmailRep":
            if email in response.text:
                return True
        elif source == "Gravatar":
            if email in response.text:
                return True
        elif source == "IntelX":
            if email in response.text:
                return True
        elif source == "LeakCheck.io":
            if email in response.text:
                return True
        elif source == "Facebook":
            if "Profile" in response.text:  # Look for a profile-related term
                return True
        elif source == "LinkedIn":
            if "LinkedIn" in response.text:
                return True
        elif source == "Twitter (X)":
            if email in response.text:
                return True
        elif source == "Instagram":
            if email in response.text:
                return True
        elif source == "Pinterest":
            if email in response.text:
                return True
        elif source == "GitHub":
            if email in response.text:
                return True
        elif source == "Reddit":
            if email in response.text:
                return True
        elif source == "TikTok":
            if email in response.text:
                return True
        return False  # Default: return false if no content matches

    for source, url in sources.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                if validate_content(source, response):  # Check for relevant content
                    msg = f"[✓] Info found via {source}: {url}"
                else:
                    msg = f"[✗] No relevant data found on {source}"
            elif response.status_code == 403:
                msg = f"[✗] Forbidden or missing API key for {source}"
            elif response.status_code == 404:
                msg = f"[✗] No record found on {source}"
            else:
                msg = f"[~] {source} returned HTTP {response.status_code}"
        except requests.RequestException as e:
            msg = f"[!] Error connecting to {source}: {e}"

        results.append(msg)
        if verbose:
            print(msg)

    return results  # ← ✅ This line is now crucial to return the collected results
