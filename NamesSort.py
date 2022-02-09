names_arr = []
print("Enter Names:")
for x in range(6):
    names = input()
    names_arr.append(names)
else:
    print("Before Sort: ")
    print(names_arr)
    names_arr.sort()
    print("After Sort: ")
    print(names_arr)