friends = {"Ralf", "Rob", "Mary"}
more_friends = {"Bob", "Anna"}
abroad = {"Rob", "Mary"}

#friends + more_friends does not work
print(friends.union(more_friends))

#next two operations are the same
print(friends - abroad)
print(friends.difference(abroad))

my_tuple = tuple(1)
print(len(my_tuple))