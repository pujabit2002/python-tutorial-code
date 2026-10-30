marks={"math":85, "science":92, "english":78, "hindi":60}
#len() ->number of key-value pairs
print(len(marks))

#sum() on values
print(sum(marks.values()))

#min() and max() on values
print(min(marks.values()))
print(max(marks.values()))

#min() and max() on keys (by default it uses keys, sorted alphabetically)
print(min(marks))
print(max(marks))