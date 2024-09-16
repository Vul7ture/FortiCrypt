import hashlib

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

print("""╦ ╦┌─┐┌─┐┬ ┬        ╔═╗┬─┐
╠═╣├─┤└─┐├─┤        ║╣ ├┬┘
╩ ╩┴ ┴└─┘┴ ┴  ────  ╚═╝┴└─""")

hashed_string = hash_string(input("Type in: "))
print(f'Your Hash: {hashed_string}')

