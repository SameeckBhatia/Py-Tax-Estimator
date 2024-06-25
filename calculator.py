from typing import Union

import numpy as np
import pandas as pd

no_tax_states = ["Florida", "Texas", "Not Scotland"]
flat_tax_states = {"Georgia": 0.0549, "Illinois": 0.0495, "Michigan": 0.0425,
                   "North Carolina": 0.0475, "Pennsylvania": 0.0307}


class Federal:
    """
    This class calculates federal tax liability based on income and country
    of residence.

    >>> canada = Federal("Canada", 50000)
    >>> canada.base_tax()
    5144.25
    >>> canada.additional_tax()
    3596.75
    >>> canada.total_tax()
    8741.0
    """

    country: str
    income: Union[int, float]
    name: str
    data: str

    def __init__(self, country: str, income: Union[int, float]) -> None:
        self.country = country
        self.income = (income if income > 0 else 0)
        self.name = country
        self.data = "brackets/federal_brackets.csv"

    def standard_deduction(self) -> float:
        if self.country == "Canada":
            if self.income <= 173205:
                return 15705
            elif self.income >= 246752:
                return 14156
            else:
                return -0.02105 * (self.income - 173205) + 15705
        elif self.country == "United Kingdom":
            if self.income <= 100000:
                return 12570
            elif self.income <= 125140:
                return -0.5 * (self.income - 100000) + 12570
            else:
                return 0
        elif self.country == "United States":
            return 14600
        else:
            return 0

    def taxable_income(self) -> Union[int, float]:
        if self.income > self.standard_deduction():
            return self.income - self.standard_deduction()
        else:
            return 0

    def base_tax(self) -> float:
        df = pd.read_csv(self.data)
        df = df[df["name"] == self.name].reset_index(drop=True)

        df["high"] = np.array(list(df["low"][1:]) + [0])

        below = [0]
        below += [row["rate"] * (row["high"] - row["low"])
                  for index, row in df[:-1].iterrows()]

        df["total_below"] = pd.Series(below).cumsum()

        base_tax = 0
        income = int(self.taxable_income())

        for index, row in df.iterrows():
            if (income in range(row["low"], row["high"])) or \
                    (income >= row["low"] and index == len(df) - 1):
                base_tax += row["rate"] * (income - row["low"])
                base_tax += row["total_below"]

        return base_tax

    def additional_tax(self) -> Union[int, float]:
        if self.name == "Canada":
            cpp = 0.0595 * (self.income - 3500 if self.income > 3500 else 0)
            ei = 0.0166 * self.income
            return cpp + ei
        elif self.name == "United Kingdom":
            ni = 0
            if int(7 * self.income / 365) in range(242, 967):
                ni += 0.08 * self.taxable_income()
            elif int(7 * self.income / 365) >= 967:
                ni += 0.02 * (self.income - 50422.14) + 3024.29
            return ni
        elif self.name == "United States":
            ssa = 0.062 * self.income if self.income < 168600 else 0.062 * 168600
            medicare = 0.0145 * self.income
            return ssa + medicare
        else:
            return 0

    def total_tax(self):
        return self.base_tax() + self.additional_tax()


class State(Federal):
    """
    This class calculates state/province tax liability based on income and
    state/province of residence. Inherits from the Federal class.

    >>> ontario = State("Canada", "Ontario", 50000)
    >>> ontario.base_tax()
    1731.8975
    >>> ontario.additional_tax()
    0
    >>> ontario.total_tax()
    1731.8975
    """

    state: str

    def __init__(self, country: str, state: str,
                 income: Union[int, float]) -> None:
        super().__init__(country, income)
        self.name = state
        self.data = "brackets/state_brackets.csv"

    def base_tax(self):
        if self.name in no_tax_states:
            return 0
        elif self.name in flat_tax_states:
            return flat_tax_states[self.name] * self.taxable_income()
        else:
            return super().base_tax()
