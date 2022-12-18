registro_funcionario = int(input('Digite o número do funcionário: '))
horas_trabalhadas = int(input('Digite o número de horas trabalhadas: '))
salario_hora = float(input('Digite o salário por hora: '))
 
resultado = horas_trabalhadas * salario_hora

print(f'NUMBER = {registro_funcionario}')
print(f'SALARY = U$ {resultado:.2f}')
