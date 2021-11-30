#List to hold all country objects
country_list = []
country_infected_percents = []
country_in_lockdown = []

NZ = ("New Zealand")
FR = ("France")
JP = ("Japan")
country_list.append(NZ)
country_list.append(FR)
country_list.append(JP)

#Function to ask user if they want to add a country or not
def main():
    country = str(input("If you would like to add in a country to help type in \"add\" or type in \"done\" and click enter. "))
    if country != "add":
        add_country()
    else :country != "done"

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
                
if __name__ == "__main__":
    main()


 
#Function to ask user which country to help
def which_country_help():
    which_country = "Which country would you like to help?"
    for country in country_list:
        which_country += "\n" + country.country_name
    while True:
        country_to_help = input(which_country)
        for country in country_list:
            if country_to_help == country.country_name:
                return country_to_help
        print("Invalid input, please try again.")
        #Check if country is valid

#Function which print the details
def print_details(self):
    details = "" + country_list + "has " + str(country_infected_percents) + " percent infected, and "
    if country_in_lockdown == True:
        details += "is in lockdown."
    else:
        details += "is not in lockdown."
    return details














    
