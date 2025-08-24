# Usar vozes do NietteTTS com Speech Dispatcher
Fazer esse processo, permiter usar as vozes do NietteTTS forar do modo interativo do Festival, usando em aplicativos que usam o Speech Dispatcher como leitor de tela ou PDF's

**Fonte:** 
https://wiki.archlinux.org/title/Festival_(Portugu%C3%AAs)

https://wiki.archlinux.org/title/Speech_dispatcher

## Instalar as vozes no seu sistema (Baseado em Debian/Ubuntu)

### Exemplo para usar voz Ana.

```bash
sudo apt-get install ./ana.deb speech-dispatcher-festival
```

## Instalar versão modificado do festival-freebsoft-utils

```bash
git clone https://github.com/NietteLabs/festival-freebsoft-utils
cd festival-freebsoft-utils
sudo cp *.scm /usr/share/festival 
```

### Para usar Festival com PulseAudio/Alsa
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

## Adicionar suporte ao Festival ao Speech Dispatcher

### Abrar o seguinte arquivo de configuração:

```bash
nano ~/.config/speech-dispatcher/speechd.conf
```

Procure pela linha:

```
#AddModule "festival"
```

para:

```
AddModule "festival"
```

## Listar vozes instaladas

```bash
spd-say -L
```

Caso houver algum erro ao executar é necessario iniciar o Festival em modo servidor:

```bash
festival --server
```
