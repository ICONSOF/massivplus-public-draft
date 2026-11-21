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
> Förslaget låter en nod spara utsläppen från varor som ligger i lager vid periodens slut, och fördela dem när varorna levereras. [MF-006](mf-006-periodregel.md) anger när en post bokförs. Det här förslaget anger hur en bokförd mängd fördelas.

En nod fördelar hela periodens T på periodens mottagare ([§5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)). Ligger inköpta varor kvar i lager vid periodens slut, går utsläppen från dem ändå till periodens kunder. Det ger tre problem:

1. När lagret byggs upp blir periodens tal höga, och när det töms blir de låga. En kund kan tro att leverantören har blivit sämre eller bättre.
2. En nod kan flytta börda mellan kunder genom att välja när den köper in.
3. Har noden inga leveranser under en period finns ingen att fördela T på, och massbalansen (bevarandeprincipen, om [MF-008](mf-008-namnbyte.md) antas) går inte att uppfylla.

[Metodologiska risker](../fordjupningar/metodologiska-risker.md#tidsdimensionen) anger lagerhantering som öppen.

## Förslag till standardtext

### §5: lägg till Lagerkonto

1. **Lagerkontot.** En nod får föra ett lagerkonto för utsläppen från inköpta varor som finns kvar i lager vid periodens slut, som råvaror, produkter i arbete eller färdiga varor. Kontot gäller hela noden och knyts inte till enskilda varor.
2. **Valet.** Noden dokumenterar om den för lagerkonto, och valet ändras bara under versionskontroll. Har noden inga leveranser under en period ska den föra lagerkonto den perioden. Hela T förs då till kontot och fördelas nästa period med leveranser.
3. **Vad som förs till kontot.** Inköp som den ekonomiska bokföringen redovisar som varulager, med Actual och Unknown var för sig. Egna Scope 1 och 2 och inköp av anläggningstillgångar förs inte dit, utom enligt punkt 2.
4. **Värdering.** Andelen som stannar i lager beräknas ur den ekonomiska bokföringen: k = utgående lagervärde / (ingående lagervärde + periodens lagerförda inköp). Utgående lagerkonto = k × (ingående lagerkonto + periodens lagerförda inflöden). Samma k gäller för Actual och Unknown.
5. **Start.** Lagerkontot är noll när noden börjar.
6. **Sena poster.** Lagerkontot följer periodregeln i MF-006. En sen post för varor i lager ändrar både periodens fördelning och lagerkontot.

### §5: ändra massbalansen

Nuvarande lydelse:

```
Σⱼ (Tᵢⱼ) = Tᵢ
```

Föreslagen lydelse:

```
Σⱼ (Tᵢⱼ) = Tᵢ − ΔLᵢ
```

> där ΔLᵢ är förändringen i nodens lagerkonto under perioden, för Actual och Unknown var för sig. Utan lagerkonto är ΔLᵢ noll.

### §8: lägg till efter definitionen av Coverage (faktisk andel, om [MF-008](mf-008-namnbyte.md) antas)

> För en nod med lagerkonto räknas Coverage på den mängd som fördelas: (S1ᵢ + S2ᵢ + Aᵢ − ΔL_Aᵢ) / (Tᵢ − ΔLᵢ), där ΔL_Aᵢ är förändringen i lagerkontots Actual.

## Exempel

En nod köper varor med 80 ton CO2e Actual och 20 ton Unknown. Egna Scope 1 och 2 är 10 ton. Lagret var tomt i början av perioden. Enligt bokföringen köptes varor för 1 000 tkr, och lagret är värt 400 tkr vid periodens slut. Nästa period köper noden inget, släpper ut 10 ton och tömmer lagret. Talen är påhittade.

Period 1 är k = 400 / 1 000 = 0,4. Kvar i lagerkontot: 0,4 × 100 = 40 ton, varav 32 Actual och 8 Unknown. Period 2 töms kontot.

| | Period 1 | Period 2 | Summa |
|---|---|---|---|
| Utan lagerkonto | 110 (A 90, U 20) | 10 (A 10) | 120 |
| Med lagerkonto | 70 (A 58, U 12) | 50 (A 42, U 8) | 120 |

Summan är densamma. Med lagerkonto följer utsläppen med när varorna levereras, och toppen i period 1 försvinner.

## Varför det fungerar med MASSIV+

Kontot gäller hela noden och värderas med lagervärden som redan finns i bokföringen. Ingen vara spåras. Posten till kunden är fortfarande en mängd för relationen och perioden ([§5, individuation](../standard/specifikation.md#individuation-av-allokeringsenheten)).

Massbalansen bevarar fortfarande ansvaret för utsläpp. Det som sparas i lagret kommer ut senare, så summan över tid är densamma. Det är bokföringsekvationen med en balansräkning. Reichelstein bygger sin redovisning av koldioxid på samma sätt (2024, s. 2136-2138).

Nodens egen Scope 3-redovisning enligt GHG Protocol påverkas inte. Där räknas inköpta varor det år de köps, och det motsvarar nodens inflöde.

## Vad det kostar

Det viktigaste priset är att signalen blir långsammare. En leverantörs minskning når kunderna först när lagret har omsatts. Med ett halvårs lager tar det ungefär ett halvår.

Därför är lagerkontot frivilligt, utom för perioder utan leveranser. En nod med litet eller stabilt lager kan avstå.

## Kapitalvaror

En maskin levereras inte vidare och förs därför inte till lagerkontot. Hur utsläppen från tillverkningen av maskinen ska fördelas är öppet. Förslaget lägger fram två alternativ.

1. **Inköpsperioden.** Utsläppen ingår i T det år maskinen köps, som i GHG Protocols Scope 3-standard. Det är enkelt, men en stor investering ger en topp i nodens tal.
2. **Avskrivning.** Utsläppen förs till ett anläggningskonto och fördelas över maskinens livslängd, med samma plan som i bokföringen. Reichelstein (s. 2135) och Jia m.fl. gör så. Toppen försvinner, men det tar längre tid innan en maskin med lägre utsläpp syns fullt ut.

## Förhållande till andra förslag

- MF-006 avgör när en post bokförs och när perioden är slutlig. Lagerkontot följer samma regel.
- I MF-002 och MF-004 justeras summan av det som fördelas för lagerförändringen.
- MF-007 gäller egna aktivitetsdata, som inte förs till lagerkontot.

## Alternativ som övervägts

- Inget lagerkonto, bara en regel för perioder utan leveranser. Enklare och snabbare signal, men topparna och möjligheten att flytta börda står kvar.
- Värdering per vara eller parti. Avvisat, eftersom det kräver spårning och gör talet till en egenskap hos varan.
- Glidande medelvärde av T. Avvisat, eftersom det bryter massbalansen inom perioden.

## Öppna frågor

- Ska egna utsläpp i tillverkade men olevererade varor också föras till lagerkontot, som i kostnadsredovisningen?
- Ska lagret vid start kunna sättas till ett underlag för U i stället för noll?
- Ska lagerkonto krävas för vissa noder, till exempel handelsnoder med stort lager?
- Kapitalvaror: alternativ 1 eller 2?
- Var går gränsen mot reservdelar och förbrukningsinventarier?

## Källor

- Jimmy Jia, Barbara Rossi, Abrar Chaudhury, Evan Taylor och Dennis West, "A reporting framework for general purpose life cycle assessment to align entity-level GHG accounting with general purpose financial statements", arbetspapper, SSRN 4395987, version 22 april 2024, s. 17-21. [doi:10.2139/ssrn.4395987](https://doi.org/10.2139/ssrn.4395987)
- Stefan Reichelstein, "Corporate carbon accounting: balance sheets and flow statements", *Review of Accounting Studies* 29 (2024), s. 2125-2156, här s. 2135-2138. [doi:10.1007/s11142-024-09830-y](https://doi.org/10.1007/s11142-024-09830-y)
- GHG Protocol, *Corporate Value Chain (Scope 3) Accounting and Reporting Standard* (2011), kapitel 5, *Time boundary of scope 3 categories*. [PDF](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard_041613.pdf)

## Beslut

Inte behandlat. Förslaget avser tillägg till §5 och §8 och en ändring av massbalansformeln i §5. Kapitalvarorna avgörs inom förslaget.
