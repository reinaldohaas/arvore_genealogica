# Levantamento de falhas — livro *Nossa Família* e árvore genealógica

## Reconferência de 05/11/2026

Feita sobre o commit `dc20bb0` e a cópia de trabalho do mesmo dia, que tem alterações ainda não commitadas (`00_prologo`, `09_matriarca_arend`, `22_mapas_e_arvores`, `scripts/arvore_livro.py`). Nesta seção, os números de linha valem para o estado atual. Nas seções 0 a 6, abaixo, os números e os nomes de arquivo são os de 04/11; vários capítulos mudaram de número desde então.

Desta vez abri também as imagens que faltavam: os três batismos (Josef, Georg Adam, Franziska), o de Maria, o assento 23/1900 e os dois óbitos de Brusque. Os capítulos foram rechecados por busca nos pontos de cada item, não relidos por inteiro. O capítulo novo `14_o_fio_do_clima.md` e a maior parte das respostas do Antigravity não foram auditados.

### A. Falhas novas ou ainda não listadas

| # | O que está errado | Onde | Como resolver | Prior. |
|---|---|---|---|---|
| R1 | **Endereço da planilha privada no GEDCOM público.** A nota de Alexandre traz rua, número e CEP, e a nota de Paula diz com qual filha viva ela morava. O mesmo texto está nos dois GEDCOM, já publicados em `origin/main`. Não há número de telefone. | `arvore_familysearch.ged:3858–3862`; o mesmo trecho em `arvore_consolidada_myheritage.ged` | Tirar as notas e decidir se o histórico do git também deve ser limpo. | **A** |
| R2 | **Descendentes possivelmente vivos no GEDCOM público.** Dos 699 indivíduos, 476 não têm nascimento nem óbito, a maioria vinda da planilha. Sem data, não dá para excluir menores. O cap. 3 diz que dos vivos fala "apenas em números". Nomes e anos respeitam a regra pedida, mas o arquivo também pode ter ido para o MyHeritage. | `arvore_familysearch.ged`; `arvore_consolidada_myheritage.ged`; cap. 3 | Decisão do autor: publicar uma versão sem esses nomes e manter a completa em `privado/`. | **A** |
| R3 | **O batismo de Josef Haas continua errado no cap. 4.** A imagem diz nascimento em *19 Mai, früh 7 Uhr*, e batismo também em 19 de maio. O cap. 4 diz "no dia seguinte, 20 de maio". O README e o cap. 17 já foram corrigidos, então o livro agora se contradiz. | `04_antes_da_partida.md:35`, `:38`, `:41` | Corrigir para 19/05. | **A** |
| R4 | **Dados deduzidos entraram no GEDCOM como se fossem fatos.** Hildegart e Frida têm nascimento em Eibenstock, c. 1908 e c. 1909, enquanto o cap. 4:97 diz que as datas não são conhecidas e 4:137 sugere Chemnitz. O lugar de nascimento de Ignazia é "Travessia da Renânia…". Anna Eller tem "Amelunxen… (ou São Bonifácio)", enquanto o cap. 21:37 diz que falta o batismo. Falta conferir a origem de cada um; o cap. 21:13 avisa que as respostas do Antigravity são só "mapa de pistas". | `arvore_familysearch.ged:409`, `:775`; registros de Hildegart e Frida (`@I354@`) | Deixar em branco ou marcar como hipótese o que não tiver fonte. | **A** |
| R5 | **"Ökonom" na página 441 pode ser má leitura.** Ampliada, a palavra não me parece *Ökonom*: começa com algo como K e lembra *Krämer* (comerciante). Não tenho certeza. Se for outra palavra, caem a "mudança de ofício" e o argumento sobre a herança. | `18_heumaden_moosbach.md:43`, `:52`, `:91`; `04_antes_da_partida.md:15`; `15_o_que_se_herda.md:19`; `README.md:146` | Segunda leitura por paleógrafo ou fórum de *Kurrent*, comparando com outros registros da mesma mão. | M |
| R6 | **Padrinho e pároco do batismo de Josef.** O README lê *Joseph Burkhart* e *Bernhard Müller*. Na imagem leio algo mais próximo de *Lienhart* e *Leonhard*, sem segurança. | `README.md:261` | Segunda leitura. | B |
| R7 | **Pessoas fictícias no GEDCOM**: "Filho(a) 3 Hoeveler" e "Filho(a) 4 Hoeveler". | `arvore_familysearch.ged`, família `@F17@` | Remover ou obter os nomes reais. | M |
| R8 | **Notas contraditórias nos registros de Luisa e Walter.** O registro traz "nasceu em Anitápolis" e "nasceu no Brasil" ao lado de "listado no *Formosa*". Os nomes principais ainda são Lina e Valter. | `arvore_familysearch.ged`, registros de Lina e Valter | Usar Luisa e Walter como nome principal e tirar a frase da planilha. | M |
| R9 | **O README se contradiz sobre o túmulo de Gertrudes.** A linha 142 diz Parque da Saudade; a linha 231 e a certidão de 1970 dizem cemitério católico. | `README.md:142` | Corrigir para cemitério católico. | M |
| R10 | **Diagrama e quadro do README desatualizados no ramo Funke.** Ainda aparecem "Família Funke & Oma Dora Funke" e "& esposo", embora o GEDCOM já traga Oscar Martin Funke e Dora Marta Aenishaenslin. | `README.md:113`, `:144` | Atualizar pelo GEDCOM, conferindo as fontes. | M |

### B. O que foi resolvido

| Item | Situação |
|---|---|
| 0.1 | README corrigido nos três batismos e no casamento de Moosbach. Conferi as imagens: Maria (07/04, Reichenberger), Georg Adam (09/03, Hartung) e Franziska (29/06, Margaretha Albrecht) estão certos. |
| 0.3 | O autor confirmou: Marise é sua irmã mais nova. Texto corrigido nos caps. 1, 2, 3, 4 e 16; em 3:119, a pergunta aos filhos agora os manda perguntar a ela, que é tia deles. |
| 0.7 | GEDCOM ampliado para 699 pessoas, com o lado de Bárbara e os colaterais. Ver R1, R2, R4, R7 e R8. |
| 1.1, 1.2 | Johann nascido em 11/07/1884; imigração datada em 26/03/1913. |
| 1.2 da tabela de filhos | Gertrudes: o README não diz mais 1911; o batismo em Teresópolis (23/11/1913) entrou no cap. 5. Luisa e Walter: livro corrigido. |
| Baldoíno | Local de nascimento corrigido no GEDCOM. |
| 2.1, 2.2, 2.11 | Carlos Doerner e Anna Eller estão declarados em `21_nota_fontes.md:35–37`. |
| 2.9 | "Bisneta da matriarca" foi retirado. |
| 2.12 | Morte de Gertrudes em 09/04/1970 no GEDCOM. |
| 2.14 | Mudança para Vidal Ramos (1927) e Brusque (1964) incluída, com base no *Jornal Mirim*: é memória de família, não documento. |
| 2.16 | Os irmãos de Adelina estão no cap. 10. Conferi a certidão de 1970, com uma ressalva: o nome que o livro lê como *Olga* me pareceu *Telga*; o GEDCOM traz Olga. |
| 3.11 | Ascendentes Funke identificados no GEDCOM e citados em `11_oma_rosita.md:27`. |
| 4.1, 4.3, 4.8 (parte) | Laguna e a recusa no Rio agora aparecem como tradição (caps. 5, 13, 19, 21). |

### C. O que continua aberto

| Item | Situação atual | Onde | Prior. |
|---|---|---|---|
| 0.2 | README ainda diz 11 filhos e "Lina e Valter"; os capítulos já dizem 12. | `README.md:140`, `:297` | **A** |
| 0.4 | GEDCOM já usa só o ano, mas o README e o cap. 11 mantêm datas completas. O README mantém a OAB. | `README.md:87`, `:117`, `:122–123`, `:132–134`, `:138`, `:171`, `:295`; `11_oma_rosita.md:11`, `:15` | **A** |
| 2.10 | A imagem do assento 23/1900 confirma Tombröck, José May e João Peters, moradores do Capivari e sem dispensa. O README transcreve outra versão (Auling/Hömke) logo abaixo da imagem, sem aviso. | `README.md:289` | **A** |
| 1.11 | Os irmãos do autor continuam fora dos capítulos; agora só estão no GEDCOM. | cap. 1 | **A** |
| 3.1 | Datas impossíveis dos filhos de Francisco Jacob seguem sem ressalva no README. | `README.md:183–194` | M |
| 0.5 | O cap. 21 já diz que a planilha é privada; os caps. 15 e 20 ainda a colocam no repositório. | `15_o_que_se_herda.md:83`; `20_epilogo.md:29` | M |
| 1.4 | "Ambos com oitenta e cinco anos": Johann tinha 84, como diz o cap. 7. | `02_fata_e_mota.md:55` | M |
| 1.8 | Oito filhos dos Meier, mas só sete nomes. | `README.md:147`; `15_o_que_se_herda.md:19` | M |
| 2.4 | Ignazia ainda nasce em 1828 em São Pedro de Alcântara no README. | `README.md:66`, `:158` | M |
| 4.2 | "No fim de 1912, Maria engravidou": um parto em 05/05/1913 pede concepção por volta de agosto de 1912. | `04_antes_da_partida.md:107` | M |
| 4.4 | "Uns vinte e cinco hectares" do Lote 17, sem fonte. | `20_epilogo.md:23` | M |
| 4.14, 2.18 | Epílogo: "maio de 2012" sem data do casamento, e "a voz dela abre o livro", embora a gravação não tenha sido transcrita. | `20_epilogo.md:13`; `01_vidal_ramos.md:7` | M |
| 4.17 | Caminho `livros_e_artigos_internet/…` não existe no repositório. | `09_matriarca_arend.md:80` | M |
| 3.8 | Só dois dos quatro filhos de Erno e Rosita têm nome. | `11_oma_rosita.md:73` | M |
| 3.10 | A reportagem de Joinville continua sem jornal, título e data. | `11_oma_rosita.md:73–93` | M |
| 1.12, 1.13, 1.16, 2.5, 2.8, 2.18, 3.2, 3.3, 4.5, 4.6 | Dependem de família ou arquivo: netos, entrevistas, casamento de Reinaldo e Bárbara, batismos, lápides, obras e túmulos. | ver seções 1 a 4 | M |

Os demais itens não foram rechecados nesta passada.

---

## Levantamento original (04/11/2026)

Levantamento feito em 04/11/2026 sobre o commit `1bc531b`. Foram lidos os 21 arquivos de `livro/capitulos/`, o `README.md` (diagrama Mermaid e quadro de gerações), o `arvore_familysearch.ged`, o texto da Marise (`livro/fontes/historia_joao_e_maria_marise_2013.txt`) e a imagem da lista de bordo do *Formosa*. A planilha do Agenor (`privado/`) foi consultada só localmente; daqui ela só aparece como nomes, contagens e anos.

**Regra de hierarquia das fontes** (pedida pelo autor): fontes primárias prevalecem sobre o texto da Marise e sobre a planilha.

1. Registros civis e paroquiais, lista de bordo do *Formosa* (Rio, 26/03/1913) e registros e lápides de cemitério.
2. Índices do FamilySearch, recenseamento de 1920 e publicações da CAPEF e de Toni Jochem.
3. Planilha do Agenor.
4. Texto da Marise e memória oral.

**Prioridade:** **A** = erro factual ou contradição que se propaga, ou risco de privacidade. **M** = lacuna importante para o leitor (Matheus e Lucas). **B** = refinamento.

**Fora do escopo desta lista, porque estão sendo corrigidos em paralelo por outra sessão:** a Parte II (enterros de Walter e Lina em Anitápolis, depois trasladados para Ituporanga), o ramo Carlos Doerner e o capítulo de Fernando Dörner. Os itens desses trechos aparecem aqui só como referência, marcados com ⟲, para conferência depois da correção.

**Dados de pessoas vivas:** este documento traz só nomes e, quando conhecidos, anos. Bisnetos e trinetos de Johann e Maria aparecem só em números, porque há menores entre eles.

---

## 0. Problemas transversais (todas as partes)

| # | O que falta ou está errado | Onde | Fonte que resolveria | Prior. |
|---|---|---|---|---|
| 0.1 | **O README contradiz a imagem dos registros de Moosbach.** Primeiro, o README dá ao casamento Meier–Voit as testemunhas *Johann Puff, Gastwirth* e *Josephus Hammerl, Schuhmacher* e o celebrante *Josephus Bogner*. A imagem (`imagens/doc2_trauung_meier_voit_1884.jpg`, conferida) mostra outras testemunhas, *Mich. Meier, Wagner, Heumaden et Johan Voit, Bauer, Burgtreswitz*, como o livro diz em 17:79, e não traz o nome do celebrante nessa linha. Segundo, os batismos do README divergem do livro. Georg Adam: README diz batismo em 10/03/1859 e padrinho *Georg Balk*; o livro (17:99) diz 09/03 e *Adam Hartung*. Franziska: README diz 30/06/1861 e madrinha *Franziska Woppmann*; o livro (17:111) diz 29/06 e *Margaretha Albrecht*. Maria: README diz 08/04/1888 e madrinha *Katharina Meier*; o livro (17:47–49) diz 07/04 e *Kath. Reichenberger*. As transcrições do README parecem fabricadas. | `README.md:252`, `README.md:253`, `README.md:42` | Imagens `doc1`–`doc4` e as páginas no Matricula (`Moosbach_Leuchtenberg005`, p. 96, 115, 441; `…013`, p. 93). Refazer o README pela leitura do cap. 17. | **A** |
| 0.2 | **O número de filhos de Johann e Maria muda de lugar para lugar.** A própria planilha fecha em **12** na linha de totais (12/63/194/109), e o cap. 3:71 também conta 12. Mas o README diz 11 (140, 276), o cap. 4:93 diz "cinco dos **onze** filhos… os outros **seis** aguentaram" (12 − 5 = 7), o cap. 5:79 atribui "onze filhos" à Marise (ela não dá total; a soma da lista dela é 12), o cap. 16:95 diz "onze filhos, dos quais sete" e o cap. 3:45 repete "11 filhos" do resumo. | `README.md:140`, `README.md:276`; `04_antes_da_partida.md:93`; `05_formosa_1913.md:79`; `16_standesamt.md:95`; `03_primos_detetives.md:45` | Planilha (linha de totais) e lista da Marise: 12 filhos, 5 perdidos e 7 criados. | **A** |
| 0.3 | **Marise Haas Lourenço é chamada de "prima", mas pela planilha é filha de Baldoíno e Adelina**, ou seja, irmã do autor. Ela aparece entre os 12 filhos de Baldoíno ("Marise X Alberto") e não há outra Marise na planilha. Se for mesmo irmã, a apresentação dela muda em vários capítulos. | `01_vidal_ramos.md:73`; `02_fata_e_mota.md:25`; `03_primos_detetives.md:11`; `04_antes_da_partida.md:67` | Confirmação do autor e planilha (bloco de Baldoíno). | **A** |
| 0.4 | **Datas completas de nascimento de pessoas vivas em arquivos públicos**, contra o critério de publicar só o ano: Matheus e Lucas, Reinaldo, Bárbara e Agenor (`README:274`). O GEDCOM publica o nascimento de Reinaldo (vivo). O README também publica o registro profissional OAB de Ilusca (viva). | `README.md:3`, `README.md:87`, `README.md:117`, `README.md:122–123`, `README.md:132–134`, `README.md:138`, `README.md:274`; `11_oma_rosita.md:11`, `11_oma_rosita.md:15`; `arvore_familysearch.ged:15–21` | Decisão do autor: reduzir a ano, retirar a OAB e exportar o GEDCOM sem os vivos. | **A** |
| 0.5 | **O livro diz que a planilha do Agenor está no repositório**, mas desde o commit `0d117c2` ela é privada e está fora do git. | `19_epilogo.md:29`; `14_o_que_se_herda.md:83` | Reescrever: "guardada no arquivo privado da família". | M |
| 0.6 | **O resumo da transcrição privada traz cônjuges errados para os filhos de Johann e Maria**: Marta Kammers, Evaldo Sens, Alfredo Sens e José (Juca) Clasen. A tabela da própria planilha e a lista de sobrenomes da Marise dão outros: Augusto (Sebold), Rosalina (da Rosa), Paula (Klettenberg), João Augusto (Boeing), Paulo (Nagel), Martin (Sautner). O resumo não é versionado, mas pode contaminar o livro se for usado como fonte. | `privado/arvore_agenor_haas_completa.md` (resumo, linhas 9–21) | Tabela da planilha original `.xls`. | M |
| 0.7 | **O GEDCOM só tem a linha direta paterna do autor**: 27 pessoas e 13 famílias, cada família com um único filho. Faltam o lado de Bárbara inteiro (Funke, Hoeveler, Lohmann, Endres, Schnack, Wingert, cerca de 20 pessoas que o README já documenta com IDs do FamilySearch), Bárbara, Matheus e Lucas, irmãos e colaterais, Hulda Peters e o 2º casamento de Carlos, e o casal Arend–Klering. | `arvore_familysearch.ged:841–892` | Nova exportação do FamilySearch a partir de Matheus/Lucas, incluindo os IDs citados no README (`G2MG-8VY`, `27QQ-TM9`, `KNYK-4J3` etc.). | **A** |

---

## 1. Ramo Haas — Johann (Fata) e Maria Meier (Mota)

### 1.1 Geração dos bisavós e de seus pais (G4–G6 de Matheus e Lucas)

| # | O que falta ou está errado | Onde | Fonte que resolveria | Prior. |
|---|---|---|---|---|
| 1.1 | **A data de nascimento de Johann no GEDCOM é 08/07/1884**, que é a data da planilha. O assento civil nº 47/1884 diz 11/07/1884. | `arvore_familysearch.ged:222` | Assento nº 47/1884 (`doc_haas_nascimento_johann_1884.jpg`). Corrigir no FamilySearch (GX1B-HM1). | **A** |
| 1.2 | **O evento de imigração de Johann no GEDCOM tem a data 07/03/1913** ("saiu da Alemanha"). Essa data vem da foto de despedida, não de um documento de embarque. A chegada documentada é Rio, 26/03/1913. | `arvore_familysearch.ged:227–228` | Lista do *Formosa*; registro de saída em Marselha. | B |
| 1.3 | **O local de sepultamento varia entre as fontes.** O GEDCOM diz "Cemitério da Igreja Católica N. Sra. das Dores (Centro), Aurora". O README diz "Cemitério Municipal/Paroquial de Aurora". A planilha diz que Johann morreu em Rio das Pacas. O livro (2:55, 7:89) não nomeia o cemitério. Também faltam a quadra, a lápide e a foto do túmulo, e não há nenhum túmulo identificado como obra de Johann. | `README.md:228`; `arvore_familysearch.ged:235`; `07_radio_no_porao.md:89` | Registro do cemitério de Aurora e foto das lápides (datas inscritas). Livro de óbitos do Registro Civil de Aurora (1969, 1973). | **A** |
| 1.4 | **Idade dos dois na morte.** O cap. 2:55 repete da Marise "ambos com 85 anos". Johann tinha 84; o próprio cap. 7:87 corrige. Também falta a certidão de óbito dos dois. | `02_fata_e_mota.md:55` | Certidões de óbito de Aurora. | M |
| 1.5 | **Irmãos de Johann sem datas nem fonte citada**: Josef, Alois, Georg, Maria, Franziska e Therese. O README não diz de onde vem a lista. | `README.md:241`; `04_antes_da_partida.md:61`; `16_standesamt.md:87` | Livros do Standesamt Leonberg (de 1876 em diante) e batismos da paróquia de Leonberg/Maxhütte. | M |
| 1.6 | **O padrinho e a hora do batismo de Joseph Haas aparecem só no README** ("Josephus Widmann, Söldnerssohn von Pitzling"; 22h00), sem conferência no livro. Pelo padrão do item 0.1, é preciso conferir. | `README.md:240`; `16_standesamt.md:23` | Imagem `batismo_joseph_haas_1847_stoffen.png` e Matricula/Augsburg. | M |
| 1.7 | **Franziska Dengler (mãe de Johann) não tem nenhuma data**, nem no README nem no GEDCOM. Josef Haas não tem data de morte. | `README.md:30`; `arvore_familysearch.ged:289–308` | Óbitos e casamento em Leonberg/Maxhütte e casamento Haas–Dengler. | B |
| 1.8 | **Irmãos da Mota**: Franziska Voit "teve 8 filhos" (README:147) e Maria seria "uma dos oito filhos" (14:19), mas o README:253 e os caps. 4:21 e 17:129 listam 7 (Johann Baptist 1885, Barbara 1886, Maria 1888, Margaretha 1890, Josef 1892, Georg 1895, Anna 1898). O cap. 4:81 diz "sete filhos". | `README.md:147`; `14_o_que_se_herda.md:19`; `04_antes_da_partida.md:81` | Livro de batismos de Moosbach 1885–1900 (Heumaden). | M |
| 1.9 | **Casamento em Eibenstock (03/08/1907) sem documento.** O único registro é a planilha; o README o põe no diagrama como certo. | `README.md:47`; `04_antes_da_partida.md:79` | Standesamt/paróquia de Eibenstock (Saxônia) ou Moosbach (*Trauungsbuch*, nota marginal). | M |
| 1.10 | **A madrinha da Mota é chamada de "tia Katharina Meier" na tradição e no README**, mas Reichenberger no livro paroquial. Ver o item 0.1; a hipótese de casamento Meier–Reichenberger está em aberto. | `README.md:253`; `17_heumaden_moosbach.md:61` | Casamentos de Moosbach/Burgtreswitz. | B |

### 1.2 Os 12 filhos (G4 para Reinaldo, tios-avós e avô para Matheus e Lucas)

O que dizem as fontes primárias: o *Formosa* lista Johann (28), Marie (25), **Luisa (2)** e **Walter (1)**. Gertrudes não está na lista.

| Filho | O que aparece no livro e no README | O que falta ou está errado | Fonte | Prior. |
|---|---|---|---|---|
| Hildegard (Hildegart) | Morreu na Alemanha (4:91; README:241) | Datas e local de nascimento e de óbito. | Civil e paroquial no local de residência de 1907–1910 (Eibenstock?). | M |
| Frida | Idem | Idem | Idem | M |
| **Luisa** (c. 1910–1911) | Está no *Formosa*. ⟲ Parte II | O **README:230** e a planilha falam em "Lina", e o README:276 diz "Lina e Valter… em Anitápolis". O GEDCOM não tem Luisa. O epílogo (19:51) afirma que ela "não sobreviveu ao primeiro ano no Brasil", sem fonte. | Óbito e sepultamento em Anitápolis e o traslado para Ituporanga (em correção). | **A** ⟲ |
| **Walter** (c. 1912) | Está no *Formosa*. ⟲ | Mesmo problema, com "Valter" no README:230 e 276. | Idem | **A** ⟲ |
| **Gertrudes** | O livro adota 05/05/1913, nascida no Brasil (3:85, 5:65). | O **README:241** ainda diz "embarcou como primogênita sobrevivente, * 22/10/1911", o que contradiz o *Formosa*. Faltam: o batismo (Laguna?), a data de morte, o cônjuge (Augusto Sebold), o local no Paraná e o cemitério. | Batismo na Matriz de Laguna, registro civil, óbito no PR. | **A** |
| Fernando (Ferdinand) (1915) | Só o ano, citado da Marise (6:37). | Dia do nascimento, cônjuge (Rosalina da Rosa), mudança para o PR, data e local de morte. | Batismo em Anitápolis e Palhoça; óbito no PR. | M |
| Alexandre (23/05/1917–16/11/1994) | Datas no README:229; livro 6:37. | Cônjuge Paula Klettenberg (1921–2007) aparece no README, mas não no livro. Falta o cemitério de Ituporanga. | Lápide em Ituporanga. | B |
| Agnes/Inês (1920) | Só o ano (6:95). | Cônjuge João Augusto Boeing, data de morte, cemitério (Aurora?). | Batismo em Ituporanga; óbito em Aurora. | M |
| Elza (1922) | Só o ano. | Cônjuge Paulo Nagel, PR, óbito. | Idem | M |
| Baldoíno (20/04/1924–18/12/2013) | Bem coberto. | **Data e igreja do casamento de 1947** (o livro admite em 1:41). O epílogo (19:13) dá as Bodas de 65 anos como "maio de 2012", mas sem a data do casamento não há como datar as Bodas. **O GEDCOM põe o nascimento em "Rio Novo, Águas Mornas"** (`ged:33`); o livro (3:99) reconhece o erro, mas o FamilySearch não foi corrigido. Falta o cemitério (o README:229 diz Ituporanga/Vidal Ramos sem precisar). | Casamento civil e religioso (Vidal Ramos/Ituporanga 1947); lápide; corrigir o GVX4-ZHK. | **A** |
| Maria (1926) | Só o ano. | Cônjuge Martin Sautner, Ribeirão das Pacas, óbito. | Batismo em Ituporanga; óbito em Aurora. | M |
| João (1932) | Morte "pequeno" (6:99). | Datas de nascimento e morte, local, sepultura. Não aparece no README nem no GEDCOM. | Batismo e óbito em Ituporanga (Águas Negras). | M |

### 1.3 Os netos (G3 de Matheus e Lucas: tios-avós e o pai)

Pela planilha, são 63 netos, assim distribuídos: Gertrudes 9, Fernando 7, Alexandre 8, Agnes 13, Elza 8, Baldoíno 12 e Maria 8. Há linhas repetidas por recasamento. **O livro não nomeia nenhum neto, salvo Agenor (1943), Marise (como "prima") e o próprio autor.** O README cita ainda Roni José (1961–1964).

| # | O que falta | Onde deveria entrar | Fonte | Prior. |
|---|---|---|---|---|
| 1.11 | **Os irmãos do autor, tios de Matheus e Lucas**, nunca aparecem: Arnaldo, Márcio, Sílvio, Marlise, Marlene, Maria, Marilda, Marise, João, Ricardo, Reinaldo e Hilton (12 filhos de Baldoíno e Adelina). Num livro dirigido a Matheus e Lucas, os tios paternos estão ausentes. Também não há o ano de nascimento de nenhum deles. | Cap. 1 ("A Casa de Vidal Ramos": a mesa, as Bodas) e um quadro no epílogo | Planilha; certidões; o próprio autor. | **A** |
| 1.12 | **Os primos-irmãos do autor, por ramo**, só nomes e anos: Gertrudes (Bertoldo, Arnoldo, Inês, Rainoldo, Frida, Rainildes, Leopoldo, Terezinha, Maria); Fernando (Yolanda, Irene, Valdemar, Lone Isolde, Norma, Antônio, Nelson); Alexandre (Agenor 1943, Marlith 1945, Jaime 1948, Lauro, Maria Ester, João Walter, Roni José 1961–1964, Beatriz 1965); Agnes (Hildegart, Edelberto, Edite, Eduardo, Edmundo, Melita, Maria, Isolde, Bernardete, Idalina, Roberto, Bernardo, Inês); Elza (Leoni, Olga, Roberto, Vera, Edite, Carlos Ernesto); Maria (Vanio José, Marli, Áuria, José Lino, Danilo, Ivone, João Martin, Cláudio Fernando). O livro poderia ter um apêndice "Os 63 netos" com nome, ano e ramo, sem dados de contato, e indicar quais já faleceram. | Cap. 3 (planilha de Londrina), cap. 7 ("Ribeirão das Pacas": os netos de Agnes e Maria) e apêndice | Planilha; consentimento dos primos vivos. | M |
| 1.13 | **Os netos que guardam a memória dos avós** (filhos de Agnes e Maria, em Ribeirão das Pacas) são citados como fonte coletiva (2:49, 7:77), mas nenhum foi entrevistado nem nomeado. | Cap. 2 e cap. 7 | Entrevistas gravadas. | M |
| 1.14 | **Quem era o "neto de vigia" do rádio no porão (1942–43)?** O cap. 7:17 não identifica. Em 1942 só os filhos de Gertrudes (n. 1913) e de Fernando (n. 1915) poderiam ter idade para isso; os anos de nascimento desses netos não estão na planilha. | Cap. 7 | Anos dos netos mais velhos e entrevista. | B |

### 1.4 Bisnetos e trinetos (G2–G1)

| # | O que falta | Onde | Fonte | Prior. |
|---|---|---|---|---|
| 1.15 | A planilha tem 194 bisnetos e 109 trinetos, mas o livro só dá o total "mais de seiscentos" (3:9). **A planilha está incompleta**: no bloco de Baldoíno, Reinaldo aparece sem filhos, ou seja, **Matheus (2002) e Lucas (2005) não estão nela**, e a 4ª geração desse ramo marca 0, embora outros ramos registrem trinetos nascidos até 2004. A data de fechamento da planilha não é dita no livro. | `03_primos_detetives.md:45`; planilha | Atualização com os primos; o livro deveria dizer que a contagem é antiga e de que ano. | M |
| 1.16 | **Matheus e Lucas (G1)**: o livro fala com eles, mas não registra o casamento de Reinaldo e Bárbara (data e local; o README:120 diz apenas "Casamento Civil, Vidal Ramos / Florianópolis"). Também não registra o batismo dos dois nem a confissão religiosa da casa, que o cap. 10:59 sugere ser mista. | Prólogo e epílogo; README:120 | Certidão de casamento; o próprio autor. | M |

---

## 2. Ramo Doerner–Preiss (Fernando e Gertrudes Dörner) e ascendentes Michels, Arend, Preis, Loch e Eller

### 2.1 Ascendentes (G5–G7)

| # | O que falta ou está errado | Onde | Fonte | Prior. |
|---|---|---|---|---|
| 2.1 | **O perfil de Carl Reinhard Doerner no FamilySearch traz a nota "obviously a merger of 3–4 different men"**, ou seja, a ficha mistura homens diferentes. O livro (10:13) e o README:148 usam esse perfil como se fosse uma pessoa só. ⟲ | `arvore_familysearch.ged:477` e `:2142` | Separar as pessoas no FamilySearch (GDGT-8H8) com batismos de Solingen e o assento nº 23/1900. | **A** ⟲ |
| 2.2 | **A nota do GEDCOM diz que a data (1858) e o lugar (RS) de nascimento de Anna Eller foram gerados automaticamente** ("Date and Location are generated"). O README:58 e 149 e o livro (10:23–25, 10:31) tratam isso como fato e constroem a cena do "minuano dos Eller" sobre a data gerada. | `arvore_familysearch.ged:391` e `:2144`; `10_solingen_e_brusque.md:23–25` | Batismo de Anna Eller e óbito em Imaruí/São Martinho (c. 1898). | **A** ⟲ |
| 2.3 | **A data de batismo de Franz Adam Eller (03/03/1832) está no GEDCOM como evento sem rótulo**, e a "St. Peter und Paul, Westfalen" não identifica a paróquia. | `arvore_familysearch.ged:644–653`; `README.md:56`, `README.md:157` | Índice de batismos da Vestfália e paróquia exata. | B |
| 2.4 | **O README dá Ignazia Loch como nascida em 1828 em São Pedro de Alcântara**, o que é impossível porque a colônia só foi assentada em 1829. O livro (8:75–79) já trata como aproximado; o README e o GEDCOM continuam iguais. A morte dela está como "von 1872 zu 1914". | `README.md:66`, `README.md:158`; `arvore_familysearch.ged:761–768` | Batismo e óbito (índices da Igreja Católica de SC, Águas Mornas e São Martinho). | M |
| 2.5 | **O nascimento de Bernard Preis é 1827 no registro e 1829 na lápide**, e a data de chegada ao Brasil não é conhecida. | `README.md:65`; `arvore_familysearch.ged:2110`; `08_barcos_de_1828.md:93` | Batismo em Schweich (Trier) e foto da lápide em Alto São Martinho. | M |
| 2.6 | **O nascimento de Helena Michels está em "Vargem do Cedro" no README e no GEDCOM**, mas em 1864 a família vivia em Vargem Grande (9:69). O README também põe a morte de Emanuel Preis em São Martinho, enquanto o GEDCOM diz Vargem do Cedro. | `README.md:73`, `README.md:151`, `README.md:150`; `arvore_familysearch.ged:321`, `:431` | Batismo de Helena (07/02/1864) e óbito de Emanuel (1927). | B |
| 2.7 | **Nikolaus Arend aparece no README só como seta para Angela**: não há esposa nem datas, e Maria Elisabetha Klering, a mãe de Angela (1ª esposa) e os irmãos não aparecem. | `README.md:69`, `README.md:161` | Batismos de Pünderich (Matricula/Trier). | B |
| 2.8 | **Anton Michels e Angela Arend: falta a data do casamento** (o livro admite em 9:51) e faltam os filhos nascidos antes de 1864. | `09_matriarca_arend.md:51–53` | Índice Ursula Buchholz (número de casamento) e livros de Santa Isabel e São Pedro de Alcântara. | M |
| 2.9 | **Erro de parentesco no cap. 10:69**: Gertrudes Preiss é chamada de "bisneta da matriarca", mas é **neta** de Angela Catharina (Angela → Helena → Gertrudes). O cap. 9:91 está certo. | `10_solingen_e_brusque.md:69` | Árvore interna. | **A** ⟲ |
| 2.10 | **Assento nº 23/1900**: a transcrição do README (celebrante Auling, testemunhas Augusto Peters e Henrique Hömke, Braço do Norte, dispensa de religião mista) diverge da imagem (10:47). O README apresenta a transcrição como se fosse a leitura da imagem. Pelo item 0.1, isso pode ser outra transcrição fabricada. | `README.md:261`, `README.md:268`; `10_solingen_e_brusque.md:47–53` | Imagem e via da matriz (Tubarão ou Braço do Norte). | **A** ⟲ |
| 2.11 | **Os filhos de Carlos Doerner**: a lista da família (10 + 5) e os índices de batismo não batem (10:29, 10:61). | `README.md:260–261` | Índices do FamilySearch e livros de São Martinho e Capivari. | M ⟲ |

### 2.2 Fernando Dörner (1897–1981) e Gertrudes Preiss (1896–1970), G4

| # | O que falta ou está errado | Onde | Fonte | Prior. |
|---|---|---|---|---|
| 2.12 | **A data de morte de Gertrudes no GEDCOM é 14/04/1970**, que é a data do termo de registro. A morte, pela certidão, foi em 09/04/1970, e o campo DEAT do GEDCOM está sem data. | `arvore_familysearch.ged:178–186` | Certidão (`doc_doerner_obito_gertrudes_preiss_1970.jpg`). | M |
| 2.13 | **Data do casamento: 1913 ou 1921.** O livro inclina-se por 1921. O README e o GEDCOM não trazem data nenhuma. | `README.md:80`; `10_solingen_e_brusque.md:71` | Imagem do registro católico (Vargem do Cedro) e do civil. | M ⟲ |
| 2.14 | **Faltam o quando e o porquê da mudança de São Martinho para Brusque.** | `10_solingen_e_brusque.md:77` | Recenseamentos e títulos de eleitor; entrevista com os filhos. | B ⟲ |
| 2.15 | **Os nomes dos jazigos no Parque da Saudade (Brusque) não constam**: faltam a quadra e a lápide. A certidão de Gertrudes diz "cemitério católico", e o README diz Parque da Saudade para os dois. | `README.md:141–142`, `README.md:231`; `10_solingen_e_brusque.md:87`, `:93` | Administração do cemitério de Brusque. | M |

### 2.3 Filhos de Fernando e Gertrudes (G3: Adelina e irmãos)

| # | O que falta | Onde deveria entrar | Fonte | Prior. |
|---|---|---|---|---|
| 2.16 | **Os irmãos de Adelina não aparecem em lugar nenhum** (livro, README e GEDCOM). O óbito de 1970 lista seis filhos vivos e o de 1981 lista cinco; os nomes estão nas certidões já digitalizadas, mas o livro não os transcreve. Também não se sabe qual filho morreu entre 1970 e 1981 (10:101). | Cap. 10 ("Dois óbitos em Brusque") e cap. 1 (memória de Adelina) | As próprias certidões (`doc_doerner_obito_*.jpg`) e a família Doerner. | **A** |
| 2.17 | **A festa da família Doerner em setembro de 2012** (10:79) não tem local, data nem participantes. | Cap. 10 | Fotos e convite. | B |
| 2.18 | **A gravação de Adelina (2012) não foi decupada.** O epílogo diz que "a voz dela abre o livro", mas o cap. 1:49 diz que nada foi transcrito. | `19_epilogo.md:13`; `01_vidal_ramos.md:49` | Transcrição do vídeo. | M |

---

## 3. Ramo de Bárbara: Lohmann, Endres, Schnack, Hoeveler e Funke (até Matheus e Lucas)

### 3.1 Ascendentes Lohmann e Schnack (G5–G8)

| # | O que falta ou está errado | Onde | Fonte | Prior. |
|---|---|---|---|---|
| 3.1 | **Os 12 filhos de Francisco Jacob Lohmann e Miguelina Endres: o README lista sem ressalva datas impossíveis.** Walter Érico (1911) e Reinholdo (1912) nascem antes do casamento de 1914; há dois Walter (1911 e 27/12/1916), possivelmente duplicata no FamilySearch (`G2MP-W4Q` / `GVPW-61W`); há três nascimentos em 1918 e dois em 1921. O livro (12:87) faz a ressalva; o README, não. A foto de Palmas mostra 11 filhos e um só Walter. | `README.md:183–194`, `README.md:105` | Batismos evangélicos ou católicos de Arroio do Meio/Estrela; mesclar a duplicata no FamilySearch. | **A** |
| 3.2 | **Rosita Érica (Oma Rosita) só tem os anos (1918–2014).** Faltam o dia e o local de nascimento, o casamento com Erno, o óbito em Joinville e o cemitério (o README:227 sugere o Municipal de Joinville). | `README.md:107`, `README.md:143`, `README.md:227`; `11_oma_rosita.md:91` | Certidão de óbito de Joinville (2014) e lápide. | M |
| 3.3 | **Miguelina Leocádia Endres: faltam os pais, a data de morte e o cemitério.** O ramo Endres não tem nenhum ascendente. | `README.md:106`, `README.md:226`; `12_vale_do_taquari.md:85` | Batismo de 1891, óbito e CAPEF. | M |
| 3.4 | **Adolfo André e Francisco Jacob aparecem ambos como nascidos em 1889.** Falta saber se eram gêmeos ou se a data está errada. | `README.md:180`; `12_vale_do_taquari.md:71` | Batismo em Arroio do Meio. | B |
| 3.5 | **A confissão religiosa é afirmada sem fonte.** O livro dá "luteranos" a todo o lado de Bárbara (10:59, 11:27). Os nomes "Francisco Jacob", "Miguelina Leocádia" e "Endres" sugerem possível casa mista ou católica. O cap. 10:59 também repete "Hoeveler, os Hoeveler". | `10_solingen_e_brusque.md:59`; `11_oma_rosita.md:27` | Livros de batismo e de casamento de 1914 (igreja). | M |
| 3.6 | **Os nomes dos irmãos Lohmann na legenda da foto de Palmas divergem do registro** ("Urbano Arno", "Reinboldo"). O livro já registra a divergência. | `12_vale_do_taquari.md:89` | — | B |

### 3.2 Hoeveler (Erno, G4) e filhos (G3: Ilusca e irmãos)

| # | O que falta | Onde deveria entrar | Fonte | Prior. |
|---|---|---|---|---|
| 3.7 | **Erno Hoeveler não tem datas, pais, origem nem cemitério.** Os Hoeveler não têm nenhum ascendente na árvore, e o prólogo (0:35) os inclui entre "os nomes que vocês carregam". | `README.md:109`, `README.md:143`; `11_oma_rosita.md:71` | FamilySearch, registros da IECLB (Estrela e Nova Petrópolis) e família. | **A** |
| 3.8 | **Erno e Rosita tiveram 4 filhos, mas só Ilusca e Walter são nomeados.** Faltam os outros dois e os anos de todos. | `11_oma_rosita.md:71` | Família (Ilusca, Walter). | M |
| 3.9 | **Walter Hoeveler ("Tio Walter")**: o livro dá a mudança para Florianópolis em 1960 e o livro *Viagens de Walter* (2013), de Katherine Funke. Faltam a ficha bibliográfica (editora) e a confirmação do ano. | `11_oma_rosita.md:87` | Catálogo da Biblioteca Nacional. | B |
| 3.10 | **As reportagens de jornal de Joinville sobre os Natais (cerca de 2015) não estão identificadas**: faltam o jornal, a data e o título. Mesmo assim, são usadas como prova ("estão documentados"). | `11_oma_rosita.md:71–85` | Acervo do jornal; ficha de fonte com título e data. | M |

### 3.3 Funke (G4–G3)

| # | O que falta | Onde deveria entrar | Fonte | Prior. |
|---|---|---|---|---|
| 3.11 | **O ramo Funke não tem nenhum ascendente identificado.** Falta o nome do pai do Dr. Carlos Heinz (o "bisavô Funke"). Falta o nome de solteira, as datas e os pais da "Oma Dora". O README chama Dora de "Funke" e atribui a ela "7 irmãos", mas esses irmãos são da família de origem dela, não Funke. O README:113 resume tudo como "Família Funke & 'Oma Dora' Funke". | `README.md:113`, `README.md:144`; `11_oma_rosita.md:49–55` | Certidão de nascimento do Dr. Carlos Heinz (1939), casamento dos pais, cemitério de Joinville. | **A** |
| 3.12 | **Os irmãos do Dr. Carlos Heinz Funke não aparecem.** Também falta identificar quem são as 9 crianças da foto antiga (filhos dos pais de Dora?). | `11_oma_rosita.md:49` | Família Funke. | M |
| 3.13 | **Dr. Carlos Heinz Funke (1939–1989)**: falta a data exata da morte, o cemitério (o README:227 sugere o Municipal de Joinville), a faculdade de Medicina e o ano de formatura. Falta também a data e o local do casamento com Ilusca. | `README.md:137`; `11_oma_rosita.md:25`, `:37` | Certidão de óbito; registro do CRM; casamento. | M |
| 3.14 | **Os filhos de Carlos Heinz e Ilusca** (Bárbara 1972, Katherine, Alessandra e Paulo Jacques) estão nomeados, mas os anos de nascimento dos três irmãos de Bárbara não constam. | `README.md:134`; `11_oma_rosita.md:25` | Família. | B |

---

## 4. Falhas narrativas: fatos sem fonte, cenas inventadas e afirmações que dependem só da Marise

Em geral, o livro marca bem as reconstituições ("imagino", "não sei"). Os problemas abaixo são os casos em que o texto da Marise passa como fato sem confirmação primária, ou em que a fonte primária contradiz a narrativa.

### 4.1 Afirmações que dependem só do texto da Marise

| # | Afirmação | Onde no livro | O que diz a fonte primária / o que confirmaria | Prior. |
|---|---|---|---|---|
| 4.1 | **O desembarque em Laguna e o "Barracão dos Imigrantes".** O livro inteiro (o título do cap. 5, 1:45, 2:53, 5:59–115, 13:43, 19:51) toma Laguna como certa. Nenhum documento a confirma. O *Formosa* foi visado no **Rio, em 26/03/1913**, e o navio seguiu para Santos ("Le Nº 70 continue sur Santos. Restent 174 passagers"). O GEDCOM não menciona Laguna. A seção "Laguna, fevereiro de 2012" (cap. 5) é construída sobre essa chegada não documentada. | `05_formosa_1913.md:1`, `:59–115`; `00_prologo.md:59`; `01_vidal_ramos.md:45` | Livro de registro da Hospedaria da Ilha das Flores (Arquivo Nacional), listas de vapores costeiros RJ→SC (abril de 1913) e registros da Inspetoria de Terras e Colonização de SC (Anitápolis). | **A** |
| 4.2 | **O nascimento de Gertrudes em 05/05/1913 em Laguna e a gravidez de Maria durante a viagem.** As duas coisas vêm só da Marise. O *Formosa* só prova a ausência de Gertrudes a bordo. As contas de gestação do livro também não fecham entre si: em 4:101 a concepção é "no fim de 1912" (seria em agosto de 1912 para um parto em maio); em 5:41 Maria está "no início do quarto ou quinto mês" em março (o que daria parto em julho ou agosto); em 5:63 ela tem "barriga de oito meses" no fim de abril (seria o 9º mês). | `04_antes_da_partida.md:101`; `05_formosa_1913.md:41`, `:63`; `07_radio_no_porao.md:93`; `19_epilogo.md:65` | Batismo de Gertrudes (Laguna, Anitápolis ou Palhoça, 1913), registro civil e certidão de casamento de Gertrudes (que traz a naturalidade). | **A** |
| 4.3 | **O navio recusado no Rio, a quarentena "de porto em porto" e os "inúmeros óbitos" a bordo.** O livro mostra as duas leituras (5:55–57) mas, no resto do texto, trata o enredo da Marise como certo. | `03_primos_detetives.md:31`; `05_formosa_1913.md:51–57` | Jornais do Rio (*Jornal do Commercio*, *Correio da Manhã*, 26–28/03/1913, movimento do porto, Hemeroteca Digital) e Diretoria de Saúde Pública. | M |
| 4.4 | **O Lote 17 em Rio do Ouro, comprado "junto com um amigo".** O epílogo acrescenta "uns vinte e cinco hectares", sem fonte nenhuma. | `06_anjos_de_gesso.md:31`; `19_epilogo.md:23` | Livro de registro de lotes do Núcleo Colonial Anitápolis (Arquivo Público de SC / Ministério da Agricultura). | M |
| 4.5 | **As obras atribuídas à família em Ituporanga** (Igreja Matriz, Casa Paroquial, Seminário Franciscano, ampliação do Hospital) aparecem várias vezes como fato. No cap. 7:51 e no cap. 16:73 são atribuídas ao próprio Johann. | `02_fata_e_mota.md:29`; `06_anjos_de_gesso.md:107`; `07_radio_no_porao.md:51`; `16_standesamt.md:73` | Livro tombo da paróquia de Ituporanga, arquivo dos Franciscanos e do hospital das Irmãs, fotos de obra. | M |
| 4.6 | **Os túmulos de granilite com anjos de gesso**, em Rio do Ouro e em Aurora, sustentam todo o motivo do livro. Nenhum túmulo é identificado. | `06_anjos_de_gesso.md:43–53`; `07_radio_no_porao.md:89`; `19_epilogo.md:65` | Levantamento fotográfico nos cemitérios de Aurora e Anitápolis; netos de Aurora. | M |
| 4.7 | **A carta da irmã da Mota avisando da guerra (1914).** A data e a remetente são deduzidas no livro. Há também uma contradição de cronologia: na Marise a carta chega ainda no tempo dos barracões e antes da compra do lote; no livro, chega em Rio do Ouro. | `06_anjos_de_gesso.md:9–17`; `07_radio_no_porao.md:29` | Carta, se existir no acervo. | B |
| 4.8 | **A tentativa de volta em 1939, a espingarda, as torturas com óleo, o rádio no porão e a ajuda humanitária de 1945.** O cap. 7 já declara que tudo vem só da Marise (ficha 7:44). Mesmo assim, o cap. 16:85 repete a espingarda e o rádio como fato e os situa em 1941. | `16_standesamt.md:85` | Depoimentos identificados; arquivo da DOPS-SC e Ituporanga. | B |
| 4.9 | **O ofício de Johann ("estucador", "família de pedreiros", "intérprete de dialetos")** vem só da Marise. O *Formosa* diz *Agricult.* e o assento de 1884 diz que o pai era *Fabrikarbeiter*. O livro discute isso (5:37), mas no resto do texto "estucador" aparece como certo. | `04_antes_da_partida.md:67–69`; `16_standesamt.md:31` | Livros de *Gewerbe* ou carteira de trabalho; documentos brasileiros (ficha consular, carteira de estrangeiro, cerca de 1938–1942, Arquivo Nacional / SC). | B |
| 4.10 | **Maria ordenhava vacas por salário.** O cap. 4:81 e o cap. 14:19 constroem toda a tese de "filha que não herdou" sobre essa frase. | `04_antes_da_partida.md:81`; `14_o_que_se_herda.md:19` | Não há como confirmar diretamente; deve ser marcado como tradição. | B |

### 4.2 Cenas e diálogos reconstituídos

Estão sinalizados, mas convém revisar o critério:

- `04_antes_da_partida.md:117`: o diálogo "*Und wenn ihr nicht zurückkommt?*".
- `06_anjos_de_gesso.md:89–93`: o diálogo "*Kommt der Vater heute?*" e a cena da tarde no Rio Novo.
- `06_anjos_de_gesso.md:17`: Maria lendo a carta à luz de lampião.
- `16_standesamt.md:69`: Josef no cartório.
- `17_heumaden_moosbach.md:67`: o batismo da Mota.
- `09_matriarca_arend.md:37`: o aniversário de Angela no mar.

**Prior. B.** Os diálogos em alemão são as reconstituições mais fortes do livro. Sugere-se marcá-los em itálico com a indicação "cena imaginada", como no cap. 16.

### 4.3 Afirmações sem fonte que não vêm da Marise

| # | Afirmação | Onde | Prior. |
|---|---|---|---|
| 4.11 | **"Os Haas eram católicos"**: plausível, mas sem fonte brasileira, como um batismo dos filhos. | `01_vidal_ramos.md:45` | B |
| 4.12 | **"*Böhmischer Wind*" como nome local do vento.** Termo não documentado. | `04_antes_da_partida.md:17` | B |
| 4.14 | **"As Bodas de 65 anos em maio de 2012"** contradiz o cap. 1:41, que diz não ter a data do casamento. Ver 1.2/Baldoíno. | `19_epilogo.md:13` | M |
| 4.15 | **A data das Bodas de Ouro, 1957**, é uma dedução (o cap. 7:79 diz isso), mas a legenda da foto (2:37) a apresenta como dado. | `02_fata_e_mota.md:37` | B |
| 4.16 | **A fazenda de Júlio Carlos Lohmann em Erechim, invadida em 1923**, vem de um comentário de blog. O livro já marca isso como tradição. | `12_vale_do_taquari.md:101`; `14_o_que_se_herda.md` (nota `julio`) | B |
| 4.17 | **A nota de fontes (cap. 20) não lista o que de fato foi usado** para as reportagens de Joinville, o blog de Fazenda Lohmann e o *Find a Grave*. A ficha 9:80 aponta para `livros_e_artigos_internet/10_…md`, caminho que não existe no repositório. | `20_nota_fontes.md:11`; `09_matriarca_arend.md:80` | M |

---

## 5. Inconsistências README ↔ GEDCOM ↔ livro (resumo para correção)

| Dado | README | GEDCOM | Livro | Prevalece |
|---|---|---|---|---|
| Nascimento de Johann | 11/07/1884 | **08/07/1884** | 11/07 | Assento nº 47 → 11/07 |
| Batismo e madrinha de Maria Meier | 08/04, Katharina Meier | — | 07/04, Reichenberger | Moosbach p. 441 → livro |
| Testemunhas do casamento Meier–Voit | Puff / Hammerl | — | M. Meier / J. Voit | Imagem → livro |
| Padrinho de Georg Adam | Georg Balk, 10/03 | — | Adam Hartung, 09/03 | Imagem (conferir) |
| Madrinha de Franziska Voit | Franziska Woppmann, 30/06 | — | Margaretha Albrecht, 29/06 | Imagem (conferir) |
| Gertrudes Haas | * 22/10/1911, embarcou | — | * 05/05/1913 (Marise) | *Formosa* exclui 1911; 1913 ainda sem prova |
| Crianças do *Formosa* | Lina/Valter (README:230, 276) | — | Luisa/Walter | *Formosa* → Luisa/Walter ⟲ |
| Filhos de Johann e Maria | 11 | — | 11 e 12 (incoerente) | Planilha (totais) → 12 |
| Local de nascimento de Baldoíno | Rio Novo, Ituporanga | **Rio Novo, Águas Mornas** | Rio Novo, Ituporanga | Ituporanga; corrigir o FamilySearch |
| Morte de Gertrudes Preiss | 09/04/1970 | 14/04/1970 (registro) | 09/04 | Certidão → 09/04 |
| Nascimento de Ignazia Loch | 1828, S. Pedro de Alcântara | idem | aproximado | Aproximado |
| Nascimento de Anna Eller | 1858, RS | "generated" | 1858, RS | Sem fonte ⟲ |
| Carlos Doerner | 1 pessoa | "merger of 3–4 men" | 1 pessoa | Separar no FamilySearch ⟲ |
| Assento nº 23/1900 | transcrição Auling/Hömke | — | duas leituras | Imagem ⟲ |
| Filhos da Mota (irmãos Meier) | "8 filhos" e 7 nomes | — | 7 e 8 | Moosbach |

---

## 6. Ordem sugerida de trabalho

1. **Privacidade (0.4)** e **transcrições fabricadas no README (0.1, 2.10)**: são erros que já estão publicados.
2. **Contagem de filhos (0.2)**, **Marise prima ou irmã (0.3)** e **parentesco de Gertrudes com Angela (2.9)**: correções de texto rápidas.
3. **Nova exportação do GEDCOM** com o lado de Bárbara e os colaterais (0.7); **corrigir no FamilySearch** a data de Johann, o local de Baldoíno e o perfil mesclado de Carlos.
4. **Novas gerações**: quadro dos 12 netos de Baldoíno e Adelina (1.11), dos irmãos de Adelina (2.16), dos filhos de Erno e Rosita (3.8) e dos ascendentes Funke (3.11). Exige conversas com a família e consentimento.
5. **Fontes primárias a buscar**: Hemeroteca Digital (Rio, março de 1913), Ilha das Flores, lotes de Anitápolis, batismo de Gertrudes, cemitérios de Aurora e de Brusque (lápides), casamento de 1947 e Eibenstock.
