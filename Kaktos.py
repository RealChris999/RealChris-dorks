import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time
import random

# Initialize colorama
init(autoreset=True)

# User agents for requests
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

def get_random_agent():
    return random.choice(USER_AGENTS)

def check_platform(url_pattern, username, platform_name):
    headers = {'User-Agent': get_random_agent()}
    url = url_pattern.format(username=username)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Common checks for 404 pages
            if any(term in response.text.lower() for term in ['not found', '404', 'does not exist', 'error']):
                return False
            return True
        elif response.status_code == 404:
            return False
        else:
            return None  # Unknown status
    
    except Exception as e:
        print(f"{Fore.YELLOW}[!] Error checking {platform_name}: {e}{Style.RESET_ALL}")
        return None

def validate_email(email):
    # Simple email validation
    return '@' in email and '.' in email.split('@')[-1]

def validate_phone(phone):
    # Greek phone validation
    phone = phone.strip().replace('+30', '').replace('0030', '')
    return phone.isdigit() and len(phone) == 10 and phone.startswith(('69', '2', '21', '22', '23', '24', '25', '26', '27', '28', '29'))

PLATFORMS = {
    "Facebook": "https://www.facebook.com/{username}",
    "Instagram": "https://www.instagram.com/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Telegram": "https://t.me/{username}",
    "Twitter": "https://twitter.com/{username}",
    "GitHub": "https://github.com/{username}",
    "Pastebin": "https://pastebin.com/u/{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "YouTube": "https://www.youtube.com/@{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
    "Steam": "https://steamcommunity.com/id/{username}",
    "Spotify": "https://open.spotify.com/user/{username}",
    "Viber": "https://chats.viber.com/{username}",
    "Skype": "https://join.skype.com/{username}",
    "WhatsApp": "https://wa.me/30{username}",  # For phone numbers
    "Replit": "https://replit.com/@{username}",
    "PeekYou": "https://www.peekyou.com/{username}",
    "PeopleFinder": "https://www.peoplefinder.com/{username}",
    "Disney+": "https://www.disneyplus.com/profiles/{username}",
    "Netflix": "https://www.netflix.com/profiles/{username}",
    "PlayStation": "https://my.playstation.com/profile/{username}",
    "Xbox": "https://account.xbox.com/profile?gamertag={username}",
    "Brave Community": "https://community.brave.com/u/{username}",
    "DuckDuckGo": "https://duckduckgo.com/?q={username}&ia=web",
    "Tor Project": "https://metrics.torproject.org/user/{username}",
    "Zedge": "https://www.zedge.net/profile/{username}",
    "Temu": "https://www.temu.com/user/{username}"
}

def check_all_platforms(username, is_email=False, is_phone=False):
    results = {}
    
    for platform, url_pattern in PLATFORMS.items():
        if is_phone and platform == "WhatsApp":
            # Special handling for WhatsApp with phone numbers
            formatted_username = username.replace('+30', '').replace('0030', '')
            url = PLATFORMS[platform].format(username=formatted_username)
        else:
            url = url_pattern.format(username=username)
        
        result = check_platform(url_pattern, username, platform)
        results[platform] = result
        
        # Print result with colors
        if result is True:
            print(f"{Fore.GREEN}[+] {platform}: Valid{Style.RESET_ALL}")
        elif result is False:
            print(f"{Fore.RED}[-] {platform}: Invalid{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[?] {platform}: Unknown{Style.RESET_ALL}")
        
        # Add delay to avoid rate limiting
        time.sleep(1)
    
    return results

def main():
    print(f"""{Fore.CYAN}
   ____ _   _ ____  _____ ___ _   _ ____  _____ ____  
  / ___| | | |  _ \| ____|_ _| \ | |  _ \| ____|  _ \ 
 | |  _| | | | |_) |  _|  | ||  \| | | | |  _| | |_) |
 | |_| | |_| |  _ <| |___ | || |\  | |_| | |___|  _ < 
  \____|\___/|_| \_\_____|___|_| \_|____/|_____|_| \_\
    {Style.RESET_ALL}""")
    print(f"{Fore.MAGENTA}Platform Checker v2.0 - Auto Validator{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}=========================================={Style.RESET_ALL}")
    
    print("\n1. Check by Username/Email")
    print("2. Check by Phone Number (+30)")
    choice = input("\nSelect an option (1-2): ")
    
    if choice == "1":
        username = input("Enter username or email: ").strip()
        if '@' in username:
            if not validate_email(username):
                print(f"{Fore.RED}Invalid email format!{Style.RESET_ALL}")
                return
            print(f"\n{Fore.BLUE}Checking email across platforms...{Style.RESET_ALL}")
            check_all_platforms(username, is_email=True)
        else:
            print(f"\n{Fore.BLUE}Checking username across platforms...{Style.RESET_ALL}")
            check_all_platforms(username)
    
    elif choice == "2":
        phone = input("Enter phone number (with +30 or 0030): ").strip()
        if not validate_phone(phone):
            print(f"{Fore.RED}Invalid Greek phone number!{Style.RESET_ALL}")
            return
        print(f"\n{Fore.BLUE}Checking phone number across platforms...{Style.RESET_ALL}")
        check_all_platforms(phone, is_phone=True)
    
    else:
        print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
