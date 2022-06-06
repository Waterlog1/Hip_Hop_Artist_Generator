
print(f"\nWelcome to Underground Hip Hop Artist Generator")
import random





# Generate a list of popular artists from the past and present
# When the user requests to continue with the game, generate another artist



#Once an artist is generated link a recommended album for the user to visit


artists= ["Roc Marciano", "Knowledge the Pirate", "Danny Brown", "Jay Rock",
 "Ab-Soul","El-P", "Big Noyd", "Termanology","Reks", "KA", "Benny The Butcher", "Conway The Machine",
 "AZ", "Flee Lord", "Stove God Cooks", "Freddie Gibbs", "Boldy James", "Armani Caesar", 
 "Baby Keem", "Cormega","Denzel Curry", "Evidence", "Kojey Radical","MF DOOM",
 "Sauce Walka","Skyzoo", "Smoke DZA","Westside Gunn"]

generate= random.choice(artists)

def your_choice():
    start= input(f"\nType 'start' to generate an artist: ")
    if start == 'start' or start =='start'.title():
        print(f"\nThe artist generated is {generate}:")
        if generate == "Danny Brown":
            print(f"\nCheck out {generate}'s 2011 album - 'XXX' ")
        elif generate == "Roc Marciano":
            print(f"\nCheck out {generate}'s 2017 album -'Rosebudd's Revenge'. ")
        elif generate == "Knowledge the Pirate":
            print(f"\nCheck out {generate}'s 2018 album - 'Flintlock'. ")
        elif generate == "Jay Rock":
            print(f"\nCheck out {generate}'s 2011 album - 'Follow me Home'.")
        elif generate == "Ab-Soul":
            print(f"\nCheck out {generate}'s' 2010 album - 'Long Term 2'.")
        elif generate == "Big Noyd":
            print(f"\nCheck out {generate}'s 1996 album - 'Episodes of a Hustla'.")
        elif generate == "Benny The Butcher":
            print(f"\nCheck out {generate}'s 2018 album - 'Tana Talk 3'. ")
        elif generate == "KA":
            print(f"\nCheck out {generate}'s 2020 album - 'Descedants of Cain'. ")
        elif generate == "Conway The Machine":
            print(f"\nCheck out {generate}'s 2020 album - 'From King to a God'.")
        elif generate == "Flee Lord":
            print(f"\nCheck out {generate}'s 2021 project - 'Delgado'.")
        elif generate == "AZ":
            print(f"\nCheck out {generate}'s 1995 album - 'Do or Die'.")
        elif generate == "Westside Gunn":
            print(f"\nCheck out {generate}'s 2018 album - 'Supreme Blientele '.")
        elif generate == "Reks":
            print(f"\nCheck out {generate}' 2008 album - 'Grey hairs'.")
        elif generate == "Freddie Gibbs":
            print(f"\nCheck out {generate}'s 2014 album - 'Pinata'.")
        elif generate == "Boldy James":
            print(f"\nCheck out {generate}' 2020 album - 'Price of tea in China'.")
        elif generate == "Sauce Walka":
            print(f"\nCheck out {generate}'s 2018 album - 'Drip God'.")
        elif generate == "Baby Keem":
            print(f"\nCheck out {generate}'s 2021 album - 'The Melodic Blue'.")
        elif generate == "Evidence":
            print(f"\nCheck out {generate}'s 2011 album - 'Cats and Dogs'.")
        elif generate == "Armani Caesar":
            print(f"\nCheck out {generate}'s 2020 album - 'The Liz'.")
        elif generate == "Kojey Radical":
            print(f"\nCheck out {generate}'s 2019 album - 'Cashmere Tears'.")
        elif generate == "Termanology":
            print(f"\nCheck out {generate}'s 2010 album - '1982'.")
        elif generate == "El-P":
            print(f"\nCheck out {generate}'s 2012 album - 'Cancer 4 Cure'.")
        elif generate == "Stove God Cooks":
            print(f"\nCheck out {generate}'s 2019 album - 'Reasonable Drought'.")
        elif generate == "Cormega":
            print(f"\nCheck out {generate}'s 2001 album - 'The Realness'.")
        elif generate == "Smoke DZA":
            print(f"\nCheck out {generate}'s 2011 album - 'Rolling Stoned'.")
        elif generate == "Denzel Curry":
            print(f"\nCheck out {generate}'s 2013 album - 'Nostalgic 64'.")
        elif generate == "Skyzoo":
            print(f"\nCheck out {generate}'s 2019 album - 'Retropolitan'.")
        elif generate == "MF DOOM":
            print(f"\nCheck out {generate}'s 2019 album - 'Mm..Food'.")
    else:
        print("Error! Please type 'start' to begin.")
        your_choice()
your_choice()


generate= random.choice(artists)


continue_generator= True

while continue_generator:
    generate= random.choice(artists)
    generate_again= input(f"\nWould you like to generate another artist? State 'yes' or 'no':")
    if generate_again == 'yes' or generate_again == 'Yes':
        your_choice()
        continue
    if generate_again == 'no' or 'No':
            continue_generator= False
            print(f"\nThank you for taking part in the Hip Hop artist generator!")
    

   

    



