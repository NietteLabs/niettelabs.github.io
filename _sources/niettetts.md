# O que é o projeto NietteTTS?

```{admonition} Observações
:class: dropdown
NietteTTS, é um projeto para Trabalho de Conclusão de Curso (TCC) sendo desenvolvindo unicamente por uma pessoa. 
No futuro o código-fonte do NietteTTS será organizada em conjuto com sua documentação para ser usado por outras pessoas para desenvolvimento do NietteTTS e ao suporte de novo idiomas.
```

NietteTTS é um MotorTTS (Text-To-Speech) que usar o software Festival Speech System para síntese de fala em Português Brasileiro (futuramente suporte a outros idiomas). Usasse o kit FestVoz para desenvolvimento das vozes com algumas modificações visando o melhorar a síntese.
As vozes são desenvolvidas usando a técnica de síntese baseada em HMM. 

## Modificações/Qualidades do NietteTTS

1. Fonemas atualizadas: Transcrições usando projeto WikiPron, para obter confiabilidade e atualidade em termos de pronúncia das palavras. 
2. G2P melhorado:
Usando Phonetisaurus G2P para treinamento rápido e melhorado em comparação com LTS Rules (Árvore de Decisão) do Festival.
3. Extração de F0 (Pitch EstimatoR) usando REAPER: Trocando o uso do SPTK-3.6 para extração F0
4. Extração de MCEP usando SPTK-4.3 com modificações de parâmetros para melhor extração.
5. Extração de STR usando SNACK (Usando script do MaryTTS como base).
6. Script diversos:
Scripts para instalação de ferramentas, extração de MCEP, STR, F0 e treinamento de modelo g2p e vocal

## Logo
Imagem usada no logo:
<a href="https://www.flaticon.com/free-icons/speak" title="speak icons">Speak icons created by Voysla - Flaticon</a>
