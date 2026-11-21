---
layout: default_banner
title: "Tiden i kedjan"
parent: "Fördjupningar"
nav_order: 14
---

# Tiden i kedjan

> **Poäng:** MASSIV+ räknar mängder per relation och period, och de blir kända först när perioden stängs. Därför behöver standarden säga vilken period en post gäller och vad som händer när den kommer sent. Med periodisering hamnar faktisk data i rätt period och det som saknas blir okänt. Det gör att även mycket djupa kedjor går att hantera utan cut-off, och att inköpare kan följa leverantörer period för period.

Texten förutsätter en grundläggande bild av MASSIV+. Läs [introduktionen](../introduktion.md) först om du inte är bekant med standarden. Reglerna föreslås i [MF-006 Periodregel](../forslag/mf-006-periodregel.md), [MF-007](../forslag/mf-007-egna-data-vid-stangning.md) och [MF-001](../forslag/mf-001-lagerhantering.md). Inget av förslagen är antaget.

---

## 1. Varför tiden blir en fråga

En nod räknar sitt T för en period och fördelar det på sina mottagare ([§3-5](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Både T och mottagarens andel gäller hela perioden. En post kan därför skickas först när avsändaren har stängt perioden, och då har mottagaren ofta redan stängt sin.

Tre forskarförslag som också bygger på bokföringens principer, beskrivna i [bokföringsanalogin](bokforingsanalogin.md#4-den-framväxande-tanken-om-bokföring-av-utsläpp), har inte den frågan. De bokför överföringen när affären görs:

- Jia m.fl. redovisar en energipost *"at the same point-in-time as the financial transaction"* (s. 8). Perioden kan vara månad, kvartal eller år (s. 22).
- Reichelstein bokför inköpet på materiallagret med leverantörens produktavtryck, eller med ett branschtal när leverantören saknar egen beräkning (s. 2134).
- Kaplan och Ramanna för posten hos säljare och köpare vid försäljningen. Kunden har *"willingly assumed the emissions"* som en del av affären (s. 5). Målet är redovisning *"in as close to real time as practicable"* (s. 1).

Reichelstein och Kaplan och Ramanna kan bokföra vid affären därför att de räknar ett tal per producerad enhet i produktkalkylen (Kaplan och Ramanna, s. 3). Talet finns när affären görs, ungefär som ett pris. MASSIV+ räknar i stället mängder per relation och period ([§5](../standard/specifikation.md#individuation-av-allokeringsenheten), [koordinatbytet](koordinatbytet.md)). Tidsfrågan är priset för det valet.

Forskarna har också tankar som MASSIV+ bygger vidare på. Reichelstein använder periodiseringar för att talen ska hamna i rätt period (s. 2127, 2140). Kaplan och Ramanna räknar med att branschtal ersätts av leverantörernas egna data i senare omgångar, allt eftersom fler ansluter (s. 4, 27-28), och Reichelstein låter ett företag börja ensamt med branschtal (s. 2145). Ingen av dem anger hur en uppgift som kommer sent ersätter uppskattningen för samma period, eller håller isär uppskattat och faktiskt i det som förs vidare. Det gör MASSIV+ med replacement rule ([§6](../standard/specifikation.md#6-replacement-rule---progressiv-dataförbättring)) och åtskillnaden mellan A och U.

## 2. Periodisering

Periodisering betyder att utsläppen räknas till den period de hör till, även när uppgiften kommer senare. MF-006 föreslår att en post gäller avsändarens period. Det som saknas när mottagaren stänger bokförs som U. När posten kommer ersätter den U, och mottagaren uppdaterar sina egna poster. De är preliminära tills organisationen förklarar perioden slutlig. Bokföringen gör likadant med en faktura som kommer efter bokslutet. MF-007 tillämpar samma regel på nodens egna data, till exempel en elfaktura som saknas.

Varje organisation väljer sin period, och alla dess noder har samma. Mellan organisationer kan perioderna skilja sig, och posten fördelas då efter leveransdatum. En kund med kvartal som köper av en leverantör med år får leverantörens årssnitt för varje kvartal. Årsposten kommer ofta efter att kvartalet är slutligt, så U står kvar tills den kommer och skillnaden går till nästa period. Ingen får mer aktuella tal än leverantörerna levererar.

Alternativet är att bokföra posten när den kommer, alltså oftast för leverantörens förra period. Det kräver inga nya versioner, men perioderna blandas och varje led lägger till en period. MF-006 visar skillnaden i ett räkneexempel.

## 3. Djupa kedjor och cut-off

Huvudflödet i en värdekedja har få steg, men flödena runt omkring fortsätter nästan utan slut: förnödenheter, tjänster, transporter, och deras leverantörer i sin tur. En livscykelanalys hanterar det med cut-off. Flöden under en gräns lämnas utanför, och den mängden försvinner ur resultatet.

I MASSIV+ slutar kedjan där deltagandet slutar. Vid den första leverantören som inte skickar en post tar U över, med full mängd ([§2](../standard/specifikation.md#u-värdets-roll)). Ingenting skärs bort. Ju fler som ansluter, desto längre når den faktiska datan.

Med periodisering gäller faktisk data rätt period. A kommer bara in från poster för perioden, och när en post är sen fylls luckan med U. Det som är äldre än perioden hamnar därför i U. Nära i kedjan är talen aktuella och faktiska, och längre bort, där någon länk inte hann med, finns bidraget kvar som okänt. Det fungerar som en cut-off i tid där ingen mängd försvinner. Ett undantag är A som en nod för via sitt lagerkonto enligt MF-001. Det redovisas öppet och motsvarar varor som levereras under perioden.

Bokförs posten i stället när den kommer, blir ett bidrag från k led bort k perioder gammalt och räknas ändå som A. I en djup kedja får A då bidrag av alla åldrar, och ingen kan se det. Det räcker att en nod bokför så för att äldre A ska följa med nedströms. Därför föreslår MF-006 en metod för alla.

Någon post långt bak i kedjan är alltid sen, så en period blir aldrig färdig av sig själv. MF-006 föreslår att varje organisation bestämmer när perioden är slutlig, senast sex månader efter periodens slut. Det som kommer senare bokförs i nästa period.

I vanlig bokföring är kedjorna lika långa, men priset bryter dem. Fakturans belopp beror inte på säljarens kostnader, så en rättelse hos säljarens leverantör ändrar inte det säljaren redan har fakturerat. I MASSIV+ är posten avsändarens T gånger kundens andel. Utsläppen förs vidare som om allt såldes till självkostnad (Kaplan och Ramanna, s. 5-6), så en rättelse uppströms ändrar posten. Det är den slutliga perioden som bryter kedjan, som bokslutet gör. Bara väsentliga rättelser ger en rättad version av en slutlig post, och de krymper i förhållande till varje nods T för varje led tills de inte längre är väsentliga.

| | Huvudflödet | Flödena runt omkring |
|---|---|---|
| Vad det är | De få stora stegen | Det som en livscykelanalys skulle skära bort |
| Hur det hanteras | Avtal om att posterna ska komma innan perioden blir slutlig | Senaste post som underlag för U, och att perioden blir slutlig |
| Status i talet | Aktuellt och faktiskt | Äldre och okänt, med full mängd |

Ingen behöver avgöra var huvudflödet slutar. Varje organisation stoppar rättelserna när den förklarar perioden slutlig. Det passar med [§8](../standard/specifikation.md#8-coverage---mått-på-datakvalitet), där uppströms-Coverage används för att prioritera insatser där flödena är stora.

## 4. Många verktyg

Organisationerna använder olika verktyg, som i bokföringen, och periodiseringen kräver inget gemensamt. Varje nod avgör utifrån sitt eget inflöde om den ska skicka en ny version, utan att se resten av kedjan ([§5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)). Det som måste vara gemensamt är postens innehåll enligt [MF-005](../forslag/mf-005-allokeringsposter.md): version, vilken post den ersätter, och om den är preliminär, slutlig eller rättad. När perioden blir slutlig och vad som är väsentligt bestämmer varje organisation själv. Bokföringen har varken ett gemensamt bokslutsdatum eller en fast procentsats för väsentlighet.

Versionerna går genom kedjan i den takt den långsammaste länken klarar. Att varje organisation förklarar sin period slutlig sätter ett tak, och det som kommer senare bokförs i nästa period. Kedjan blockeras aldrig. Den blir bara mindre aktuell för den perioden.

## 5. Leverantörsutvärdering

Specifikationens sammanfattning beskriver MASSIV+ som ett sätt att sätta KPI:er för minskade utsläpp, som krav eller incitament mot leverantörer, och som ett upphandlingsverktyg. Periodiseringen avgör om det fungerar.

- Varje relation får en mängd utsläpp per period, i rätt period. Inköparen kan följa en leverantörs minskning period för period.
- Utvärderingen bör bygga på den slutliga versionen. Innan perioden är slutlig påverkas Coverage av hur snabba leverantörens egna leverantörer är, och mäter då förseningar i stället för datakvalitet.
- Andelen poster som kommer inom en avtalad tid är ett mått som kan ställas som krav. §6 nämner redan avtal med krav på rapportering.
- Leverantörer med olika perioder jämförs på den längsta, till exempel helår. Den som vill följa leverantörer kvartal för kvartal behöver be dem om kvartal.
- En förändring kan bero på verklig minskning, på att okänt ersatts av faktiskt eller på ändrade definitioner ([metodologiska risker](metodologiska-risker.md#verklig-förändring-mot-dataförbättring)). Med perioder som inte blandas går de att skilja åt.

För att jämföra två leverantörer räknar inköparen mängd per inköpt kvantitet, alltså postens mängd delad med de egna inköpen. Talet används för inköparens beslut och förs inte vidare som ett produkttal.

## 6. Offertförfrågan

Vid en offertförfrågan finns ingen relation än och därför ingen post. En post beskriver en relation och en period i efterhand, som en faktura. En offert behöver ett tal om framtiden, som ett pris.

Anbudsgivaren kan lämna ett **offererat värde**: den avsändande nodens senaste slutliga T och allokeringsregel tillämpade på den offererade volymen, med period, Coverage och version av emissionsfaktorerna. Värdet gäller en viss nod. En leverantör med flera noder kan offerera från den nod som ska leverera ([MF-004](../forslag/mf-004-nodindelning.md)).

Det offererade värdet är ingen allokeringspost. Det bokförs inte som A och förs inte vidare. Det beskriver en relation som inte finns än, och utan den gränsen glider det lätt mot ett tal per produkt.

Periodiseringen ger fem följder:

1. Offerten bygger på den slutliga versionen, så att ingen offererar på ett preliminärt tal.
2. Kortare perioder ger aktuellare anbud. En leverantör som stänger kvartalsvis kan offerera på förra kvartalets data.
3. Avtalet kan följa upp offert mot utfall period för period, med bonus eller avdrag om parterna vill, eftersom utfallet kommer för rätt period.
4. För en ny leverantör finns ingen tidigare post. MF-006 rekommenderar då det offererade värdet som underlag för U tills den första posten kommer.
5. En anbudsgivare utan MASSIV+ kan bara lämna underlag för U, till exempel en EPD ([§2](../standard/specifikation.md#separation-av-faktisk-och-okänd-data)). Skillnaden syns i Coverage.

## 7. Öppna frågor

- Är sex månader rätt yttre gräns för när en period ska vara slutlig, och behövs ett riktvärde för väsentlighet? Frågorna ställs i MF-006.
- Kan en leverantörs egen preliminära deklaration räknas som A, så att signalen når kunden redan under perioden?
- Lagerkontot i MF-001 ger jämnare tal, men en leverantörs minskning når kunderna först när lagret omsätts. Hur ska den avvägningen göras?
- Ska det offererade värdet beskrivas i standarden, i en vägledning eller bara i avtal och verktyg?

## Källor

- Jimmy Jia, Barbara Rossi, Abrar Chaudhury, Evan Taylor och Dennis West, "A reporting framework for general purpose life cycle assessment to align entity-level GHG accounting with general purpose financial statements", arbetspapper, SSRN 4395987, version 22 april 2024, s. 8 och 22. Arbetspappret saknar tryckta sidnummer; sidorna avser PDF-filen. [doi:10.2139/ssrn.4395987](https://doi.org/10.2139/ssrn.4395987)
- Robert S. Kaplan och Karthik Ramanna, *E-ledgers Carbon Accounting*, Blavatnik School of Government Working Paper BSG-WP-2025-62, augusti 2025, s. 1, 3, 4, 5, 6 och 27-28. Publicerad i *Management Science*, 2026. Sidhänvisningarna gäller arbetsversionen. [doi:10.1287/mnsc.2025.03520](https://doi.org/10.1287/mnsc.2025.03520)
- Stefan Reichelstein, "Corporate carbon accounting: balance sheets and flow statements", *Review of Accounting Studies* 29 (2024), s. 2125-2156, här s. 2127, 2134, 2140 och 2145. [doi:10.1007/s11142-024-09830-y](https://doi.org/10.1007/s11142-024-09830-y)
