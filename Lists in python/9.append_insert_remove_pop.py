lst=["Anirudh", 54,21.98, True, "Surat"]
print(lst)
lst.append(100)
print(lst)
lst.append("Delhi")
print(lst)


lst.insert(2,"Delhi")
print(lst)
lst.insert(0,"Muskan")
print(lst)


x=lst.pop()
print(x)

x=lst.pop(2)
print(x)
print(lst)

lst.remove(21.98)
print(lst)