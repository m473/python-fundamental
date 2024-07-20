# format json / dictionary
users = {
    "id"        : 1,
    "name"      : "Leanne Graham",
    "username"  : "Bret",
    "email"     : "Sincere@april.biz",
    "address"   : {
            "street"    : "Kulas Light",
            "suite"     : "Apt. 556",
            "city"      : "Gwenborough",
            "zipcode"   : "92998-3874",
            "geo"   : {
                "lat"   : "-37.3159",
                "lng"   : "81.1496"
            }
        }
}
print(users)
print('\n', users["id" ])
print('\n', users["name" ])
print('\n', users["username"])
print('\n', users["email"])
print('\n', users["address"])
print('\n', users["address"]["street"])
print('\n', users["address"]["geo"])
print('\nLat : ', users["address"]["geo"]["lat"])

# merubah dari python dictionary menjadi json --> package bawaan python yaitu json
print("\npython dict")
print(users)
print('tipe data : ', type(users))
import json
result = json.dumps(users) # merubah python dict menjadi string , string json, ini bisa dikirim ke aplikasi lain
print('\nubah dict to json')
print ('\ndumps : ', result)
print ('\ntipe data : ', type(result))


# menulis ke file
with open('result.json', 'w') as file:
    json.dump(users, file)
