
import pytest
from course_registration import can_register, waitlist_position, late_fee


# CAN_REGISTER: TEST BOTH OUTCOMES OF EVERY CONDITION

def test_valid_student_status():
    assert can_register("regular", 10, 3, True) == "registered"


def test_invalid_student_status():
    with pytest.raises(ValueError, match="unknown status"):
        can_register("invalid", 10, 3, True)


def test_positive_course_credits():
    assert can_register("regular", 10, 3, True) == "registered"


def test_zero_course_credits():
    with pytest.raises(ValueError, match="invalid course credits"):
        can_register("regular", 10, 0, True)


def test_prerequisites_false():
    assert can_register("regular", 10, 3, False) == "prerequisites missing"


def test_prerequisites_true():
    assert can_register("regular", 10, 3, True) == "registered"


def test_credit_limit_exceeded():
    assert can_register("regular", 22, 4, True) == "credit limit exceeded"


def test_credit_limit_not_exceeded():
    assert can_register("regular", 10, 3, True) == "registered"


# WAITLIST_POSITION: TEST BOTH OUTCOMES OF EVERY CONDITION

def test_invalid_capacity():
    with pytest.raises(ValueError, match="invalid capacity"):
        waitlist_position(10, 0, 2)


def test_valid_capacity():
    assert waitlist_position(10, 20, 0) == 0


def test_enrolled_below_capacity():
    assert waitlist_position(10, 20, 0) == 0


def test_enrolled_at_capacity():
    assert waitlist_position(20, 20, 3) == 4


def test_waitlist_length_at_limit():
    assert waitlist_position(20, 20, 10) == -1


def test_waitlist_length_below_limit():
    assert waitlist_position(20, 20, 3) == 4


# LATE_FEE: TEST BOTH OUTCOMES OF EVERY CONDITION

def test_zero_days_late():
    assert late_fee(0, 10, False) == 0


def test_positive_days_late():
    assert late_fee(5, 10, False) == 500


def test_waiver_enabled():
    assert late_fee(5, 10, True) == 0


def test_waiver_disabled():
    assert late_fee(5, 10, False) == 500


def test_late_fee_within_seven_days():
    assert late_fee(7, 10, False) == 500


def test_late_fee_after_seven_days():
    assert late_fee(10, 10, False) == 800


def test_credits_above_twenty():
    assert late_fee(5, 25, False) == 750


def test_credits_not_above_twenty():
    assert late_fee(5, 10, False) == 500


def test_fee_exceeds_maximum():
    assert late_fee(30, 25, False) == 2000


def test_fee_does_not_exceed_maximum():
    assert late_fee(5, 10, False) == 500
