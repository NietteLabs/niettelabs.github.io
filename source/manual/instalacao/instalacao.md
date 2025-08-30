# Instalação das vozes do NietteTTS em seu sistema

Disponível somente para sistemas operacionais (Debian/Ubuntu) ou que baseiam neles.

## Download das vozes

Navegue em [releases do NietteTTS](https://github.com/NietteLabs/NietteTTS/releases), na versão recente e baixe uma das vozes disponíveis em .deb.

Navegue em [releases do phonetisaurus-deb](https://github.com/NietteLabs/phonetisaurus-deb/releases/), na versão recente e baixe o pacote .deb da arquitetura da sua máquina.

### Como saber arquitetura da minha máquina (notebook/computador/outros)
Para saber sua arquitetura da sua máquina, basta digitar:
```bash
uname -m
```
| Saída do `uname -m`| arquitetura/arquivo |
| ------------------ | ---------------------|
| x86_64 | amd64.deb |
| armv7l | armhf.deb |
| aarch64 | arm64.deb |

## Instalação da voz (Modo Gráfico)

Após escolher e baixar o arquivo da voz e G2P, clique duas vezes em cada arquivo .deb ara abrir sua loja de aplicativos e clique em instalar, após isso ocorrerá a solicitação de senha para fazer instalação.

## Instalação da voz (Modo Terminal)

Caso seu sistema não tiver um instalador .deb gráfico, é possível fazer a instalação via terminal usado *apt*.

**Abrar seu terminal e digite o seguinte comando:**

```bash
sudo apt-get install ./arquivo_da_sua_arquitetura.deb ./voz.deb
```

**Exemplo com amd64 (x86_64) e Voz Paula está na pasta download:**
```bash
sudo apt-get install ./Download/amd64.deb ./Download/festival-pt-niettelabs-paula-cg.deb
```

Após executar um desses comandos, é necessário digitar a senha para fazer a instalação (é geralmente solicitado).

## Usar as vozes no modo interativo (Festival)
Para iniciar Festival em modo interativo:
```bash
festival
```

Para listar as vozes instaladas no Festival:
```scheme
(voice.list)
```

Selecionar voz:
```scheme
(voice_nome_completo_voz_que_escolheu)
```

### Exemplo
Usar a voz Paula para sintetizar texto:
```scheme
(voice_niettelabs_pt_paula_cg) 
```

Sintetizar fala a partir um texto:
```scheme
(SayText "Seu texto Aqui")
```

```{admonition} Dica
:class: tip
Caso houver aspas simples (') ou duplas ("), é necéssario colocar \ nelas para Festival conseguir ler.

**Exemplo de texto com aspas duplas:**

```scheme
(SayText "O Livro \"Pequeno Manual Anti-Transfobia\" de Júlia Klee")
```


