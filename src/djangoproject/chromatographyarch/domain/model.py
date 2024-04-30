from datetime import date
from typing import List, Optional, Set


class DomainAnalyticalMethod:

    def __init__(self, method_name, method_description, sample_matrix, cost_per_sample):
        self.method_name = method_name
        self.method_description = method_description
        self.sample_matrix = sample_matrix
        self.cost_per_sample = cost_per_sample

    def __str__(self):
        return f"self.method_name"
