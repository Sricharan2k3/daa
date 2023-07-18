def graph_coloring(subjects):
    clashes = {}
    for subject in subjects:
        subject_code = subject[1]
        clashes[subject_code] = set(subject[2])

    timetable = {}
    colors = {}
    num_colors = len(subjects)

    def backtrack(subject_code):
        if subject_code == len(subjects):
            return True

        for color in range(1, num_colors+1):
            if is_color_valid(subject_code, color):
                colors[subject_code] = color
                if backtrack(subject_code+1):
                    return True
                colors.pop(subject_code)

        return False

    def is_color_valid(subject_code, color):
        for neighbour in clashes[subjects[subject_code][1]]:
            if neighbour in colors and colors[neighbour] == color:
                return False
        return True

    if backtrack(0):
        for subject_code, color in colors.items():
            if color not in timetable:
                timetable[color] = []
            timetable[color].append(subjects[subject_code][1])
    else:
        print("No valid timetable possible.")

    return timetable


subjects = [
    ("A", "C1", ["C2", "C3"]),
    ("B", "C2", ["C1"]),
    ("C", "C3", ["C1", "C4"]),
    ("D", "C4", ["C3"]),
    ("E", "C5", []),
]

timetable = graph_coloring(subjects)
for color, subjects in timetable.items():
    print(f"Timetable {color}:")
    for subject in subjects:
        print(subject)
    print()
