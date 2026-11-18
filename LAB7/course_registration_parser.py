
def format_course_code(code):
    """
    Formats 'cs 301' as 'CS301'.
    Returns None for invalid input.
    """
    if not isinstance(code, str):
        return None

    parts = code.split()

    if len(parts) != 2:
        return None

    dept, number = parts

    if not dept.isalnum() or not number.isalnum():
        return None

    return dept.upper() + number


def total_credits(text):
    """
    Adds up comma-separated course credits.
    Returns 0 for invalid input.
    """
    if not isinstance(text, str) or not text.strip():
        return 0

    try:
        credits = [int(value.strip()) for value in text.split(',')]

        if any(value < 0 for value in credits):
            return 0

        return sum(credits)

    except ValueError:
        return 0


def parse_student_record(line):
    """
    Parses 'SRN|name|status' into a dictionary.
    Returns None for invalid input.
    """
    if not isinstance(line, str):
        return None

    parts = line.split('|')

    if len(parts) != 3:
        return None

    srn, name, status = [part.strip() for part in parts]

    if not srn or not name or not status:
        return None

    return {
        "srn": srn.upper(),
        "name": name,
        "status": status.lower()
    }


def main():
    print("==== Running format_course_code ====")
    value = input("Enter a course code as DEPT NUMBER (e.g. cs 301): ")
    print("Formatted course code:", format_course_code(value))

    print("\n==== Running total_credits ====")
    value = input("Enter course credits separated by commas (e.g. 4,3,4): ")
    print("Total credits:", total_credits(value))

    print("\n==== Running parse_student_record ====")
    value = input("Enter a student record as SRN|name|status (e.g. pes1ug23cs001|Asha|regular): ")
    print("Student record:", parse_student_record(value))


if __name__ == "__main__":
    main()
