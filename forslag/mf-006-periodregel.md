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
> Förslaget anger vilken period en allokeringspost gäller och vad som händer när den kommer efter att mottagaren har stängt perioden. Det bygger på allokeringsposten i [MF-005](mf-005-allokeringsposter.md), som hänvisar till "standardens periodregler". [MF-007](mf-007-egna-data-vid-stangning.md) behandlar samma fråga för nodens egna aktivitetsdata.

En nod räknar sitt T för en rapporteringsperiod och fördelar hela mängden på sina mottagare ([§3-5](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). I T ingår de poster noden får från sina leverantörer. En leverantör kan skicka sin post först när den har stängt sin egen period, och de flesta organisationer stänger ungefär samtidigt. När mottagaren stänger har därför en del av periodens poster ännu inte kommit.

Specifikationen säger inte vad som då gäller. [§6](../standard/specifikation.md#6-replacement-rule---progressiv-dataförbättring) säger att uppdaterade värden propageras "i efterföljande rapporteringsperioder", och [§7](../standard/specifikation.md#7-cirkulära-flöden) tillåter att ett cirkulärt beroende bryts med föregående periods data. [Metodologiska risker](../fordjupningar/metodologiska-risker.md#tidsdimensionen) anger synkronisering mellan perioder som öppen.

## Förslag till standardtext

### §6: lägg till Period för allokeringsposter

1. **Perioden.** Varje nod väljer och dokumenterar sin rapporteringsperiod. Perioden får vara högst tolv månader. Kortare perioder, till exempel kvartal, är tillåtna.
2. **Posten gäller avsändarens period.** En allokeringspost gäller avsändarens rapporteringsperiod för de leveranser posten omfattar. Mottagaren bokför posten i den egna period som omfattar leveranserna. När avsändarens och mottagarens perioder inte sammanfaller fördelas posten med en dokumenterad regel, till exempel efter leveransdatum.
3. **Det som saknas vid stängningen är okänt.** Har en post inte kommit när mottagaren stänger perioden bokförs motsvarande inköp som U enligt §2. Som underlag för U rekommenderas, i denna ordning:
   1. avsändarens senaste post för samma relation
   2. summan av avsändarens senaste poster till mottagaren
   3. ett värde som avsändaren har offererat för relationen
   4. annat underlag enligt §2.
4. **En sen post ersätter U.** När posten kommer ersätter den underlaget enligt replacement rule. Före den slutliga perioden enligt punkt 6 är mottagarens utgående poster preliminära. Mottagaren uppdaterar dem när sena poster kommer, så ofta den väljer. Versionerna utfärdas enligt MF-005.
5. **Periodens definitioner gäller.** En ny version av en post räknas med de definitioner som gällde för perioden: nodindelning, allokeringsregel och version av emissionsfaktorerna. En senare ändring av någon av dem ändrar inte tidigare perioders poster, i enlighet med §3.
6. **Slutlig period.** Varje nod bestämmer och dokumenterar när en period blir slutlig. Perioden ska vara slutlig senast sex månader efter periodens slut. Utgående poster markeras som preliminära eller slutliga, och Coverage redovisas utåt på den slutliga versionen. En post som kommer efter att mottagaren har förklarat perioden slutlig behandlas enligt punkt 7.
7. **Rättelse efter slutlig period.** En sen post eller ett fel som upptäcks efter att perioden har förklarats slutlig bokförs i nästa öppna period. Är skillnaden väsentlig utfärdar noden i stället en ny version av de berörda slutliga posterna, markerad som rättad. Varje nod dokumenterar hur den bedömer väsentlighet.
8. **En metod.** En post får inte bokföras i en annan period än den gäller, utom enligt punkt 7.

### §6, steg 4: ändra

Nuvarande lydelse:

> Uppdaterade värden propageras och allokeras i efterföljande rapporteringsperioder

Föreslagen lydelse:

> Uppdaterade värden propageras och allokeras som nya versioner av de berörda periodernas poster, enligt periodregeln

### §8: lägg till efter definitionen av Coverage

> Coverage som redovisas utåt avser periodens slutliga version, som noden har förklarat slutlig enligt periodregeln i §6.

## Varför periodisering

Det finns tre sätt att svara på frågan.

| Alternativ | Regel | Följd |
|---|---|---|
| Vänta | Mottagaren stänger först när alla poster för perioden har kommit | Ingen kan stänga förrän alla uppströms har stängt. Cykler mellan organisationer kräver en central part. Går emot den lokala disciplinen i §5 |
| Bokför när posten utfärdas | Mottagaren tar med de poster som utfärdats under perioden, oftast för avsändarens föregående period | Ingen väntar och ingen gissar. Perioderna blandas, och varje led lägger till en period |
| Periodisering, detta förslag | Posten gäller avsändarens period. Det som saknas vid stängningen är U, som ersätts när posten kommer | Ingen väntar och talet hamnar i rätt period. Kräver versioner |

Introduktionen och förstasidan ställer fyra krav som ger svaret:

1. **Faktisk data eller okänt.** Med periodisering blir det som saknas U, vilket är vad U är till för. Bokförs posten när den utfärdas får mottagaren faktisk data för fel period, utan att det syns.
2. **Operativ signal i rätt period.** Specifikationens sammanfattning lovar KPI:er "år för år eller kvartalsvis". De förutsätter att perioderna inte blandas, liksom uppdelningen av en förändring i verklig förändring och ersatt U som [metodologiska risker](../fordjupningar/metodologiska-risker.md#verklig-förändring-mot-dataförbättring) föreslår.
3. **Avstämning mellan parterna.** Med periodisering anger båda parter samma period för samma post.
4. **Lokal disciplin och ensidig start.** Periodisering kräver ingen väntan och ingen samordning.

## Bokföringsanalogin

Förslaget följer hur bokföringen hanterar en faktura som kommer efter bokslutet ([bokföringsanalogin](../fordjupningar/bokforingsanalogin.md)):

| Bokföring | MASSIV+ |
|---|---|
| Inköpet hör till perioden då det görs | Posten gäller leveranserna under avsändarens period |
| Upplupen kostnad vid bokslutet | Underlag för U när posten inte har kommit |
| Fakturan kommer och den upplupna kostnaden vänds | U ersätts enligt replacement rule |
| Kreditfaktura eller ny faktura med hänvisning | Ny version av posten enligt MF-005 |
| Varje företag avgör när bokslutet är klart, inom yttre gränser som tiden till årsstämman | Varje nod avgör när perioden är slutlig, senast sex månader efter periodens slut |
| Fel som upptäcks efter bokslutet: väsentliga rättas för sin period, övriga förs in i innevarande period. Väsentlighet bedöms utan fast procentsats | Efter slutlig period: väsentliga skillnader ger en rättad version, övriga bokförs i nästa period. Noden dokumenterar sin bedömning |
| Stängda år öppnas inte | Periodens definitioner gäller för nya versioner |

En skillnad mot bokföringen förklarar varför posterna alls behöver versioner. Fakturans belopp är känt när affären görs, eftersom priset är avtalat och inte beror på säljarens kostnader. Rättar säljarens leverantör en faktura ändras säljarens kostnader men inte det pris säljaren redan har fakturerat, så rättelsen stannar hos säljaren. En allokeringspost är i stället avsändarens T för perioden gånger kundens andel, och i T ingår avsändarens inflöde. Kaplan och Ramanna beskriver det som att utsläpp förs vidare som om allt såldes till självkostnad. En rättelse uppströms ändrar därför avsändarens post, och båda delarna av posten blir kända först när perioden stängs. Den slutliga perioden i punkt 6 bryter kedjan på samma sätt som bokslutet: det som kommer senare går vidare med nästa periods post.

## Exempel

Leverantören har egna S1+S2 på 100 ton CO2e per kvartal och sänker till 70 ton under andra kvartalet. Leverantören säljer allt till Grossisten, som har 10 ton egna utsläpp och säljer allt till Tillverkaren, som har 20 ton egna. Alla tre stänger fyra veckor efter kvartalets slut, samma dag. Talen är påhittade.

**Med periodregeln**, andra kvartalet:

| När | Grossisten | Tillverkaren |
|---|---|---|
| Stängning, version 1 | Leverantörens post har inte kommit. Underlag för U är Leverantörens senaste post, 100 ton. T = 110, Coverage 9 % (preliminärt) | Grossistens post har inte kommit. U = 110. T = 130, Coverage 15 % (preliminärt) |
| Leverantörens post kommer | Version 2: A = 70, T = 80, Coverage 100 % | |
| Grossistens version 2 kommer | | Version 2: A = 80, T = 100, Coverage 100 % |

**Om posten i stället bokförs när den utfärdas**, ser Grossisten minskningen i tredje kvartalet och Tillverkaren i fjärde. Med årsperioder blir det ett år per led.

Med periodregeln når minskningen Tillverkaren inom några veckor efter stängningen och hamnar i andra kvartalet. Versionerna går vidare så snart posterna kommer, medan den andra metoden bara kan föra vidare en gång per stängning.

## Djupa kedjor

Värdekedjor är i praktiken mycket djupa, särskilt för de mindre flöden som omger huvudflödet. Periodregeln ger dem tre egenskaper:

- **A gäller rätt period.** A kommer bara in från poster för perioden. När en länk är sen fyller punkt 3 luckan med U. Bidrag som är äldre än perioden hamnar därför i U, med full mängd. Undantaget är A som en nod för via sitt lagerkonto enligt MF-001. Det redovisas öppet och motsvarar varor som levereras under perioden. Bokförs posten när den utfärdas är ett bidrag från k led bort k perioder gammalt och räknas ändå som A, utan att det syns.
- **En period kan avslutas.** Någon post långt bak i kedjan är alltid sen. Varje nod förklarar sin period slutlig, och det som kommer senare bokförs i nästa period, utom väsentliga rättelser.
- **Rättelser stannar vid den slutliga perioden.** När en nod har förklarat sin period slutlig går en sen post vidare med nästa periods post, inte som en ny version av den gamla. Bara väsentliga rättelser ger en rättad version, och en rättelse krymper i förhållande till varje nods T för varje led, eftersom varje nod lägger till egna utsläpp och andra inflöden och fördelar skillnaden på sina kunder. Den blir därför oväsentlig efter några led.

Fördjupningen [Tiden i kedjan](../fordjupningar/tiden-i-kedjan.md) utvecklar resonemanget.

## Många verktyg

Periodregeln kräver inget gemensamt verktyg. Varje nod tillämpar punkterna 3-7 utifrån sitt eget inflöde, utan att se resten av kedjan, i linje med §5. Det som behöver vara gemensamt är postens innehåll enligt MF-005, inklusive markeringen preliminär eller slutlig. När en period blir slutlig och vad som är väsentligt bestämmer varje nod själv, som i bokföringen. Mottagaren behöver bara veta om ett värde är preliminärt eller slutligt.

## Ändrade definitioner

Punkt 5 skiljer två saker åt:

- **Omräkning för jämförelse.** När nodindelningen ändras räknas föregående period om internt, så att perioderna går att jämföra ([MF-004](mf-004-nodindelning.md), punkt 5).
- **Ny version av en post.** En ny version skickas till mottagaren och ersätter en tidigare post.

Ett definitionsbyte ger bara det första. Annars skulle varje byte av nodindelning, allokeringsregel eller emissionsfaktorer ge nya versioner genom hela kedjan. Bokföringen gör på samma sätt: jämförelsetalen räknas om när en redovisningsprincip ändras, men fakturorna skickas inte om.

När avsändarens nodindelning ändras kan den tidigare relationen sakna motsvarighet. Rangordningen i punkt 3 anger då vilket underlag som används i stället.

## Konsekvenser

**Avsändaren** utfärdar en preliminär version vid stängningen och en slutlig när perioden förklaras slutlig, och fler däremellan om den vill. Efter den slutliga perioden ger bara väsentliga rättelser en ny version.

**Mottagaren** stänger i tid utan att vänta. Leverantörer som deklarerar men är sena syns som U tills deras poster kommer. Coverage är preliminärt tills noden har förklarat perioden slutlig.

**Verktygen** behöver hantera versioner, markera preliminära och slutliga värden och kunna utfärda nya versioner när sena poster kommer. Kraven kan uppfyllas av flera verktyg, eftersom de följer av postens innehåll.

**Små noder** kan välja tolv månader som period och förklara perioden slutlig ungefär samtidigt som årsredovisningen. Då har de flesta poster kommit, och nya versioner blir få. En nod vars leverantörer inte deklarerar har inga poster att vänta på.

**Extern rapportering** använder den version som gäller vid rapportens datum. Senare skillnader behandlas enligt punkt 7.

## Förhållande till andra delar

- **MF-005** anger postens innehåll, inklusive version och hänvisning till ersatt post. Detta förslag anger när posten bokförs och när en ny version utfärdas.
- **MF-007** tillämpar samma princip på nodens egna aktivitetsdata.
- **§7.** Tidssegmentering mellan perioder är fortfarande tillåten för att lösa cirkulära beroenden.
- **MF-001** föreslår ett lagerkonto för utsläpp från inköpta varor som ligger i lager vid periodens slut. Periodregeln avgör när en post bokförs, lagerkontot hur en bokförd mängd fördelas. En sen post för lagerförda inköp påverkar också lagerkontot, och lagerkontot följer periodregeln.

## Alternativ som övervägts

- **Att bokföra posten när den utfärdas.** Enklare för avsändaren, eftersom inga nya versioner behövs. Avvisat eftersom perioderna blandas och A får en ålder som inte syns.
- **Ingen väsentlighet, allt efter slutlig period bokförs i nästa period.** Enklast. Avvisat eftersom en stor sen post då hamnar i fel period, vilket bokföringen inte godtar för väsentliga fel.
- **Att låta varje nod välja metod.** Avvisat eftersom varje mottagare då måste veta vilken metod avsändaren använder, och en nod som bokför när posten utfärdas för in äldre A i kedjan.
- **Ett gemensamt fönster och en gemensam gräns**, till exempel åtta veckor och fem procent. Det skulle göra värdena enhetliga. Avvisat eftersom bokföringen klarar sig utan, och eftersom det mottagaren behöver är att veta om ett värde är slutligt. Gemensamma värden kan växa fram som branschpraxis eller standardinställningar i verktygen.
- **Att låta köparen bestämma när en period är slutlig.** Avvisat eftersom en leverantör har många köpare.

## Öppna frågor

- Är sex månader rätt yttre gräns för när en period ska vara slutlig?
- Behövs ett riktvärde för väsentlighet som inte är bindande, till exempel i en vägledning?
- En nod kan kalla en stor och ofördelaktig rättelse oväsentlig och skjuta den till nästa period. Ingen mängd försvinner, men den hamnar i fel period. Räcker det att noden dokumenterar sin bedömning av väsentlighet?
- Ska Coverage också redovisas vid stängningen, och i så fall hur skiljs det från det slutliga värdet?
- Kan avsändarens egen preliminära deklaration räknas som A? §2 säger att skillnaden gäller ansvarig avsändare och inte numerisk kvalitet. Det skulle låta signalen nå mottagaren redan under perioden.
- En skillnad som bokförs i nästa period kan göra U negativt i den perioden. [MF-002](mf-002-utspadning.md) utgår från mängder som inte är negativa.

## Beslut

Inte behandlat. Förslaget avser tillägg till §6 och §8 och en ändring i §6, steg 4.
