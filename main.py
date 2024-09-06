def verifica_letra_a(string):
  # Converte a string para minúsculas para tratar 'a' e 'A' de forma unificada
  string_minuscula = string.lower()

  # Conta quantas vezes a letra 'a' aparece na string
  contagem_a = string_minuscula.count('a')

  # Verifica se a letra 'a' aparece na string
  if contagem_a > 0:
      return f"A letra 'a' aparece {contagem_a} vezes na string."
  else:
      return "A letra 'a' não aparece na string."

# Exemplo: String definida no código
string_informada = "Ana Carolina adora aprender linguagens de programação."

# Alternativamente, você pode solicitar a entrada do usuário descomentando a linha abaixo
# string_informada = input("Informe uma string: ")

# Chama a função e imprime o resultado
print(verifica_letra_a(string_informada))
