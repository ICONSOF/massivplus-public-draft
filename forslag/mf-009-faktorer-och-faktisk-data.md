---
layout: default_banner
title: "MF-009 Faktorer, faktisk data, verifierbarhet och fördelningsordning"
parent: "Förslag"
nav_order: 9
forslag_id: MF-009
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§2, §3"
forslag_forfattare: Birger Löfgren
---

# MF-009 Faktorer, faktisk data, verifierbarhet och fördelningsordning

> **Status:** Utkast, 2026-11-23. Ingår inte i standarden. Berör §2 och §3. Författare: Birger Löfgren.
>
> Förslaget samlar fyra ändringar som kom fram när specifikationen jämfördes med redovisningsforskningens förslag: E-ledgers (Kaplan och Ramanna), Reichelsteins balansräkning för koldioxid och principerna från ICC:s expertpanel (se [Bokföringsanalogin](../fordjupningar/bokforingsanalogin.md#4-den-framväxande-tanken-om-bokföring-av-utsläpp)). Ändringarna kan bedömas var för sig.

Fyra luckor i §2 och §3:

1. **Faktorsetet täcker bara förbränning och köpt energi.** §2 har faktorer *"per bränsleslag och energibärare"*. Processutsläpp, där koldioxid frigörs ur en råvara, och läckage av andra växthusgaser har ingen regel. Specifikationen anger inte heller enhet eller GWP-värden. [MF-003](https://github.com/ICONSOF/massivplus-public-draft/blob/forslag/mf-003-ets/forslag/mf-003-ets.md) täcker processutsläpp i anläggningar som ingår i EU ETS, men inte andra.
2. **A bestäms av källan.** Bara en MASSIV+-deklaration räknas som A. En leverantör som för en löpande redovisning av utsläpp per produkt, till exempel enligt E-ledgers, blir U hos kunden, även om talen gäller periodens leveranser och är granskade.
3. **Inget gör A verifierbart.** §2 säger att A vilar på ansvarig avsändare. Det finns inget krav på att talen ska gå att granska och ingen uppgift om de är granskade. [Metodologiska risker](../fordjupningar/metodologiska-risker.md#konsistens-är-inte-korrekthet) anger verifieringen som hanterad i riktning.
4. **§3 saknar ordning mellan fördelningsmetoderna.** Massa, energi, kvantitet och intäkt räknas upp sida vid sida. Metodologiska risker säger att MASSIV+ följer ISO 14044 och GHG Protocol med fysiska samband före ekonomiska, men specifikationen säger det inte.

## Förslag till standardtext

### 1. §2, Standardiserade emissionsfaktorer: ändra och lägg till

Nuvarande lydelse, andra meningen:

> MASSIV+ tillhandahåller därför ett gemensamt, fastställt set av emissionsfaktorer per bränsleslag och energibärare som samtliga noder är skyldiga att använda - inga egna emissionsfaktorer tillåts för dessa komponenter.

Föreslagen lydelse:

> MASSIV+ tillhandahåller därför ett gemensamt, fastställt set av emissionsfaktorer som samtliga noder är skyldiga att använda - inga egna emissionsfaktorer tillåts för dessa komponenter.

Lägg till efter stycket:

> Utsläppen redovisas i ton koldioxidekvivalenter (CO2e). Setet täcker tre slags källor:
>
> - **Förbränning och köpt energi:** faktorer per bränsleslag och energibärare.
> - **Processutsläpp,** där koldioxid frigörs ur en råvara, till exempel när kalksten bränns: faktorer per råvara, eller en kolbalans som bygger på uppmätt kolhalt i det som går in i och ut ur processen.
> - **Läckage** av andra växthusgaser, till exempel köldmedier: läckt mängd, till exempel påfylld mängd, gånger gasens GWP-värde (global uppvärmningspotential över 100 år).
>
> GWP-värdena hämtas från den IPCC-rapport som setet anger.

### 2. §2, Separation av faktisk och okänd data: ersätt stycket om A-värden

Nuvarande lydelse:

> A-värden förutsätter att leverantören själv har utfärdat en MASSIV+-deklaration för sina Scope 1+2. Externa primärdatakällor (EPD, PCF, PACT/Catena-X) kan användas som grund för mer välunderbyggda U-underlag hos mottagaren, men räknas inte som A - distinktionen handlar om ansvarig avsändare, inte om numerisk kvalitet.

Föreslagen lydelse:

> Ett A-värde är en deklaration som leverantören själv har utfärdat. Den ska gälla periodens leveranser till mottagaren, vara en del av leverantörens hela utsläppsmassa enligt massbalansen (§5), hålla isär det faktiska och det okända enligt §4 och bygga på Scope 1 och 2 beräknade enligt detta avsnitt. En deklaration som uppfyller kraven räknas som A, också när den tagits fram ur leverantörens löpande redovisning av utsläpp per produkt. Uppgifter som inte uppfyller dem, till exempel en EPD eller en PCF som beräknats för en produkt vid ett tillfälle och delas genom PACT eller Catena-X, kan ge ett bättre underlag för U hos mottagaren men räknas inte som A. Distinktionen handlar om ansvarig avsändare och periodens leveranser, inte om numerisk kvalitet.

### 3. §2: lägg till Verifierbarhet

Nytt delavsnitt efter Separation av faktisk och okänd data:

> ### Verifierbarhet
>
> En nod dokumenterar sina tal så att en oberoende granskare kan följa dem: från aktivitetsdata och mottagna poster, via emissionsfaktorer, nodindelning och allokeringsregel, till de poster noden lämnar. Varje deklaration anger om den är granskad, och i så fall av vem och med vilken säkerhet, till exempel begränsad eller rimlig säkerhet enligt ISAE 3000. Vilken granskning som krävs av vilka aktörer bestäms i det regelverk som tillämpar standarden.

### 4. §3: lägg till ordning mellan metoderna

Lägg till efter listan över tillåtna metoder:

> Metoden väljs i denna ordning, som i ISO 14044 (avsnitt 4.3.4.2) och GHG Protocols Scope 3-standard (avsnitt 8.3):
>
> 1. Undvik fördelning där det går, genom en nodindelning som knyter utsläppen till de leveranser de hör till (§1).
> 2. Fördela efter ett fysiskt samband: massa, energi eller kvantitet.
> 3. Fördela efter värde eller med annan proportionell metod, när inget fysiskt samband speglar vad som ger upphov till utsläppen.
>
> Noden dokumenterar varför den valt sin metod.

### Följdändring i introduktionen

Princip 3, nuvarande lydelse: *"samma gemensamma set av emissionsfaktorer för Scope 1+2 - per bränsleslag och energibärare."* Föreslagen lydelse: *"samma gemensamma set av emissionsfaktorer för Scope 1+2 - per bränsleslag och energibärare, och för processutsläpp och läckage av andra växthusgaser."*

## Varför

**Faktorerna.** Principen om gemensamma faktorer finns för att skillnaden mellan två noders Scope 1 ska bero på verksamheten och inte på faktorvalet (§2). Den bär bara så långt setet räcker. För cement, kalk, kemi och kylanläggningar utanför EU ETS finns i dag ingen metod för en stor del av Scope 1. Faktorer per råvara och GWP-värden är lika standardiserbara som faktorer per bränsle. Kolbalansen behövs när råvarans kolhalt varierar, och den bygger på mätning, vilket är faktisk data.

**A efter kriterier.** Kraven i förslaget är de skäl som redan står bakom §2: en ansvarig avsändare, periodens faktiska leveranser och massbalansen. En EPD faller på att den gäller en beräkning vid ett tillfälle och inte periodens leveranser till en viss kund. En löpande redovisning per produkt, som E-ledgers föreslår, gör inte det. Där förs posten samtidigt hos säljaren och köparen, och talen gäller aktuell produktion (Kaplan och Ramanna 2025, s. 2 och 5). Med kriterier kan en sådan leverantör lämna A till en MASSIV+-kund, och MASSIV+ kan användas av företag utan produktkalkyl i samma kedja som företag med.

**Verifierbarhet.** Alla tre förslagen i redovisningsforskningen gör granskning till en del av redovisningen. Kaplan och Ramanna kräver granskning med rimlig säkerhet av egna utsläpp, fördelning och överföring (s. 3). ICC-panelens princip *Verifiability* kräver att redovisningen *"allows a qualified independent party to attest"* (ICC 2026, s. 2), alltså att den går att granska. Förslaget lägger samma gräns. Standarden kräver att talen går att granska och att mottagaren ser om de är granskade. Vem som måste granskas, och hur noga, bestäms i regelverket runt standarden. Den finansiella redovisningen har samma uppdelning mellan redovisningsstandarden, granskningsstandarden och lagens krav för olika storlekar. Utan uppgiften om granskning kan en kund inte skilja ett granskat A från ett självdeklarerat, och Coverage blir ett mått på hur många som deltar.

**Ordningen.** Ordningen följer ISO 14044 och GHG Protocol. Den dikterar ingen nyckel, och noden väljer fortfarande efter situation och kostnad. Den hindrar att ett ekonomiskt mått används där ett fysiskt samband finns. Med intäktsnyckel får två kunder som köper samma vara till olika pris olika utsläpp per ton, och en kund som betalar mer för en grönare vara får en större del av utsläppen (se exemplet). Kaplan och Ramanna avvisar enkla fördelningsbaser för utsläpp just därför att olika kunder köper olika saker (s. 8). Steg 1 är MASSIV+:s motsvarighet till ISO:s uppdelning av processen: en nodindelning som följer kopplingen mellan inköp och försäljning ([MF-004](mf-004-nodindelning.md)).

## Exempel

En nod har T = 1 000 ton CO2e och säljer 100 ton av samma vara till var och en av två kunder. Kund X betalar 2 miljoner kronor, eftersom den har köpt med certifierat lägre utsläpp i leverantörsledet. Kund Y betalar 1 miljon. Talen är påhittade.

| Nyckel | Kund X | Kund Y | Summa |
|---|---|---|---|
| Massa | 500 | 500 | 1 000 |
| Intäkt | 667 | 333 | 1 000 |

Summan är densamma med båda nycklarna. Med intäktsnyckel får X, som betalat för en grönare vara, en tredjedel mer utsläpp än med massnyckel. Med ordningen i förslaget används massa, om inte noden visar att värdet speglar vad som ger upphov till utsläppen. Har X:s inköp en egen koppling till grönare råvara är steg 1 rätt väg: en nodindelning som ger X den råvarans utsläpp.

## Förhållande till andra förslag

- **MF-003** låter ETS-anläggningar använda sina verifierade utsläpp. Det här förslaget ger en regel för processutsläpp och läckage utanför ETS. MF-003-grenen säger att en PCF inte räknas som faktisk data. Det stämmer med punkt 2 för en PCF som beräknats vid ett tillfälle.
- **MF-005** får en rad Granskning i tabellen över postens innehåll, med hänvisning hit.
- **MF-006** frågar om avsändarens preliminära deklaration kan räknas som A. Kraven i punkt 2 hindrar det inte, så länge deklarationen gäller periodens leveranser.
- **MF-002 och MF-004.** D mäter hur mycket av leverantörernas utsläpp som hamnar hos fel kund. Ordningen i punkt 4 minskar avvikelsen, och steg 1 bygger på nodindelningen i MF-004.

## Alternativ som övervägts

- **Granskningsnivåer i standarden,** till exempel självdeklaration för små aktörer och tredje part för stora. Avvisat. Nivåerna beror på marknad, storlek och reglering, och de hör till regelverket runt standarden, på samma sätt som revisionsplikten står i lag och inte i redovisningsstandarden. Resonemanget utvecklas i en kommande fördjupning.
- **En fast nyckel per falltyp.** Avvisat, som i ISO 14044 och GHG Protocol. Sektorvisa konventioner kan växa fram ovanpå standarden.
- **Att varje PCF räknas som A.** Avvisat. En produktberäkning vid ett tillfälle gäller inte periodens leveranser och stämmer inte mot avsändarens massbalans.
- **En kanal per gas,** som Kaplan och Ramanna föreslår (s. 3-4), i stället för CO2e. Inte valt för att hålla posterna enkla, men se öppna frågor.

## Öppna frågor

- Vilken IPCC-rapport ska setet bygga på, och hur hanteras byte till en senare?
- Ska granskningsstatus ha fasta värden, till exempel ingen, begränsad och rimlig säkerhet?
- Ska gaserna kunna redovisas var för sig i posten, vid sidan av CO2e?
- Kan en del av en post vara A och resten U när den kommer från en redovisning per produkt, till exempel leverantörens egna utsläpp som A och uppströmsdelen som U?
- Räcker en dokumenterad motivering i steg 3, eller behövs exempel på när värde speglar vad som ger upphov till utsläppen?

## Källor

- ISO 14044:2006, *Environmental management - Life cycle assessment - Requirements and guidelines*, avsnitt 4.3.4.2.
- GHG Protocol, *Corporate Value Chain (Scope 3) Accounting and Reporting Standard* (2011), avsnitt 8.3 med figur 8.2, s. 88-89. [PDF](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard_041613.pdf)
- Robert S. Kaplan och Karthik Ramanna, *E-ledgers Carbon Accounting*, Blavatnik School of Government Working Paper BSG-WP-2025-62, augusti 2025, s. 2-5 och 8. Publicerad i *Management Science*, 2026, [doi:10.1287/mnsc.2025.03520](https://doi.org/10.1287/mnsc.2025.03520). Sidhänvisningarna gäller arbetsversionen.
- ICC Technical Expert Panel on Carbon Accounting, [*Mission, Opportunity, and Principles*](https://iccwbo.org/wp-content/uploads/sites/3/2026/07/2026_ICC_Technical_Expert_Panel_on_Carbon_Accounting_EN.pdf) (juli 2026), s. 2.
- IAASB, *ISAE 3000 (Revised), Assurance Engagements Other than Audits or Reviews of Historical Financial Information*.

## Beslut

Inte behandlat. Förslaget avser ändringar i §2 och §3 och en följdändring i introduktionen.
