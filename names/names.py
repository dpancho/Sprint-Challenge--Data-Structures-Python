import time
from dll_queue import Queue

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
q = Queue()
for name_2 in names_2:
    q.enqueue(name_2)
while q.len() > 0:
    name = q.dequeue()
    if name in names_1:
        duplicates.append(name)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#####COMMENTED OUT, but runs faster than above
# # new dictionary to store names
# names2_dict = {}

# # Store each name once,. 
# for name in names_2:
#     names2_dict[name] = 1
#     # print (names2_dict)

# # comapre list and if duplicates, append to dupilicates list
# for name in names_1:
#     if names2_dict.get(name) == None:
#         pass
#     else:
#         duplicates.append(name)

# end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print(f"runtime: {end_time - start_time} seconds")