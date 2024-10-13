# START
full_name = "altory jobran kfar qassem"

print(f"Length of string: {len(full_name)}")

print(full_name.upper())

print(full_name.lower())

print(full_name.startswith("altory"))

print(full_name.endswith("kfar qassem"))

name_list = full_name.split()
print(name_list)

new_string = full_name.replace(" ", "*")
print(new_string.split("*"))

print(full_name.center(50, "="))

print(full_name[3:])

print(full_name[:4])

print(full_name[::2])

print(full_name.title())

# END
