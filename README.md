# Simulação de Urna Eletrônica em Python

Este projeto consiste em uma simulação de urna eletrônica desenvolvida em Python, criada como parte de um projeto integrador do curso de Análise e Desenvolvimento de Sistemas. O objetivo é demonstrar o funcionamento de um sistema de votação eletrônica, permitindo o registro de votos para prefeito e vereador, além da apuração dos resultados.

## Funcionalidades

-   **Zerésima:** Exibe a lista de candidatos com 0 votos, demonstrando que a votação ainda não foi iniciada.
-   **Votação para Prefeito e Vereador:** Permite aos usuários registrarem seus votos para candidatos a prefeito e vereador.
-   **Validação de Votos:** Verifica se o número do candidato digitado é válido, exibindo mensagens de erro para números inválidos.
-   **Confirmação de Voto:** Solicita a confirmação do voto antes de registrá-lo.
-   **Apuração dos Resultados:** Calcula e exibe o número de votos de cada candidato, além de determinar os vencedores para prefeito e vereador.
-   **Votos em Branco e Nulos:** Permite registrar votos em branco e nulos.
-   **Votações multiplas:** Permite que vários votos sejam computados, até que o usuário decida finalizar a votação.

## Pré-requisitos

-   Python 3.x instalado

## Como Executar

1.  Clone este repositório:

    ```bash
    git clone [https://github.com/EricaPMello/urna-eletronica-python.git](https://github.com/EricaPMello/urna-eletronica-python.git)
    ```

2.  Navegue até o diretório do projeto:

    ```bash
    cd urna-eletronica-python
    ```

3.  Execute o script principal:

    ```bash
    python main.py
    ```

## Instruções de Uso

1.  Ao iniciar o programa, você terá duas opções:
    -   Digite `1` para imprimir a zerésima.
    -   Digite `2` para iniciar a votação.
2.  Se escolher iniciar a votação, siga as instruções na tela para votar em prefeito e vereador.
3.  Digite o número do candidato desejado e confirme seu voto.
4.  Após registrar os votos, você pode continuar votando ou finalizar a votação.
5.  Ao finalizar a votação, o programa exibirá os resultados com o número de votos de cada candidato e os vencedores.

## Estrutura do Código

-   O código utiliza dicionários (`candidatos_prefeito`, `candidatos_vereador`) para armazenar os candidatos e seus números correspondentes.
-   Dicionários (`votos_prefeito`, `votos_vereador`) são usados para contabilizar os votos de cada candidato.
-   Funções (`votar_prefeito`, `votar_vereador`, `apurar_resultados`) organizam o fluxo de votação e apuração.
-   Loops `while` garantem a repetição da votação até que o usuário decida finalizar.

## Tecnologias Utilizadas

-   Python 3.x

## Status do Projeto

Concluído como parte de um projeto integrador do curso de Análise e Desenvolvimento de Sistemas.

## Contato

Linkedin: https://www.linkedin.com/in/erica-mello-dev/

## Informações Adicionais

Este projeto foi desenvolvido como um exercício prático para aplicar os conhecimentos adquiridos durante o curso de Análise e Desenvolvimento de Sistemas. Ele demonstra a implementação de um sistema de votação eletrônica de forma didática e funcional.
