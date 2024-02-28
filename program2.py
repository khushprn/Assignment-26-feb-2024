ns = set()

while True:
    n = input("Enter a name or you can press enter to exit : ")
    if n == "":
        break
    elif n in ns:
        print("Existing name")
    else:
        print("New name")
        ns.add(n)

print("\nList of names:")
for n in ns:
    print(n)