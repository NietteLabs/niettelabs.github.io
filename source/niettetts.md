# O que é o projeto NietteTTS?

NietteTTS é um MotorTTS que usar Festival Speech Synthesis System para sintése de fala em Português Brasileiro (futuro novos idiomas) para Festival contanto com vozes construida usando FestVoz usando a sintése fala usando HMM com adições de scrips e modificações para sintése de alta qualidade.

## Modificações/Qualidades do NietteTTS

1. Fonemas em formato IPA:
Transcrições fóneticas de palavras retiradas da Wikipedia usando o projeto WikiPron, para obter atualidade e qualidade.
2. G2P melhorado:
Usando Phonetisaurus G2P para treinamento rápido e melhorado em comparação com LTS Rules (Árvore de Decisão) do Festival.
3. Extração de F0 (Pitch EstimatoR) usando REAPER:
Extração de F0 usando REAPER, sendo melhor que o SPTK-3.6 usado por padrão pelo projeto FestVox.
4. Extração de MCEP usando SPTK-4.3 e modificações de paramentros para extração.
5. Extração de STR usando SNACK (Baseando e usando script do MaryTTS).
6. Script diversos:
Scripts para instalação de ferramentas, extração de MCEP, STR, F0 e treinamento de modelo g2p e vocal

# Observações 
- O NietteTTS está sendo desenvolvindo apenas por uma pessoa (Pallas13) sendo esse projeto para Trabalho de Conclusão de Curso (TCC) do Curso Técnico em Desenvolvimento de Sistemas devido ao tempo, falta de recursos comp>
- Para as vozes serem usadas no Speech Dispatcher é necessario seguir passo a passo de instalação. O funcionamento é instavél.
