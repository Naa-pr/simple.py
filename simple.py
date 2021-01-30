print("let's transform your age to minute and second")
a=input("Enter your name plz:")
print("Hello",a)
try:
    b=int(input("Enter your age plz:"))
    days=b*365
    hour=b*8760
    minutes=b*525600
    seconds=b*31536000
    print("You hve born ", b, " days ago")
    print("You hve born ", hour, " hours ago")
    print("You hve born ", minutes, " minutes ago")
    print("You hve born ", seconds, " seconds ago")
except Exception as e:
    print(e)
print("Remember it is an aproximate time")
