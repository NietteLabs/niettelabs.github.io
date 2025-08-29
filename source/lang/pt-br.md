# Português Brasileiro

## Informações gerais
Fonemas: [Lista de Fonemas Usadas](https://github.com/CUNY-CL/wikipron/blob/master/data/phones/phones/por_bz_broad.phones), formato IPA retiradas do projeto WikiPron

Dicionario: [Dicionario](https://github.com/CUNY-CL/wikipron/blob/master/data/scrape/tsv/por_latn_bz_broad_filtered.tsv), fornecido pelo projeto WikiPron

Foi usando [REAPER](https://github.com/google/REAPER) para extração de F0 para extração de MCEP [SPTK-4.3](https://github.com/sp-nitech/SPTK). Na extração de MCEP foram usado como base o artigo [*Simple Methods for Improving Speaker-Similarity of HMM-Based Speech Synthesis - Junichi Yamagishi, Simon King*](https://www.cstr.ed.ac.uk/downloads/publications/2010/JunichiICASSP10.pdf) para valores de MCEP Order e Alpha para melhor extração para as vozes de 16hz e 44hz . Script para extração de STR do MaryTTS foi usando para extração de STR das vozes.

**Valores usados:**

| Sample Rate | MCEP Order | Alpha    |
| ----------- | ---------- | -------- |
| 16000hz     | 49         | 0.42     |
| 44000hz     | 68         | 0.713969 |

## Vozes

```{admonition} Observação sobre o calculo de MCD
:class: caution dropdown
O treinamento foi feito usado todo os áudios do corpus do falante, sem divisão para avaliação, para o calculo de MCD foi usado 10% dos áudios.

[Mais sobre o MCD](https://learnius.com/slp/9+Speech+Synthesis/1+Fundamental+Concepts/3+Evaluation/mel+cepstral+distortion+(MCD))
```

| Nome    | Corpus usando                                                    | Descrição                                                                                                                                                                                                                                                                                                                                                                                                             | MCD  |
| ------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Ana     | [CETUC](https://gitlab.com/fb-audio-corpora/alcaim16k-DVD1de4)   | O [Centro de Estudos em Telecomunicações (CETUC)](https://www.ctc.puc-rio.br/laboratorios-cetuc), através do Professor Doutor Abraham Alcaim, gentilmente cedeu ao LaPS, **para fins de pesquisa exclusivamente**, seu corpus de áudio para Português Brasileiro. Esse corpus, é composto por áudios de 1.000 sentenças, gravados por 101 locutores, totalizando aproximadamente 143 horas de áudio. Locutor ID: F050 | 3.80 |
| Paula   | [CETUC](https://gitlab.com/fb-audio-corpora/alcaim16k-DVD1de4)   | O [Centro de Estudos em Telecomunicações (CETUC)](https://www.ctc.puc-rio.br/laboratorios-cetuc), através do Professor Doutor Abraham Alcaim, gentilmente cedeu ao LaPS, **para fins de pesquisa exclusivamente**, seu corpus de áudio para Português Brasileiro. Esse corpus, é composto por áudios de 1.000 sentenças, gravados por 101 locutores, totalizando aproximadamente 143 horas de áudio. Locutor ID: F000 | 3.90 |
| Pieroni | [THLS](https://gitlab.com/lfelipesv/1000-sentences-thls-dataset) | Open Source Brazilian Portuguese Speech Dataset with 1000 sentences balanced phonetically. (Feito downgrade de 48hz para 44hz)                                                                                                                                                                                                                                                                                        | 3.72 |

```{admonition} Sobre MCD
:class: tip
MCD - Mel Cepstral Distortion (MCD), foi gerado comparado similaridade dos áudios gerados (sintetizados) com os áudios usando para treinamento de voz. 
<br>
**MCD <= 0 - Perfeito**;
<br>
**MCD <= 1 - Muito bom**;
<br>
**MCD <= 2 - Bom**;
<br>
**MCD <= 3 - Médiano**;
<br>
**MCD <= 4 - Ruím**;
<br>
**MDD >= 5 - Muito Rúim**;
```

## Amostras
**Texto 1:** 

> Pequeno Manual Anti-Transfobia<br>
> Prefácio: A Dor que Ensina e a Inspiração que Guia<br>
> Por Júlia Klee<br>
> Este livro nasce de uma necessidade urgente e de uma profunda
> admiração. A urgência vem da minha própria trajetória, marcada pela dor
> da transfobia em sua forma mais íntima e dilacerante. Durante muito
> tempo, a transfobia era para mim um conceito distante, uma palavra
> carregada de um peso que eu não compreendia em sua totalidade,
> embora soubesse de sua existência e de sua capacidade de ferir e matar. A
> real dimensão dessa violência só me atingiu de forma visceral quando a
> vivenciei na pele, vinda de quem eu menos esperava: minha própria mãe.
> A ameaça velada, o medo em seus olhos apenas pelo fato de eu ser quem
> eu sou, Júlia, uma mulher trans, rasgou em mim uma ferida que ainda
> lateja. Foi nesse momento de dor profunda que a transfobia deixou de ser
> uma abstração e se tornou uma realidade palpável, uma força opressora
> que tenta nos anular, nos silenciar, nos apagar do mundo.<br>
> ***[Pequeno Manual Anti-Transfobia - Por Júlia Klee](https://loja.uiclap.com/titulo/ua99785/)***

| Voz     | Audio                                                                                                                                                     |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ana     | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/ana/livro.wav" type="audio/wave"><br></audio>     |
| Paula   | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/paula/livro.wav" type="audio/wave"><br></audio>   |
| Pieroni | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/pieroni/livro.wav" type="audio/wave"><br></audio> |


**Texto 2:**
> Hoje, na janela, brilha o Sol<br>
> E mesmo assim, estou tão triste<br>
> Pois não sei como vai ser<br>
> Eu sem você<br>
> Essa noite, quase nem dormi<br>
> Só em pensar<br>
> Que fomos tão felizes, e como vai ser<br>
> Eu sem você<br>
> Você vai embora, e meus sonhos vão contigo<br>
> Me esquecerás, me esquecerás<br>
> Sei que vou perder um grande amor e um bom amigo<br>
> Me diga, então, como vai ser<br>
> Eu sem você, eu sem você<br>
> Sei que não adianta mais pensar<br>
> No que passou<br>
> Não vai ser fácil porque sei que vou sofrer<br>
> Eu sem você<br>
> Essa noite, quase nem dormi<br>
> Só em pensar<br>
> Que fomos tão felizes, e como vai ser<br>
> Eu sem você<br>
> Você vai embora, e meus sonhos vão contigo<br>
> Me esquecerás, me esquecerás<br>
> Sei que vou perder um grande amor e um bom amigo<br>
> Me diga, então, como vai ser<br>
> Eu sem você, eu sem você<br>
> Você vai embora, e meus sonhos vão contigo<br>
> Me esquecerás, me esquecerás<br>
> Sei que vou perder um grande amor e um bom amigo<br>
> Me diga, então, como vai ser<br>
> Você vai embora, e meus sonhos vão contigo<br>
> Me esquecerás, me esquecerás<br>
> Sei que vou perder um grande amor e um bom amigo<br>
> Me diga, então, como vai ser<br>
> Você vai embora, e meus sonhos vão contigo<br>
> Me esquecerás, me esquecerás<br>
> Sei que vou perder um grande amor e um bom amigo<br>
> Me diga, então, como vai sofrer<br>
> ***Eu Sem Você (Por Que Te Vás) - Lílian***

| Voz     | Audio                                                                                                                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ana     | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/ana/musica.wav" type="audio/wave"><br></audio>     |
| Paula   | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/paula/musica.wav" type="audio/wave"><br></audio>   |
| Pieroni | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/pieroni/musica.wav" type="audio/wave"><br></audio> |

**Texto 3:**
> Eu sempre penso em ti.<br>
> Eu sempre amarei a ti.<br>
> Sempre aqui para ti.<br>
> <br>
> Sinto saudades de ti em todos os dias.<br>
> Quero está em seus braços, ao seu corpo quente.<br>
> Quero vê-la você todos os dias.<br>
> Quero ouvir sua bela voz em meus ouvidos.<br>
> Você é uma das pessoas mais belas que conheci.<br>
> Você é bondosa.<br>
> é corajosa.<br>
> é consciente.<br>
> Você é uma raridade nesse mundo que vivemos.<br>
> Perdão aos meus erros.<br>
> Eu sempre estou a tentar melhorar o meu ser, para ti e para mim.<br>
> Eu suporto o sofrimento dessa realidade em minha mente.<br>
> O sofrimento mental é doloroso de sentir.<br>
> Junto com o grande cansaço e tristeza.<br>
> Mas com tudo isso, estou de pé para conseguir nossa felicidade.<br>
> Você é uma razão da minha vivencia.<br>
> O meu objetivo de viver com ti é a força é o que energizar o meu corpo.<br>
> Eu desejo do fundo do meu coração e da minha mente;<br>
> Que você consiga realizar os seus sonhos;<br>
> Que consiga, combate a escuridão em nossa realidade.<br>
> Que tenha a mente forte que habita em ti.<br>
>Todos os momentos, eu estarei aqui.<br>
> Eu irei ao seu alcance para ter ajudar.<br>
>Sempre te amarei e estarei contigo.<br>
> Eu te amor do fundo do meu coração.<br>
> ***Texto feito pela Pallas para sua amada Niette***

| Voz     | Audio                                                                                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ana     | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/ana/amor_niette_05-11-24.wav" type="audio/wave"><br></audio>     |
| Paula   | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/paula/amor_niette_05-11-24.wav" type="audio/wave"><br></audio>   |
| Pieroni | <audio controls><br><source src="https://github.com/NietteLabs/NietteTTS/raw/refs/heads/main/samples/pt/pieroni/amor_niette_05-11-24.wav" type="audio/wave"><br></audio> |
