# Guia de Redação — *Nossa Família — Da Alemanha ao Sul do Brasil*

Documento de referência para escrever os capítulos. Ele resolve os conflitos entre as fontes e fixa o formato. Em caso de dúvida, **este guia prevalece sobre o roteiro**.

## 1. Fontes (ler antes de escrever)

| Fonte | Caminho |
| :--- | :--- |
| Roteiro (estrutura, beats) | `docs/roteiro_livro.md` |
| Árvore, datas, legendas de fotos | `README.md` |
| **Texto do centenário (Marise Haas Lourenço, 30/03/2013)** — tradição oral escrita, com erros; usar só como pergunta ou citação, nunca como fato | `livro/fontes/historia_joao_e_maria_marise_2013.txt` |
| **Hierarquia (decisão do autor, nov/2026):** documentos da época > planilha do Agenor > texto da Marise (tradição, com erros conhecidos). Nunca narrar como fato o que só a Marise diz. | — |
| Planilha do Agenor (só as notas dos patriarcas e da 1ª geração) | `privado/arvore_agenor_haas_completa.md` (local, fora do git) |
| GEDCOM (datas, lugares, notas de 1828/1847) | `arvore_familysearch.ged` |
| Acervo da internet (catálogo) | `docs/acervo_livros_e_fotos_internet.md` |
| Dossiês locais (Lohmann/CAPEF, Fazenda Lohmann, Funke, Natais de Joinville, Censo 1920, paleografia de Moosbach) | `C:\Users\haas\OneDrive\Documentos\familia_haas\livros_e_artigos_internet\0*.md` |

## 2. Voz, tom e formato

- **Língua:** português do Brasil, prosa literária de não-ficção. Nada de listas com marcadores no corpo do texto, nem negrito decorativo e emojis.
- **Narrador:** Reinaldo Haas, em 1ª pessoa, físico e meteorologista da UFSC. A voz é calorosa, precisa e com humor discreto. Ele pensa em massas de ar, retrotrajetórias, frentes e reanálises, e usa essas imagens com moderação: uma ou duas por capítulo, sem forçar.
- **Passado reconstituído:** em 3ª pessoa próxima, com o lugar e a data no início da seção, em itálico (*Heumaden, Alto Palatinado — abril de 1888*).
- **Honestidade:** o que não está documentado vem com marcas como "imagino", "é provável", "conta-se na família". **Não invente fatos no tempo presente** (encontros, conversas, visitas que não constam das fontes). Diálogos inventados só cabem em cenas históricas e devem ser poucos e curtos.
- **Extensão:** de 3.500 a 4.500 palavras por capítulo; o Prólogo e o Epílogo, de 2.000 a 3.000.
- **Formato do arquivo:** Pandoc Markdown, um arquivo por capítulo em `livro/capitulos/NN_nome.md`, começando com:

  ```markdown
  ## Capítulo N — Título {#cap-N}

  > *Epígrafe curta (opcional, de autoria própria ou de domínio público).*
  ```

  O Prólogo e o Epílogo usam `## Prólogo — Título {#prologo .unnumbered}` e `## Epílogo — Título {#epilogo .unnumbered}`.
- **Subseções:** use `###` com títulos curtos, entre 3 e 6 por capítulo.
- **Coordenadas:** logo abaixo do título, em uma linha, `*27,6° S · 49,4° O — Ituporanga, SC*` (valores aproximados vêm do GEDCOM ou do README).
- **Ficha do Arquivo:** onde houver documento, use um bloco cercado:

  ```markdown
  ::: ficha
  **Ficha do Arquivo** — Assento nº 47/1884, Standesamt Leonberg (hoje Maxhütte-Haidhof). Transcrição/tradução: …
  :::
  ```

- **Fotos:** só as listadas na seção 6, com o caminho `imagens/arquivo.jpg`:

  ```markdown
  ![Legenda completa em uma frase ou duas.](imagens/arquivo.jpg){width=85%}
  ```

  Deixe linha em branco antes e depois. Não use outras imagens.
- **Notas:** use notas de rodapé do Pandoc (`[^1]`) para fontes e ressalvas, com moderação.

## 3. Fatos canônicos e como tratar os conflitos

**Ramo Haas–Meier (1913)**
- Johann Haas nasceu em 11/07/1884, às 17h, em Sandberg/Leonberg (hoje Maxhütte-Haidhof), filho do operário Josef Haas (* 19/05/1847, Stoffen, Landsberg am Lech; filho de Georg Haas, *Ziegelknecht*, e de Maria Anna Albrecht) e de Franziska Dengler. A data vem do assento nº 47 de 13/07/1884. O Agenor anotou "08 de julho"; prevalece o registro civil.
- Maria Katharina Meier (Meyer) nasceu em 07/04/1888, às 2h, em Heumaden (paróquia de St. Peter und Paul, Moosbach), filha do *Ökonom* Georg Adam Meier (* 09/03/1859) e de Franziska Voit (* 29/06/1861). Os pais casaram em 23/11/1884. Foi batizada em 08/04/1888; a madrinha foi a tia Katharina Meier. A parteira foi a Sra. Glas.
- O casamento de Johann e Maria foi em 03/08/1907, em Eibenstock.
- No ofício, Johann vinha de família de pedreiros e se especializou em gesso (molduras de janelas, portais, altares). Era intérprete de dialetos. Maria ordenhava vacas por salário.
- As duas primeiras filhas, Hildegard (ou Hildegart) e Frida, morreram na Alemanha.
- **Foto de despedida:** *"Zum Andenken! vor unserer Abreise nach Brasilien, 7. März 1913"*.
- **Manifesto do *Formosa*** (lido diretamente no fac-símile): linhas 161–164 — Haas Johann, 28, casado; Haas Marie, 25, casada; Haas Luisa, 2; Haas Walter, 1. Constam como alemães, agricultores, procedentes de Marselha, 3ª classe. O documento está assinado "Rio, le 26 Mars 1913", com a nota "Le Nº 70 continue sur Santos. Restent 174 passagers".
- **Pós-chegada (versão do texto do centenário):** o desembarque no Rio foi recusado e o navio seguiu de porto em porto em quarentena. A família desembarcou em Laguna e foi para o Barracão dos Imigrantes, onde, seis dias depois, em 5 de maio, nasceu Gertrudes. Luisa e Walter não resistiram.
- **Conflito a narrar abertamente (não esconder):** a planilha do Agenor registra Gertrudes como nascida em 22/10/1911 na Alemanha. Registra também duas crianças, "Lina" e "Valter", nascidas e sepultadas em Rio do Ouro/Anitápolis. Além disso, diz que a família saiu em 13/03 e chegou ao Rio em 26/04/1913, e que "não foi encontrado o registro do desembarque em Florianópolis". O narrador trata isso como um enigma de investigador. O manifesto confirma Luisa (2) e Walter (1) a bordo e não lista nenhuma Gertrudes. O nome "Lina" pode ser Luisa, e o "Valter" da planilha pode ser o Walter. O lugar do sepultamento — Laguna ou Anitápolis — e a data de Gertrudes seguem abertos, à espera de registros paroquiais.
- Lote 17, Rio do Ouro (Anitápolis), comprado com um amigo; terra seca e ácida. Ali Johann fez túmulos em granilite com anjos de gesso. Nasceram Fernando (1915) e Alexandre (23/05/1917).
- Em 1918 a família foi para Ituporanga: aluguel no centro, depois terra em Rio Novo, mata derrubada a machado. Em Rio Novo nasceram Agnes/Inês (1920), Elza (1922), Baldoíno (20/04/1924) e Maria (1926). Depois vieram Águas Negras (por causa da escola) e João (1932), que morreu pequeno.
- Os Haas construíram em Ituporanga a Igreja Matriz, a Casa Paroquial, o Seminário Franciscano e a ampliação do Hospital das Irmãs. Fernando, Alexandre e Baldoíno aprenderam o ofício de pedreiro.
- Em 1939, Johann quis voltar à Alemanha e a guerra frustrou o plano. Em 1941–45 vieram as perseguições: o rádio no porão com um neto de vigia e a espingarda à mão. Em 1945, ajuda humanitária enviada à Alemanha. Use a formulação do texto do centenário sobre as torturas ("notícias de pessoas sendo torturadas… obrigadas a ingerir óleo") como **notícia que chegava à família**, não como fato verificado.
- Depois: Fernando, Gertrudes e Elza foram para o Paraná; Agnes e Maria, para Ribeirão das Pacas (Aurora); Baldoíno, para Vidal Ramos; Alexandre ficou em Ituporanga. Johann morreu em 19/03/1969 e Maria em 08/11/1973, ambos com 85 anos, e estão sepultados em Aurora, junto a túmulos feitos por ele.
- O centenário foi em 30/03/2013, com mais de 600 descendentes. Os sobrenomes aliados citados por Marise: Meyer (da Mota), Sebold (Tio Augusto), da Rosa (Tia Rosalina), Klettenberg (Tia Paula), Boeing (Tio João), Nagel (Tio Paulo), Doerner (Tia Adelina), Sautner (Tio Martin).
- Baldoíno Haas (20/04/1924–18/12/2013) e Adelina Doerner Haas (30/10/1926–22/02/2019) casaram em 1947 e fizeram Bodas de 65 anos em 2012. Reinaldo nasceu em 20/06/1965. Bárbara Funke Haas nasceu em 27/07/1972.
- Agenor Haas (n. 1943), engenheiro civil, é primo-irmão de Reinaldo, filho de Alexandre e Paula Klettenberg. A planilha dele tem 291 linhas: 11 filhos, 63 netos, 194 bisnetos, 109 trinetos e 55 notas.

**Ramo Doerner–Preiss–Michels–Arend–Loch–Eller–Peters:** veja o roteiro (Caps. 8–10) e o README. Pontos de atenção:
- A data de nascimento de Ignazia Loch, "1828, São Pedro de Alcântara", é anterior à fundação da colônia (1829). Trate como data aproximada e diga isso.
- Carlos Doerner teve 10 filhos com Anna Eller (Fernando é o caçula, de 24/08/1897) e 5 com Hulda Peters, com quem casou em 29/04/1900, em Capivari. O assento nº 23 inclui a dispensa de *religião mista*.

**Ramo Lohmann–Schnack–Endres–Hoeveler–Funke:** veja o roteiro (Caps. 11–12) e o README, que são detalhados. A Casa Lohmann fica em Palmas, Arroio do Meio, RS, na cota de 45 m, em frente ao Salto do Rio Taquari (lat −29,3303°, lon −51,9179°). O perfil topográfico do autor compara a casa com as cheias de 1941, 2023 e maio de 2024. A Fazenda Lohmann ficava em Roca Sales/Estrela, com 24 colônias compradas em 1870.

**Viagem de 2018:** Roma (24/01), Florença (28/01), Veneza (29/01), Maxhütte-Haidhof (06/02, Standesamt na Regensburger Straße 18, oficial Peter Henn) e Greenwich (16/02). Não há informação sobre o trecho de 30/01 a 05/02: não o detalhe. Narre que o sistema municipal mostrou um Haas nascido em Leonberg em 1941 vivendo na cidade, **sem nome, sem rua e sem inventar encontro**.

## 4. Enchentes — fatos que podem ser usados (sem exagerar a precisão)

- **Rio Tubarão, março de 1974:** a enchente de 24–25/03/1974 devastou Tubarão. É o maior desastre natural da história de SC até então; os números oficiais mais citados falam em cerca de 200 mortos e dezenas de milhares de desabrigados. Depois dela, o rio foi retificado e canalizado. Laguna fica na foz do Tubarão. Em 1973–74 havia La Niña: o clima não é destino.
- **Vale do Itajaí:** grandes cheias históricas em Blumenau em 1880 e 1911 (esta, dois anos antes da chegada dos Haas). Em julho de 1983, cerca de 15,3 m em Blumenau, num ano de El Niño forte (1982–83). Em agosto de 1984, cerca de 15,5 m. Em novembro de 2008, chuva persistente com fluxo de leste vindo do mar contra a serra, deslizamentos (Morro do Baú, Ilhota, Gaspar, Blumenau) e cerca de 135 mortes em SC. Em 2011, Rio do Sul. As barragens de contenção são a Oeste (Taió), a Sul (Ituporanga, rio Itajaí do Sul, anos 1970) e a Norte (José Boiteux, concluída em 1992). A Barragem Norte inundou parte da Terra Indígena Ibirama-Laklãnõ (Xokleng), um conflito ainda vivo. Brusque fica no Itajaí-Mirim, com cheias em 1984, 2008 e 2011. Ituporanga, Aurora e Vidal Ramos ficam no Alto Vale.
- **Taquari–Antas (RS):** a cheia de maio de 1941. Em setembro de 2023, um ciclone extratropical (4–5/09) causou mais de 50 mortes no Vale do Taquari, com Muçum, Roca Sales, Arroio do Meio e Lajeado devastados. Houve nova cheia em novembro de 2023. Em maio de 2024 veio a maior catástrofe climática do RS (cerca de 180 mortos no estado), com o Taquari batendo recordes em Lajeado e Estrela. Era ano de El Niño forte (2023–24). O README do autor menciona o pico de 12/05/2024 em Palmas.
- **Meteorologia comum:** jato de baixos níveis a leste dos Andes trazendo umidade da Amazônia, frentes semi-estacionárias, ciclones extratropicais e El Niño. As colônias foram assentadas junto aos rios — a água era estrada, energia e risco.
- **Ligação pessoal (pode ser dita):** o autor trabalha com modelagem de cheias, hidrologia e previsão (Itajaí, Taquari, HEC-RAS, WRF). Não detalhe projetos específicos.

## 5. Herança — temas comuns aos ramos

- **Direito de herança na Europa:** a partilha igualitária (*Realteilung*) do Hunsrück, do Mosela, da Renânia e do Palatinado retalhava a terra a cada geração e empurrava famílias para a emigração (Michels, Arend, Preis). Na Baviera antiga e na Vestfália dominava o herdeiro único (*Anerbenrecht*): os irmãos que não herdavam viravam oleiros, operários e emigrantes (Georg Haas, *Ziegelknecht*, e Josef Haas, operário da Maximilianshütte).
- **Nas colônias brasileiras:** o lote colonial (a "colônia", de cerca de 25 ha) e famílias de 10 a 15 filhos (Carlos Doerner teve 15; Francisco Lohmann, 12; Johann Haas, 11). Era comum um filho ficar com os pais e indenizar os irmãos, enquanto os demais partiam para novas frentes (Alto Vale, Oeste, Paraná). Ver a antropóloga Ellen F. Woortmann, *Herdeiros, parentes e compadres* (1995), sobre colonos do Sul. Os descendentes dos Haas se espalharam para o Paraná (Fernando, Gertrudes, Elza; Agenor em Londrina).
- **Heranças imateriais:** o ofício (o prumo e o gesso de Johann passando a filhos e netos pedreiros; as rodas de Heumaden; as lâminas de Solingen; o magistério de Vô Erno; a medicina do Dr. Carlos Heinz Funke); a fé (católicos Haas/Meier/Preiss/Michels; luteranos Doerner, Lohmann e Hoeveler; a dispensa de "religião mista" em 1900; o próprio casamento de famílias de confissões diferentes); a língua (perdida e reaprendida); os nomes (o *Leocádia* de Miguelina, que passou a Ilusca); o risco hídrico (casas e lotes à beira de rios que voltam a subir).
- **A herança como responsabilidade:** o repositório digital é o novo "lote" que se entrega aos filhos.

## 6. Fotos disponíveis por capítulo (todas em `imagens/`)

| Cap. | Arquivos e legendas-base |
| :--- | :--- |
| 2 | `foto_familia_johann_haas_e_maria_meyer.jpg` (Johann, Maria e os sete filhos criados em SC); `haas_bodas_de_ouro_fata_e_mota.jpg` (o Fata e a Mota nas Bodas de Ouro); `haas_primeiros_netos_do_fata.jpg` (os primeiros netos do Fata, acervo da família) |
| 3 | `haas_irmaos_reunidos.jpg` (irmãos Haas reunidos, acervo da família) |
| 4 | `batismo_joseph_haas_1847_stoffen.png` (batismo de Joseph Haas, Stoffen, 20/05/1847); `haas_familia_do_fata_alemanha.jpg` (a família do Fata na Alemanha, antes de 1913; identificação individual a confirmar); `meier_familia_da_mota_alemanha_casamento.jpg` (fotografia de casamento da família da Mota na Alemanha; identificação a confirmar); `meier_familia_da_mota_alemanha.jpg` (a família da Mota na Alemanha) |
| 5 | `haas_despedida_abreise_brasilien_1913.jpg` ("Zum Andenken! vor unserer Abreise nach Brasilien, 7. März 1913"); `doc_haas_navio_formosa_1913.jpg` (manifesto do *Formosa*, linhas 161–164) |
| 10 | `casamento_carlos_doerner_hulda_peters_1900.png`; `doc_doerner_obito_fernando_1981.jpg`; `doc_doerner_obito_gertrudes_preiss_1970.jpg` |
| 11 | `lohmann_4_geracoes_oma_rosita_ilusca_barbara_matheus.jpg`; `funke_oma_dora_7_irmaos_1983.jpg`; `funke_bisavo_e_familia_oma_dora.jpg`; `hoeveler_vo_erno_escola.jpg`; `lohmann_bisavo_francisco_e_bisavo_michelina.jpg` |
| 12 | `lohmann_familia_completa_palmas_arroio_do_meio.png`; `lohmann_casa_nova_palmas_arroio_do_meio.png`; `lohmann_visita_tio_arlindo_2012.jpg`; `lohmann_visita_tio_armando_2012.jpg`; `lohmann_visita_tio_urbano_2012.jpg`; `lohmann_visita_tia_sunta_2012.jpg` |
| 13 | `lohmann_perfil_topografico_enchente_2024_palmas.png` (perfil topográfico e hidrológico da Casa Lohmann frente às cheias de 1941, 2023 e 2024) |
| 16 | `doc_haas_nascimento_johann_1884.jpg` |
| 17 | `doc1_maria_meier_1888.jpg`; `doc2_trauung_meier_voit_1884.jpg`; `doc3_adam_meier_1859.jpg`; `doc4_franziska_voit_1861.jpg` |

## 7. Privacidade (obrigatório)

- Não publique endereços, telefones ou e-mails de ninguém.
- Não cite dados de descendentes vivos que constam da planilha do Agenor (só os nomes de filhos e cônjuges da 1ª geração, já falecidos ou históricos).
- Não nomeie o Haas de Leonberg nascido em 1941.
- Pessoas vivas da família próxima (Reinaldo, Bárbara, Matheus, Lucas, Ilusca, Katherine, Agenor, Marise) podem ser nomeadas como no roteiro, sem detalhes íntimos novos.

## 8. Estrutura final (19 capítulos; o 14, "O Fio do Tempo", sobre o clima, foi incluído em nov/2026)

| Arquivo | Conteúdo |
| :--- | :--- |
| `00_prologo.md` | Prólogo — As Coordenadas de Duas Vidas |
| `01`–`03` | Parte I — Ecos na Serra Catarinense (Vidal Ramos; Fata e Mota; primos-detetives) |
| `04`–`07` | Parte II — O Vapor *Formosa* e a Floresta |
| `08`–`10` | Parte III — Os Pioneiros de 1828, o Mosela e Solingen |
| `11`–`12` | Parte IV — Os Horizontes de Bárbara (Funke, Hoeveler, Lohmann, Schnack, Endres) |
| `13`–`14` | **Parte V — Três Rios e uma Herança** (NOVA): Cap. 13 "Três Rios, Uma Só Chuva" (Tubarão 1974, Itajaí 1880–2008, Taquari 1941–2024); Cap. 14 "O Que Se Herda" |
| `15`–`18` | Parte VI — Inverno na Baviera (Alpes; Standesamt; Heumaden e Moosbach; Greenwich) |
| `19_epilogo.md` | Epílogo — A Bússola Entregue a Matheus e Lucas |

As enchentes também aparecem **entrelaçadas** nos outros capítulos, com uma ou duas passagens curtas: Laguna e Tubarão no Cap. 5; Ituporanga e a Barragem Sul no Cap. 6; o Alto Vale e Aurora no Cap. 7 ou no Cap. 1; Brusque e o Itajaí-Mirim no Cap. 10; Roca Sales, Estrela e Arroio do Meio no Cap. 12.
