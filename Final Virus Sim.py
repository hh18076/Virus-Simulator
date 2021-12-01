#List that hold alls country 
country_list = []
country_percentage_infected = []
country_in_lockdown = []

#Introduction
print("Welcome to my Virus Simulator! In this simulation there will be 5 days, each day may only choose ONE country to help.")
print("The percentage of infected for the country that is assisted will decrease by 40%, wheareas other countries increases by 20%.")
print("At the end of each day, there will be a display showing the status of each country.")
print("")



#Function that gets country data
def add_country_game():
    add_country = ""
    #Loop will continue to add countries until user is finished
    while True:
        add_country = input("Type in the name of country you would like to add in and then press enter. Once you are done adding your countries type in \"done\" and press enter. ")
        #This will just create space
        print("")
        #If the user has added a valid country, the country will be added to the list
        if add_country != "done":
            while len(add_country) == 0:
                print("You haven't typed anything, try again")
                add_country = input()
            #I would also include validation here to ensure that the user is entering an integer, once the user is done the function will break
            infected_percentage = int(input("Enter in the current percentage of people infected for " + add_country + " and press enter. "))
            print("")
            country_list.append(add_country)
            country_percentage_infected.append(infected_percentage)
            country_in_lockdown.append(False)
        else:
            break
        



#Function that runs every 5 new day. Requires argument of the country to assist.
def new_day(support_country):
    print("___ A NEW DAY ___")
    list_index = 0
    for country in country_list:
        #The percentage of infected people is lowered by 40% if the country is aided.
        #However, if the country's infection rate is already at 40% or lower, there is no possibility to have less than 0% infected.
        #The percentage of infected people increases by 20% if the country is not aided.
        #However, if the country is now at or above 80% infested, it is impossible for it to become 100% infected.
        if country == support_country:
            if country_percentage_infected[list_index] >= 40:
                country_percentage_infected[list_index] = country_percentage_infected[list_index] - 40
            else:
                country_percentage_infected[list_index] = 0
        else:
            if country_percentage_infected[list_index] >= 80:
                country_percentage_infected[list_index] = 100
            else:
                country_percentage_infected[list_index] = country_percentage_infected[list_index] + 20
        #Print the country's current situation.
        print(print_info(country_list[list_index], country_percentage_infected[list_index], country_in_lockdown[list_index]))
        list_index += 1
    print("___ END OF THE DAY ___")
    




#Function that asks the user which country they want to assist.
def ask_country_to_assist():
    #Create a string to show to the user which options are avaliable
    assist_country = "Which country do you want to assist? Choose one from the list below."
    for country in country_list:
        assist_country += "\n" + country
    #Verify that the option chosen is still valid. Checks the country list to determine if it's a valid country, return name of the country if it is valid
    while True:
        help_country = input(assist_country)
        for country in country_list:
            if help_country == country:
                return help_country
        #If the entry is invalid, print an error message and return to the top of the loop.
        print("The input you have entered is Invalid, try again.")




#Function to print the current infected percentage and lockdown status
def print_info(country_list, country_percentage_infected, country_in_lockdown):
  info = "" + country_list + " currently has " + str(country_percentage_infected) + " percent infected, and "
  if country_percentage_infected >= 80:
      country_in_lockdown = True
      info += "is in lockdown."
  else:
    info += "is not in lockdown."
  return info

add_country_game()
for i in range(0, 5):
    new_day(ask_country_to_assist())

print("Thank you for playing.")






        



