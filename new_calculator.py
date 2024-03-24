import pandas as pd
import numpy as np
from typing import Union


class Federal:

    def __init__(self, country: str, income: float) -> None:
        self.country = country
        self.income = income
        self.name = country
        self.data = "federal_brackets.csv"

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

        for index, row in df.iterrows():
            if self.taxable_income() in range(row["low"], row["high"]):
                base_tax += row["rate"] * (self.taxable_income() - row["low"])
                base_tax += row["total_below"]

        return base_tax

    def additional_tax(self) -> Union[int, float]:

        if self.name == "Canada":
            cpp = 0.0595 * (self.income - 3500)
            ei = 0.0166 * self.income
            return cpp + ei
