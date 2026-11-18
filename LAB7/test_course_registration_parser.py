
import pytest
from hypothesis import given, strategies as st

from course_registration_parser import (
    format_course_code,
    total_credits,
    parse_student_record
)


# HYPOTHESIS FUZZ TESTS

@given(st.text() | st.none())
def test_format_course_code_no_crash(s):
    try:
        format_course_code(s)
    except Exception as e:
        assert False, f"format_course_code crashed with: {e}"


@given(st.text() | st.none())
def test_total_credits_no_crash(s):
    try:
        total_credits(s)
    except Exception as e:
        assert False, f"total_credits crashed with: {e}"


@given(st.text() | st.none())
def test_parse_student_record_no_crash(s):
    try:
        parse_student_record(s)
    except Exception as e:
        assert False, f"parse_student_record crashed with: {e}"


# FUNCTIONAL TESTS

def test_valid_course_code():
    assert format_course_code("cs 301") == "CS301"


def test_invalid_course_code():
    assert format_course_code("") is None
    assert format_course_code(None) is None


def test_valid_total_credits():
    assert total_credits("4,3,4") == 11


def test_invalid_total_credits():
    assert total_credits("") == 0
    assert total_credits(None) == 0
    assert total_credits("4,abc,3") == 0


def test_valid_student_record():
    result = parse_student_record("pes1ug23cs001|Asha|REGULAR")

    assert result == {
        "srn": "PES1UG23CS001",
        "name": "Asha",
        "status": "regular"
    }


def test_invalid_student_record():
    assert parse_student_record("") is None
    assert parse_student_record(None) is None
    assert parse_student_record("SRN|Asha") is None
