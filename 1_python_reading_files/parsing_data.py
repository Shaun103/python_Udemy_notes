# parsing making sense of data 

def main():
    print()


    input_filename = 'country_info.txt'

    # with open(input_filename) as country_file:
    #     for row in country_file:
    #         data = row.strip('\n').split('|')
    #         print(data)

#__________________________________________________________________


    countries = {}

    with open(input_filename) as country_file:
        # country_file.readline() # gets rid of the file heading
        for row in country_file:
            data = row.strip('\n').split('|')
            country, capital, code, code3, dialing, timezone, currency = data
            # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t') # error handling
            # print(country, capital, code, code3, dialing, timezone, currency)

            country_dict = {
                'name': country,
                'capital': capital,
                'cc3': code3,
                'dialing_code': dialing,
                'timezone': timezone,
                'currency': currency,
            }
            # print(country_dict)


            countries[country.casefold()] = country_dict
            countries[code.casefold()] = country_dict
            countries[currency.casefold()] = country_dict



    # __prints all information for all countries__
    print(countries)  
    
    # __prints country by name or code__#
    print(countries['antarctica']) 
    print(countries['spain'])
    print(countries['au'])
    print(countries['us'])
# ________________________________________________________________________________________________

    # choose a country from the dictionary and display its capital 
    # while True:
    #     chosen_country = input("Please enter the name of a country: ").casefold()
    #     if chosen_country in countries:
    #         country_data = countries[chosen_country]
    #         # print(country_data) # all country info shown
    #         # print(country_data['capital']) # just the country capital 
    #         print(f"The capital of {str.title(chosen_country)} is {country_data['capital']}")
    #     elif chosen_country == 'quit':
    #         print("...Exiting program")
    #         break
    #     else:
    #         print(f"{chosen_country} not list") 


if __name__ == "__main__":
    main()