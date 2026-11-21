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
> [MF-006](mf-006-periodregel.md) anger vad som gäller när en leverantörs post saknas vid stängningen. Detta förslag gäller samma situation för nodens egna aktivitetsdata, till exempel en elfaktura som inte har kommit. Förslagen kan bedömas var för sig.

En nod räknar sina egna Scope 1 och 2 från aktivitetsdata: bränsle, el, värme och annan energi, med standardens emissionsfaktorer ([§2](../standard/specifikation.md#standardiserade-emissionsfaktorer-för-scope-1-och-2)). När perioden stängs saknas ibland en del av underlaget. Elfakturan för periodens sista månad har inte kommit, eller en mätaravläsning saknas.

Specifikationen säger inte vad som då gäller. Ett vanligt sätt är att använda föregående månad tills fakturan kommer. Värdet ingår då i S1 eller S2. §8 räknar nodens egna Scope 1 och 2 som faktisk data, så ett uppskattat värde får samma status i Coverage som ett uppmätt. Det går emot den andra principen: ingen uppskattning får samma status som faktisk data.

U är i dag definierat som okända uppströmsutsläpp (§2). Specifikationen saknar en plats för den okända delen av nodens egna utsläpp.

## Förslag till standardtext

### §2: lägg till Egna aktivitetsdata som saknas vid stängningen

1. **S1 och S2 bygger på aktivitetsdata för perioden.** Fakturor, mätaravläsningar, tankkortsrapporter och verifierade utsläppsrapporter räknas som aktivitetsdata.
2. **Det som saknas är okänt.** Saknas aktivitetsdata för en del av perioden när noden stänger, bokförs motsvarande utsläpp som U. Underlaget för U tas fram med bästa tillgängliga metod. Rekommenderat underlag är motsvarande del av föregående period, eller avtalad volym, med standardens emissionsfaktorer.
3. **Uppdelning i redovisningen.** Noden redovisar U för egna utsläpp skilt från U för uppströmsflöden. I allokeringen behandlas båda som Unknown enligt §4.
4. **Ersättning.** När aktivitetsdata kommer flyttas mängden från U till S1 eller S2 enligt replacement rule. Nya versioner av nodens utgående poster följer periodregeln i MF-006.

### §2, tabellen över komponenter: ändra beskrivningen av Uᵢ

Nuvarande lydelse:

> Upstream Unknown - okända uppströmsutsläpp

Föreslagen lydelse:

> Unknown - okända utsläpp: uppströmsflöden utan faktisk grund samt egna utsläpp vars aktivitetsdata saknas vid stängningen

## Varför

Principen om faktisk data eller okänt gäller hela T. En nod som räknar in en uppskattning i S1 eller S2 visar högre Coverage än underlaget motiverar. Nodens kunder tar emot uppskattningen som Actual enligt §4 och kan inte skilja den från uppmätt data.

Uppskattningen behöver inte göras på ett annat sätt än i dag. Skillnaden är var den bokförs. Som U syns den i Coverage, följer med som Unknown till kunderna och ersätts när underlaget kommer.

## Exempel

En nod har elförbrukning med ett utsläpp på 30 ton CO2e per månad och dieselförbrukning med 40 ton per kvartal. Elfakturan för kvartalets sista månad har inte kommit vid stängningen. Noden har inga uppströmsflöden. Talen är påhittade.

| | S1 | S2 | U | T | Coverage |
|---|---|---|---|---|---|
| Uppskattningen i S2, som i dag | 40 | 90 | 0 | 130 | 100 % |
| Enligt förslaget, version 1 | 40 | 60 | 30 | 130 | 77 % |
| Enligt förslaget, version 2 när fakturan kommer | 40 | 88 | 0 | 128 | 100 % |

Mängden är densamma i version 1. Det som skiljer är att kunderna får veta att 30 ton saknar faktisk grund tills fakturan har kommit.

## Konsekvenser

- **Coverage** sjunker tillfälligt för noder som stänger innan alla fakturor har kommit. Med avräkningsfönstret i MF-006 är det slutliga värdet opåverkat om fakturan kommer inom fönstret.
- **Uppströms-Coverage**, A / (A + U), behöver avgränsas till uppströmsflöden. Därför redovisas de två delarna av U skilt enligt punkt 3.
- **EU ETS-anläggningar** använder sina verifierade utsläpp. Kommer verifieringen efter stängningen gäller samma regel som för andra aktivitetsdata.

## Alternativ som övervägts

- **Att tillåta uppskattningar i S1 och S2 under en gräns**, till exempel fem procent av nodens egna utsläpp. Enklare, men principen om faktisk data eller okänt skulle då gälla med ett undantag.
- **En ny komponent vid sidan av U**, för okända egna utsläpp. Tydligare, men det ger en femte komponent i T och ändrar formlerna i §4 och §8. Förslaget håller i stället isär delarna i redovisningen men behandlar dem lika i beräkningen.

## Öppna frågor

- Ska uppdelningen av U i egna och uppströms vara ett krav eller en rekommendation?
- Behövs en gräns under vilken en uppskattning får ingå i S1 och S2?
- Hur förhåller sig förslaget till noder som rapporterar Scope 1 enligt EU ETS, där verifieringen kan komma månader efter årsskiftet?

## Beslut

Inte behandlat. Förslaget avser tillägg till §2 och en ändring av komponenttabellen i §2.
