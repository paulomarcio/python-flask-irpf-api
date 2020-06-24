
class CalculateInssAliquot:

    @staticmethod
    def execute(salary):
        if salary <= 1045:
            return salary * 0.075
        elif salary > 1045 and salary <= 2089.60:
            result_one = 1045 * 0.075
            result_two = (salary - 1045) * 0.09
            return result_one + result_two
        elif salary > 2089.60 and salary <= 3134.4:
            first_base = 1045
            second_base = 2089.60 - 1045
            third_base = salary - first_base - second_base

            result_one = first_base * 0.075
            result_two = second_base * 0.09
            result_three = third_base * 0.12
            return result_one + result_two + result_three
        elif salary > 3134.4 and salary <= 6101.06:
            first_base = 1045
            second_base = 2089.60 - 1045
            third_base = 3134.4 - first_base - second_base
            fourth_base = salary - first_base - second_base - third_base

            result_one = first_base * 0.075
            result_two = second_base * 0.09
            result_three = third_base * 0.12
            result_four = fourth_base * 0.14
            return result_one + result_two + result_three + result_four
        else:
            return 713.1
