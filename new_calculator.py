import pandas as pd
import numpy as np
from typing import Union


class Federal:

    def __init__(self, country: str, income: float) -> None:
        self.country = country
        self.income = income

    def standard_deduction(self) -> float:
        if self.country == "Canada":
            if self.income <= 173205:
                return 15705
            elif self.income >= 246752:
                return 14156
            else:
                return -0.02105 * (self.income - 173205) + 15705
        elif self.country == "United States":
            return 13850
        else:
            return 0
