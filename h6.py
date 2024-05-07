first_line = ["alex ovechkin", "gabriel landeskog", "brad marchand"]
first_line_upper = ['', '', '']
i = 0
for player in first_line:
    first_line_upper[i] = player.title()
    i += 1

print('Capitalized names: ', first_line_upper)

first_line_last_names = [full_name.split(" ")[1] for full_name in first_line]
print("Last names of first line: ", first_line_last_names)

first_line_a_only = [x.title() for x in first_line if x.startswith("a")]
print("First line a only: ", first_line_a_only)
