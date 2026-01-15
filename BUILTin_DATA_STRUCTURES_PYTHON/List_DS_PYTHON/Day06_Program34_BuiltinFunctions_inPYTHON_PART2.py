#this is program34 which covers remaining built In functions In the list : 
#There are so many functions in the list. 
#One thing must be clear that BUILT IN FUNCTIONS work on list by passing list name inside () always remembers this thing,
#Below program contains REMAINING BUILT IN FUNCTIONS excluding len(), max(), min(), sum(), list()

List1 = [10, 20, 30, 0, 40, 50] #added zero to show false elements in the list.
List2 = [40, 50, 60, 70, 80, 90, 100,55] #added 55 at last to show the list is UNSORTED.

# 5) sorted() function returns a NEW sorted list without changing original list
print(f"\nSorted List1 is: {sorted(List1)}\nSorted List2 is: {sorted(List2)}")

# 6) reversed() function returns reverse iterator so we convert it into list
print(f"\nReversed List1 is: {list(reversed(List1))}")
print(f"Reversed List2 is: {list(reversed(List2))}")

#DEFINITION OF WHAT MEANS TRUE AND FALSE HERE IS : 
# One-line answer (exam ready):
# In a list, a true element is any non-zero or non-empty value, 
#while a false element is 0, False, None, or an empty value like '' or [].


# 7) any() function returns True if ANY element of the list is True / non-zero
print(f"\nAny true element in List1: {any(List1)}")
print(f"Any true element in List2: {any(List2)}")

# 8) all() function returns True if ALL elements of the list are True / non-zero
print(f"\nAll elements true in List1: {all(List1)}")
print(f"All elements true in List2: {all(List2)}")

# 9) enumerate() function returns index and value pair of the list
print("\nEnumerate List1:")
for i in enumerate(List1):
    print(i)

print("\nEnumerate List2:")
for i in enumerate(List2):
    print(i)

# 10) zip() function combines two lists element by element
print("\nZipped List1 and List2:")
for i in zip(List1, List2):
    print(i)

# 11) round() function can be used with list values (example using result)
Result = [10.4, 20.6, 30.5]
print(f"\nRounded Result List is: {[round(x) for x in Result]}")

#NOTE:
#All above are BUILT IN FUNCTIONS because list name is passed inside ()
#Methods will be covered separately in next programs
