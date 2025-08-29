# Usar vozes do NietteTTS com Speech Dispatcher
Fazer esse processo, permiter usar as vozes do NietteTTS forar do modo interativo do Festival, usando em aplicativos que usam o Speech Dispatcher como leitor de tela ou PDF's

```{admonition} Aviso
:class: caution
O funcionamento com Speech Dispatcher está em frase experimental, cuidado ao usar as vozes do NietteTTS com Speech Dispatcher.
```

**Fontes:** 

[Página do Festival na wiki.archlinux.org](https://wiki.archlinux.org/title/Festival_(Portugu%C3%AAs))

[Página do Speech Dispatcher na wiki.archlinux.org](https://wiki.archlinux.org/title/Speech_dispatcher)

## Downlaod da voz e do G2P

Siga ess tutorial de instalçao das vozes do NietteTTS em: [Instalação](https://niettelabs.github.io/manual/instalacao/instalacao.html)

### Instalar o módulo do Speech Dispatch Festival

```bash
sudo apt-get install speech-dispatcher-festival
```

### Instalar versão modificado do festival-freebsoft-utils

```bash
git clone https://github.com/NietteLabs/festival-freebsoft-utils
cd festival-freebsoft-utils
sudo cp *.scm /usr/share/festival 
```

## Para usar Festival com PulseAudio/Alsa
Edite o arquvivo ```~/.festivalrc```

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

## Adicionar suporte ao Festival no Speech Dispatcher

## Abrar o seguinte arquivo de configurações:

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


