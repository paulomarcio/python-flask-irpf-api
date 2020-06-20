

class CalculateInssAliquot:

    @staticmethod
    def execute(salary):
        if salary <= 1830.29:
            return salary * 0.08
        elif salary > 1830.29 and salary <= 3050.52:
            return salary * 0.09
        else:
            return salary * 0.11
