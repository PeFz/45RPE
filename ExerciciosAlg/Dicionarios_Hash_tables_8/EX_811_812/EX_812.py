import EX_811 as pt

class PatientDataBase:
    def __init__(self):
        self.patients = []

    def addPatient(self, paciente):
        if not isinstance(paciente, pt.PatientRecord):
            return False
        self.patients.append(paciente)
        return True

    def motivoBuscar(self, id, data):
        for p in self.patients:
            if p.id == id and p.data == data:
                return p.motivo
        return "Vazio"  # se não encontrar

    def prescricaoBuscar(self, id, data):
        for p in self.patients:
            if p.id == id and p.data == data:
                return p.tratamento
        return "Vazio"
