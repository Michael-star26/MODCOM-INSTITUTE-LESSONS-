# Dictionary
# colection of key-value pairs which are ordered and changable/mutable
# can be created using curly braces{}
# Accepts info of any data type
# create a dictionary of a movie

movie={
    "Name":"Money Heist",
    "Main Actor":"Tokyo",
    "Release Date":"26/6/2019",
    "Genre":"Thriller"
}
print(movie)
print(type(movie))
print(movie["Name"])
print(movie["Main Actor"])
print(movie["Release Date"])
print(movie["Genre"])
# change items
movie["Release Date"]="20/7/2020"
print(movie)
# add an item(pair key and value)
movie["Cost"]="20,000,000"
print(movie)
# update the release date to a list of items
movie["Release Date"]="25/8/2020","26/6/2019","30/5/2017"
print(movie)
#Access All keys in A dictionary
print(movie.keys())
#Access All jvalues in A dictionary
print(movie.values())


# create a dictionary with duplicate values
# person,name,DOB,Class,nationality
details={"Name":"Owino Michael",
         "DOB":"23/7/2004",
         "Class":"KIMA",
         "Class":"KIMA",
         "Nationality":"Kenyan",
         "Married?":False}
print(details)
# access first release date
print(movie["Release Date"][-2])
details["Age"]=25
print(details)
# Delete items in a dictionary
del details["Class"]
print(details)
del (details)
print(details)
# read on python sets and conditional statements
# Do a research on how python can be used in decision making
# come up with real life examples
