#1st
name="Anirudh"
def greet():
    print(f"Hey {name}! Good morning")
greet()

#2nd 
name="Anirudh"
def greet():
    name="Muskan" # This is local variable
    print(f"Hey {name}! Good morning")
greet()
print(name)
