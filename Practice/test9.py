# import copy

# original_list = [1, 2, [3, 4]]
# shallow_copied_list = copy.copy(original_list)

# print(f"Original: {original_list}")
# print(f"Shallow Copy: {shallow_copied_list}") 

# original_list[0] = 99  # Modifies only original_list
# print(f"After modifying original[0]: {original_list}")
# print(f"Shallow Copy: {shallow_copied_list}") 

# original_list[2][0] = 88 # Modifies the nested list in both
# print(f"After modifying original[2][0]: {original_list}") 
# print(f"Shallow Copy: {shallow_copied_list}") 

# original_list[1] = 20
# print(f"After modifying original[0]: {original_list}") 
# print(f"Shallow Copy: {shallow_copied_list}") 
 # Deep Copy

import copy

original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

print(f"Original: {original_list}")
print(f"Deep Copy: {deep_copied_list}")

original_list[0] = 99
print(f"After modifying original[0]: {original_list}")
print(f"Deep Copy: {deep_copied_list}")

original_list[2][0] = 88
print(f"After modifying original[2][0]: {original_list}")
print(f"Deep Copy: {deep_copied_list}")