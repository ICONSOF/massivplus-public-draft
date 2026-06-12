---
layout: default
title: "MASSIV+"
permalink: /
---

# MASSIV+

> Öppen standard för beräkning och propagering av utsläppsdata i värdekedjor - på organisationsnivå.

---

## Vad är problemet?

Den övergripande utmaningen är omställningen till netto noll klimatpåverkan; allt annat är ohållbart. Att minska utsläpp kräver data som visar var en åtgärd ska sättas in. Sådan information är notoriskt svår att etablera. Etablerade standarder för beräkning av klimatpåverkan är breda och lämnar svåra frågor obesvarade - frågor som kräver specialistkompetens. Svårast är att beräkna de indirekta emissionerna, så kallade Scope 3. Men faktum är att även de relativt enklare emissionerna från användning av bränsle och energi som el och fjärrvärme - Scope 1 och 2 - också är svåra att etablera för den oinsatte. Metoderna kräver alltid uppskattningar, och dagens praxis omfattar mer eller mindre sofistikerade metoder för att göra dessa ofta grova antaganden. Data blir därmed godtycklig, vilket är svårt att grunda välriktade åtgärder på.

## Hypoteser

Två krav följer. Datan måste vara faktisk snarare än uppskattad - godtyckliga emissionsfaktorer ger godtycklig data - och den måste ligga på rätt nivå.

Bolagsnivå (typisk årsredovisning) är för grov: den visar att en kategori är stor, men inte vilken anläggning, vilken leverantörsrelation eller vilket flöde som driver den. Skillnaden mellan *"vår Scope 3 är 80 % av totalen"* och *"anläggning B står för X kton"* är skillnaden mellan att veta att man har ett problem och att kunna göra något åt det. Produktnivå (PCF) ligger i andra änden: metodologiskt precis, men kräver LCA-kompetens och spårbarhet genom hela kedjan - i praktiken oåtkomlig för de allra flesta organisationer.

Mellan dessa två nivåer finns ett tomrum som operativt sammanfaller med mandatet för åtgärder: **organisationsenhetsnivå**. Tillräckligt detaljerat för att vägleda åtgärder, tillräckligt aggregerat för att vara realistiskt att samla in.

Om vi på den nivån väljer ett gemensamt, standardiserat set av Scope 1- och Scope 2-emissionsfaktorer, underlättar vi för organisationer att etablera denna data. Informationen som behövs ligger nära verksamheten och kräver inga eller väldigt få gissningar.

Om man delar den informationen skapas Scope 3 utan gissningar - eftersom mitt Scope 1 och 2 är ditt Scope 3.

## Tre frågor en sådan ansats måste lösa

Att redovisa utsläpp på organisationsnivå och propagera dem genom värdekedjan reser tre metodologiska frågor:

- **Aggregering.** Hur aggregeras data från en komplex värdekedja utan att dess användbarhet går förlorad?
- **Allokering.** Hur allokeras uppströms utsläpp till en enskild nod, och vidare från en nod med flera utflöden (multi-output)?
- **Intern handel.** Många bolag tillverkar en produkt i steg över flera anläggningar utan att spåra produktdata internt. Hur hanteras informationsförlusten vid denna interna handel?

Hur MASSIV+ besvarar dem beskrivs i [introduktionen](introduktion.md) och i [specifikationen](standard/specifikation.md).

## Vad gör MASSIV+?

MASSIV+ modellerar värdekedjan som ett riktat nätverk av noder. Varje nod rapporterar sina egna Scope 1+2 med standardiserade emissionsfaktorer och allokerar dem proportionellt vidare till sina kunder. Mottagaren bygger sin Scope 3 nedifrån från faktisk data - inte uppifrån med branschschabloner.

Standarden vilar på tre principer:

- **Ditt Scope 1+2 är mitt Scope 3.** Bilateral bokföring av utsläppsflöden mellan motparter. Scope 3 byggs nedifrån från verklig data.
- **Faktisk data eller okänt.** Ingen uppskattning får samma status som faktisk data. Faktisk data (A) och okänt (U) hålls strukturellt åtskilda; U kvantifieras bara som täckningsunderlag för Coverage.
- **Standardiserade emissionsfaktorer.** Alla noder använder samma fastställda set. Eftersom ditt Scope 1+2 är någons Scope 3 måste underlaget vara jämförbart.

---

## Läsguide

Beroende på hur djupt du vill gå:

| Läsning | Tid | Innehåll |
|---|---|---|
| **[Introduktion](introduktion.md)** | 10 min | Genomgång av problem, idé, principer och funktionsförskjutning. Står på egna ben. |
| **[Specifikation](standard/specifikation.md)** | 45 min | Den fullständiga tekniska beskrivningen av standarden - den normativa kärnan. Noddefinition, allokering, massbalans, replacement rule, Coverage, cirkulära flöden. |
| **[Positionering](positionering/README.md)** | 5-15 min styck | Hur MASSIV+ förhåller sig till praktik, standarder och regelverk: jämförelse med andra ramverk, positionering och affärsvärde, MASSIV+ vs ecoinvent. |
| **[Fördjupningar](fordjupningar/README.md)** | 5-15 min styck | Fristående texter som fördjupar och utvecklar konceptet: bokföringsanalogin, exempel i stålvärdekedjan, metodologiska risker, avfallsförbränning, kompensation. |

Förslag på läsväg för en första gång: **läs introduktionen.** Den ger hela tankefiguren. Därefter kan du klicka vidare till det som intresserar mest. Den fullständiga specifikationen är till för den som vill ner i de tekniska detaljerna.

---

## Hur du kan bidra

Det här är ett publikt utkast under utveckling, och förslag är välkomna. Se [CONTRIBUTING.md](CONTRIBUTING.md) för hur frågor, kommentarer och ändringsförslag tas emot. Tröskeln är låg: du behöver bara ett Github-konto, ingen lokal Git-installation.

## Status och kontakt

MASSIV+ är ett pågående utvecklingsarbete. Texterna här är arbetsdokument under granskning och vidareutveckling. Frågor och kommentarer går till `info@massivplus.org` eller via [Discussions](https://github.com/ICONSOF/massivplus-public-draft/discussions).

Senaste version av specifikationen: 2026-05-25.

Källkod för referensimplementationen (en interaktiv simulator) ligger i ett separat repo: [ICONSOF/MASSIV_node_approach](https://github.com/ICONSOF/MASSIV_node_approach).
