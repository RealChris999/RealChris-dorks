import webbrowser
import urllib.parse

def email_search(email):
    dorks = [
        f"site:facebook.com intext:{email}",
        f"site:instagram.com intext:{email}",
        f"site:twitter.com intext:{email}",
        f"site:linkedin.com intext:{email}",
        f"site:tiktok.com intext:{email}",
        f"intext:{email}",
        f"filetype:pdf {email}",
        f"inurl:{email.split('@')[1]} intext:{email.split('@')[0]}"
    ]
    return dorks

def phone_search(phone):
    # Remove country code if present
    if phone.startswith('+30'):
        phone = phone[3:]
    elif phone.startswith('0030'):
        phone = phone[4:]
    
    dorks = [
        f"site:facebook.com intext:{phone}",
        f"site:instagram.com intext:{phone}",
        f"site:viber.com intext:{phone}",
        f"site:whatsapp.com intext:{phone}",
        f"site:skype.com intext:{phone}",
        f"intext:{phone}",
        f"filetype:pdf {phone}",
        f"intext:{phone} (694|695|696|697|698|699)",
        f"intext:{phone} site:gr"
    ]
    return dorks

def name_search(name):
    # Greek to Greeklish conversion (basic)
    greeklish = name.lower()
    greeklish = greeklish.replace('α', 'a').replace('β', 'v').replace('γ', 'g')
    greeklish = greeklish.replace('δ', 'd').replace('ε', 'e').replace('ζ', 'z')
    greeklish = greeklish.replace('η', 'i').replace('θ', 'th').replace('ι', 'i')
    greeklish = greeklish.replace('κ', 'k').replace('λ', 'l').replace('μ', 'm')
    greeklish = greeklish.replace('ν', 'n').replace('ξ', 'x').replace('ο', 'o')
    greeklish = greeklish.replace('π', 'p').replace('ρ', 'r').replace('σ', 's')
    greeklish = greeklish.replace('τ', 't').replace('υ', 'y').replace('φ', 'f')
    greeklish = greeklish.replace('χ', 'ch').replace('ψ', 'ps').replace('ω', 'o')
    
    dorks = [
        f'site:facebook.com "{name}"',
        f'site:instagram.com "{name}"',
        f'site:linkedin.com "{name}"',
        f'site:tiktok.com "{name}"',
        f'site:twitter.com "{name}"',
        f'"{name}" site:gr',
        f'"{name}" filetype:pdf',
        f'"{name}" intitle:"about"',
        f'"{greeklish}"',
        f'"{name}" AND ("profile" OR "about" OR "contact")'
    ]
    return dorks

def search_google(dorks):
    for dork in dorks:
        query = urllib.parse.quote_plus(dork)
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new_tab(url)

def main():
    print("""
  ____ ____  ____  _  ___ _ ____ _____ 
 / ___/ ___||  _ \| |/ / | / ___| ____|
| |  _\___ \| | | | ' /| | \___ \  _|  
| |_| |___) | |_| | . \| |___|_) | |___ 
 \____|____/|____/|_|\_\_____|____/_____|
    """)
    print("Google Dork Generator - Greek Edition")
    print("------------------------------------")
    print("(1) Search By Email")
    print("(2) Search Phone Number (+30)")
    print("(3) Search Full name (Greeklish & Ελληνικά)")
    print("------------------------------------")
    
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        email = input("Enter email address: ").strip()
        if "@" not in email:
            print("Invalid email address")
            return
        dorks = email_search(email)
    elif choice == "2":
        phone = input("Enter phone number (with or without +30): ").strip()
        if not phone.isdigit() and not phone.startswith(('+30', '0030')):
            print("Invalid phone number format")
            return
        dorks = phone_search(phone)
    elif choice == "3":
        name = input("Enter full name: ").strip()
        if not name:
            print("Name cannot be empty")
            return
        dorks = name_search(name)
    else:
        print("Invalid choice")
        return
    
    print("\nGenerated Google Dorks:")
    for i, dork in enumerate(dorks, 1):
        print(f"{i}. {dork}")
    
    print("\nOpening search results in browser...")
    search_google(dorks)

if __name__ == "__main__":
    main()
