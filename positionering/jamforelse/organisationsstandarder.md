---
layout: default
title: "Organisationsstandarder"
nav_order: 4
---

# MASSIV+ och organisationsnivåstandarderna

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

GHG Protocol och ISO 14064-1 verkar på samma nivå som MASSIV+ - organisationen snarare än produkten. Det här är de två standarder MASSIV+ ligger närmast och översätter principer ifrån.

---

## MASSIV+ vs. GHG Protocol

GHG Protocol och MASSIV+ svarar på olika frågor. GHG Protocol är världens dominerande ramverk för företags klimatredovisning - Corporate Standard (Scope 1-2) och Scope 3 Standard (värdekedjeutsläpp) - och svarar på frågan *"vad är bolaget X:s totala fotavtryck?"*. Det enskilda bolaget är central enhet: varje företag mäter sina egna Scope 1-2 och skattar Scope 3 uppdelat i 15 kategorier, ofta med EEIO-schabloner eller spenddatabaser som grund. Uppskattningar blandas in i det totala Scope 3-värdet utan att andelen osäker data alltid är transparent nedströms.

MASSIV+ svarar på en annan fråga: *"vad är detta flödes utsläpp genom värdekedjan?"*. Standarden utgår från ett nätverk av noder snarare än ett enskilt bolag. Utsläpp propageras matematiskt längs faktiska leverantörsrelationer istället för att skattas kategorivis per bolag. Faktisk data (A) och okänt (U) hålls strikt åtskilda och kvantifieras via Coverage-måttet - U är inte ett konkurrerande utsläppsanspråk utan ett täckningsunderlag som visar hur stor del av emissionsbilden som ännu saknar faktisk grund. För Scope 1 och 2 använder alla noder ett gemensamt, fastställt set av emissionsfaktorer per bränsle och energibärare - vilket eliminerar den godtycklighet i emissionsfaktorval som är ett känt problem i GHG Protocol-rapportering. Scope 1- och Scope 2-data enligt GHG Protocol är direkt användbar som ingångsvärde i MASSIV+-noder - systemen är komplementära och förstärker varandra.

GHG Protocols egen datakvalitetshierarki rangordnar leverantörsspecifik primärdata högst, över branschsnitt och proxydata, och Scope 3-vägledningen uppmuntrar aktörer att klättra mot den toppen. MASSIV+ gör det översta steget till strukturellt förval. Eftersom mottagarens Scope 3 är leverantörens faktiska Scope 1+2, allokerad längs den faktiska affärsrelationen, bär underlaget per konstruktion den specifika motpartens data. Relevansen kommer alltså av routningen längs relationen, inte enbart av att datan är faktisk. Det skiljer ut två kvalitetsaxlar som annars buntas i ett samlat datakvalitetsbetyg: Coverage mäter andelen faktisk data, medan relevansen styrs av nodgranulariteten - hur nära det faktiska A-värdet ligger just den leverans mottagaren tar emot.

| Dimension | GHG Protocol | MASSIV+ |
|---|---|---|
| Frågan som besvaras | "Vad är bolaget X:s totala fotavtryck?" | "Vad är detta flödes utsläpp genom värdekedjan?" |
| Output | Bolagsinventering, redovisning | Operativ flödesdata |
| Central enhet | Enskilt bolag | Nod i ett nätverk |
| Scope 3-hantering | 15 kategorier, skattas per bolag | Flödespropagering längs leverantörsrelationer |
| Okänd datas roll | Blandas in i Scope 3-värdet som uppskattning | Strukturellt åtskild från faktisk data (U vs A); U kvantifieras som täckningsunderlag, inte utsläppsanspråk |
| Emissionsfaktorer S1+S2 | Aktören väljer själv | Standardiserat gemensamt set för alla noder |
| Datakvalitetstransparens | Data quality indicators per kategori | Coverage-mått per nod |
| Krav för att starta | Fullständig kategoribedömning förväntas | Kan starta med partiell täckning |
| Datarelevans | Leverantörsspecifik primärdata överst i hierarkin, i praktiken sällan nådd | Leverantörsspecifik data som strukturellt förval; relevans styrs av nodgranularitet |

---

## MASSIV+ vs. ISO 14064-1

ISO 14064-1 är ISO-familjens organisationsnivåstandard för kvantifiering och rapportering av växthusgasutsläpp och upptag - den ISO-formella systern till GHG Protocol Corporate Standard. Standarden är programmeneutral och har en specificerad verifieringsstack: ISO 14064-3 (verifiering), ISO 14065 (verifieringsorgan) och ISO 14066 (kompetenskrav). Sedan andra upplagan (2018) ersätter sex kategorier den tidigare Scope 1/2/3-strukturen: kategori 1 (direkta), 2 (importerad energi), 3 (transport), 4 (produkter org köper), 5 (användning av sålda produkter) och 6 (övriga indirekta).

MASSIV+ verkar på samma nivå som ISO 14064-1. Designansatsen är att linjera med standardens struktur, snäva några av dess tillåtna val för att uppnå jämförbarhet, och addera ett operativt flödeslager där standarden inte tar ställning.

**Linjerat med 14064-1.** Flera av MASSIV+:s grunddrag är direkt sammanfallande med 14064-1:

- **Primärdata.** MASSIV+:s A-komponent är operativt identisk med 14064-1 definition 3.2.2: *"quantified value of a process or an activity obtained from a direct measurement or a calculation based on direct measurements."* Coverage motsvarar primärdataandel per nod.
- **Massbalans.** 14064-1 Annex C (informativ) listar massbalans bland tillåtna kvantifieringsmodeller för direkta utsläpp. MASSIV+ generaliserar samma princip från källnivå till nätverksnivå.
- **Location-based el som default.** 14064-1 Annex E (normativ) föreskriver location-based för importerad el; marknadsbaserat tillåts som tilläggsinformation under kontraktskvalitetskriterier. MASSIV+:s standardiserade EF-set per nät är konsistent med detta.
- **Substance over form.** 14064-1 Annex A:s konsolideringsfilosofi - att rapportering ska följa ekonomisk substans snarare än juridisk form - delar anda med MASSIV+:s nivå-agnostiska nodval.
- **Verifieringsväg.** 14064-3 + 14065 + 14066 är den naturliga verifieringsstacken för en MASSIV+-nod som tar rollen som rapporteringsentitet under 14064-1.

**Strängare val inom 14064-1:s tillåtna utrymme.** 14064-1 låter organisationen välja kvantifieringsmodell, EF-källor och signifikanströsklar (clauses 5.2.3, 6.2). MASSIV+ snävar tre av dessa val på standardnivå:

- **EF-källor:** gemensamt set obligatoriskt för alla noder. Val: jämförbarhet mellan noder.
- **Signifikanströskel:** ingen tröskel - massbalansen täcker allt, det som saknas markeras som U. Val: heltäckning utan exklusion.
- **Datakvalitetsmetadata:** A och U hålls strukturellt åtskilda på värdenivå snarare än hanteras som metadata. Val: spårbarhet och progressiv förbättring.

Inget av detta bryter mot 14064-1. MASSIV+ utnyttjar standardens "the organization shall select"-utrymme genom att göra valet på standardnivå istället för rapportörsnivå.

**Additivt lager där 14064-1 inte tar ställning.** Tre saker MASSIV+ tillför som ligger utanför 14064-1:s scope, inte i konflikt med det:

- **Inter-enhets-flöden med Share-koefficienter.** 14064-1 har ingen formell modell för utsläppsflöden mellan organisationer utöver Cat 4/Cat 5-kategorisering hos respektive part. MASSIV+ tillför propageringsmodellen.
- **Massbalans som nätinvariant.** 14064-1 erkänner massbalans per källa; MASSIV+ gör den till ett konserveringsvillkor för hela nätet.
- **Operativ kontinuerlig uppdatering.** 14064-1 är rapportcentrerat (typiskt årligt); MASSIV+ är operativt och uppdateras löpande.

**Mappningen i båda riktningar.** En nods rapporterade kategori 1 + kategori 2 enligt 14064-1, eventuellt verifierad enligt 14064-3, är direkt användbar som A-data i en MASSIV+-nod - Coverage blir nära 1 i den utsträckning rapporteringen är komplett. Omvänt hamnar en MASSIV+-allokerad emissionssiffra från en leverantörsnod specifikt i mottagarens **kategori 4** (purchased goods), som ett bättre alternativ till sekundärdatabaser.

**Vad som genuint kräver kompletterande arbete för 14064-1-konformitet.** En nod som vill rapportera enligt 14064-1 utöver MASSIV+:s standardomfång behöver komplettera med kategori 5 (användning av sålda produkter) och kategori 6 (övriga indirekta), samt göra signifikansbedömning enligt clause 5.2.3. Cat 2 enligt 14064-1 är dessutom smalare än GHG Protocols Scope 2 - bränsle-uppströms-EF och T&D-förluster ligger i Cat 3 respektive Cat 4 - vilket kräver explicit mappning av MASSIV+:s S1+S2-värde.

### Nodbegreppet och 14064-1:s organisations- och anläggningsnivåer

ISO 14064-1 har tre nivåbegrepp: **organization** (3.4.2), **organizational boundary** (3.4.7) och **facility** (3.4.1). Båda definitionerna av relevans är medvetet breda. Organization är *"person or group of people that has its own functions with responsibilities, authorities and relationships to achieve its objectives"* med Note 1: *"includes... or part or combination thereof, whether incorporated or not, public or private."* Facility är *"single installation, set of installations or production processes... defined within a single geographical boundary, organizational unit or production process."*

Båda standarder är alltså nivå-agnostiska på sin egen sida: 14064-1:s organization kan vara hela koncernen eller en del därav, och MASSIV+:s nod kan vara hela bolaget eller en granulär enhet. Den korrekta beskrivningen är inte att nod = facility och rapporteringsentitet = organization. Den korrekta beskrivningen är symmetrisk:

> En MASSIV+-nod kan vara en 14064-1-organization om och endast om rapporteringsentiteten *är* den noden - dvs. heltäckningskravet tillämpas på just den noden, och den uppfyller substans-, konsoliderings- och fullspektrumkraven i 14064-1.

Det öppnar för en användning: i ett större bolag kan flera noder *var för sig* vara 14064-1-organizations med egen verifiering, samtidigt som de är noder i ett MASSIV+-nätverk som propagerar flöden mellan dem. 14064-1 modellerar inte denna syster-organization-relation, men hindrar den inte heller.

Fyra strukturkrav avgör om en given nod kan ta 14064-1-organization-rollen: (a) substanskravet i 3.4.2 - egen funktion, ansvar, befogenhet, relationer, mål, (b) deklarerad konsolideringsmetod (control eller equity share) per clause 5.1, (c) fullspektrumrapportering över alla sex kategorier per clauses 5.2.4 och 9.3, och (d) konsekvent gränsdragning över tid per clause 8.1.2. När någon av dessa inte är uppfylld - typexempel: nod = produktionslinje utan självständig ledning - är noden en 14064-1-facility inom en större organization, inte en organization i sig.

| Dimension            | ISO 14064-1                                                           | MASSIV+                                                                                            |
| -------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Frågan som besvaras  | "Vad är denna organisations totala fotavtryck?"                       | "Vad är detta flödes utsläpp genom värdekedjan?"                                                   |
| Rapporteringsentitet | Organization (3.4.2), konsolidering: control eller equity share (5.1) | Rapporteringsentitet (deklareras; konsolideringsmetod ärvs implicit från finansiell konsolidering) |
| Granulär enhet       | Facility (3.4.1)                                                      | Nod - även grafnod med flöden till andra noder                                                     |
| Kategoristruktur     | Sex kategorier (kat 1-6)                                              | S1, S2, A, U per nod; flöden mellan noder                                                          |
| Indirekta utsläpp    | Signifikanströskel definieras av organisationen                       | Massbalans, all data redovisas (A) eller markeras (U)                                              |
| Primärdata           | Definition 3.2.2                                                      | A-komponent, samma operativa definition                                                            |
| Kvantifieringsmodell | Org väljer (mätning, modell, massbalans, EF·aktivitetsdata)           | Massbalans + standardiserat EF-set                                                                 |
| El, default          | Location-based (Annex E, normativ)                                    | Standardiserat EF-set, location-based                                                              |
| EF-val Scope 1+2     | Organisationen väljer                                                 | Standardiserat gemensamt set                                                                       |
| Verifiering          | 14064-3 + 14065 + 14066 (frivillig stack)                             | Förlitar sig på 14064-3-stacken                                                                    |
