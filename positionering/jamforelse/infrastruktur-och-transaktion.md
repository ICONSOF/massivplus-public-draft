---
layout: default
title: "Infrastruktur och transaktion"
nav_order: 6
---

# MASSIV+ och infrastruktur- och transaktionslagret

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

DPP och BEAst är bärare och kanaler snarare än beräkningsstandarder: ett register respektive en affärstransaktionsstandard som MASSIV+-data kan flöda i. Det skiljer dem från beräknings- och deklarationsstandarderna och motiverar att de behandlas tillsammans.

---

## MASSIV+ vs. DPP (Digital Product Passport)

DPP är ett EU-reglerat krav under ESPR (EU 2024/1781) - ett digitalt identitetskort för produkten som samlar information om material, kemikalier, reparerbarhet, återvinningsbarhet och koldioxidavtryck. Batterier regleras separat (EU 2023/1542) och är först ut med obligatoriskt pass från 18 februari 2027; arbetsplanen 2025-2030 pekar därefter ut järn/stål (den första egentliga delegerade akten), textil, aluminium och däck som prioriterade sektorer, med indikativa datum som rimligen förskjuts. Den tekniska infrastrukturen har tagit ett stort steg: CEN/CENELEC JTC 24 publicerade i slutet av maj 2026 den första uppsättningen EN 1821x-standarder som definierar hur passet identifieras, bärs, överförs, lagras och görs interoperabelt (bland andra EN 18219 unika identifierare, EN 18220 databärare, EN 18216 dataöverföring, EN 18222 API:er); ytterligare standarder i serien väntas senare 2026.

En avgränsning följer direkt av detta och är central för relationen till MASSIV+: EN 1821x styr *hur* passet bärs och utbyts, medan *vilka* datafält som krävs bestäms per produktgrupp av delegerade akter (och identitet och semantik av GS1/ECLASS). DPP är alltså självt tvålagrat - en bärarstandard som är metodneutral för de flesta fält, med innehållskraven i ett separat lager. Det speglar MASSIV+:s egen uppdelning i ett semantiskt lager (vad ett tal betyder) och ett utbyteslager (hur det flyttas), och det gör bärardelen till något MASSIV+ kan använda snarare än konkurrera med.

DPP:s dataarkitektur är dessutom decentraliserad snarare än en central databas. EU:s DPP-register håller de unika identifierarna och en hänvisning till var det fullständiga passet ligger; själva passdatan stannar hos den ansvariga aktören eller en godkänd tjänsteleverantör och nås via databäraren. Det är samma datasuveränitet - datan delas, den samlas inte in centralt - som MASSIV+:s utbyte förutsätter. Det gör också "register" till en oprecis etikett: passet är ett decentraliserat dataobjekt med ett centralt id-register ovanpå.

DPP och MASSIV+ opererar i grunden på olika logiska nivåer. DPP är ett dataobjekt som svarar på *"vad vet vi om den här produkten och var lagras det?"*; MASSIV+ är en beräknings- och propageringsstandard. För merparten av passets fält - material, kemikalier, reparerbarhet, återvinningsbarhet - är passet metodneutralt och bär det datakällan levererar. Koldioxidfältet är undantaget, och där blir relationen mer än en nivåskillnad.

ESPR fastställer att ett avtryck ska bäras men överlåter metoden till sektorspecifika delegerade akter. Där ett avtryck krävs är metoden föreskriven: EU:s referens är PEF (kommissionens rekommendation (EU) 2021/2279) och ISO 14067 - produktnivå-LCA uttryckt som kg CO₂e per funktionell enhet. Batteripasset (EU 2023/1542), det första DPP:t i drift, visar det konkret: obligatorisk avtrycksdeklaration enligt PEF-metoden, funktionell enhet en kWh levererad energi över batteriets livslängd, systemgräns cradle-to-grave (vaggan till graven, dvs. hela livscykeln) men med användningsfasen undantagen enligt batteriregelns egen avgränsning, och företagsspecifik data obligatorisk för samtliga tillverkningssteg. Koldioxidfältet ärver alltså en föreskriven metod.

Två konsekvenser är värda att hålla isär. Den första gäller jämförbarhet. Eftersom koldioxidfältet ärver en metod med betydande frihetsgrader (val av systemgräns, allokering och bakgrundsdata) är fältets värden inte utan vidare jämförbara mellan aktörer, och passets uttalade ändamål är transparens, spårbarhet och cirkularitet snarare än jämförbarhet på klimatfältet. Det är precis den luckan MASSIV+ adresserar i Scope 1+2-ledet: gemensamma emissionsfaktorer och Coverage gör underlaget jämförbart och kvalitetsmärkt. Den andra gäller åtkomst. DPP:s åtkomst är skiktad - konsumentvyn är öppen baskunskap, medan full materialsammansättning och Scope 3-underlag ligger i den behörighetsstyrda B2B-vyn. Ett MASSIV+-nodvärde hör hemma i den behörighetsstyrda vyn, mot en identifierad motpart, inte i det öppna konsumentledet.

Därför går DPP:ns relation till MASSIV+ på koldioxidsidan genom MASSIV+:s relation till [produktstandarderna](produktstandarder.md), snarare än vid sidan av den. Ett MASSIV+-nodvärde är en annan storhet än en PEF-PCF: det gäller en nod och inte en produkt, det täcker det uppströms ledet snarare än cradle-to-grave, och det allokerar och kvalitetsmärker enligt egen logik (massa, energi eller värde; Coverage = A/(A+U)) i stället för PEF:s allokerings- och DQR-regler. DPP är förankrat i produktartefakten - en ny produkt får ett nytt pass som refererar uppströms pass - medan MASSIV+ är förankrat i organisationen och affärsrelationen (se [koordinatbytet](../../fordjupningar/koordinatbytet.md)). Det är därför ett MASSIV+-nodvärde är *underlag* till passets koldioxidfält, inte fältet självt: för en reglerad produktgrupp som batterier utgör MASSIV+-data underlaget som den föreskrivna avtrycksberäkningen förbrukar.

Komplementariteten ligger ett steg in. PEF- och batteriberäkningen kräver företagsspecifik data för de egna processerna men vilar uppströms på sekundär databasdata, utan krav på leverantörsspecifika underlag eller kvalitetsmärkning av det ledet. Det är precis det ledet MASSIV+ förstärker: propagerad primärdata med ett täckningsmått i stället för branschsnitt. MASSIV+ matar alltså den uppströms primärdata som den föreskrivna PCF-beräkningen förbrukar - samma roll som mot EPD, PACT och ISO 14067 - och om värdet kan föras direkt in i avtrycksfältet avgörs av produktgruppens delegerade akt.

| Dimension | DPP | MASSIV+ |
|---|---|---|
| Rättslig grund | Obligatorisk (ESPR 2024/1781) | Frivilligt ramverk |
| Systemtyp | Dataobjekt (bärarstandard EN 1821x) | Propageringssystem |
| Central enhet | Produkt (artefakt) | Nod (organisatorisk enhet) |
| Datalagring | Decentraliserad hos aktören; centralt id-register | Decentraliserad; självrapportering per nod |
| Koldioxidfältets metod | PEF / ISO 14067 per delegerad akt | Nodnivå-allokering; Coverage = A/(A+U) |
| Jämförbarhet på klimatfältet | Inte garanterad (öppen metod, frihetsgrader) | Gemensamma EF + Coverage gör underlaget jämförbart |
| Relation | Bärare; koldioxidfältet ärver produktstandardernas metod | Uppströms primärdatakälla till den föreskrivna PCF-beräkningen |

---

## MASSIV+ och BEAst

BEAst (Byggbranschens Elektroniska Affärsstandard) är byggsektorns informationsstandard för de affärsprocesser som omger en leverans: upphandling, inköp, logistik och fakturering. Den ideella föreningen bakom standarden har över 100 medlemmar. Den centrala standarden BEAst Supply 4.0 definierar den digitala följesedeln och utbyte av miljö- och klimatdata för transport, maskin och bulkmaterial, byggd på UBL (Universal Business Language) med PEPPOL som transportlager. Meddelandekedjan omfattar order, orderbekräftelse, leveransavisering (e-följesedel med exakta kvantiteter, artikel- och sändningsreferenser, ankomsttid och ansvarigt transportföretag) och transportstatus. Sedan 2023 kan en leverantör rapportera bränsleförbrukning per transport digitalt i enhetligt format, och köparen kan kräva mer detaljerade uppgifter - exempelvis bränsleförbrukning eller referenser till EPD och säkerhetsdatablad för godset. Trafikverket ställer från mars 2024 krav på rapportering av bränsleförbrukning enligt BEAst i upphandlingar för väg och anläggning.

BEAst och MASSIV+ ligger på olika logiska nivåer och är komplementära. BEAst standardiserar affärstransaktionen mellan två identifierade parter; MASSIV+ standardiserar utsläppsbokföringen på organisationsnivå. De möts i den bilaterala transaktionen, och strukturmatchningen är ovanligt tät:

- **Bilateral logik på samma teknikrygg.** MASSIV+:s princip "ditt Scope 1+2 är mitt Scope 3" har samma struktur som e-fakturan: säljarens utgående post är köparens ingående, och kedjan terminerar hos slutkonsumenten. BEAst Supply 4.0 vilar på UBL/PEPPOL, samma rygg som den europeiska e-fakturan. Den bilaterala kanal MASSIV+:s specifikation lämnar till separata tekniska dokument finns alltså redan byggd och sektoradopterad.
- **Allokeringsnyckeln finns i meddelandet.** MASSIV+ §3 tillåter allokering per massa, kvantitet eller värde. Leveransaviseringen bär kvantiteter och artikelreferenser; fakturan bär värdet. De underlag en nod behöver för sina Share-koefficienter passerar alltså redan genom BEAst.
- **Identifierad motpart.** MASSIV+ kräver en namngiven nod i andra änden för att bokföringen ska gå ihop. BEAst löser partsidentifiering (PEPPOL) i sina meddelanden.

Skillnaden ligger i vad som är standardiserat på klimatsidan. BEAst:s klimatdata är på transaktions- och aktivitetsnivå - bränsleförbrukning för en transport, plus möjlighet att referera EPD för godset. Det är metodologiskt närmare en transport- eller produktdeklaration än MASSIV+:s nodnivå, där nodens totala Scope 1+2 fördelas över samtliga kunder. Det BEAst lämnar öppet är precis det MASSIV+ tillför: ett gemensamt emissionsfaktorset som gör bränsledata jämförbar mellan aktörer (BEAst tar inte ställning till vilken faktor en liter diesel ska multipliceras med), samt A/U-separation, Coverage och massbalans som gör enskilda följesedelsvärden till en koherent och propagerbar kedja - samma steg från lösa punktdeklarationer till värdekedjebild som skiljer MASSIV+ från en ren EPD-strategi (se [EPD-avsnittet](produktstandarder.md#epd--iso-14025)). Relationen liknar den till DPP - BEAst är en bärare och datakälla, inte ett beräkningssystem - men är tätare än DPP eftersom den är bilateral och transaktionsbunden, vilket matchar MASSIV+:s egen logik. MASSIV+-beräknad data (Actual, Unknown, Coverage) kan bäras som strukturerade element på en BEAst-följesedel eller faktura.

En praktisk konsekvens värd att hålla framme: bygg är en sektor där en bilateral transaktionsstandard redan är adopterad, redan bär en första klimatdatapunkt och har regulatoriskt tryck bakom sig. Det gör sektorn till en stark kandidat som ledsektor för tidig MASSIV+-adoption, eftersom skenan, partsidentifieringen och aktivitetsdatan redan ligger på plats. Den vinkeln hör hemma i [positionering och affärsvärde](../positionering-och-affarsvarde.md) om den utvecklas vidare.

| Dimension | BEAst (Supply 4.0) | MASSIV+ |
|---|---|---|
| Central enhet | Affärstransaktion / meddelande mellan två parter | Nod (organisatorisk enhet) |
| Systemtyp | Transaktions- och utbytesstandard | Propageringssystem |
| Teknikrygg | UBL / PEPPOL | Specificeras separat (data spaces) |
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
