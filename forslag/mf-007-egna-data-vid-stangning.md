---
layout: default_banner
title: "MF-007 Egna aktivitetsdata som saknas vid stängningen"
parent: "Förslag"
nav_order: 7
forslag_id: MF-007
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§2, §8"
forslag_forfattare: Birger Löfgren
---

# MF-007 Egna aktivitetsdata som saknas vid stängningen

> **Status:** Utkast, 2026-11-21. Ingår inte i standarden. Berör §2 och §8. Författare: Birger Löfgren.
>
> [MF-006](mf-006-periodregel.md) gäller leverantörsposter som saknas när perioden stängs. Det här förslaget gäller nodens egna data, till exempel en elfaktura som inte har kommit. Förslagen kan bedömas var för sig.

En nod räknar sina egna Scope 1 och 2 från fakturor, mätaravläsningar och liknande ([§2](../standard/specifikation.md#standardiserade-emissionsfaktorer-för-scope-1-och-2)). När perioden stängs saknas ibland en del, till exempel elfakturan för sista månaden.

Ett vanligt sätt är att använda förra månadens värde tills fakturan kommer. Uppskattningen hamnar då i S1 eller S2, som §8 räknar som faktisk data. Det går emot principen att ingen uppskattning får samma status som faktisk data. Specifikationen har i dag bara U för uppströmsflöden och ingen plats för okända egna utsläpp.

## Förslag till standardtext

### §2: lägg till Egna aktivitetsdata som saknas vid stängningen

1. **Aktivitetsdata.** S1 och S2 bygger på aktivitetsdata för perioden: fakturor, mätaravläsningar, tankkortsrapporter och verifierade utsläppsrapporter.
2. **Det som saknas är okänt.** Saknas aktivitetsdata när noden stänger perioden, bokförs motsvarande utsläpp som U. Rekommenderat underlag är samma del av förra perioden, eller avtalad volym, med standardens emissionsfaktorer.
3. **Redovisning.** Noden redovisar U för egna utsläpp skilt från U för uppströmsflöden. I allokeringen behandlas båda som Unknown enligt §4.
4. **Ersättning.** När aktivitetsdata kommer flyttas mängden från U till S1 eller S2 enligt replacement rule. Nya versioner av nodens poster följer periodregeln i MF-006.

### §2, tabellen över komponenter: ändra beskrivningen av Uᵢ

Nuvarande lydelse:

> Upstream Unknown - okända uppströmsutsläpp

Föreslagen lydelse:

> Unknown - okända utsläpp: uppströmsflöden utan faktisk grund samt egna utsläpp vars aktivitetsdata saknas vid stängningen

## Varför

Uppskattningen görs på samma sätt som i dag. Skillnaden är var den bokförs. Som U syns den i Coverage, går vidare till kunderna som Unknown och ersätts när fakturan kommer. I S1 eller S2 får kunderna den som Actual och kan inte skilja den från uppmätt data.

## Exempel

En nod har el som ger 30 ton CO2e per månad och diesel som ger 40 ton per kvartal. Elfakturan för kvartalets sista månad har inte kommit vid stängningen. Noden har inga uppströmsflöden. Talen är påhittade.

| | S1 | S2 | U | T | Coverage |
|---|---|---|---|---|---|
| Som i dag, uppskattningen i S2 | 40 | 90 | 0 | 130 | 100 % |
| Enligt förslaget, vid stängningen | 40 | 60 | 30 | 130 | 77 % |
| Enligt förslaget, när fakturan kommit | 40 | 88 | 0 | 128 | 100 % |

Vid stängningen är mängden densamma. Skillnaden är att kunderna ser att 30 ton saknar faktisk grund tills fakturan har kommit.

## Konsekvenser

- Coverage sjunker tillfälligt för en nod som stänger innan alla fakturor har kommit. Kommer fakturan innan perioden är slutlig enligt MF-006 påverkas inte det slutliga värdet.
- Uppströms-Coverage, A / (A + U), ska bara räkna uppströmsflöden. Därför redovisas de två delarna av U skilt.
- En anläggning i EU ETS använder sina verifierade utsläpp. Kommer verifieringen efter stängningen gäller samma regel.

## Alternativ som övervägts

- Att tillåta uppskattningar i S1 och S2 under en gräns. Enklare, men principen om faktisk data eller okänt skulle då ha ett undantag.
- En egen komponent för okända egna utsläpp. Tydligare, men det ger en femte komponent i T och ändrar formlerna i §4 och §8.

## Öppna frågor

- Ska uppdelningen av U i egna och uppströms vara ett krav eller en rekommendation?
- Behövs en gräns under vilken en uppskattning får ingå i S1 och S2?
- Hur ska noder i EU ETS göra, när verifieringen kan komma månader efter årsskiftet?

## Beslut

Inte behandlat. Förslaget avser tillägg till §2 och en ändring av komponenttabellen i §2.
