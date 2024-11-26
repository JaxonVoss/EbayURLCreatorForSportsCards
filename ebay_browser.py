import webbrowser

def add_array_to_url(temp_array):
    url = ""
    for temp in temp_array:
        url += "+" + temp
    return url

def open_links(auction_or_bin, years, brands, players):
    for a_or_bin in auction_or_bin:
        for year in years:
            for brand in brands:
                for player in players:
                    brand_array = brand.split()
                    player_array = player.split()

                    # Builds the urls
                    url1 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + year
                    url1 += add_array_to_url(brand_array)
                    url1 += add_array_to_url(player_array)
                    url1 += "&_sacat=0&LH_"

                    url2 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + year
                    url2 += add_array_to_url(brand_array)
                    url2 += add_array_to_url(player_array)
                    url2 += "&_sacat=0&_sop=10&LH_Sold=1&LH_Complete=1&rt=nc&LH_All=1"
                    
                    # Checks if auction or bin
                    if a_or_bin == 'a':
                        url1 += "Auction=1&_sop=1"
                    else:
                        url1 += "BIN=1&_sop=10"

                    # Launches the web browser
                    webbrowser.open_new_tab(url1)
                    webbrowser.open_new_tab(url2)

def auction_or_bin_choice():
    auction_or_bin = []
    while True:
        a_or_bin = input("Auction, Buy It Now, or Both (a, bin, or both): ")
        if a_or_bin == "a" or a_or_bin == "bin" or a_or_bin == "both":
            if a_or_bin == "both":
                auction_or_bin.append("a")
                auction_or_bin.append("bin")
            else:
                auction_or_bin.append(a_or_bin)
            return auction_or_bin
        print("Try again!")

def years_choice():
    years = []
    number_of_years = 0
    
    while True:
        number_of_years = input("How many years: ")
        if number_of_years.isdigit():
            break
        print("Try again!")
    
    for i in range(int(number_of_years)):
        while True:
            year = input("Enter Year: ")
            if year.isdigit():
                years.append(year)
                break
            print("Try again!")
            
    return years

def brands_choice():
    brands = []
    number_of_brands = 0
    brand_flag = True

    while True:
        number_of_brands = input("How many brands: ")
        if number_of_brands.isdigit():
            break
        print("Try again!")

    for i in range(int(number_of_brands)):
        while brand_flag:
            brand = input("Brand: ")
            temp_brand_array = brand.split()
            for brnd in temp_brand_array:
                brand_flag = False
                if not brnd.isalnum():
                    print("Try again!")
                    brand_flag = True
                    break
            brands.append(brand)
        brand_flag = True
    return brands

def player_choice():
    players = []
    number_of_players = 0
    player_flag = True

    while True:
        number_of_players = input("How many players: ")
        if number_of_players.isdigit():
            break
        print("Try again!")

    for i in range(int(number_of_players)):
        while player_flag:
            player = input("Player: ")
            temp_player_array = player.split()
            for plyr in temp_player_array:
                player_flag = False
                if not plyr.isalnum():
                    print("Try again!")
                    player_flag = True
                    break
            players.append(player)
        player_flag = True
    return players
        
def main():
    auction_or_bin = []
    years = []
    brands = []
    players = []

    auction_or_bin = auction_or_bin_choice()
    years = years_choice()
    brands = brands_choice()
    players = player_choice()

    open_links(auction_or_bin, years, brands, players)

if __name__ == "__main__":
    main()
