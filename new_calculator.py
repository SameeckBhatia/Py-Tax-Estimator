import pandas as pd
import numpy as np
from typing import Union


class Federal:

    def __init__(self, country: str, income: float) -> None:
        self.country = country
        self.income = income
