given_version = input().split(".")
new_version = "".join(given_version)
new_version = int(new_version) + 1
print(".".join(str(new_version)))