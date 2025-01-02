dict1 = {"user" : "12345", "yiğit" : "55"}

def register(name,password):
    if name in dict1:
        print("This username already exist.")
        return False   
    else:
        dict1[name] = str(password)
        return True
def check_login(name,password):
    if name in dict1:
        if dict1[name] == str(password):
            print("Login succesfull.")
            return True
        else:
            print("Wrong password.")
            return False
    else:
        print("No user with this username.")
        return False
    
def remove(username):
    if username in dict1:
        del dict1[username]
        return True
    else:
        print("No user with this username.")
        return False

print(dict1)
register("Büşra",4567)

print(dict1)
register("İsmail","İsmail123")
print(dict1)
check_login("İsmail","İsmail123")
check_login("İSmail","İsmail123")

remove("user")
print(dict1)
remove("Ahmet")