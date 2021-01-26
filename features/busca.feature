# language: pt

Funcionalidade: Hospedagens

Cenário: Busca por hospedagem em Manaus
    Dado que entrei no site do "Trivago"
    Quando digitar "Manaus" na barra de busca
        E clicar em "Manaus" na sugestão
        E clicar em "Aceitar" no pop-up de cookies
        E clicar em "Pesquisar"
        E e escolher o tipo "Avaliações e Sugestões"
    Então é apresentado o resultado das "Pesquisas"

Cenário: Validação de resultados
    Dado que clico tenho meu primeiro "resultado"
    Quando verifico as "Avaliações"
    Então verifico o primeiro "Valor" do primeiro da lista

