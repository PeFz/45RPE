'''
Considere um tipo de dado para registrar pacientes em uma centro de assistência médica. Cada registro
contém um identificador inteiro para o paciente, e strings para a data, motivo da visita e tratamento
prescrito. Projete e implemente a classe PatientRecord, sobrescrevendo o método __hash__. Escreva
um programa para testar essa classe
'''

class PatientRecord:
    def __init__(self, id,data, motivo, tratamento):
        self.id = id
        self.data = data
        self.motivo = motivo
        self.tratamento = tratamento

    def __hash__(self):
        return hash((self.id, self.data, self.motivo, self.tratamento))

    def __eq__(self, other):
        if not isinstance(other, PatientRecord):
            return False
        return (self.id == other.id and self.data == other.data and
                self.motivo == other.motivo and self.tratamento == other.tratamento)

    def __str__(self):
        return (f"Id: {self.id},"
                f" Data: {self.data},"
                f" Motivo: {self.motivo},"
                f" Tratamento: {self.tratamento}")

