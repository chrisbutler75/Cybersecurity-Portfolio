# Program Name: Lab12py (use the name the program is
#saved as)
# Student Name: Chris B
# Assignment Number: Lab12
# Purpose:  The program reads a file of student grades and calculates the average numeric grade for each class section.
#assignment




# grade conversion table
grade_map = {
    "A": 100,
    "B": 89,
    "C": 79,
    "D": 74,
    "F": 69
}

# dictionary to store section totals and counts
sections = {}
 
# open the grades file
with open("grades.txt", "r") as l:
    for line in l:
        parts = line.strip().split("\t")  # break apart ID, section, grade
        section = int(parts[1])
        letter = parts[2]

        score = grade_map[letter]  # convert letter to number

        # if section not seen before start it
        if section not in sections:
            sections[section] = {"total": 0, "count": 0}

        # add score to that section
        sections[section]["total"] += score
        sections[section]["count"] += 1

# now print averages
for sec in sorted(sections.keys()):
    avg = sections[sec]["total"] / sections[sec]["count"]
    print(f"Section {sec} average: {avg}")

