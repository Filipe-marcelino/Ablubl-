def atribuir_notas(alunos: list[str],
                  notas: list[int]) -> list[dict[str, int]]:
  atribuicao: list[dict[str, int]] = []
  for i in range(len(alunos)):
      d = {'aluno': alunos[i], 'nota': notas[i]}
      atribuicao.append(d)
  return atribuicao


d: dict[str,int] = {'idade' : 2}
#aqui se botar os tipos em discordancia o código roda, mas o vs reclama

alunos = ['Adriana', 'Bárbara', 'Caio', 'Dênis']
notas = [89, 57, 60, 28]
print(atribuir_notas(alunos, notas))


