import argparse
from recon.username import username_recon
from recon.email import email_recon
from utils.validators import validate_email, validate_username
from ai_core.analyzer import analyze_recon

def main():
    parser = argparse.ArgumentParser(description="🛰️ AI OSINT Crawler - Phase 1")
    parser.add_argument('--username', type=str, help='Username to search for')
    parser.add_argument('--email', type=str, help='Email to search for')
    args = parser.parse_args()

    # Initialize results container
    recon_results = []

    if args.username:
        if validate_username(args.username):
            print(f"\n[+] Starting recon for username: {args.username}")
            username_recon_results = username_recon(args.username)
            if username_recon_results:
                recon_results.extend(username_recon_results)
        else:
            print("[!] Invalid username format.")

    if args.email:
        if validate_email(args.email):
            print(f"\n[+] Starting recon for email: {args.email}")
            email_recon_results = email_recon(args.email)
            if email_recon_results:
                recon_results.extend(email_recon_results)
        else:
            print("[!] Invalid email format.")

    # If we have results, analyze them
    if recon_results:
        print("\n[+] Analyzing results with AI...")
        analysis = analyze_recon("username" if args.username else "email", args.username or args.email, recon_results)
        print("\n===== AI ANALYSIS =====")
        print(analysis)
    else:
        print("[!] No valid results found for analysis.")

if __name__ == "__main__":
    main()
