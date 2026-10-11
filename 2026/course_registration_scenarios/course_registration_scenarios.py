"""
Extended scenario runner for the course registration activity diagram.

Reuses the Student/Course model and register_for_course() logic from
course_registrationv2.py, but exercises a wider mix of SUCCESS and DENIED
cases (denial via missing prerequisites/permissions, denial via a full
course, and denial via both failing at once).
"""

from course_registrationv2 import Course, Student, register_for_course


def main():
    scenarios = [
        # SUCCESS: has prerequisites, course open
        (Student(name="Alice", has_prerequisites=True), Course(name="CS101", is_full=False)),
        # SUCCESS: no prerequisites but has special permission, course open
        (Student(name="Bob", has_prerequisites=False, has_permissions=True), Course(name="CS101", is_full=False)),
        # SUCCESS: has prerequisites, different course open
        (Student(name="Frank", has_prerequisites=True), Course(name="CS202", is_full=False)),
        # DENIED: no prerequisites, no permissions, AND course full (both branches fail)
        (Student(name="Carol", has_prerequisites=False, has_permissions=False), Course(name="CS101", is_full=True)),
        # DENIED: has prerequisites, but course is full (branch B fails only)
        (Student(name="Dave", has_prerequisites=True), Course(name="CS202", is_full=True)),
        # DENIED: no prerequisites, no permissions, course open (branch A fails only)
        (Student(name="Eve", has_prerequisites=False, has_permissions=False), Course(name="CS303", is_full=False)),
    ]

    results = []
    for student, course in scenarios:
        print("=" * 50)
        result = register_for_course(student, course)
        results.append((student.name, result))
        print(f"Result: {'SUCCESS' if result else 'DENIED'}")
        print()

    print("=" * 50)
    print("Summary:")
    for name, result in results:
        print(f"  {name}: {'SUCCESS' if result else 'DENIED'}")


if __name__ == "__main__":
    main()
