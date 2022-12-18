nome_funcionario = str(input('Digite o nome do funcionário: '))
salario_fixo = float(input('Digite o salário fixo: '))
total_vendas = float(input('Digite o valor total de vendas efetuadas: '))

bonus = total_vendas * 0.15
total = salario_fixo + bonus

print(f'TOTAL = R$ {total:.2f}')
