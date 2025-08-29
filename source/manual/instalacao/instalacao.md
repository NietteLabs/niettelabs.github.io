# Instalação das vozes do NietteTTS em seu sistema

Disponível apenas para sistema operativos (Debian/Ubuntu) ou que baseiam neles.

## Download das vozes

Vai em [releases do NietteTTS](https://github.com/NietteLabs/NietteTTS/releases), na versão recente e baixe uma das vozes disponíveis em .deb.

Vai em [releases do phonetisaurus-deb](https://github.com/NietteLabs/phonetisaurus-deb/releases/), na versão recente e baixe o pacote .deb da arquitetura da sua máquina.

### Como saber arquitectura da minha máquina (notebook/computador/outros)
Para saber sua arquitectura do sua máquina, basta digitar:
```bash
uname -m
```
| Saída do `uname -m`| arquitectura/arquivo |
| ------------------ | ---------------------|
| x86_64 | amd64.deb |
| armv7l | armhf.deb |
| aarch64 | arm64.deb |

## Instalação da voz (Modo Gráfico)

Após escolher e baixar o arquivo da voz e G2P, apenas clique duas vezes em cada arquivo .deb ara abrir sua loja de apps e clique em instalar, após isso ocorrerá a solitação de senha para fazer instalação.

## Instalação da voz (Modo Terminal)

Caso seu sistema não tiver um instalador .deb gráfico, é possivel fazer a instalação via terminal usado *apt*.

**Abrar seu terminal e digite o seguite comando:**

```bash
sudo apt-get install ./arquivo_da_sua_arquitetura.deb ./voz.deb
```

**Exemplo com amd64 (x86_64) e Voz Paula está na pasta download:**
```bash
sudo apt-get install ./Download/amd64.deb ./Download/festival-pt-niettelabs-paula-cg.deb
```

Após executar um desses comandos, é necessario digitar a senha para fazer a instalação (na maioria dos casos).

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


