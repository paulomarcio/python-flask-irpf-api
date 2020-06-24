from flask_restful import Resource, reqparse

from services.inss import CalculateInssAliquot
from services.irpf import CalculateIrpf

class Irpf(Resource):
    def post(self):
        body = reqparse.RequestParser()
        body.add_argument('name')
        body.add_argument('salary')
        body.add_argument('dependents')

        data = body.parse_args()

        name = data['name']
        salary = float(data['salary'])
        dependents = int(data['dependents'])
        inss = CalculateInssAliquot.execute(salary)
        irpf = CalculateIrpf.execute(salary, inss, dependents)

        return {'aliquota': irpf['aliquot'], 'parcela': irpf['value'], 'inss': float("{0:.2f}".format(inss)), 'dependentes': irpf['dependents'], 'irpf': irpf['total']}
