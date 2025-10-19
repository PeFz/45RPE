import EX_811 as Paciente
import EX_812 as DataBase


# Programa de teste para a classe PatientRecord
def main():
    # Criando alguns registros de pacientes (usando a classe dentro de Paciente)
    p1 = Paciente.PatientRecord(1,  "2025-10-19", "Dor de cabeça", "Analgésico")
    p2 = Paciente.PatientRecord(2, "2025-10-19", "Gripe", "Antigripal")
    p3 = Paciente.PatientRecord(1, "2025-10-19", "Dor de cabeça", "Analgésico")

    print("=== Registros Criados ===")
    print(p1)
    print(p2)
    print(p3)
    print()

    # Testando igualdade
    print("=== Teste de Igualdade ===")
    print("p1 == p2:", p1 == p2)  # False
    print("p1 == p3:", p1 == p3)  # True
    print()

    # Testando hash
    print("=== Teste de Hash ===")
    print("hash(p1):", hash(p1))
    print("hash(p3):", hash(p3))  # Igual ao hash(p1)
    print()

    # Testando uso em um conjunto (simulando armazenamento em um DataBase)
    print("=== Inserindo no DataBase ===")
    pacientes = DataBase.PatientDataBase()
    pacientes.addPatient(p1)
    pacientes.addPatient(p2)
    pacientes.addPatient(p3)  # p1 e p3 são iguais → não duplica

    print(pacientes.motivoBuscar(1, "2025-10-19" ))
    print(pacientes.prescricaoBuscar(1, "2025-10-19"))

if __name__ == "__main__":
    main()
