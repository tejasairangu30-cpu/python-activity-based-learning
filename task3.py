# Smart Classroom Timetable Allocation

# Courses: (Course Name, Number of Students)
courses = [
    ("Python", 50),
    ("Mathematics", 40),
    ("Physics", 60),
    ("English", 30)
]

# Classrooms: (Room Name, Capacity)
rooms = [
    ("Room A", 45),
    ("Room B", 60),
    ("Room C", 70)
]

# Available periods
periods = ["9-10 AM", "10-11 AM", "11-12 PM"]

# Timetable: (Course, Room, Period)
timetable = [
    ("Python", "Room B", "9-10 AM"),
    ("Mathematics", "Room A", "9-10 AM"),
    ("Physics", "Room C", "10-11 AM"),
    ("English", "Room A", "10-11 AM")
]

assigned_courses = set()
used_slots = set()
valid = True

print("SMART CLASSROOM TIMETABLE")
print("-" * 50)

for course, room, period in timetable:
    # Find course details
    course_info = next(
        (c for c in courses if c[0] == course), None
    )
    room_info = next(
        (r for r in rooms if r[0] == room), None
    )

    if course_info is None or room_info is None:
        print("Error: Invalid course or classroom:", course)
        valid = False
        continue

    students = course_info[1]
    capacity = room_info[1]

    # Check whether the period is valid
    if period not in periods:
        print("Error: Invalid period:", period)
        valid = False
        continue

    # Check classroom capacity
    if students > capacity:
        print("Capacity exceeded:", course, "in", room)
        valid = False

    # Check whether the course is already scheduled
    if course in assigned_courses:
        print("Duplicate course:", course)
        valid = False

    # Check whether the room is already occupied
    slot = (room, period)
    if slot in used_slots:
        print("Room clash:", room, "during", period)
        valid = False

    assigned_courses.add(course)
    used_slots.add(slot)

    print(course, "->", room, "->", period)

# Check whether every course is scheduled
missing = [c[0] for c in courses
           if c[0] not in assigned_courses]

if missing:
    print("\nUnscheduled courses:", missing)
    valid = False

print("-" * 50)

if valid:
    print("Result: Timetable is valid.")
else:
    print("Result: Timetable has errors.")
