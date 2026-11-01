# 🌳 Árvore Genealógica — Famílias Haas, Meier, Doerner, Funke & Hoeveler

Repositório dedicado à preservação histórica, documentação comprobatória e transcrição de registros das famílias **Haas**, **Meier**, **Doerner**, **Funke** e **Hoeveler**, reunindo fontes dos arquivos civis e eclesiásticos da Alemanha (Baviera) e do Brasil (Santa Catarina).

---

## 📌 Árvore Genealógica Unificada (Alto Contraste)

```mermaid
graph TD
    classDef default fill:#1e293b,stroke:#64748b,stroke-width:2px,color:#ffffff;
    classDef trisavos fill:#1e293b,stroke:#94a3b8,stroke-width:2px,color:#ffffff;
    classDef bisavos fill:#0f3f6e,stroke:#38bdf8,stroke-width:2px,color:#ffffff;
    classDef avos fill:#1e1b4b,stroke:#818cf8,stroke-width:2px,color:#ffffff;
    classDef pais fill:#14532d,stroke:#4ade80,stroke-width:2px,color:#ffffff;
    classDef casamento fill:#334155,stroke:#cbd5e1,stroke-width:1px,color:#ffffff;
    classDef casal fill:#701a75,stroke:#f472b6,stroke-width:3px,color:#ffffff;

    %% RAMO HAAS (Baviera)
    JH1["<b>Josef Haas</b><br/><i>* Sandberg/Leonberg</i>"]:::trisavos --- M_JH["Casamento"]
    FD1["<b>Franziska Dengler</b>"]:::trisavos --- M_JH
    M_JH --> B_JH["<b>Johann Haas</b><br/><i>* 11.07.1884 (Sandberg, Baviera)<br/>† 1969 (Aurora, SC)</i>"]:::bisavos

    %% RAMO MEIER & VOIT (Heumaden, Baviera)
    MM1["<b>Georg Adam Meier</b><br/><i>* 09.03.1859 (Heumaden)</i>"]:::trisavos --- M_MV["Casamento: 23.11.1884"]
    FV1["<b>Franziska Voit</b><br/><i>* 29.06.1861 (Burgtreswitz)</i>"]:::trisavos --- M_MV
    M_MV --> B_MM["<b>Maria Meier (Meyer)</b><br/><i>* 07.04.1888 (Heumaden)<br/>† 1973 (Aurora, SC)</i>"]:::bisavos

    %% CASAMENTO BISAVÓS HAAS x MEIER (1907 na Alemanha)
    B_JH --- CasalHaasMeier["💍 <b>Casamento: 1907 (Alemanha)</b><br/><i>Imigração em 1913 no navio Formosa</i>"]:::casamento
    B_MM --- CasalHaasMeier
    CasalHaasMeier --> A_BH["<b>Baldoíno Haas</b><br/><i>* 1924 (Ituporanga, SC)</i>"]:::avos

    %% RAMO DOERNER & PREISS (Santa Catarina)
    CD1["<b>Carlos Dörner</b>"]:::trisavos --- M_CD["Casamento"]
    AE1["<b>Anna Eller</b>"]:::trisavos --- M_CD
    M_CD --> B_FD["<b>Fernando Dörner</b><br/><i>* ~1898 (Imaruí, SC)<br/>† 21.05.1981 (Brusque, SC)</i>"]:::bisavos

    MP1["<b>Manoel Preiss (Preus)</b>"]:::trisavos --- M_MP["Casamento"]
    HM1["<b>Helena Michels</b>"]:::trisavos --- M_MP
    M_MP --> B_GP["<b>Gertrudes Preiss</b><br/><i>* ~1896 (Imaruí, SC)<br/>† 09.04.1970 (Brusque, SC)</i>"]:::bisavos

    B_FD --- CasalDoernerPreiss["💍 <b>Casamento em SC</b>"]:::casamento
    B_GP --- CasalDoernerPreiss
    CasalDoernerPreiss --> A_AD["<b>Adelina Doerner</b><br/><i>* Imaruí / Brusque, SC</i>"]:::avos

    %% CASAMENTO BALDOÍNO x ADELINA
    A_BH --- CasalBaldoinoAdelina["💍 <b>Casamento: 1947</b><br/><i>65 anos de bodas em 2012</i>"]:::casamento
    A_AD --- CasalBaldoinoAdelina
    CasalBaldoinoAdelina --> P_RH["⭐ <b>Reinaldo Haas</b>"]:::casal

    %% RAMO FUNKE & HOEVELER (Esposa Bárbara)
    EH1["<b>Erno Hoeveler</b><br/><i>('Vô Erno')</i>"]:::trisavos --- M_EH["Casamento"]
    RO1["<b>Rosita Hoeveler</b><br/><i>('Oma Rosita')</i>"]:::trisavos --- M_EH
    M_EH --> M_ILH["<b>Ilusca Leocádia Hoeveler</b>"]:::pais

    PF1["<b>Família Funke</b>"]:::trisavos --> P_CHF["<b>Carlos Heinz Funke</b>"]:::pais

    P_CHF --- CasalFunkeHoeveler["💍 <b>Casamento</b>"]:::casamento
    M_ILH --- CasalFunkeHoeveler
    CasalFunkeHoeveler --> P_BFH["⭐ <b>Bárbara Funke Haas</b><br/><i>* 27.07.1972</i>"]:::casal

    %% CASAL ATUAL
    P_RH === CasalAtual["💑 <b>Reinaldo Haas & Bárbara Funke Haas</b>"]:::casamento === P_BFH
```

---

## 📋 Quadro Sinótico das Gerações

| Geração | Linha / Ramo | Pessoa | Datas & Locais | Filiação / Cônjuge |
| :--- | :--- | :--- | :--- | :--- |
| **Geração Atual** | **Haas — Funke** | **Reinaldo Haas** | Santa Catarina | Filho de Baldoíno Haas e Adelina Doerner; casado com Bárbara Funke Haas |
| **Geração Atual** | **Funke — Hoeveler** | **Bárbara Funke Haas** | * 27/07/1972 | Filha de Carlos Heinz Funke e Ilusca Leocádia Hoeveler Funke; casada com Reinaldo Haas |
| **Avós (Pat.)** | **Haas** | **Baldoíno Haas** | * 1924 em Ituporanga, SC | Filho de Johann Haas e Maria Meier; casou-se em 1947 com Adelina Doerner |
| **Avós (Pat.)** | **Doerner** | **Adelina Doerner Haas** | Imaruí / Vidal Ramos / Brusque, SC | Filha de Fernando Dörner e Gertrudes Preiss; casou-se com Baldoíno Haas |
| **Pais (Esposa)** | **Funke** | **Carlos Heinz Funke** | Santa Catarina | Pai de Bárbara Funke Haas; casado com Ilusca Leocádia Hoeveler |
| **Pais (Esposa)** | **Hoeveler** | **Ilusca Leocádia Hoeveler Funke** | Santa Catarina | Filha de Erno Hoeveler e Rosita Hoeveler; mãe de Bárbara Funke Haas |
| **Bisavós** | **Haas** | **Johann Haas** | * 11/07/1884 (Sandberg/Leonberg, Baviera) <br/> † 1969 (Aurora, SC) | Filho de Josef Haas e Franziska Dengler; casou-se em 1907 na Alemanha com Maria Meier |
| **Bisavós** | **Meier (Meyer)** | **Maria Meier Haas** | * 07/04/1888 (Heumaden, Baviera) <br/> † 1973 (Aurora, SC) | Filha de Georg Adam Meier e Franziska Voit; casou-se em 1907 com Johann Haas |
| **Bisavós** | **Doerner** | **Fernando Dörner** | * ~1898 em Imaruí, SC <br/> † 21/05/1981 em Brusque, SC | Filho de Carlos Dörner e Anna Eller; casou-se com Gertrudes Preiss |
| **Bisavós** | **Preiss** | **Gertrudes Preiss Doerner** | * ~1896 em Imaruí, SC <br/> † 09/04/1970 em Brusque, SC | Filha de Manoel Preiss e Helena Michels; casou-se com Fernando Dörner |
| **Trisavós** | **Meier** | **Georg Adam Meier** | * 09/03/1859 (Rückersrieth / Heumaden, Baviera) | Filho de Michael Meier e Margaretha Pfannenstein; casou-se em 23/11/1884 com Franziska Voit |
| **Trisavós** | **Voit** | **Franziska Voit Meier** | * 29/06/1861 (Burgtreswitz, Baviera) | Filha de Johann Voit e Barbara Woppmann; casou-se em 23/11/1884 com Georg Adam Meier |
| **Trisavós** | **Haas** | **Josef Haas** | Sandberg / Leonberg, Baviera | *Fabrikarbeiter* (operário / pedreiro); casado com Franziska Dengler |
| **Trisavós** | **Dengler** | **Franziska Dengler Haas** | Sandberg / Leonberg, Baviera | Mãe de Johann Haas |
| **Trisavós** | **Doerner** | **Carlos Dörner** | Santa Catarina | Casado com Anna Eller; pais de Fernando Dörner |
| **Trisavós** | **Eller** | **Anna Eller Dörner** | Santa Catarina | Mãe de Fernando Dörner |
| **Trisavós** | **Preiss** | **Manoel Preiss** | Imaruí, SC | Casado com Helena Michels; pais de Gertrudes Preiss |
| **Trisavós** | **Michels** | **Helena Michels Preiss** | Imaruí, SC | Mãe de Gertrudes Preiss |

---

## 📷 Fotografia Histórica — Johann Haas e Maria Meyer Haas

<p align="center">
  <img src="imagens/foto_familia_johann_haas_e_maria_meyer.jpg" width="80%" alt="Família Johann Haas e Maria Meyer Haas com os filhos" />
</p>
<p align="center"><i>Johann Haas, Maria Meyer Haas e filhos (Fernando, Alexandre, Gertrudes, Agnes, Elza, Baldoíno e Maria).</i></p>

---

## 📜 Registros Documentais Comprobatórios

### 1. Certidão Civil de Nascimento de Johann Haas (1884, Baviera)
* **Ofício:** *Standesamt Leonberg* (atualmente Maxhütte-Haidhof, Baviera), Registro nº 47/1884
* **Nascimento:** 11 de julho de 1884 em Sandberg
* **Pai:** Josef Haas (*Fabrikarbeiter*) | **Mãe:** Franziska Haas, nascida Dengler

![Nascimento de Johann Haas 1884](imagens/doc_haas_nascimento_johann_1884.jpg)

---

### 2. Lista Oficial de Bordo — Chegada ao Brasil no Navio *Formosa* (1913)
* **Data de Desembarque:** 26 de março de 1913 (Vapor *Formosa*, procedência Marselha)
* **Entradas:** 
  * Nº 161: **Haas, Johann** (28 anos, agricultor)
  * Nº 162: **Haas, Maria** (25 anos, agricultora)
  * Nº 163: **Haas, Luisa** (2 anos)
  * Nº 164: **Haas, Walter** (1 ano)

![Lista de Passageiros Navio Formosa 1913](imagens/doc_haas_navio_formosa_1913.jpg)

---

### 3. Casamento dos Trisavós Georg Adam Meier & Franziska Voit (1884, Moosbach)
* **Data:** 23 de novembro de 1884
* **Livro:** *Trauungen 1853–1935* (`Moosbach_Leuchtenberg013`), Página 93, Registro nº 20
* **Paróquia:** St. Peter und Paul, Markt Moosbach, Diocese de Regensburg

![Casamento Meier - Voit 1884](imagens/doc2_trauung_meier_voit_1884.jpg)

---

### 4. Batismo da Bisavó Maria Meier (1888, Moosbach / Heumaden)
* **Nascimento:** 07 de abril de 1888, às 2:00 da madrugada em Heumaden
* **Livro:** *Taufen 1847–1904* (`Moosbach_Leuchtenberg005`), Página 441, Reg. nº 36

![Batismo de Maria Meier 1888](imagens/doc1_maria_meier_1888.jpg)

---

### 5. Certidão de Óbito de Fernando Dörner (1981, Brusque, SC)
* **Ofício:** Registro Civil de Brusque, SC (Livro C-32, Fls. 51, Termo nº 1400)
* **Falecimento:** 21 de maio de 1981 (83 anos, viúvo de Gertrudes Preiss)
* **Filiação:** Carlos Dörner e Anna Eller

![Óbito de Fernando Dörner 1981](imagens/doc_doerner_obito_fernando_1981.jpg)

---

### 6. Certidão de Óbito de Gertrudes Preiss Dörner (1970, Brusque, SC)
* **Ofício:** Registro Civil de Brusque, SC (Livro 32, Fls. 178, Termo nº 7778)
* **Falecimento:** 09 de abril de 1970 (74 anos, casada com Fernando Dörner)
* **Filiação:** Manoel Preiss e Helena Michels
* **Filhos Registrados:** Hilda, Ana, Lindolfo, **Adelina**, Irma, Olga, Lino Fernando

![Óbito de Gertrudes Preiss Dörner 1970](imagens/doc_doerner_obito_gertrudes_preiss_1970.jpg)
