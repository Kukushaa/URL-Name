url = input("Enter your web. Site: ")

find = url.find("https://")

if find == -1: 
    if url.count("www.") < 1:
        pass

    else:
        url = url[4:]

else: 
    url = url[find + 8:]

    if url.count("www.") < 1:
        pass

    else:
        url = url[4:]

dot = url.find(".")

if url.find(".") == -1:
    print(f'Your website\'s name is \"{url.upper()}"')

else:
    print(f'Your website\'s name is \"{url[:dot].upper()}"')