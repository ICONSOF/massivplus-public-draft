---
layout: default_banner
title: "MF-001 Lagerhantering"
parent: "Förslag"
nav_order: 1
forslag_id: MF-001
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§5, §8"
forslag_forfattare: Birger Löfgren
---

# MF-001 Lagerhantering

> **Status:** Utkast, 2026-11-21. Ingår inte i standarden. Berör §5 och §8. Författare: Birger Löfgren.
>
> Förslaget låter en nod hålla kvar utsläpp från inköpta varor som ligger i lager vid periodens slut, i ett lagerkonto för hela noden. [MF-006](mf-006-periodregel.md) anger när en post bokförs. Detta förslag anger hur en bokförd mängd fördelas när varorna inte levereras samma period som de köps in.

En nod fördelar periodens hela T på periodens mottagare ([§3](../standard/specifikation.md#krav-på-allokeringsregeln), [§5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)). Köper noden in varor som ligger kvar i lager vid periodens slut, fördelas utsläppen från dem ändå på periodens kunder. Nästa period levereras varorna utan att utsläppen från dem följer med.

- När lagret är stabilt jämnar det ut sig över tid.
- När lagret byggs upp blir periodens tal höga, och när det töms blir de låga. En kund kan läsa en sådan topp som att leverantören har blivit sämre.
- En nod kan lägga stora inköp i en period där en viss kund dominerar och på så sätt flytta börda mellan kunder över tid.
- Har noden inga leveranser under en period finns ingen att fördela T på, och massbalansen i §5 går inte att uppfylla. Specifikationen säger inte vad som då gäller.

[Metodologiska risker](../fordjupningar/metodologiska-risker.md#tidsdimensionen) anger lagerhantering som öppen.

## Förslag till standardtext

### §5: lägg till Lagerkonto

1. **Lagerkontot.** En nod får föra ett lagerkonto för utsläpp från inköpta varor som vid periodens slut finns kvar i nodens lager som råvaror, produkter i arbete eller färdiga varor. Lagerkontot gäller hela noden och knyts inte till enskilda varor eller artiklar.
2. **Val och konsekvens.** Noden dokumenterar om den för lagerkonto. Valet gäller från period till period och ändras bara under versionskontroll, som nodindelningen i §1. Har noden inga leveranser under en period ska den föra lagerkonto för perioden, och hela T förs då till lagerkontot. Det frigörs i nästa period med leveranser.
3. **Vad som förs till lagerkontot.** Inflöden från inköp som nodens ekonomiska bokföring redovisar som varulager, med Actual och Unknown var för sig. Egna Scope 1 och 2 och inköp av anläggningstillgångar förs inte till lagerkontot, utom enligt punkt 2.
4. **Värdering.** Lagerkontot värderas med genomsnittsmetoden och lagervärdena i den ekonomiska bokföringen. Kvoten k är utgående lagervärde delat med summan av ingående lagervärde och periodens lagerförda inköp. Utgående lagerkonto är k gånger summan av ingående lagerkonto och periodens lagerförda inflöden. Kvoten tillämpas lika på Actual och Unknown.
5. **Start.** Lagerkontot är noll vid början av nodens första period.
6. **Sena poster och rättelser.** Ersätter en sen post U för lagerförda inköp påverkar ersättningen både periodens fördelning och lagerkontot. Lagerkontot följer periodregeln i MF-006: det är preliminärt tills perioden är slutlig, och skillnader därefter behandlas enligt dess punkt 7.

### §5: ändra massbalansen

Nuvarande lydelse:

```
Σⱼ (Tᵢⱼ) = Tᵢ
```

Föreslagen lydelse:

```
Σⱼ (Tᵢⱼ) = Tᵢ − ΔLᵢ
```

> där ΔLᵢ är förändringen i nodens lagerkonto under perioden, för Actual och Unknown var för sig. För en nod utan lagerkonto är ΔLᵢ noll.

### §8: lägg till efter definitionen av Coverage

> För en nod med lagerkonto avser Coverage den mängd som fördelas under perioden: (S1ᵢ + S2ᵢ + Aᵢ − ΔL_Aᵢ) / (Tᵢ − ΔLᵢ), där ΔL_Aᵢ är förändringen i lagerkontots Actual.

## Lagerkontot följer inte varorna

Kontot gäller hela noden och värderas med den lagerförändring som redan finns i den ekonomiska bokföringen. Ingen vara spåras och inget tal knyts till en artikel. Noden håller bara tillbaka den andel av periodens lagerförda inflöden som motsvarar andelen av lagret som finns kvar.

Posten till kunden är fortfarande en mängd för relationen och perioden ([§5, individuation](../standard/specifikation.md#individuation-av-allokeringsenheten)). Det lagerkontot ändrar är hur stor del av nodens intag som fördelas under perioden.

Massbalansen bevarar fortfarande ansvaret för utsläpp. Det som förs till lagerkontot kommer ut en senare period, så summan över tid är densamma. Det är bokföringsekvationen med en balansräkning. Reichelstein bygger sin redovisning av koldioxid på samma sätt: egna och inköpta utsläpp förs till lager och vidare när varorna säljs, och summan för företaget påverkas inte av fördelningsregeln *"provided there are no build-ups or depletions in inventory"* (2024, s. 2136-2138). Lagerkontot tar hand om det fall där summan annars påverkas.

## Exempel

En nod köper in varor med 80 ton CO2e Actual och 20 ton Unknown under en period. Egna Scope 1 och 2 är 10 ton. Bokföringen visar ingående lager 0, lagerförda inköp 1 000 tkr och utgående lager 400 tkr. Nästa period köper noden inget, har 10 ton egna utsläpp och tömmer lagret. Talen är påhittade.

Period 1: k = 400 / (0 + 1 000) = 0,4. Utgående lagerkonto = 0,4 × 100 = 40 ton, varav 32 Actual och 8 Unknown.

Period 2: k = 0 / (400 + 0) = 0. Lagerkontot töms, och 40 ton frigörs.

| | Fördelas period 1 | Fördelas period 2 | Summa |
|---|---|---|---|
| Utan lagerkonto | 110 (Actual 90, Unknown 20) | 10 (Actual 10) | 120 |
| Med lagerkonto | 70 (Actual 58, Unknown 12) | 50 (Actual 42, Unknown 8) | 120 |

Summan är densamma. Med lagerkonto får kunderna i period 2 del av utsläppen från de varor de får, och toppen i period 1 försvinner. Coverage i period 1 blir 58 / 70 = 83 %.

## Signalen blir långsammare

Med lagerkonto når en leverantörs minskning kunderna först när lagret omsätts. Har noden ett halvårs lager tar det ungefär ett halvår innan minskningen syns fullt ut. Utan lagerkonto syns den i periodens fördelning direkt.

Det är förslagets viktigaste kostnad. Lagerkontot ger jämnare tal och ett tal som speglar periodens leveranser bättre. Det sker på bekostnad av hur snabbt en förändring uppströms når kunderna.

## A och U i lager

Actual och Unknown går in i och ut ur lagerkontot i samma proportion. Det gör att U som ligger i lager ersätts när en sen post kommer (punkt 6) och att Coverage räknas på det som faktiskt fördelas.

Utan lagerkonto gäller allt A i en nods utgående poster samma period som posterna ([MF-006](mf-006-periodregel.md)). Med lagerkonto kan en del av A komma från tidigare perioders inköp. Den delen redovisas öppet i nodens lagerkonto och motsvarar varor som faktiskt levereras under perioden.

## Kapitalvaror

Inköp av anläggningstillgångar förs inte till lagerkontot, eftersom en maskin inte levereras vidare till kunderna. Hur utsläppen från tillverkningen av maskinen ska fördelas är ännu inte avgjort. Förslaget lägger fram två alternativ.

**Alternativ 1: inköpsperioden.** Utsläppen ingår i T för den period då maskinen köps. GHG Protocols Scope 3-standard räknar kapitalvaror på det sättet, det år de köps. Det är enkelt, och en investering syns direkt i periodens fördelning. Ett år med en stor investering ger en topp i nodens tal.

**Alternativ 2: avskrivning.** Utsläppen förs till ett anläggningskonto och fördelas över tillgångens nyttjandeperiod, med samma avskrivningsplan som i den ekonomiska bokföringen. Det ligger nära bokföringen och följer samma resonemang som lagerkontot: maskinen används för leveranserna under flera perioder. Reichelstein delar upp kapitalvarornas koldioxid i årliga avskrivningar (2024, s. 2135), och Jia m.fl. föreslår detsamma. Toppen vid investeringen försvinner, men det tar längre tid innan en maskin med lägre utsläpp syns fullt ut. Noden behöver föra kontot per tillgång eller grupp av tillgångar, vilket bokföringen redan gör.

Med båda alternativen gäller massbalansen över tid. Alternativ 2 kräver en term för anläggningskontot i formeln för massbalans, på samma sätt som lagerkontot.

## Nodens egen Scope 3-redovisning

Lagerkontot påverkar bara hur noden fördelar till sina kunder. Rapporterar noden enligt GHG Protocol räknas inköpta varor det år de köps (Scope 3-standarden, avsnittet *Time boundary of scope 3 categories*). Det motsvarar nodens inflöde av A och U, oberoende av lagerkontot.

## Små noder

Lagerkontot är frivilligt, utom för perioder utan leveranser. En nod med litet eller stabilt lager kan avstå. Då gäller massbalansen som i dag, och lagerförändringarna jämnar ut sig över tid. En nod som väljer år som period enligt MF-006 har dessutom mindre lagerförändring i förhållande till periodens flöde än en nod som räknar per kvartal.

## Förhållande till andra förslag

- **MF-006** avgör vilken period en post gäller och när den är slutlig. Lagerkontot följer samma regel.
- **MF-002** jämför utgående och inkommande mängder för ett område. För en nod med lagerkonto ska jämförelsen justeras för lagerförändringen.
- **MF-004** kräver att nodens hela T fördelas. För en nod med lagerkonto avser det T minus lagerförändringen.
- **MF-007** gäller egna aktivitetsdata, som inte förs till lagerkontot.

## Alternativ som övervägts

- **Inget lagerkonto, med en särskild regel för perioder utan leveranser.** Enklare och ger snabbare signal. Toppar vid lageruppbyggnad och möjligheten att flytta börda med tidpunkten för inköp står kvar.
- **Värdering per artikel eller parti.** Skulle göra talet till en egenskap hos varan och kräva spårning, vilket specifikationen undviker i nod-till-nod-flöden.
- **Först in, först ut.** Kräver att partier hålls isär. Genomsnittsmetoden räcker och finns redan i bokföringen.
- **Glidande medelvärde av T över flera perioder.** Jämnar ut toppar men bryter massbalansen inom perioden och skiljer inte lager från andra svängningar.
- **Krav på lagerkonto när lagret ändras mycket.** Skulle kräva en gräns. Förslaget lämnar valet till noden, med krav bara för perioder utan leveranser.

## Öppna frågor

- **Egna utsläpp i tillverkade varor.** Ska egna Scope 1 och 2 för varor som tillverkats men inte levererats också föras till lagerkontot, som i Reichelsteins modell och i kostnadsredovisningen? Förslaget avstår för att hålla det enkelt.
- **Ingående lager vid start.** Ska det kunna sättas till ett underlag för U i stället för noll, så att utsläppen från varor som köpts före första perioden inte faller bort?
- **Frivilligheten.** Räcker det att valet är dokumenterat och konsekvent, eller ska lagerkonto krävas för vissa noder, till exempel handelsnoder med stort lager?
- **Kapitalvaror.** Alternativ 1 eller 2 i avsnittet om kapitalvaror, och om alternativ 2 ska vara frivilligt på samma sätt som lagerkontot.
- **Gränsen mot kapitalvaror.** Var går gränsen för förbrukningsinventarier och reservdelar som lagerförs men används i den egna verksamheten?

## Källor

- Jimmy Jia, Barbara Rossi, Abrar Chaudhury, Evan Taylor och Dennis West, "A reporting framework for general purpose life cycle assessment to align entity-level GHG accounting with general purpose financial statements", arbetspapper, SSRN 4395987, version 22 april 2024, s. 17-21. [doi:10.2139/ssrn.4395987](https://doi.org/10.2139/ssrn.4395987)
- Stefan Reichelstein, "Corporate carbon accounting: balance sheets and flow statements", *Review of Accounting Studies* 29 (2024), s. 2125-2156, här s. 2135-2138. [doi:10.1007/s11142-024-09830-y](https://doi.org/10.1007/s11142-024-09830-y)
- GHG Protocol, *Corporate Value Chain (Scope 3) Accounting and Reporting Standard* (2011), kapitel 5, *Time boundary of scope 3 categories*. [PDF](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard_041613.pdf)

## Beslut

Inte behandlat. Förslaget avser tillägg till §5 och §8 och en ändring av massbalansformeln i §5. Hur kapitalvaror ska behandlas avgörs inom förslaget.
