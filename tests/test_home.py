import pytest
from hypothesis import given
from hypothesis.strategies import integers

from ajo.home.salary import Salary


@given(salary=integers(1500, 4000), mojo_goal=integers(10000, 30000))
def test_mojo_progress(salary, mojo_goal):
    """
    GIVEN provided salary and saving_name as arguments to saving_split
    WHEN saving_split is called
    THEN it should return portion of salary for saving_name
    """
    sal = Salary(salary=salary)
    assert sal.mojo_progress(mojo_goal) == 0 + (salary * 0.2 * 100) / mojo_goal


def test_salary():
    """
    GIVEN None is provided as argument to class Salary
    WHEN check_salary method is called
    THEN return 0
    """
    salary = Salary(None)
    assert salary.check_salary == 0


def test_missing_salary():
    """
    GIVEN No argument is provided to class Salary
    WHEN
    THEN Raise TyperError
    """
    with pytest.raises(TypeError, match=r"missing 1 required positional argument: 'salary'"):
        Salary()


def test_mojo_progress_against_none():
    """
    GIVEN None is provided as argument to class Salary
    WHEN mojo_progress is callled
    THEN return 0
    """
    sal = Salary(salary=None)
    mojo_goal = 10
    assert sal.mojo_progress(mojo_goal) == 0 + (0 * 0.2 * 100) / mojo_goal


def test_mojo_progress_against_string():
    """
    GIVEN String is provided as salary value to class Salary
    WHEN mojo_progress method is called
    THEN raise ValueError
    """
    sal = Salary("Ade")
    with pytest.raises(ValueError, match=r"salary can either be integer or float"):
        sal.mojo_progress(10)
