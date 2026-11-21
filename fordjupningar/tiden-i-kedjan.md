---
layout: default_banner
title: "Tiden i kedjan"
parent: "Fördjupningar"
nav_order: 14
---

# Tiden i kedjan

> **Poäng:** MASSIV+ räknar mängder per relation och period, och de blir kända först när perioden stängs. Därför måste standarden säga vilken period en post gäller och vad som händer när den kommer sent. Med periodisering hamnar faktisk data i rätt period, och det som är äldre blir okänt, utom det som en nod öppet för via sitt lagerkonto. Det gör att även oändligt djupa kedjor går att hantera utan cut-off, och att inköpare kan utvärdera leverantörer och följa upp avtal period för period.

Texten förutsätter en grundläggande bild av MASSIV+. Läs [introduktionen](../introduktion.md) först om du inte är bekant med standarden. Den normativa regeln föreslås i [MF-006 Periodregel](../forslag/mf-006-periodregel.md), som ännu inte är antagen.

---

## 1. Varför tiden blir en fråga

En nod räknar sitt T för en period och fördelar hela mängden på sina mottagare ([§3-5](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Både T och mottagarens andel är storheter för hela perioden. En allokeringspost kan därför utfärdas först när avsändaren har stängt perioden, och då har mottagaren ofta redan stängt sin.

Tre forskarförslag som också för över redovisningens principer till utsläpp har inte den frågan, eftersom de bokför överföringen när affären görs:

- **Jia m.fl.** (Oxford) redovisar en energipost *"at the same point-in-time as the financial transaction"* (s. 8). Perioden kan vara månad, kvartal eller år (s. 22).
- **Reichelstein** (Mannheim) debiterar materiallagret vid inköpet med leverantörens produktavtryck, eller med ett branschtal när leverantören saknar egen beräkning (s. 2134). Skillnaden i tid mellan när utsläppet uppstår och när varan säljs hanteras med periodiseringar och lager (s. 2127 och 2140).
- **Kaplan och Ramanna** (Oxford och Harvard) för posten hos säljare och köpare vid försäljningen, där kunden *"willingly assumed the emissions"* som en del av affären (s. 5). Målet är redovisning *"in as close to real time as practicable"* (s. 1).

Reichelstein och Kaplan och Ramanna kan bokföra vid affären därför att de bär ett tal per producerad enhet, framräknat i produktkalkylen. Talet finns när affären görs, ungefär som ett pris. Jia m.fl. anger inte hur säljarens tal når köparen. MASSIV+ följer affärsrelationen och räknar mängder per relation och period ([§5](../standard/specifikation.md#individuation-av-allokeringsenheten), [koordinatbytet](koordinatbytet.md)). På bokföringsspråk är de två produktförslagen löpande lagerredovisning och MASSIV+ periodisk. Tidsfrågan är priset för relationskoordinaten.

Två saker hos forskarna stöder ändå den väg MASSIV+ föreslår. Reichelstein använder periodiseringar för att talen ska hamna i rätt period. Och ingen av de tre har något som motsvarar replacement rule: ett branschtal som bokförs vid inköpet står kvar. Det är ersättningen av okänt med faktiskt ([§6](../standard/specifikation.md#6-replacement-rule---progressiv-dataförbättring)) som gör periodisering möjlig i MASSIV+.

## 2. Periodisering

MF-006 föreslår att en post gäller avsändarens period. Det som saknas när mottagaren stänger bokförs som U. När posten kommer ersätter den U, och mottagaren uppdaterar sina egna poster, som är preliminära tills noden förklarar perioden slutlig. Det är så bokföringen hanterar en faktura som kommer efter bokslutet: en upplupen kostnad vid bokslutet som vänds när fakturan kommer.

Alternativet vore att bokföra posten när den utfärdas, alltså oftast för avsändarens föregående period. Det kräver inga nya versioner, men perioderna blandas och varje led lägger till en period. Hur de två skiljer sig i ett räkneexempel visas i MF-006.

## 3. Djupa kedjor och cut-off

Värdekedjor är i praktiken mycket djupa. Huvudflödet har få steg, men de flöden som omger det fortsätter nästan utan slut: förnödenheter, tjänster, transporter, och deras leverantörer i sin tur. En livscykelanalys hanterar det med cut-off. Flöden under en gräns lämnas utanför, och den mängden försvinner ur resultatet.

**Kedjan slutar där deltagandet slutar.** I MASSIV+ når kedjan så långt som leverantörerna utfärdar poster. Vid den första leverantören som inte gör det tar U över, med full mängd ([§2](../standard/specifikation.md#u-värdets-roll)). Ingenting skärs bort. Ju fler som ansluter, desto djupare blir den del av kedjan som bygger på faktisk data.

**Faktisk data gäller rätt period.** Med periodisering kommer A bara in från poster för perioden. En nod för vidare sina egna utsläpp och sitt A för perioden, och när en leverantörs post är sen fyller noden luckan med U. Steg för steg följer att det som är äldre än perioden hamnar i U. Långt bak i kedjan, där någon länk inte hann med, finns bidraget kvar som okänt med full mängd. Nära i kedjan är det aktuellt och faktiskt. Det fungerar som en cut-off i tid där ingen mängd försvinner: andelen faktisk data och aktualiteten avtar med avståndet, men mängden är komplett. Undantaget är A som en nod för via sitt lagerkonto ([MF-001](../forslag/mf-001-lagerhantering.md)). Det redovisas öppet i lagerkontot och motsvarar varor som faktiskt levereras under perioden.

Bokförs posten när den utfärdas blir det omvänt. Ett bidrag från k led bort är k perioder gammalt och räknas ändå som A. I en djup kedja innehåller A då bidrag av alla åldrar, och ingen kan se det. Det räcker att en enda nod bokför så för att äldre A ska följa med nedströms. Därför föreslår MF-006 en metod för alla.

**En period blir slutlig när noden säger det.** Någon post långt bak i kedjan är alltid sen. En period kan därför inte bli slutlig genom att allt har kommit in. MF-006 föreslår att varje nod, som i bokföringen, själv bestämmer när dess period är slutlig, senast sex månader efter periodens slut. Det som kommer senare bokförs i nästa period.

**Rättelser stannar vid den slutliga perioden.** I vanlig bokföring är kedjorna lika oändliga, men priset bryter dem vid varje led. Fakturans belopp beror inte på säljarens kostnader, så en rättelse hos säljarens leverantör ändrar inte det säljaren redan har fakturerat. I MASSIV+ finns inget pris som bryter kedjan. Posten är avsändarens T gånger kundens andel, och utsläpp förs vidare som om allt såldes till självkostnad (Kaplan och Ramanna, s. 5-6). En rättelse uppströms ändrar därför avsändarens post. Det är den slutliga perioden som bryter kedjan, på samma sätt som bokslutet: det som kommer senare går vidare med nästa periods post. Bara väsentliga rättelser ger en rättad version av en slutlig post, och de krymper i förhållande till varje nods T för varje led tills de inte längre är väsentliga.

| | Huvudflödet | Kanten |
|---|---|---|
| Vad det är | De få stora stegen | Det som en livscykelanalys skulle skära bort |
| Hur det hanteras | Avtal om att poster ska komma i tid före den slutliga perioden | Senaste post som underlag för U, och att perioden förklaras slutlig, utan särskilt arbete |
| Status i talet | Aktuellt och faktiskt | Äldre och okänt, med full mängd |

Ingen behöver avgöra var huvudflödet slutar. Varje nod stoppar rättelserna lokalt genom att förklara sin period slutlig. Det följer [§8](../standard/specifikation.md#8-coverage---mått-på-datakvalitet), där uppströms-Coverage används för att prioritera insatser där uppströmsflödena är stora.

## 4. Många verktyg

MASSIV+ bygger på en decentraliserad ansats, där organisationerna använder olika verktyg på samma sätt som i bokföringen. Periodiseringen kräver inget gemensamt verktyg. Varje nod avgör utifrån sitt eget inflöde om den ska utfärda en ny version, utan att se resten av kedjan ([§5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)). Det som behöver vara gemensamt är postens innehåll, inklusive version, hänvisning till den post som ersätts ([MF-005](../forslag/mf-005-allokeringsposter.md)) och markeringen preliminär eller slutlig. När en period blir slutlig och vad som är väsentligt bestämmer varje nod själv, som i bokföringen. Där finns varken ett gemensamt bokslutsdatum eller en fast procentsats för väsentlighet.

Versionerna går genom kedjan i den takt den långsammaste länken klarar. Den som räknar för hand håller tillbaka dem som kommer efter. Att varje nod förklarar sin period slutlig sätter ett tak: det som kommer senare bokförs i nästa period. Kedjan blockeras aldrig, den blir bara mindre aktuell för den perioden.

## 5. Leverantörsutvärdering

Specifikationens sammanfattning beskriver MASSIV+ som ett sätt att sätta KPI:er för kontinuerlig utsläppsminskning, som krav eller incitament mot leverantörer, och som ett upphandlingsverktyg. Periodiseringen avgör om det fungerar i praktiken.

- **Trenden per leverantör.** Varje relation får en mängd utsläpp per period, i rätt period. Inköparen kan följa en leverantörs minskning kvartal för kvartal. Bokförs posten när den utfärdas innehåller leverantörens kvartal i stället äldre kvartal från dess egna leverantörer.
- **Utvärdering på slutlig version.** Innan leverantören har förklarat perioden slutlig påverkas Coverage av hur snabba leverantörens egna leverantörer är. Utvärderingen bör bygga på den slutliga versionen, annars mäter Coverage förseningar i stället för datakvalitet.
- **Punktlighet.** Andelen poster som kommer inom en avtalad tid är ett mått som kan ställas som krav i avtal. §6 nämner redan avtal som specificerar rapporteringskrav.
- **Samma period.** En leverantör med kvartal och en med år jämförs på helår. Posten anger vilken period den gäller, så jämförelsen går att göra.
- **Orsaken till en förändring.** En förändring kan bero på verklig minskning, på att okänt ersatts av faktiskt eller på ändrade definitioner ([metodologiska risker](metodologiska-risker.md#verklig-förändring-mot-dataförbättring)). Med perioder som inte blandas går de att skilja åt.

För att jämföra två leverantörer räknar inköparen mängd per inköpt kvantitet, alltså postens mängd delad med de egna inköpen. Talet hör till inköparens beslut och relationen. Det förs inte vidare som ett produkttal.

## 6. Offertförfrågan och offererat värde

Vid en offertförfrågan finns ingen relation än och därmed ingen post. En post beskriver en relation och en period i efterhand, som en faktura. En offert behöver ett tal om framtiden, som ett pris.

Anbudsgivaren kan lämna ett **offererat värde**: den avsändande nodens senaste slutliga T och allokeringsregel tillämpade på den offererade volymen, med period, Coverage och version av emissionsfaktorerna angivna. Värdet gäller en viss nod. En leverantör med flera noder kan offerera från den nod som ska leverera ([MF-004](../forslag/mf-004-nodindelning.md)).

Det offererade värdet är inte en allokeringspost. Det bokförs inte som A och förs inte vidare. Det beskriver en relation som inte finns än, och utan den avgränsningen glider det lätt mot ett tal per produkt.

Periodiseringen ger fem följder:

1. **Offerten bygger på slutlig version**, så att ingen offererar på ett preliminärt tal.
2. **Kortare perioder ger aktuellare anbud.** En leverantör som stänger kvartalsvis kan offerera på förra kvartalets data. Det ger ett skäl att välja kortare period.
3. **Avtalet kan följa upp offert mot utfall.** Utfallet kommer för rätt period efter stängningen, så offererat värde och faktiskt utfall kan jämföras period för period, med bonus eller avdrag om parterna vill. Bokförs posten när den utfärdas jämför uppföljningen olika perioder.
4. **Offerten kan fylla luckan för en ny leverantör.** Innan den första posten har kommit finns ingen tidigare post att använda som underlag för U. MF-006 rekommenderar då det offererade värdet.
5. **Anbudsgivare utan MASSIV+** kan bara lämna underlag för U, till exempel en EPD ([§2](../standard/specifikation.md#separation-av-faktisk-och-okänd-data)). Skillnaden syns i Coverage.

## 7. Öppna frågor

- **Yttre gräns och väsentlighet.** Om sex månader är rätt yttre gräns för när en period ska vara slutlig, och om det behövs ett riktvärde för väsentlighet när en slutlig period rättas. Frågorna ställs i [MF-006](../forslag/mf-006-periodregel.md).
- **Preliminär deklaration.** Om en leverantörs egen preliminära deklaration kan räknas som A, så att signalen når kunden redan under perioden.
- **Lager.** [MF-001](../forslag/mf-001-lagerhantering.md) föreslår ett lagerkonto för hela noden. Det ger jämnare tal men gör att en leverantörs minskning når kunderna först när lagret omsätts. Hur den avvägningen ska göras är öppen.
- **Offererat värde.** Om det ska beskrivas i standarden, i en vägledning eller bara i avtal och verktyg.

## Källor

- Jimmy Jia, Barbara Rossi, Abrar Chaudhury, Evan Taylor och Dennis West, "A reporting framework for general purpose life cycle assessment to align entity-level GHG accounting with general purpose financial statements", arbetspapper, SSRN 4395987, version 22 april 2024, s. 8 och 22. [doi:10.2139/ssrn.4395987](https://doi.org/10.2139/ssrn.4395987)
- Robert S. Kaplan och Karthik Ramanna, *E-ledgers Carbon Accounting*, Blavatnik School of Government Working Paper BSG-WP-2025-62, augusti 2025, s. 1, 3, 5 och 6. Publicerad i *Management Science*, 2026. Sidhänvisningarna gäller arbetsversionen. [doi:10.1287/mnsc.2025.03520](https://doi.org/10.1287/mnsc.2025.03520)
- Stefan Reichelstein, "Corporate carbon accounting: balance sheets and flow statements", *Review of Accounting Studies* 29 (2024), s. 2125-2156, här s. 2127, 2134 och 2140. [doi:10.1007/s11142-024-09830-y](https://doi.org/10.1007/s11142-024-09830-y)
