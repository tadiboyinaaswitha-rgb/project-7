pwd = input("Enter password to validate: ")
errors = []

if len(pwd) < 8:
    errors.append("Must be at least 8 characters long.")

has_upper = False
has_lower = False
has_digit = False
has_spec = False

for ch in pwd:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif not ch.isspace():
        has_spec = True

if not has_upper:
    errors.append("Must include at least one uppercase letter.")
if not has_lower:
    errors.append("Must include at least one lowercase letter.")
if not has_digit:
    errors.append("Must include at least one digit.")
if not has_spec:
    errors.append("Must include at least one special character.")

for i in range(len(pwd) - 2):
    if pwd[i] == pwd[i + 1] == pwd[i + 2]:
        errors.append(f"Contains 3 consecutive identical characters ('{pwd[i]*3}').")
        break

prohibited = ["password", "admin", "1234", "qwerty"]
lower_pwd = pwd.lower()
for word in prohibited:
    if word in lower_pwd:
        errors.append(f"Contains prohibited substring ('{word}').")

print("\n----- PASSWORD VALIDATION REPORT -----")
if len(errors) == 0:
    print("Status: STRONG & VALID PASSWORD")
else:
    print("Status: INVALID PASSWORD")
    print("Failed Conditions:")
    for err in errors:
        print("  -", err)
