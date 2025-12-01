import pathlib
import sys
import re

#Read the file specified on the command line from current directory
file_name = sys.argv[1]
#file_name = 'infile.txt'
file_path = pathlib.Path(file_name)
if not file_path.is_file():
    print(f"File {file_name} not found.")
    sys.exit(2)
file_content = file_path.read_text()

#Count successful logins
all_success = re.findall(r"LOGIN SUCCESS from (.+)", file_content)
successes = len(all_success)

#Count Failed logins
all_fails = re.findall(r"LOGIN FAILURE from (.+)", file_content)
failures = len(all_fails)

#Build a list of possible attackers (more than 1 login failure)
list_of_attackers = []
for eachip in all_fails:
    if (all_fails.count(eachip) > 1) and (eachip not in list_of_attackers):
        list_of_attackers.append(eachip)

print(f"Login Successes: {successes}")
print(f"Login Failures: {failures}")
print(f"Possible attacker(s): {sorted(list_of_attackers)}")