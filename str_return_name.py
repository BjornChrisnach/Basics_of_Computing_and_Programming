full_name = input("Enter full name, split up with a space: ")
space_index = full_name.find(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]
initials = first_name[0] + last_name[0]

print("First name:", first_name)
print("Last name:", last_name)
print("Initials", initials)