import webbrowser

def add_array_to_url(temp_array):
    url = ""
    for temp in temp_array:
        url += "+" + temp
    return url

def open_links(auction_or_bin, year, brand, player):
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
    if auction_or_bin == 'a':
        url1 += "Auction=1&_sop=1"        
    else:
        url1 += "BIN=1&_sop=10"

    # Launches the web browser
    webbrowser.open_new_tab(url1)
    webbrowser.open_new_tab(url2)

def auction_or_bin_choice():
    while True:
        auction_or_bin = input("Auction or Buy It Now (a or bin): ")
        if auction_or_bin == "a" or auction_or_bin == "bin":
            return auction_or_bin
        print("Try again!")

def year_choice():
    while True:
        year = input("Year: ")
        if year.isdigit():
            return year
        print("Try again!")

def brand_choice():
    brand = ""
    brand_flag = True
    while brand_flag:
        brand = input("Brand: ")
        temp_brand_array = brand.split()
        for brnd in temp_brand_array:
            brand_flag = False
            if not brnd.isalnum():
                print("Try again!")
                brand_flag = True
                break
    return brand

def player_choice():
    player = ""
    player_flag = True
    while player_flag:
        player = input("Player: ")
        temp_player_array = player.split()
        for plyr in temp_player_array:
            player_flag = False
            if not plyr.isalnum():
                print("Try again!")
                player_flag = True
                break
    return player
        
def main():
    auction_or_bin = ""
    year = ""
    brand = ""
    player = ""

    auction_or_bin = auction_or_bin_choice()
    year = year_choice()
    brand = brand_choice()
    player = player_choice()

    open_links(auction_or_bin, year, brand, player)

if __name__ == "__main__":
    main()
