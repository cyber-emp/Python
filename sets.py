# sets are unordered and dont allow duplicates
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
'''

# 3 ''' before and 3  ''' after code comments it out so that when you run the file you dont see the output

# *operations with sets*
#union adds both sets together and removes duplicates
#intersection finds common elements in two sets and returns them
#difference finds the elements that are present in 1 not the other.



set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union
union_set = set1.union(set2)
print(union_set)

#intersection
inter_set = set1.intersection(set2)
print(inter_set)

#difference
diff_set = set1.difference(set2)
print(diff_set)

# sets are used when you need to work with unique elements.  removing duplicates from lists, checking membership