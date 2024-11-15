# START

fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

print("Reversed names:", list(map(lambda f: f[::-1], fruits)))

print("First letters:", list(map(lambda f: f[0], fruits)))

print("Uppercase names:", list(map(lambda f: f.upper(), fruits)))

print("Middle letters:", list(map(lambda f: f[len(f) // 2], fruits)))

print("fruits ending with 's' modified:", list(map(lambda f: f + "!" if f.endswith('s') else f, fruits)))

# END
