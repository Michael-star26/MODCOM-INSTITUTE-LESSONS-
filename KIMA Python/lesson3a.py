# create a tuple of social media apps
social_media_apps=("Facebook","Whatsapp","Twitter","Instagram")
print(social_media_apps)
print(type(social_media_apps))
# tuple
# use parenthesis (round brackets)
# immutable-items cannot be changed
# ordered


# Allows duplicates
social_media_apps=("Facebook","Whatsapp","Twitter","Instagram","Twitter")
print(social_media_apps)
# try appending
# social_media_apps.append("Reddit")
# print(social_media_apps)------Not Supported in tuple

# access items
print(social_media_apps[0])
print(social_media_apps[0:3])
#  tuple length
print(len(social_media_apps))
# to create a tuple of item use comma after the item
app=("Reddit",)
print(app)
print(type(app))
population=(5000000)
print(type(population)) #integer
print(type(population,)) #tuple because of the comma
# tuple accepts items of any data type
# Create a tuple with int,float,bolean data types
 
my_tuple=("Michael",3.142,True,500,["Yellow","Green"])
print(my_tuple)
print(type(my_tuple))

list_1=["item 1",(78,90)]
print(list_1)

