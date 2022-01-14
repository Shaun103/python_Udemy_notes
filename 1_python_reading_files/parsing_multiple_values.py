
def main():
    print()
    input_filename = 'country_info.txt'

    countries = {}

    with open(input_filename) as country_file:
        country_file.readline() # gets rid of the file heading
        for row in country_file:
            data = row.strip('\n').split('|')
            country, capital, code, code3, dialing, timezone, currency = data
            # error checking
            # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t') # error handling
            # print(country, capital, code, code3, dialing, timezone, currency)


            country_dict = {
                'name': country,
                'capital': capital,
                'code': code,
                'cc3': code3,
                'dialing_code': dialing,
                'timezone': timezone,
                'currency': currency,
            }
            # error checking
            # print(country_dict)


            # __allows you to parse through code__
            countries[country.casefold()] = country_dict
            countries[code.casefold()] = country_dict
            countries[currency.casefold()] = country_dict


    print(countries['armenia'])
    print(countries['france'])
    

    # choose a country from the dictionary and display its capital 
    while True:
        choice = input("Please enter the name of a country: ").casefold()
        if choice in countries:
            country_data = countries[choice]
            print(country_data) # all country info shown 
            print("Money used: ", country_data['currency'])
            print(f"The capital of {str.title(choice)} is {country_data['capital']}")
        elif choice == 'quit':
            print("...Exiting program")
            break
        else:
            print(f"{choice} not list")

#__________________________________________________________________________________________________

    # for key in countries.keys():
    #     if 'dollar' in key:
    #         print(countries[key])
        



    # print(countries)





if __name__ == "__main__":
    main()