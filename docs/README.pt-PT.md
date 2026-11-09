# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Todos os idiomas](../README.md#languages)

Game Localization é uma skill de agente para traduzir, editar e revisar textos de jogos no ChatGPT, no Codex e no Claude. Abrange menus, tutoriais, diálogos, legendas, textos de loja e documentação de projetos para Steam, PlayStation, Xbox e jogos para dispositivos móveis.

[Instalação](#instalação) · [Usar a skill](#usar-a-skill) · [Atualizar ou remover](#atualizar-ou-remover) · [Apoiar o autor](#apoiar-o-autor) · [Plano de desenvolvimento](../ROADMAP.md) · [Histórico de alterações](../CHANGELOG.md)

## Recursos

- Aplica a terminologia aprovada no projeto e registra novos termos como propostas.
- Preserva chaves de localização, marcadores como `{player_name}` e `%s`, tags, quebras de linha significativas e outros elementos protegidos.
- Verifica os limites de extensão e separa as traduções de dúvidas, correções da fonte e observações de controlo de qualidade.
- Oferece uma [seleção de 30 idiomas e variantes](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) e aceita listas personalizadas.
- Inclui um [glossário inicial de 75 termos nos 30 idiomas e variantes](../game-localization/references/glossary/README.md), com definições em inglês e propostas de tradução.

A skill contém instruções e referências. Funciona sem chave de API do projeto, conector ou serviço em segundo plano. A edição depende das ferramentas do chat. Antes do lançamento, verifique a interface na versão compilada do jogo e os textos da loja na pré-visualização da plataforma.

## Instalação

| Ambiente | Pacote |
| --- | --- |
| ChatGPT ou Codex com permissão para enviar plugins | [ZIP do plugin do ChatGPT](../packages/game-localization-chatgpt-v0.1.9.zip) |
| Claude ou espaços do ChatGPT habilitados para enviar skills independentes | [ZIP da skill independente](../packages/game-localization-skill-v0.1.9.zip) |
| Codex local ou Claude Code | [Instalar da pasta de origem](#instalação-local-com-um-comando) |

No GitHub, abra o link do pacote e escolha **Download raw file**. Envie o ZIP sem extrair.

### ChatGPT e Codex

1. Abra a opção de carregamento de plugins na versão web do ChatGPT. Proprietários e administradores autorizados podem usar **Admin console → Plugins → Add → Upload plugin**.
2. Selecione o ZIP do plugin. Após a validação, abra **Game Localization** em **Plugins** e escolha **Install plugin** se estiver disponível. Envios pessoais podem aparecer em **Personal → Created by me**.
3. Abra um novo chat no ChatGPT ou no Codex. Digite `@` e selecione **Game Localization**.

Se o espaço aceitar skills independentes, acesse **Plugins → Skills → Create → Upload from your computer** e envie o ZIP correspondente. Aguarde a análise e siga as instruções. As opções dependem da conta e do espaço de trabalho. [Guia de plugins da OpenAI](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Guia de skills da OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Ative **Code execution and file creation** nas definições do Claude se a conta ou o espaço exigir.
2. No Claude na Web ou no Claude Desktop, abra **Customize → Skills**. No layout novo, abra **Plugins** na barra lateral e procure os controlos em **Your plugins**.
3. Escolha **+ → Create skill → Upload a skill** e selecione o ZIP independente. Ative `game-localization` quando aparecer.
4. Abra um novo chat e peça ao Claude para usar **Game Localization**. Se aparecer em **+** ou **/** no campo da mensagem, selecione a skill ali.

Em espaços geridos, um administrador pode precisar ativar ou enviar as skills. [Guia de skills do Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nova barra lateral do Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Instalação local com um comando

Os comandos utilizam o ramo `main` de [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Funcionam depois de publicados o repositório e o ramo. As ligações relativas para os ZIP também funcionam noutros ramos, etiquetas e forks.

Em um chat local do Codex, selecione `$skill-installer` e envie a pedido abaixo. Autorize o acesso à rede se lhe for pedido e abra uma nova sessão. [Guia de skills do Codex](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

A Skills CLI de terceiros instala a mesma pasta para o Codex local e o Claude Code com um comando. Execute-o no projeto com Node.js 22.20 ou posterior. Mantenha as opções `-a` dos agentes desejados. Adicione `-g` para instalar ao nível do utilizador. [Referência da Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

No chat do terminal local do Claude Code, use a entrada do shell para instalar somente para o Claude. Verifique a URL do repositório antes de executar. [Entrada de shell no Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Em uma nova sessão, invoque `$game-localization` no Codex ou `/game-localization` no Claude Code. Para instalar manualmente no Claude Code, copie toda a pasta `game-localization/` para `.claude/skills/` no projeto ou `~/.claude/skills/` na sua pasta de utilizador. [Guia de skills do Claude Code](https://code.claude.com/docs/en/skills)

Nas versões alojadas do ChatGPT e do Claude, use os controlos de carregamento ou instalação da conta. Uma menção chama a skill instalada. Para compartilhar um link, publique no diretório da plataforma ou compartilhe a skill ou o plugin em um espaço compatível. [Compartilhamento de plugins do ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Compartilhamento de skills do Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Usar a skill

1. Anexe o texto ou ficheiro de origem e o glossário atual do projeto para os idiomas de destino. Se não houver glossário, peça explicitamente um rascunho.
2. Informe os idiomas de origem e destino, a plataforma, o tipo de conteúdo e o formato de saída. Inclua, quando fizer diferença, limites de caracteres, capturas de ecrã, notas sobre os falantes ou exemplos de variáveis.
3. Para folhas de cálculo, indique as colunas de origem e destino e solicite uma nova cópia. Para textos do jogo, informe chaves ou IDs estáveis. Para a loja, indique o campo e o limite obrigatório, se houver.
4. Consulte o relatório separado para saber se o resultado está pronto a usar ou ainda é um rascunho. O relatório apresenta separadamente a verificação do ficheiro, a revisão linguística e a verificação no jogo ou na pré-visualização da loja. Indica também o passo seguinte para cada questão pendente. Aprove os termos no glossário do projeto antes de os reutilizar.

Para a interface do jogo, o relatório de entrega inclui uma lista de verificações por prioridade, com o ecrã, o ID da cadeia, os passos para reproduzir o cenário e o critério de aceitação. Os valores longos das variáveis e o texto que possa ficar cortado vêm primeiro. Se o tipo de letra e a largura útil forem conhecidos, a competência pode estimar o espaço necessário. [Verificações no jogo](../game-localization/references/in-build-qa.md)

Use o [modelo de glossário do projeto](../game-localization/references/project-glossary-template.md) para separar os termos aprovados das propostas. Guarde o ficheiro atualizado e anexe-o à próxima conversa.

**Exemplo para folha de cálculo**

~~~text
Use Game Localization para traduzir a coluna ENGLISH da livro de cálculo em anexo para o alemão (de-DE). Escreva as traduções em GERMAN em uma nova cópia .xlsx. Use o glossário anexo e a coluna DESCRIPTION como contexto. Preserve as chaves, as colunas de origem, os marcadores e as tags. Liste separadamente as dúvidas de terminologia e as verificações com os IDs das linhas.
~~~

Nos ficheiros `.xlsx` compatíveis, indique a folha, a linha de cabeçalhos, a coluna com IDs estáveis, a coluna de origem e a coluna de destino existente. Com Python 3.9 ou posterior, a competência escreve as traduções por ID numa nova cópia e verifica se o resto do livro de cálculo foi preservado. Se não for possível verificar o livro, pode propor um CSV com IDs. [Instruções para Excel](../game-localization/references/xlsx-qa.md)

**Exemplo para página da loja**

~~~text
Use Game Localization para localizar esta descrição curta da Steam do inglês para o português do Brasil (pt-BR). Comece um rascunho de glossário, se necessário. Mantenha o título do jogo e respeite o limite de caracteres indicado. Entregue o texto da loja e um relatório separado.
~~~

### Verificar traduções em CSV

Para um CSV com IDs de linha estáveis, indique os cabeçalhos das colunas de ID, texto de origem e tradução. Se estiver disponível o Python 3.9 ou uma versão posterior, a skill compara o ficheiro de origem com o traduzido e assinala IDs em falta ou duplicados, traduções vazias, alterações a marcadores ou tags suportados e traduções que excedam os limites de extensão. [Instruções para verificar ficheiros CSV](../game-localization/references/csv-qa.md)

Experimente o [exemplo inicial com 12 linhas](../game-localization/examples/first-run/README.md), que inclui um rascunho de tradução, um glossário aprovado e um exemplo de relatório.

### As nossas definições dos modelos

| Ambiente | Modelo | Nível de raciocínio |
| --- | --- | --- |
| ChatGPT Work ou Codex | GPT-6.1 Sol | High ou superior, quando disponível |
| Claude | Claude Opus 5.5 | High ou superior, quando disponível |

**High+** é uma abreviação para High ou um nível superior disponível no cliente. Selecione o modelo e o nível no cliente. A skill funciona independentemente dessa preferência. [Definições dos modelos da OpenAI](https://learn.chatgpt.com/docs/models) · [Níveis de raciocínio do Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Atualizar ou remover

| Instalação | Atualizar | Remover |
| --- | --- | --- |
| Plugin do ChatGPT ou Codex | Se gere o carregamento, use **Upload new version** nos detalhes do plugin. Instalações de diretório ou espaço recebem atualizações dessa fonte. | Abra **Plugins → Installed → Game Localization** e escolha **Uninstall plugin** se disponível. Consulte o administrador sobre instalações geridas. |
| Skill independente do ChatGPT | Na área de gestão, substitua o carregamento pessoal pelo ZIP independente mais recente. | Abra **Plugins → Skills**, procure em **Installed** ou **Created by me** e use a opção de remoção disponível. Administradores gerem as skills do espaço. |
| Skill personalizada do Claude | Envie o novo ZIP independente pela área de gestão. Desative a versão anterior se surgir um segundo item. | Abra em **Customize → Skills** ou **Plugins** e desative. Se carregou o ficheiro, escolha **⋯ → Delete** e confirme. |
| Skill local instalada com Skills CLI | Execute `npx skills update game-localization` para um ramo seguido ou instale a partir da nova etiqueta. | Execute `npx skills remove game-localization` no mesmo projeto. Adicione `-g` se instalou globalmente. |
| Pasta local ou Codex Skill Installer | Substitua a pasta `game-localization/` pela versão mais recente. | Remova `game-localization/`. O Codex pode carregá-la de `.agents/skills/`, `~/.agents/skills/` ou `~/.codex/skills/`. O Claude Code usa `.claude/skills/` ou `~/.claude/skills/`. Inicie outra sessão se necessário. |

[Gestão de plugins da OpenAI](https://learn.chatgpt.com/docs/plugins) · [Gestão de skills personalizadas do Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Código-fonte e pacotes

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) define quando a skill é ativada e como processa um lote.
- [`game-localization/references/`](../game-localization/references/) contém as regras e as versões do glossário por idioma.
- [`packaging/chatgpt/`](../packaging/chatgpt/) contém o manifesto e o ícone do plugin.
- [`packages/`](../packages/) contém os ficheiros prontos para carregar.

Para reconstruir os dois ZIPs da mesma fonte, execute `python scripts/package.py` na raiz do repositório com Python 3.9 ou posterior. A versão é indicada no manifesto do plugin ChatGPT. Antes de distribuir, envie cada ZIP ao produto correspondente e teste um lote pequeno com glossário e marcador protegido.

## Licença

Game Localization está disponível sob a [licença MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Apoiar o autor

Se o Game Localization for útil à sua equipa, pode [apoiar Maled1kt através do DonationAlerts](https://www.donationalerts.com/r/maled1kt). Os donativos são inteiramente voluntários.
