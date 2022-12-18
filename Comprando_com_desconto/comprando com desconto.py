preco_mercadoria = float(input('Digite o valor da mercadoria: '))

quantidade_mercadoria = int(input('Digite a quantidade de mercadoria: '))

preco_total = quantidade_mercadoria * preco_mercadoria

desconto = preco_total * 0.1

desconto_quantidade = quantidade_mercadoria * 0.01

desconto_total1 = desconto + desconto_quantidade

desconto_total = preco_mercadoria - desconto_total1

print(f"Total: R$ {preco_total:.2f}")

print(f"Total com deconto: R$ {desconto_total:.2f}")
