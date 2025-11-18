# Usar vozes do NietteTTS com Speech Dispatcher
Fazer esse processo, possibilitar usar as vozes do NietteTTS não em modo interativo do Festival, usando em aplicativos que usam o Speech Dispatcher como leitor de tela ou PDFs.

```{admonition} Aviso
:class: caution
O funcionamento com Speech Dispatcher está em fase experimental, tenha cuidado ao usar as vozes do NietteTTS com Speech Dispatcher.
```

**Fontes:** 

[Página do Festival na wiki.archlinux.org](https://wiki.archlinux.org/title/Festival_(Portugu%C3%AAs))

[Página do Speech Dispatcher na wiki.archlinux.org](https://wiki.archlinux.org/title/Speech_dispatcher)

## Download da voz e do G2P

Siga esse tutorial de instalação das vozes do NietteTTS em: [Instalação](https://niettelabs.github.io/manual/instalacao/instalacao.html)

### Instale o módulo do Speech Dispatch Festival

```bash
sudo apt-get install speech-dispatcher-festival
```

### Instale a versão modificada do festival-freebsoft-utils

```bash
git clone https://github.com/NietteLabs/festival-freebsoft-utils
cd festival-freebsoft-utils
sudo cp *.scm /usr/share/festival 
```

## Para usar Festival com PulseAudio/Alsa
Edite o arquivo ```~/.festivalrc```

**PulseAudio:**
```scheme
(Parameter.set 'Audio_Required_Format 'aiff)
(Parameter.set 'Audio_Method 'Audio_Command)
(Parameter.set 'Audio_Command "paplay $FILE --client-name=Festival --stream-name=Speech")
```

**Alsa:**
```scheme
(Parameter.set 'Audio_Method 'Audio_Command)
(Parameter.set 'Audio_Command "aplay -q -c 1 -t raw -f s16 -r $SR $FILE")
```

## Adicione suporte ao Festival no Speech Dispatcher

## Abra o seguinte arquivo de configurações:

```bash
nano ~/.config/speech-dispatcher/speechd.conf
```

Procure e edite essa linha:

```linuxconfig
#AddModule "festival"
```

para:

```linuxconfig
AddModule "festival"
```

## Listar vozes instaladas

```{admonition} Observação
:class: note
Caso houver algum erro ao executar é necessario iniciar o Festival em modo servidor:
```bash
festival --server &
```

```bash
spd-say -L
```


