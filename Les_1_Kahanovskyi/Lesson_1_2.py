geographic_dict = {' Ukraine ': ' Kiev ',' UK ': ' London ', ' Poland ': ' Varshava '}

country_list = [' Ukraine ', ' Poland ', 'Russia', 'USA']

for i in range(len(country_list)):

    if country_list[i] in geographic_dict.keys():

        print(geographic_dict[country_list[i]])
