# PROJECT 7 – PASSWORD POLICY VALIDATION ENGINE

## About the Project
The Password Policy Validation Engine project is designed to check candidate passwords against multiple security requirements, including minimum length, character variety, triple character repetition, and banned substrings. It collects all rule violations and reports every failed condition clearly.

## Technologies Used
- **Python** – Used to develop the password strength validation program.
- **Strings & String Methods** – Used to inspect characters (`isupper`, `islower`, `isdigit`, `isspace`, `lower`) and substrings.
- **Lists** – Used to store validation errors and prohibited substrings.
- **Loops** – Used to scan characters, check consecutive runs, and test banned words.
- **Conditional Statements** – Used to enforce each password rule and print the report.

## Main Features
- Accepts a candidate password string from the user.
- Checks for minimum length of 8 characters and presence of uppercase, lowercase, digit, and special characters.
- Detects three consecutive identical characters (such as `aaa` or `sss`).
- Blocks prohibited substrings (`password`, `admin`, `1234`, `qwerty`) case-insensitively and lists all failures.

## Algorithm
1. Start the program.
2. Read the candidate password and initialize an empty `errors` list.
3. Check if length is less than 8 and record an error if so.
4. Loop through each character to detect uppercase, lowercase, digit, and non-space special characters.
5. Append missing character-category errors if any category is absent.
6. Check adjacent triplets for three identical consecutive characters.
7. Check lowercase password for prohibited substrings and record matches.
8. Print `STRONG & VALID PASSWORD` if no errors exist, or list all failed conditions.
9. Stop the program.

## Sample Output
Enter password to validate: Admin1234

----- PASSWORD VALIDATION REPORT -----
Status: INVALID PASSWORD
Failed Conditions:
  - Must include at least one special character.
  - Contains prohibited substring ('admin').
  - Contains prohibited substring ('1234').

## Conclusion
This project helps enforce strong password policies with clear feedback on every violated rule. It demonstrates Python concepts such as strings, string methods, lists, loops, and conditional statements.
