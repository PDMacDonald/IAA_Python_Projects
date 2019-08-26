
import sys
sys.path.insert( 1, "C:/Users/prest/Desktop/IAA_PY/Dark_Sky_Exercise" )

# Import forecastiopy to access dark skies api for weather data
from forecastiopy import ForecastIO
from forecastiopy import FIODaily
import City as c
import CSV_Util as csv


### Hard coded input ###
key = 'ac30dc22b9edb1514eb51c0cda898d4e'
out_file_name = "Temp3.csv"

cities = []
cities.append(c.City( "Anchorage, Alaska", 61.2181 , -149.9003 ))
cities.append(c.City( "Buenos Aires", -34.6037 , -58.3816))
cities.append(c.City( "Sao Jose dos Campos, Brazil", -23.2237, -45.9009))
cities.append(c.City( "San Jose, Costa Rica", 9.9281, -84.0907 ))
cities.append(c.City( "Nanaimo, Canada",49.1659, -123.9401))
cities.append(c.City( "Ningbo, China", 29.8683, 121.5440))
cities.append(c.City( "Giza, Egypt", 30.0131, 31.2089))
cities.append(c.City( "Mannheim, Germany", 49.4875, 8.4660))
cities.append(c.City( "Hyderabad, India", 17.3850, 78.4867))
cities.append(c.City( "Tehran, Iran", 35.6892, 51.3890))
cities.append(c.City( "Bishkek, Kyrgyzstan", 42.8746, 74.5698))
cities.append(c.City( "Riga, Latvia", 56.9496, 24.1052))
cities.append(c.City( "Quetta, Pakistan", 30.1798, 66.9750))
cities.append(c.City( "Warsaw, Poland", 52.2297, 21.0122))
cities.append(c.City( "Dhahran, Saudia Arabia", 26.2361, 50.0393))
cities.append(c.City( "Madrid, Spain", 40.4168, -3.7038))
cities.append(c.City( "Oldham, United Kingdom", 53.5409, -2.1114))

col_names = []
col_names.append("City")
col_names.append("lat")
col_names.append("lon")
col_names.append("Min_1")
col_names.append("Max_1")
col_names.append("Min_2")
col_names.append("Max_2")
col_names.append("Min_3")
col_names.append("Max_3")
col_names.append("Min_4")
col_names.append("Max_4")
col_names.append("Min_5")
col_names.append("Max_5")
col_names.append("Min_avg")
col_names.append("Max_max")




#Obtain and read in weather data through Python3 wrapper for Dark Sky API

for i in range(len(cities)):

    fio = ForecastIO.ForecastIO(key, latitude = cities[i].get_lat(), 
                                longitude = cities[i].get_lon())
    

    daily = FIODaily.FIODaily( fio )
    
    for day in range(2, 7):
        
        val = daily.get( day )
        cities[i].add_minmax( str(val[ "temperatureMin" ]), 
                              str(val[ "temperatureMax" ]))


#Write to CSV
csv.print_as_csv(out_file_name, cities, col_names)


print("Dark Sky data was successfully recieved and processed into an appropriate CSV output.")


# END OF PROGRAM