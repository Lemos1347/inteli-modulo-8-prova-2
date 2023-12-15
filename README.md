# Inteli módulo 8 prova 2
Este repositório contém os códigos para a seguinte atividade:

> [!NOTE]
> Em um mundo onde a tecnologia é uma ferramenta chave para inclusão e acessibilidade, surge a necessidade de soluções inovadoras para auxiliar pessoas com desafios na comunicação verbal, como aqueles com condições que limitam a fala. Uma instituição sem fins lucrativos cujo objetivo é melhorar a qualidade de vida de indivíduos acometidos por essa limitação contratou-o como um consultor de tecnologia. Sua tarefa é montar uma prova de conceito de uma aplicação que utiliza arquiteturas modernas de aprendizado profundo como ferramenta de sintetização de voz, potencialmente agindo como uma ponte valiosa para a comunicação, permitindo que pessoas com desafios na fala, incluindo aquelas no espectro autista, se expressem de maneira mais eficaz em seu cotidiano. Para tal, deve-se desenvolver: Uma interface de terminal. O usuário deve ser capaz de inserir frases para sintetização de forma contínua, sem precisar reinicializar a aplicação cada vez que precisar inserir uma frase. Integração com um modelo de machine learning capaz de sintetização de fala. (Lembre-se que a API da OpenAI está bloqueada durante o período de prova) Reprodução do áudio gerado pelo modelo de sintetização de fala.

## Sobre os arquivos

Nesse repositório você encontrará um arquivo python que é uma aplicação de terminal que integra funcionalidades de text-to-speech. O objetivo é digitar palavras no terminal, e transformá-lo em um novo arquivo de áudio. Além disso, há um arquivo de audio de teste (caso queira ver o resultado sem rodar o programa).

## Como executar

> [!IMPORTANT]
> Para executar os códigos é necessário ter o Python 3.6 ou superior instalado em sua máquina.

Para instalar e executar este projeto, siga estas etapas:

1. Clone o repositório:

   ```
   git clone https://github.com/Lemos1347/inteli-modulo-8-prova-2.git
   ```

2. Navegue até o diretório do projeto:

   ```
   cd inteli-modulo-8-prova-2
   ```

3. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

Por fim, execute o seguinte comando no terminal:

```
python3 main.py
```

Você será guiado por um menu interativo para gerar o seu audio.
