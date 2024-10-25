# python data types
 
ideas = ['expenser', 'Locale_BNB','SeeAI','Ecommerce', 'shopping list']

ideas.append('klinsept') # adds item to the end
ideas.insert(2, 'Utheri') # inserts item at a specific index arg1

# print(dir(ideas))
print(ideas[-1]) # get the last item in the list

print(ideas[0:2]) # get all the values from index 0 upto but not including index 2
print(ideas[2:]) # gets from index 2 to the last
print(ideas[:3]) # gets from index 0 upto but not including index 3


courses = ['Comp', 'Art', 'music', 'Education']

ideas.extend(courses) # add two lists together (individual items)

# ideas.remove('Art') # removes the argument

print(ideas.pop()) # removes last item , can pass an argument



print('\n## sort\n')

ideas.reverse()
ideas.sort(reverse=True)
print(sorted(ideas))
print(ideas)

print('\n## Find\n')


print(ideas.index('Art'))

print( 'Art' in ideas)

for i in enumerate(ideas, start=2):
    print(i)

print('-'.join(ideas))