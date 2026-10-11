"""
Implementation of the Course Registration activity diagram.

Flow:
  (start) -> Receive course registration request -> fork
    Branch A: Check prerequisites
        [hasPrerequisites]        -> join
        [doesNotHavePrerequisites] -> Check special permissions
            [hasPermissions] -> join
            [noPermissions]  -> (end, registration denied)
    Branch B: Verify course not full
        [notFull] -> join
        [full]    -> (end, registration denied)
  join -> Complete registration -> (end)

Branches A and B run concurrently (fork bar), and the join waits for both
to finish before proceeding.
"""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    has_prerequisites: bool
    has_permissions: bool = False  # only consulted if prerequisites are missing


@dataclass
class Course:
    name: str
    is_full: bool


def receive_course_registration_request(student: Student, course: Course) -> None:
    print(f"Receive course registration request: {student.name} -> {course.name}")


def check_prerequisites(student: Student) -> bool:
    """Decision node: Check prerequisites."""
    print("Check prerequisites...")
    if student.has_prerequisites:
        print("  [hasPrerequisites] -> join")
        return True
    print("  [doesNotHavePrerequisites] -> Check special permissions")
    return False


def check_special_permissions(student: Student) -> bool:
    """Decision node: Check special permissions (only reached without prerequisites)."""
    print("Check special permissions...")
    if student.has_permissions:
        print("  [hasPermissions] -> join")
        return True
    print("  [noPermissions] -> (end)")
    return False


def verify_course_not_full(course: Course) -> bool:
    """Decision node: Verify course not full."""
    print("Verify course not full...")
    if not course.is_full:
        print("  [notFull] -> join")
        return True
    print("  [full] -> (end)")
    return False


def complete_registration(student: Student, course: Course) -> None:
    print(f"Complete registration: {student.name} is registered for {course.name}")


def register_for_course(student: Student, course: Course) -> bool:
    """
    Runs the full activity diagram for a single registration attempt.
    Returns True if registration completed, False if it ended early (denied).
    """
    receive_course_registration_request(student, course)

    # ---- Fork into two concurrent branches ----

    # Branch A: prerequisites / special permissions
    def branch_a():
        """Prerequisites / special-permissions branch."""
        if check_prerequisites(student):
            return True
        if check_special_permissions(student):
            return True
        return False

    def branch_b():
        """Course capacity branch."""
        return verify_course_not_full(course)

    # Run both branches concurrently on separate threads, as the fork bar implies.
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_a = executor.submit(branch_a)
        future_b = executor.submit(branch_b)
        branch_a_ok = future_a.result()
        branch_b_ok = future_b.result()

    # ---- Join: both branches must succeed ----
    if not branch_a_ok:
        print("Registration denied: no prerequisites and no special permissions")
        return False
    if not branch_b_ok:
        print("Registration denied: course is full")
        return False

    complete_registration(student, course)
    return True


def main():
    scenarios = [
        Student(name="Alice", has_prerequisites=True),
        Student(name="Bob", has_prerequisites=False, has_permissions=True),
        Student(name="Carol", has_prerequisites=False, has_permissions=False),
    ]
    courses = [
        Course(name="CS101", is_full=False),
        Course(name="CS101", is_full=False),
        Course(name="CS101", is_full=True),
    ]

    for student, course in zip(scenarios, courses):
        print("=" * 50)
        result = register_for_course(student, course)
        print(f"Result: {'SUCCESS' if result else 'DENIED'}")
        print()


if __name__ == "__main__":
    main()
