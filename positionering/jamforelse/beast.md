---
layout: default_banner
title: "BEAst"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 13
---

# MASSIV+ och BEAst

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. BEAst och [DPP](dpp.md) är bärare och kanaler snarare än beräkningsstandarder - en affärstransaktionsstandard respektive ett register som MASSIV+-data kan flöda i. Ny här? Läs [introduktionen](../../introduktion.md) först.

BEAst (Byggbranschens Elektroniska Affärsstandard) är byggsektorns informationsstandard för de affärsprocesser som omger en leverans: upphandling, inköp, logistik och fakturering. Den ideella föreningen bakom standarden har över 100 medlemmar. Den centrala standarden BEAst Supply 4.0 definierar den digitala följesedeln och utbyte av miljö- och klimatdata för transport, maskin och bulkmaterial, byggd på UBL (Universal Business Language) med PEPPOL som transportlager. Meddelandekedjan omfattar order, orderbekräftelse, leveransavisering (e-följesedel med exakta kvantiteter, artikel- och sändningsreferenser, ankomsttid och ansvarigt transportföretag) och transportstatus. Sedan 2023 kan en leverantör rapportera bränsleförbrukning per transport digitalt i enhetligt format, och köparen kan kräva mer detaljerade uppgifter - exempelvis bränsleförbrukning eller referenser till EPD och säkerhetsdatablad för godset. Trafikverket ställer från mars 2024 krav på rapportering av bränsleförbrukning enligt BEAst i upphandlingar för väg och anläggning.

BEAst och MASSIV+ ligger på olika logiska nivåer och är komplementära. BEAst standardiserar affärstransaktionen mellan två identifierade parter; MASSIV+ standardiserar utsläppsbokföringen på organisationsnivå. De möts i den bilaterala transaktionen, och strukturmatchningen är ovanligt tät:

- **Bilateral logik på samma teknikrygg.** MASSIV+:s princip "ditt Scope 1+2 är mitt Scope 3" har samma struktur som e-fakturan: säljarens utgående post är köparens ingående, och kedjan terminerar hos slutkonsumenten. BEAst Supply 4.0 vilar på UBL/PEPPOL, samma rygg som den europeiska e-fakturan. Den bilaterala kanal som MASSIV+:s specifikation ännu lämnar öppen finns alltså redan byggd och sektoradopterad.
- **Allokeringsnyckeln finns i meddelandet.** MASSIV+ §3 tillåter allokering per massa, kvantitet eller värde. Leveransaviseringen bär kvantiteter och artikelreferenser; fakturan bär värdet. De underlag en nod behöver för sina Share-koefficienter passerar alltså redan genom BEAst.
- **Identifierad motpart.** MASSIV+ kräver en namngiven nod i andra änden för att bokföringen ska gå ihop. BEAst löser partsidentifiering (PEPPOL) i sina meddelanden.

Skillnaden ligger i vad som är standardiserat på klimatsidan. BEAst:s klimatdata är på transaktions- och aktivitetsnivå - bränsleförbrukning för en transport, plus möjlighet att referera EPD för godset. Det är metodologiskt närmare en transport- eller produktdeklaration än MASSIV+:s nodnivå, där nodens totala Scope 1+2 fördelas över samtliga kunder. Det BEAst lämnar öppet är precis det MASSIV+ tillför: ett gemensamt emissionsfaktorset som gör bränsledata jämförbar mellan aktörer (BEAst tar inte ställning till vilken faktor en liter diesel ska multipliceras med), samt A/U-separation, Coverage och massbalans som gör enskilda följesedelsvärden till en koherent och propagerbar kedja - samma steg från lösa punktdeklarationer till värdekedjebild som skiljer MASSIV+ från en ren EPD-strategi (se [EPD-avsnittet](epd.md)). Relationen liknar den till DPP - BEAst är en bärare och datakälla, inte ett beräkningssystem - men är tätare än DPP eftersom den är bilateral och transaktionsbunden, vilket matchar MASSIV+:s egen logik. MASSIV+-beräknad data (Actual, Unknown, Coverage) kan bäras som strukturerade element på en BEAst-följesedel eller faktura.

En praktisk konsekvens värd att hålla framme: bygg är en sektor där en bilateral transaktionsstandard redan är adopterad, redan bär en första klimatdatapunkt och har regulatoriskt tryck bakom sig. Det gör sektorn till en stark kandidat som ledsektor för tidig MASSIV+-adoption, eftersom skenan, partsidentifieringen och aktivitetsdatan redan ligger på plats. Den vinkeln hör hemma i [positionering och affärsvärde](../positionering-och-affarsvarde.md) om den utvecklas vidare.

| Dimension | BEAst (Supply 4.0) | MASSIV+ |
|---|---|---|
| Central enhet | Affärstransaktion / meddelande mellan två parter | Nod (organisatorisk enhet) |
| Systemtyp | Transaktions- och utbytesstandard | Propageringssystem |
| Teknikrygg | UBL / PEPPOL | Ännu ej specificerad (data spaces) |
| Klimatdata | Bränsle/CO₂ per transport, maskin, bulk; EPD-referens för gods | Nodens totala Scope 1+2 allokerat per kund |
| Konsistensgrund | Gemensamt meddelandeformat | Massbalans + standardiserat EF-set |
| Datakvalitetsmått | Saknas (köpare kan begära mer detalj) | Coverage = A/(A+U) per nod |
| Sektor | Byggsektorn | Sektoragnostiskt |
| Relation | Bärare och datakälla för MASSIV+-flöden | Bokföringslager ovanpå transaktionen |

### Nodnivån och BEAst:s parter

MASSIV+:s organisationsfokus, noden, möter BEAst:s partsidentifiering utan principiell krock, men nivåvalet behöver deklareras och mappas. BEAst identifierar parter med GLN (Global Location Number), som i sig är nivå-agnostiskt: en GLN kan peka på en juridisk person eller på en specifik plats eller leveranspunkt. Det speglar MASSIV+:s egen hållning, där en nod kan vara ett helt bolag eller en enskild anläggning. För det vanliga fallet, där leverantörens juridiska person sammanfaller med noden och en GLN, är mappningen i praktiken trivial: periodens BEAst-leveranser per kund ger allokeringsbasen, och nodens egna energidata ger totalen.

Två frågor kräver dock undersökning snarare än att antas bort:

- **Nod-till-part-mappning.** När noden modelleras finare än den kommersiella parten - en nod per fabrik eller produktionslinje, men fakturering under en gemensam GLN - säger BEAst inte vilken nod en viss leverans kom från. Den interna uppdelningen måste göras på företagets egen data och ligger ovanför BEAst.
- **Täckning av nodens utflöde.** Massbalansen kräver att nodens hela utflöde för perioden fördelas. BEAst ger leveranserna till BEAst-anslutna kunder, men en nod kan också leverera till kunder utanför BEAst, till slutkonsument, på export eller internt. Allokeringsbasens nämnare måste vara hela utflödet, inte bara den BEAst-täckta delen.

En egenskap i BEAst talar dessutom för MASSIV+:s nodmodell: klimatdatan gäller transporten och namnger ansvarigt transportföretag. De utsläppen hör i MASSIV+-termer till transportnodens Scope 1, medan godsets utsläpp hör till producentnoden. Att BEAst redan skiljer leverantör från transportör på följesedeln stödjer behandlingen av dem som separata noder.
