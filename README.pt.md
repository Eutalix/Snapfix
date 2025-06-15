# Snapfix

Snapfix é uma ferramenta para organizar automaticamente as entradas `.desktop` de aplicativos Snap no menu do usuário. 

---

## Visão Geral

* **O que faz**: detecta snaps instalados, cria/atualiza arquivos `.desktop` em `~/.local/share/applications/`, corrige categorias, resolve ícones e adiciona ação de desinstalação via Polkit (`pkexec snap remove`).
* **Distribuição**: fornecida como binário/autônomo pronto para download em Releases do GitHub.
* **Objetivo**: permitir que o usuário organize aplicativos Snap no Linux Mint automaticamnte.

---

## Download do Binário

1. Faça download com:

    ```bash
    wget "https://github.com/Eutalix/Snapfix/releases/download/v1.0/snapfix"
    ```
    
    ou baixe o arquivo na página [Releases](https://github.com/Eutalix/snapfix/releases)

3. Salve o arquivo em um diretório de sua preferência, por exemplo `~/snapfix` ou `~/bin`.

---

## Tornar Executável

Após o download, torne o arquivo executável:

```bash
chmod +x ~/snapfix
```

---

## Adicionar ao PATH via bashrc (opcional)

Para facilitar o uso, você pode adicionar o local do binário ao seu `PATH` editando o arquivo `~/.bashrc` (ou `~/.zshrc`, conforme shell). Por exemplo, se você salvou o executável em `~/snapfix`, adicione:

```bash
# Snapfix
export PATH="$HOME/snapfix:$PATH"
```

Ou, se renomeou e salvou em `~/bin` como `snapfix`:

```bash
# Snapfix
export PATH="$HOME/bin:$PATH"
```

Depois de editar, recarregue o bashrc:

```bash
source ~/.bashrc
```

### Adicionar automaticamente via comando

Se preferir, use um único comando para adicionar ao final do `~/.bashrc`. Por exemplo, para o executável em `~/snapfix`:

```bash
echo 'export PATH="$HOME/snapfix:$PATH"' >> ~/.bashrc
```

Ou, se estiver em `~/bin/snapfix`:

```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
```

E recarregue:

```bash
source ~/.bashrc
```

Agora basta chamar `snapfix` de qualquer lugar:

```bash
snapfix --help
```

## Execução Básica

Abra um terminal e chame o binário diretamente:



* `--auto`: executa em loop contínuo (padrão a cada 300s).
* `--force`: força recriar entradas existentes.
* `--debug`: logs detalhados.
* `--background`: inicia em background (roda `--auto` em subprocesso).
* `--autostart`: configura execução automática ao inicializar o sistema (cria arquivo em `~/.config/autostart`).
* `--version`: exibe versão.

### Exemplos

* **Ajuda**

  ```bash
  ~/snapfix --help
  ```

  Você verá a ajuda.

* **Executar uma vez (manual)**:

  ```bash
  ~/snapfix
  ```

  Atualiza/cria entradas `.desktop` para snaps atualmente instalados.

* **Executar com debug**:

  ```bash
  ~/snapfix --debug
  ```

  Mostra logs de quais snaps foram processados, ícones resolvidos, entradas puladas, etc.

* **Forçar recriação**:

  ```bash
  ~/snapfix --force
  ```

  Recria todas as entradas, mesmo as já existentes.

* **Modo contínuo**:

  ```bash
  ~/snapfix --auto
  ```

  Executa repetidamente a cada intervalo (padrão 300 segundos).

* **Modo background**:

  ```bash
  ~/snapfix --background
  ```

  Retorna ao terminal e roda em segundo plano.

* **Configurar autostart**:

  ```bash
  ~/snapfix --autostart
  ```

  No próximo login, Snapfix rodará automaticamente em segundo plano.

---

## Configuração Opcional

Embora o executável venha com configurações padrão, é possível usar um arquivo de configuração JSON em `~/.config/snapfix/config.json` para ajustar filtros e intervalos:

### Exemplo de `~/.config/snapfix/config.json`

```json
{
  "skip_patterns": ["url-handler", "show-updates"],
  "skip_name_patterns": ["Show Updates", "URL Handler"],
  "freedesktop_categories": {"CustomRaw": "Utility"},
  "mapping": {"CustomRaw": "Utility"},
  "loop_interval": 600
}
```

* Crie a pasta se não existir:

  ```bash
  mkdir -p ~/.config/snapfix
  ```
* Edite ou crie o arquivo JSON com as opções desejadas.
* Execute o binário normalmente: ele detecta e carrega essa configuração.
* Caso queira usar config em outro local, use flag `--config`:

  ```bash
  ~/snapfix --config /caminho/outro/config.json
  ```

---

## Integração com o Menu

* Após execução, as entradas `.desktop` são criadas em `~/.local/share/applications/`.
* Abra seu menu de aplicativos (ex.: GNOME, KDE, Cinnamon) e verifique se os apps Snap aparecem corretamente com ícone e categoria.
* Para desinstalar via menu, clique com o botão direito no ícone e use a ação “Desinstalar” adicionada. Se não aparecer, use terminal: `snap remove <snap_name>`.

---

## Remoção Completa

* Para parar execução contínua: mate o processo em background (`ps aux | grep snapfix`, `kill <pid>`).
* Para remover config:

  ```bash
  rm -rf ~/.config/snapfix
  ```
* Para remover entradas `.desktop` criadas, remova manualmente de `~/.local/share/applications/` arquivos iniciados com nome de snaps indesejados.
* Para remover binário: exclua o arquivo executável copiado em `~/` ou outro local.

---

## Contato e Suporte

* Para bugs ou dúvidas, acesse a página de [Issues](https://github.com/Eutalix/snapfix/issues)
