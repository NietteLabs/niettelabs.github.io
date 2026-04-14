# O que é o projeto Fest-TTS?

```{admonition} Observações
:class: dropdown
Fest-TTS, foi um projeto Trabalho de Conclusão de Curso (TCC) desenvolvido unicamente por uma pessoa. 
No futuro o código-fonte do Fest-TTS será organizada em conjuto com sua documentação para ser usado por outras pessoas para desenvolvimento do Fest-TTS e ao suporte de novo idiomas.
```

Fest-TTS é um MotorTTS (Text-To-Speech) que usar o software Festival Speech System para síntese de fala em Português Brasileiro (futuramente suporte a outros idiomas). Usasse o kit FestVoz para desenvolvimento das vozes com algumas modificações visando o melhorar a síntese.
As vozes são desenvolvidas usando a técnica de síntese baseada em HMM. 

## Modificações/Qualidades do Fest-TTS

1. Fonemas atualizadas: Transcrições usando projeto WikiPron, para obter confiabilidade e atualidade em termos de pronúncia das palavras. 
2. G2P melhorado:
	1. Usando Phonetisaurus G2P para treinamento rápido e melhorado em comparação com LTS Rules (Árvore de Decisão) do Festival.
3. Extração de Featutes melhorado:
	1. F0 (Freqüência Fundamental) usando REAPER: Trocando o uso do SPTK-3.6 para extração.
	2. MCEP usando SPTK-4.3 com modificações de parâmetros para melhor extração.
	3. STR usando SNACK (Usando script do MaryTTS como base).
4. Script diversos:
	1. Scripts para instalação de ferramentas, extração de MCEP, STR, F0 e treinamento de modelo g2p e vocal


# Monografia 

A monografia contendo informações de desenvolvimento, construção das vozes e outras informações está disponivél em [monografia.pdf](https://github.com/PallasSpeechSystem/Fest-TTS/blob/main/monografia.pdf).

