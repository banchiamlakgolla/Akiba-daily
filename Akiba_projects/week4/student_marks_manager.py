# Creates a list containing at least five student marks
original_mark = [75, 80, 65, 90, 85]

shared_ref = original_mark

copied_mark = original_mark.copy()
copied_mark.append(95)

print("Original marks:", original_mark)
print("Shared reference:", shared_ref)
print("Copied marks:", copied_mark)

print("\nOriginal and shared reference are identical: ",  original_mark is shared_ref)
print("Original and copied lists have equal values: ", original_mark == copied_mark)
print("Original and copied lists are identical: ", original_mark is copied_mark)
