
class CalculateInssAliquot:

    @staticmethod
    def execute(salary):
        if salary <= 1045:
            return salary * 0.075
        elif salary > 1045 and salary <= 2089.60:
            base_one = salary * 0.075
            base_two = (salary - 1045) * 0.09
            return base_one + base_two
        elif salary > 2089.60 and salary <= 3134.4:
            base_one = salary * 0.075
            base_two = (2089.60 - 1045) * 0.09
            base_three = (salary - 2089.60) * 0.12
            return base_one + base_two + base_three
        elif salary > 3134.4 and salary <= 6101.06:
            base_one = salary * 0.075
            base_two = (2089.60 - 1045) * 0.09
            base_three = (3134.4 - 2089.60) * 0.12
            base_four = (salary - 3134.4) * 0.14
            return base_one + base_two + base_three + base_four
        else:
            return 713.1
