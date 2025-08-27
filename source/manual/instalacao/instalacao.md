# Instalação das vozes do NietteTTS em seu sistema

Disponível apenas para sistema operativos (Debian/Ubuntu) ou que baseiam neles.

## Download das vozes

Vai em [releases do NietteTTS](https://github.com/NietteLabs/NietteTTS/releases), na versão recente e baixe uma das vozes disponíveis em .deb.

## Instalação da voz (Modo Gráfico)

Após escolher e baixar o arquivo da voz, apenas clique duas vezes para abrir sua loja de apps e clique em instalar, após isso ocorrerá a solitação de senha para fazer instalação.

## Instalação da voz (Modo Terminal)

Caso seu sistema não tiver um instalador .deb, é possivel fazer a instalação via terminal usado *apt*. 

**Abrar seu terminal e digite o seguite comando:**

```bash
sudo apt-get install ./(onde_sua_voz_deb_estar).deb
```

**Exemplo voz Paula está baixada em Download:**

```bash
sudo apt-get install ./Download/festival-pt-niettelabs-paula-cg.deb
```

Após executar um desses comandos, é necessario digitar a senha para fazer a instalação (na maioria dos casos).

## Usar as vozes no modo interativo (Festival)

**Para usar as vozes em modo interativo do Festival:**
Para iniciar Festival em modo interativo
```bash
festival
```

Para listar as vozes instaladas no Festival
```lisp
(voice.list)
```

**Quando aparacer sua voz instalada:**
Para listar as vozes instaladas no Festival
```lisp 
(voice_nome_completo_voz_que_escolher)
```

**Exemplo para voz Paula**
```lisp
(voice_niettelabs_pt_paula_cg) 
```

**Fazer a voz falar**
```lisp
(SayText "Seu texto Aqui")
```

## Observações
Caso houver aspas simples (') ou duplas ("), é necéssario colocar \ nelas para Festival conseguir ler

**Exemplo**
```lisp
(SayText "O Livro \"Pequeno Manual Anti-Transfobia\" de Júlia Klee")
```
