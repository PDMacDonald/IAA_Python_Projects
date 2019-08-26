#Takes a list of column names and returns a csv string version
def col_names_csv_str(col_names, d):

    col_names_csv_str = ""

    for i in range(len(col_names) - 1):
        col_names_csv_str += "\"" + col_names[i] + "\"" + d

    col_names_csv_str += "\"" + col_names[len(col_names) - 1] + "\"" + "\n"

    return col_names_csv_str


#Output procedure
def print_as_csv(out_file, cities, col_names):

    out = open(out_file, "w+")
    d = "," #delimiter

    #Output csv formatted column names
    out.write(col_names_csv_str(col_names, d))

    #Write out city weather data in csv format
    for city in cities:
        
        csv_str = "\"" + city.get_city_ref() + "\"" + d + str(city.get_lat()) + d + str(city.get_lon()) + d

        five_day_minmax = city.get_5d_minmax()

        for day in five_day_minmax:
            csv_str += str(day[ "min" ]) + d + str(day[ "max"]) + d
        
        csv_str += str(city.get_min_avg()) + d + str(city.get_max_avg()) + "\n"

        out.write(csv_str)

    out.close

def f_to_c(Fahrenheit):
    return round((Fahrenheit - 32) * 5/9, 2)