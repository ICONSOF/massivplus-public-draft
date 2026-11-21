---
layout: default_banner
title: "MF-006 Periodregel"
parent: "Förslag"
nav_order: 6
forslag_id: MF-006
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§3, §6, §8"
forslag_forfattare: Birger Löfgren
---

# MF-006 Periodregel

> **Status:** Utkast, 2026-11-21. Ingår inte i standarden. Berör §3, §6 och §8. Författare: Birger Löfgren.
>
> Förslaget anger vilken period en allokeringspost gäller och vad som händer när den kommer sent. Det kompletterar [MF-005](mf-005-allokeringsposter.md), som anger vad posten innehåller. [MF-007](mf-007-egna-data-vid-stangning.md) gäller samma fråga för nodens egna data, och [MF-001](mf-001-lagerhantering.md) gäller varor i lager.

En nod räknar sitt T för en period och fördelar det på sina mottagare ([§3-5](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). I T ingår leverantörernas poster. En leverantör kan skicka sin post först när den har stängt sin egen period, och de flesta stänger ungefär samtidigt. När mottagaren stänger saknas därför ofta en del av posterna.

Specifikationen säger inte vad som gäller då. [Metodologiska risker](../fordjupningar/metodologiska-risker.md#tidsdimensionen) anger frågan som öppen.

Förslaget är periodisering: utsläppen räknas till den period de hör till, även när uppgiften kommer senare. Det är samma sak som bokföringen gör med en faktura som kommer efter bokslutet.

## Förslag till standardtext

### §6: lägg till Period för allokeringsposter

1. **Perioden.** Varje rapporteringsentitet väljer och dokumenterar sin rapporteringsperiod, högst tolv månader. Alla noder inom entiteten har samma period och stängs samtidigt, så allokeringar mellan dem räknas i samma stängning.
2. **Posten gäller avsändarens period.** En allokeringspost mellan organisationer gäller avsändarens period för de leveranser den omfattar. Mottagaren bokför den i sin egen period för samma leveranser. Har avsändaren och mottagaren olika perioder fördelas posten med en dokumenterad regel, till exempel efter leveransdatum.
3. **Det som saknas är okänt.** Har en post från en annan organisation inte kommit när mottagaren stänger perioden, bokförs inköpet som U enligt §2. Som underlag rekommenderas i tur och ordning:
   1. avsändarens senaste post för samma relation
   2. summan av avsändarens senaste poster till mottagaren
   3. ett värde som avsändaren har offererat för relationen
   4. annat underlag enligt §2.
4. **Preliminära poster.** När den saknade posten kommer ersätter den U enligt replacement rule. Fram till att perioden är slutlig är nodens utgående poster preliminära, och noden uppdaterar dem så ofta den vill.
5. **Periodens definitioner.** En ny version av en post räknas med den nodindelning, allokeringsregel och version av emissionsfaktorerna som gällde för perioden.
6. **Slutlig period.** Varje rapporteringsentitet bestämmer och dokumenterar när en period blir slutlig, senast sex månader efter periodens slut. Posterna markeras som preliminära eller slutliga. Coverage (faktisk andel, om [MF-008](mf-008-namnbyte.md) antas) redovisas utåt på den slutliga versionen.
7. **Efter slutlig period.** En post eller ett fel som kommer fram efter att perioden har blivit slutlig bokförs i nästa period. Är skillnaden väsentlig utfärdar noden i stället en rättad version av de slutliga posterna. Noden dokumenterar hur den bedömer väsentlighet.
8. **En metod.** En post bokförs alltid i den period den gäller, utom enligt punkt 7.

### §6, steg 4: ändra

Nuvarande lydelse:

> Uppdaterade värden propageras och allokeras i efterföljande rapporteringsperioder

Föreslagen lydelse:

> Uppdaterade värden propageras och allokeras som nya versioner av de berörda periodernas poster, enligt periodregeln

### §8: lägg till efter definitionen av Coverage

> Coverage som redovisas utåt avser periodens slutliga version enligt periodregeln i §6.

## Som i bokföringen

| Bokföring | MASSIV+ |
|---|---|
| Inköpet hör till perioden då det görs | Posten hör till avsändarens period |
| Upplupen kostnad när fakturan saknas vid bokslutet | U när posten saknas vid stängningen |
| Fakturan kommer och ersätter uppskattningen | Posten kommer och ersätter U |
| Företaget avgör när bokslutet är klart, inom lagens gränser | Noden avgör när perioden är slutlig, senast efter sex månader |
| Väsentliga fel i ett stängt år rättas, övriga förs in i nästa år | Väsentliga skillnader ger en rättad version, övriga bokförs i nästa period |

Bokföringen har varken ett gemensamt bokslutsdatum eller en fast procentsats för väsentlighet. Förslaget har det inte heller.

En skillnad finns. En faktura har ett pris som avtalades när affären gjordes. Rättar säljarens leverantör sin faktura påverkas inte det säljaren redan har fakturerat. En allokeringspost är däremot avsändarens T gånger kundens andel, så en rättelse hos avsändarens leverantör ändrar posten. Därför behöver posterna versioner. Det som hindrar rättelserna från att gå vidare utan slut är att varje nod förklarar sin period slutlig, på samma sätt som bokslutet gör.

## Varför periodisering

Det finns två andra sätt att lösa frågan.

| Sätt | Hur | Problem |
|---|---|---|
| Vänta | Mottagaren stänger först när alla poster har kommit | Ingen kan stänga förrän alla uppströms har stängt. Går emot att varje nod sköter sin massbalans (bevarandeprincipen, om [MF-008](mf-008-namnbyte.md) antas) själv (§5) |
| Bokföra när posten kommer | Mottagaren tar med de poster som kommit under perioden, oftast för leverantörens förra period | Perioderna blandas. Varje led lägger till en period, och faktisk data för fel period ser ut som aktuell |

Periodisering är det enda av de tre sätten som både låter alla stänga i tid och håller talen i rätt period. Det behövs för de KPI:er "år för år eller kvartalsvis" som specifikationens sammanfattning lovar, och för att en kund ska kunna skilja en verklig minskning från bättre data.

## Exempel

Leverantören har 100 ton CO2e egna utsläpp per kvartal och sänker till 70 ton under andra kvartalet. Allt säljs till Grossisten (10 ton egna), som säljer allt till Tillverkaren (20 ton egna). Alla stänger samma dag, fyra veckor efter kvartalet. Talen är påhittade.

| Andra kvartalet | Grossisten | Tillverkaren |
|---|---|---|
| Vid stängningen | Leverantörens post saknas. U = 100 (senaste posten). T = 110, preliminärt | Grossistens post saknas. U = 110. T = 130, preliminärt |
| Leverantörens post kommer | A = 70. T = 80 | |
| Grossistens nya version kommer | | A = 80. T = 100 |

Minskningen når Tillverkaren några veckor efter stängningen och hamnar i andra kvartalet. Bokförs posterna i stället när de kommer, ser Tillverkaren minskningen först i fjärde kvartalet.

## Konsekvenser

- Avsändaren skickar en preliminär version vid stängningen och en slutlig när perioden är slutlig.
- Mottagaren stänger i tid. Sena leverantörer syns som U tills deras poster kommer.
- Verktygen behöver hantera versioner och markera preliminärt och slutligt. Det enda som måste vara gemensamt är postens innehåll enligt MF-005. Varje nod tillämpar reglerna själv, så det krävs inget gemensamt verktyg.
- En liten organisation kan välja tolv månader som period och förklara den slutlig ungefär samtidigt som årsredovisningen. Då har de flesta poster kommit.
- Inom en organisation har alla noder samma period, eftersom heltäckningen i §1 gäller per period och interna flöden räknas i samma stängning. Bokföringen gör likadant: ett bolag har ett räkenskapsår.
- Mellan organisationer kan perioderna skilja sig. En kund med år lägger ihop leverantörens kvartalsposter. En kund med kvartal fördelar leverantörens årspost efter leveransdatum och får leverantörens årssnitt för varje kvartal. Årsposten kommer ofta efter att kundens kvartal är slutligt. Då står U kvar tills posten kommer, och skillnaden går till nästa period enligt punkt 7. En kund får alltså inte mer aktuella tal än leverantörerna levererar.
- Ändras nodindelningen räknas föregående period om internt för jämförelsens skull ([MF-004](mf-004-nodindelning.md), punkt 5), men redan skickade poster ändras inte. Punkt 5 ovan säger det.
- Med lagerkonto enligt MF-001 kan en del av A i en post komma från tidigare perioders inköp. Det redovisas öppet i lagerkontot.

Hur regeln fungerar i djupa kedjor och vid leverantörsutvärdering beskrivs i fördjupningen [Tiden i kedjan](../fordjupningar/tiden-i-kedjan.md).

## Alternativ som övervägts

- Att bokföra posten när den kommer. Avvisat, se ovan.
- Att varje nod väljer metod. Avvisat, eftersom varje mottagare då måste veta vilken metod avsändaren använder.
- Ett gemensamt fönster och en gemensam väsentlighetsgräns, till exempel åtta veckor och fem procent. Avvisat, eftersom bokföringen klarar sig utan och mottagaren bara behöver veta om ett värde är slutligt.
- Ingen väsentlighet, så att allt efter slutlig period bokförs i nästa period. Avvisat, eftersom stora sena poster då hamnar i fel period.

## Öppna frågor

- Är sex månader rätt yttre gräns?
- Behövs ett riktvärde för väsentlighet som inte är bindande?
- En nod kan kalla en stor rättelse oväsentlig för att skjuta den till nästa period. Räcker det att bedömningen är dokumenterad?
- Ska Coverage även redovisas vid stängningen, skilt från det slutliga värdet?
- Kan avsändarens egen preliminära deklaration räknas som A? Då når signalen mottagaren redan under perioden. §2 säger att skillnaden mellan A och U gäller vem som är ansvarig avsändare, inte hur exakt talet är.

## Beslut

Inte behandlat. Förslaget avser tillägg till §6 och §8 och en ändring i §6, steg 4.
