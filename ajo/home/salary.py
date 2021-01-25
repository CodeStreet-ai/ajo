from dataclasses import dataclass
from typing import Union


@dataclass
class Salary:
    salary: Union[float, int]
    already_in_mojo: Union[float, int] = 0
    mojo: float = 0.2
    smile: float = 0.1
    maintenance: float = 0.1
    other: float = 0.6

    def mojo_progress(self, mojo_goal: Union[float, int]) -> float:
        """
        :param mojo_goal: Amount you are aiming to attain
        :return: Amount you currently have in your mojo account
        """
        mojo_percent = self.salary * self.mojo * 100
        return self.already_in_mojo + mojo_percent / mojo_goal
