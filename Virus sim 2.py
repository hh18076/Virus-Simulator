
country_list = []

NZ = ("New Zealand")
FR = ("France")
JP = ("Japan")
country_list.append(NZ)
country_list.append(FR)
country_list.append(JP)

def add_country():
    while True:
        country = input("Which country would you like to add? ")
        if country != "done":
            infected = int(input("What percent of the country is infected? "))
        else:
            break
        newlist = country
        i = country_list.append(newlist)
        for i in country_list:
            print(i)

def main():
    country = input("If you would like to add in a country type in \"add\" or type in \"done\" and click enter ")
    if country.lower() == "add":
        add_country()
    elif country.lower() == "done":
        help()


if __name__ == "__main__":
    main()
