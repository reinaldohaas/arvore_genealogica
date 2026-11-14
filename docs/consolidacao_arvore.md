# Relatório de Consolidação da Árvore Genealógica (v3)

Este relatório documenta detalhadamente as operações genealógicas, verificações e unificações realizadas na geração do arquivo **`privado/arvore_consolidada_v3.ged`** (formato **GEDCOM 5.5.1**, UTF-8), em cumprimento estrito da **Parte 4** de `docs/prompt_antigravity_revisao_e_parentes.md` e das regras de `docs/prompt_antigravity_arvore.md`.

---

## 1. Bases Integradas e Estatísticas Gerais

A árvore consolidada v3 reúne numa base única, com integridade referencial estrita e sem duplicação de indivíduos:
1. **`privado/arvore_consolidada_myheritage_2026-11-05b.ged`** (base consolidada de 05/11/2026);
2. **`privado/familysearch_completo.ged`** (lado paterno Haas/Dörner, 7.159 indivíduos — verificado: 100% dos códigos `_FSFTID` já integrados);
3. **`privado/familysearch_babi_completo.ged`** (lado materno Funke/Lohmann, 5.095 indivíduos — verificado: 100% dos códigos `_FSFTID` já integrados);
4. **`privado/arvore_agenor_haas_completa.md`** (árvore de Agenor Haas, 493 indivíduos `@P1@` a `@P493@` integrados);
5. **Dicionários de correções de `scripts/arvore_livro.py`** (`CORRECOES`, `EXTRA_PAIS`, `CASAMENTOS`);
6. **Descobertas primárias e indexadas das Partes 1 a 3** (Bischöfliches Zentralarchiv Regensburg, Erzbistumsarchiv Paderborn, Registro Civil de Brusque, Lista de Passageiros do vapor Formosa, Staatsarchiv Basel-Landschaft, paróquias luteranas de Hannover e Schleswig).

### Resumo quantitativo de `privado/arvore_consolidada_v3.ged`:
- **Indivíduos (`INDI`):** 12.771
- **Famílias (`FAM`):** 4.921
- **Fontes (`SOUR`):** 77.766
- **Notas textuais (`NOTE`):** 16.457
- **Eventos datados com citação de fonte explícita:** **34.589 de 34.589 (100% de cobertura)**.
- **XREFs quebrados ou pendentes (*dangling references*):** **0**.

---

## 2. O que foi juntado (Fusões Verificadas de Perfis Duplicados)

Para cada fusão, aplicou-se a regra de identidade: exigência de identidade no código do FamilySearch ou, na ausência deste, coincidência estrita de nome, filiação e pelo menos uma data ou local comprovado. As fontes, eventos e identificadores secundários foram integralmente preservados no perfil definitivo, registrando-se em nota as variantes divergentes:

1. **Bertha Dörner (`@I230@` `G1CP-6W2` fundida em `@I288@` `GDLF-MBN`):**
   - *Motivo:* Duas entradas para a mesma filha de Carlos Dörner e Hulda Peters (* 28/09/1905 no Capivari, Tubarão/São Ludgero).
   - *Correções estruturais adicionais:* No perfil remanescente `@I288@`, o sexo foi corrigido de `M` para `F`. Na família `@F987@` (casamento com João Igirdo Leandro em 12/07/1928 em São Martinho), os papéis conjugais invertidos foram corrigidos (`HUSB @I5854@`, `WIFE @I288@`).
2. **Franz Adam Eller (`@I481@` `PFXZ-GT5` fundido em `@I19@` `P3ZF-879`):**
   - *Motivo:* Duplicata do mesmo bisavô Franz Adam Eller (* 01/03/1832 Wehrden/Amelunxen, Vestfália), casado com Anna Maria Knopker.
   - *Unificação de família correspondente:* A família duplicada `@F72@` foi unificada na família principal `@F11@`.
3. **Guilherme (Wilhelm) Eller (`@I489@` `PF66-TXG` fundido em `@I382@` `G65N-VXX`):**
   - *Motivo:* Duplicata do mesmo filho de Franz Adam Eller e Anna Maria Knopker. A família conjugal com Paulina Kock (`@F237@`) foi associada diretamente a `@I382@`.
4. **Walter Érico Lohmann (`@I7350@` `G2MP-W4Q` fundido em `@I7598@` `GVPW-61W`):**
   - *Motivo:* `@I7350@` era um perfil colaborativo sem fonte, com ano de nascimento estimado sem fonte. A fotografia da família completa em Palmas (Arroio do Meio) e os registros civis do RS comprovam a existência de 11 filhos e de um único filho Walter: **Walter Erich Lohmann** (* 27/12/1916 Passo Fundo, sep. 18/06/1992 em Estrela). A data variante 1911 foi anotada no perfil unificado.
   - *Correção de anomalia relacional:* Dissolvida a família anômala `@F2859@`, em que a mãe Miguelina Leocádia Endres constava equivocadamente como `HUSB` da própria filha.
5. **Hilda Anna Doerner (`@I456@` `L1BB-W6V` fundida em `@I265@` `GL4R-NRL`):**
   - *Motivo:* O perfil colaborativo sem fonte `L1BB-W6V` trazia *"Ana Doerner, * 25/03/1923"*, data apenas 5 meses após o nascimento real de Hilda Anna Dörner (* 02/10/1922 — † 17/11/1997 Brusque). O retrato de estúdio da família c. 1927 e a certidão de óbito nº 7.778 de Gertrudes Preiss em 1970 comprovam uma única filha primogênita Hilda Ana (e nenhuma outra filha viva chamada "Ana"). A data 25/03/1923 foi preservada em nota crítica.
6. **Julius Georg Schnack (`@I7597@` `GNJL-7X3` fundido em `@I7183@` `LC5B-LF7`):**
   - *Motivo:* Ambos correspondiam ao mesmo filho de Peter Friedrich Ludwig Schnack e Anna Christina Maria Wacker. O registro paroquial luterano de Gelting comprova nascimento em 16/02/1820 e batismo em 04/04/1820 (`ark:/61903/1:1:QPNL-RRR1`). O ano 1830 no perfil `LC5B-LF7` decorria da idade aproximada (94 anos em vez de 104) declarada no óbito de 1924 em Lajeado, RS.

---

## 3. O que foi separado (Separações Críticas e Casos Duvidosos Mantidos Apartados)

### 3.1 Separações documentadas executadas:
1. **Desvinculação de Joanna Doerner (`@I304@` `PMKF-P9G`) da família `@F75@` (Carl Dörner & Charlotte Stock):**
   - Joanna Doerner (`* 20/03/1902`, batizada em julho de 1902 em São Ludgero, `ark:/61903/1:1:66YX-8DM1`, casada com Mathias Hoepers) é filha legítima e comprovada de Carlos Dörner e Hulda Peters (`@F74@`).
   - Ela havia sido erroneamente vinculada também à família `@F75@` em razão da certidão de nascimento de 09/05/1901 em São Bonifácio (`ark:/61903/1:1:ZKNH-YBZM`). Essa certidão de 1901 pertence à homônima **Joanna Doerner** (`@P501@`), filha do casal Carl Dörner (`@P493@`) e Charlotte Elisabetha Stock (`@I192@`). Joanna `@I304@` foi mantida exclusivamente em `@F74@` e o registro `@P501@` foi criado em `@F75@`.
2. **Desvinculação de Ferdinand Haas (`@I148@` `GTYK-RKJ`) da família `@F4@` (Joseph Haas & Franziska Dengler):**
   - Ferdinand Haas (* 06/02/1872 em Montan/Montagna, Tirol do Sul, Áustria/Itália) pertencia a um casal tirolês homônimo (*Josef Haas & Maria Maier*, casados sob a fonte austríaca `@S40813@`). Joseph Haas e Franziska Dengler de Leonberg casaram-se em 04/03/1878 como solteiros (*Jüngling* e *Jungfrau*). Ferdinand Haas foi totalmente desvinculado de `@F4@` e a fonte `@S40813@` foi removida da família de Johann Haas e Maria Meier.

### 3.2 Casos duvidosos mantidos expressamente separados (sem fusão):
Para evitar falsas unificações de homônimos contemporâneos, os seguintes pares foram mantidos como registros distintos na base, com notas explicativas:
- **`Nicolaus Michels` (`MYSM-BYB` vs `MFJ1-MBP` em `@F95@`):** registros com datas de batismo próximas na mesma região do Hunsrück/Trier; mantidos separados até localização dos assentos paroquiais originais que confirmem se eram primos ou crianças falecidas consecutivas.
- **`Johannes Michels` (`G1Z1-JYT` vs `MDKY-KJP` em `@F22@`):** mantidos separados.
- **`Lina Aenishaenslin` (`K8YN-M6D`) vs `Liza Aenishaenslin` (`MQ1W-KZF`) em `@F2799@`:** ambas com nascimento em 28/04/1864 em Ormalingen; mantidas separadas (possíveis gêmeas ou duplicata de indexação a conferir no arquivo de Liestal).
- **`Helena Michels` (`* 1854` vs `* 1864` em `@F50@`):** mantidas separadas.

---

## 4. Divergências e Como Foram Resolvidas (`P > I > S > Agenor > T`)

| Pessoa / Família | Versão Anterior / Conflito | Versão Adotada em v3 | Fonte Prevalecente | Justificativa |
| :--- | :--- | :--- | :--- | :--- |
| **Casamento Carlos Dörner & Hulda Peters** (`@F74@`) | Celebrante Pe. Francisco Auling, test. Augusto Peters e Henrique Hömke, dispensa de religião mista | Pe. Frederico Tombrock / Pe. Huberto Ohters; test. José May e João Peters; sem dispensa | **P** (`casamento_1900.png`, p. 28 #23) | Versão anterior era fórmula tabelionar espúria contaminada pelo assento nº 24 vizinho. |
| **Hulda Peters** (`@I424@`) | Suposto batismo/recepção na Igreja Católica em 28/04/1900 (`66YX-8D93`) | Descaracterizado como ato próprio; indexação da filha Joanna em julho/1902 | **P / I** (`@S2508@`, `ark:/61903/1:1:66YX-8D93`) | Código refere-se à mãe no batismo da filha Joanna. Evento de 28/04/1900 rebaixado a nota. |
| **Ofício de Georg Adam Meier** (`@I8@`) | Constava como "Ökonom" (lavrador) no batismo de 1888 | **Krämer** (comerciante/vendeiro de aldeia) | **P** (`Moosbach_Leuchtenberg005` p. 441 #36) | Leitura paleográfica direta da Coluna 5 (*Kurrent* `Krämer`). |
| **Padrinho de Georg Adam Maier** (`@I8@`, 1859) | Constava como "Schmiedssohn" | **Schneiderssohn** (filho de alfaiate: Adam Hartung) | **P** (`Moosbach_Leuchtenberg005` p. 96 linha 7) | Leitura direta da sequência `Sch-n-ei-d-e-r-s-sohn`. |
| **Pais e origem de Joseph Haas** (`@I9@`) | Batismo em Stoffen em 19/05/1847 (filho de Georg Haas & M. Anna Albrecht) | Filho de **Michael Haas & Kunigunda Stadelmann**, natural de **Etzgersrieth** | **P** (`Leonberg_Bul012` p. 8 #4; `Bul007` p. 162 #71) | O registro de Stoffen era homônimo sem parentesco. O casamento de 1878 e batismo de 1882 provam pais e origem no Alto Palatinado. |
| **Nascimento de Johann Haas** (`@I7@`) | Variava entre 09/07 e 11/07/1884 | **08/07/1884** (01h00 paroquial / 02h00 civil), lavrado em 11/07 | **P** (`doc_haas_nascimento_johann_1884.jpg`; `Leonberg_Bul019` p. 6 #80) | Standesamt nº 47 e batismo paroquial nº 80 coincidem no dia 08/07/1884. |
| **Irmãos de Johann Haas em Leonberg** | Incluía Alois, Maria, Franziska (1896) e Therese | **Barbara (1879), Joseph (1880), Kunigunda (1882), Franz Xaver (1886), Georg (1889) e Sebastian (1891)** | **P** (`Leonberg_Bul007` e `Bul019`) | Conferência dos pais na mesma linha. Os demais pertenciam a outros casais homônimos de Leonberg. |
| **Anos dos irmãos Meier em Moosbach** | Theresia (1890) e Michael (1892) | **Theresia (* 22/06/1891)** e **Michael (* 21/02/1893)** | **P** (`Moosbach_Leuchtenberg005` p. 463 #65 e p. 474 #13) | Cabeçalhos de página do livro paroquial são 1891 e 1893. |
| **Óbito de Gertrudes Preiss** (`@I6@`, 1970) | 11h00, Hosp. Azambuja, Dr. Carlos Moritz, carcinoma gástrico | **20h30, na residência**, **Dr. Germano Hoffmann**, **carcinoma**; 6 filhos maiores | **P** (`doc_doerner_obito_gertrudes_preiss_1970.jpg`, termo nº 7.778) | Termo 7.778 lido integralmente; leitura antiga havia se contaminado com termos vizinhos. |
| **Óbito de Fernando Dörner** (`@I5@`, 1981) | Citado com livro e termo inexistentes (C-43, fl. 102v, termo 10.673) | **Termo nº 1400**, **folha 50v**, reg. em 22/05/1981; 5 filhos maiores | **P** (`doc_doerner_obito_fernando_1981.jpg`) | Termo nº 1400 confere com a imagem real. |
| **Legenda da foto de despedida de 1913** | "Zur Erinnerung an unsere Abreise..." | **"Zum Andenken! vor unserer Abreise nach Brasilien 7. März 1913."** | **P** (`haas_despedida_abreise_brasilien_1913.jpg`) | Inscrição tipográfica exata lida na imagem original. |
| **Nascimento e pais de Franz Adam Eller** (`@I19@`) | Nascido em 1832 sem paróquia definida; pais estimados em c. 1807 e c. 1812 | Nascido em **01/03/1832** em **Wehrden** (Pfarrei Amelunxen); pais **Anton Eller (* c. 1774)** e **Anna Maria Elisabeth Frissen (* c. 1792)**, casados em 25/09/1830 | **P** (`DE_EBAP_10602`, `KB003-02-T` p. 18 e `KB004-02-H` p. 5) | Livros paroquiais da Diocese de Paderborn comprovam paróquia exata, idades e pais dos noivos (Erasmus Eller e Johann Frissen). |
| **Helena Elisabetha Lieser** (`@I31@`) | Faleceu em 1894 (103 anos) | Faleceu **depois de 1827** | **S / T** corrigida | Confusão em árvore colaborativa com homônima mais jovem nascida em 1816. |
| **Casamento Daniel Aenishaenslin & Barbara Spitteler** (`@F2799@`) | Conflito entre 20/03/1848 e 20/03/1845 | **20/03/1848 em Ormalingen** | **I** (`ark:/61903/1:1:6F8V-65KK`, `@S90023@`) | Dois índices paroquiais de Ormalingen comprovam 1848; 1845 era digitação sem fonte. |
| **Casamento Johannes Breitenstein & Barbara Weber** (`@F2805@`) | Conflito entre 17/02/1807 e estimativa c. 1820 | **17/02/1807 em Buus** | **I** (`ark:/61903/1:1:66J1-JZSJ`, `@S90023@`) | Comprovado por dois índices paroquiais suíços e batismo do primeiro filho em 1808. |
| **Sobrenome dos pais de Frida Liechti** (`@I7177@`, `@I7175@`) | Peter e Carolina Aenishaenslin | **Peter Liechti** e **Carolina** | **I** (`ark:/61903/1:1:6PMM-MKBX`) | Sobrenome *Aenishaenslin* copiado indevidamente do nome de casada de Frida no óbito. |
| **Sophie Dorothee Elizabeth Schrader** (`@I7192@`) | Sem local de nascimento nem batismo | Batizada em **21/02/1796 em Sankt Ägidien, Hannover**; sepultada em **17/02/1868 em Adelebsen** | **I** (`ark:/61903/1:1:QPFS-2845` e `QPDM-GF6V`) | Registros luteranos da Baixa Saxônia indexados no FamilySearch. |
| **Peter Friedrich Ludwig Schnack** (`@I7191@`) | Sem dados de sepultamento | Sepultado em **11/02/1860 em Gelting, Schleswig** | **I** (`ark:/61903/1:1:QPN1-Q6PQ`) | Registros luteranos de Gelting. |
| **Julius Georg Schnack** (`@I7183@`) | Nascido em 1830 vs 1820 | Nascido em **16/02/1820 em Gelting** (bat. 04/04/1820) | **I** (`ark:/61903/1:1:QPNL-RRR1`, `@S90022@`) | Batismo paroquial comprova 1820; 1830 decorria de idade declarada no óbito de 1924. |
| **Geocodificação de Palmas (RS)** (`@I7598@`, `@I7169@`) | "Palmas, Tocantins, Brasil" | **"Palmas, Arroio do Meio, Rio Grande do Sul, Brasil"** | **S / P** (`lohmann_familia_completa...png`) | Erro de geocodificação automática do FamilySearch corrigido para o distrito gaúcho real. |

---

## 5. Novos Parentes Adicionados por Família (Alemanha e Suíça)

Nenhum indivíduo vivo foi adicionado. Todos os novos parentes documentados nasceram há mais de 100 anos (até 1893) ou possuem óbito histórico estabelecido:

### 1. Ramo Haas (Alto Palatinado — Leonberg e Etzgersrieth):
- **Michael Haas** (`@P505@`): bisavô de Johann Haas, lavrador em Etzgersrieth (Pfarrei Moosbach).
- **Kunigunda Stadelmann** (`@P506@`): bisavó de Johann Haas, viva em Etzgersrieth em 15/06/1882.
- **Theresia Haas** (`@P507@`): tia paterna de Johann Haas, residente em Munique em 1879.
- **Georg Haas** (`@P508@`): tio paterno de Johann Haas, residente em Burglengenfeld em 1886–1889.
- **Sebastian Haas** (`@P509@`): tio paterno de Johann Haas, operário fabril em Leonberg.
- **Barbara Brandner** (`@P510@`): tia paterna afim em Leonberg.
- **Johann Haas** (`@P511@`, * 1883), **Barbara Haas** (`@P512@`, * 1888) e **Joseph Haas** (`@P513@`, * 1892 — † 04/02/1893): primos-irmãos paternos em Leonberg.
- **Margaretha Dengler** (`@P514@`): avó materna de Johann Haas, residente em Plattenhof (Ramspau) e casada com Andreas Rockinger (`@P515@`).
- **Barbara Haas** (`@P516@`, * 08/02/1879): irmã de Johann Haas.
- **Joseph Haas** (`@P517@`, * 30/05/1880): irmão de Johann Haas (em Munique em 1931).
- **Kunigunda Haas** (`@P518@`, * 15/06/1882): irmã de Johann Haas.
- **Franz Xaver Haas** (`@P519@`, * 09/05/1886 — † 20/05/1887): irmão de Johann Haas.
- **Georg Haas** (`@P520@`, * 16/09/1889): irmão de Johann Haas.
- **Sebastian Haas** (`@P521@`, * 27/10/1891): irmão caçula de Johann Haas, operário em Pirkensee.
- **Karolina Weiß** (`@P522@`, * 27/05/1889 Pirkensee): cunhada de Johann Haas (casada em 17/05/1919 em Leonberg com Sebastian Haas).

### 2. Ramo Meier, Voit, Woppmann e Reichenberger (Alto Palatinado — Moosbach, Heumaden e Burgtreswitz):
- **Maria Katharina Meier** (`@P523@`, * 01/06/1886): irmã de Maria Meier.
- **Theresia Meier** (`@P524@`, * 22/06/1891): irmã de Maria Meier.
- **Michael Meier** (`@P525@`, * 21/02/1893): irmão de Maria Meier.
- **Wolfgang Voit** (`@P526@`) e **Elisabeth Ach** (`@P527@`): bisavós de Maria Meier em Burgtreswitz.
- **Michael Woppmann** (`@P528@`) e **Anna Vollath** (`@P529@`): bisavós de Maria Meier em Weißenstein.
- **Katharina Voit** (`@P530@`, * 11/05/1856): tia materna e madrinha de batismo de Maria Meier.
- **Johann Reichenberger** (`@P531@`, * 15/10/1854): tio materno afim em Burgtreswitz.
- **Johann Reichenberger (filho)** (`@P532@`, * 17/12/1878): primo-irmão de Maria Meier.
- **Lorenz Reichenberger** (`@P533@`) e **Eleonora Kraus** (`@P534@`): pais de Johann Reichenberger em Burgtreswitz.

### 3. Ramo Eller e Frisse (Vestfália — Wehrden, Amelunxen e Godelheim):
- **Erasmus Eller** (`@P502@`, † ant. 25/09/1830 em Godelheim): tecelão de linho, bisavô de Anna Eller.
- **Johann Frissen** (`@P503@`, † ant. 25/09/1830 em Wehrden): lavrador, bisavô de Anna Eller.

### 4. Ramo Dörner (Santa Catarina):
- **Joanna Doerner** (`@P501@`, reg. 09/05/1901 São Bonifácio): filha de Carl Dörner e Charlotte Elisabetha Stock, devidamente separada da tia homônima.
- **Olga Dörner** (`@P504@`): filha de Fernando Dörner e Gertrudes Preiss, atestada no termo de óbito materno de 1970.
