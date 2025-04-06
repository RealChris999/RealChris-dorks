import webbrowser

def generate_dork(choice, query):
    base_url = "https://www.google.com/search?q="
    
    # Αναζήτηση για email
    if choice == "1":  
        dork = f'site:pastebin.com OR site:github.com OR site:linkedin.com OR site:facebook.com OR site:twitter.com OR site:instagram.com OR site:tiktok.com OR site:telegram.org OR site:reddit.com OR site:steamcommunity.com OR site:viber.com OR site:whatsapp.com OR site:discord.com OR site:microsoft.com OR site:xbox.com OR site:playstation.com "{query}"'
    
    # Αναζήτηση για αριθμό τηλεφώνου
    elif choice == "2":  
        dork = f'site:facebook.com OR site:twitter.com OR site:linkedin.com OR site:instagram.com OR site:tiktok.com OR site:telegram.org OR site:viber.com OR site:whatsapp.com OR site:reddit.com OR site:discord.com OR site:microsoft.com OR site:xbox.com OR site:playstation.com "{query}"'
    
    # Αναζήτηση για ονοματεπώνυμο (Greeklish & Ελληνικά)
    elif choice == "3":  
        # Ελέγχουμε και Greeklish (όπως "papadopoulosgiwrgos") και Ελληνικά (όπως "παπαδόπουλος")
        dork = f'site:peoplefinder.com OR site:peekyou.com OR site:linkedin.com OR site:facebook.com OR site:twitter.com OR site:instagram.com OR site:tiktok.com OR site:telegram.org OR site:reddit.com OR site:steamcommunity.com OR site:discord.com OR site:microsoft.com OR site:xbox.com OR site:playstation.com "{query}" OR "{query.replace(" ", "")}" OR "{query.replace(" ", "_")}" OR "{query.replace(" ", "").lower()}"'
    
    else:
        print("Λάθος επιλογή! Παρακαλώ εισάγετε 1, 2 ή 3.")
        return
    
    search_url = base_url + dork.replace(" ", "+")
    print("Ανοίγω αναζήτηση στο Google...")
    webbrowser.open(search_url)

def main():
    print("Επιλέξτε τι θέλετε να αναζητήσετε:")
    print("1 - Search By Email")
    print("2 - Search By Phone (+30)")
    print("3 - Search By Full Name (Greeklish & Ελληνικά)")
    
    choice = input("Δώστε την επιλογή σας (1/2/3): ")
    query = input("Εισάγετε το στοιχείο για αναζήτηση: ")
    
    generate_dork(choice, query)

if __name__ == "__main__":
    main()
