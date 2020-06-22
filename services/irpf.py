

class CalculateIrpf:

    @staticmethod
    def execute(salary, inss, dependents):
        aliquot = 0
        value = 0
        total = 0
        dependents = dependents * 189.59

        if salary <= 1903.98:
            aliquot = 0
            value = 0
        elif salary > 1903.98 and salary <= 2826.65:
            aliquot = 0.075
            value = 142.8
        elif salary > 2826.65 and salary <= 3751.05:
            aliquot = 0.15
            value = 354.80
        elif salary > 3751.05 and salary <= 4664.68:
            aliquot = 0.225
            value = 636.13
        else:
            aliquot = 0.275
            value = 869.36

        irpf_base_value = (salary - inss) - dependents
        irpf_aliquot_value = (irpf_base_value * aliquot)
        total = irpf_aliquot_value - value

        return {
            'value': float("{0:.2f}".format(value)),
            'aliquot': float("{0:.2f}".format(aliquot * 100)),
            'dependents': float("{0:.2f}".format(dependents)),
            'total': float("{0:.2f}".format(total))
        }
