#A List to hold all the countries
country_list = []

NZ = ("New Zealand")
FR = ("France")
JP = ("Japan")
country_list.append(NZ)
country_list.append(FR)
country_list.append(JP)


#Function that will ask the user which countries to add
def add_country():
    #Loop allows user to keep adding countries until user is done
    while True:
        country = input("Which country would you like to add? ")
        if country != "done":
            infected = int(input("What percent of the country is infected? "))
        #If the user is done adding the countries, this will break out of function
        else:
            break
        newlist = country
        i = country_list.append(newlist)
        for i in country_list:
            print(i)

#Function to ask user if they will want to add a country or not
def main():
    country = input("If you would like to add in a country type in \"add\" or type in \"done\" and click enter ")
    if country.lower() == "add":
        add_country()
    elif country.lower() == "done":
        help()


if __name__ == "__main__":
    main()
