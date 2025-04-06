import webbrowser

def generate_dork(choice, query):
    base_url = "https://www.google.com/search?q="
    
    if choice == "1":  # Email search
        dork = f'site:pastebin.com OR site:github.com OR site:linkedin.com OR site:facebook.com OR site:twitter.com OR site:instagram.com OR site:tiktok.com OR site:telegram.org OR site:google.com OR site:reddit.com OR site:steamcommunity.com "{query}"'
    elif choice == "2":  # Phone number search
        dork = f'site:facebook.com OR site:twitter.com OR site:linkedin.com OR site:instagram.com OR site:tiktok.com OR site:telegram.org OR site:viber.com OR site:whatsapp.com OR site:reddit.com "{query}"'
    elif choice == "3":  # Full name search (Greeklish & Greek)
        dork = f'site:peoplefinder.com OR site:peekyou.com OR site:linkedin.com OR site:facebook.com OR site:twitter.com OR site:instagram.com OR site:tiktok.com OR site:telegram.org OR site:reddit.com OR site:steamcommunity.com "{query}" OR "{query.replace(" ", "")}" OR "{query.replace(" ", "_")}"'
    else:
        print("Μη έγκυρη επιλογή!")
        return
    
    search_url = base_url + dork.replace(" ", "+")
    print("Άνοιγμα Google αναζήτησης...")
    webbrowser.open(search_url)

def main():
    print("Επιλέξτε αναζήτηση:")
    print("1 - Αναζήτηση με Email")
    print("2 - Αναζήτηση με Τηλέφωνο (+30)")
    print("3 - Αναζήτηση με Ονοματεπώνυμο (Greeklish & Ελληνικά)")
    
    choice = input("Δώστε επιλογή (1/2/3): ")
    query = input("Εισάγετε την αναζήτηση: ")
    
    generate_dork(choice, query)

if __name__ == "__main__":
    main()
