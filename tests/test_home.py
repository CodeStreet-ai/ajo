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
