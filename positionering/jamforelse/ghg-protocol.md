---
layout: default_banner
title: "GHG Protocol"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 4
---

# MASSIV+ vs. GHG Protocol

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. GHG Protocol och [ISO 14064-1](iso-14064-1.md) verkar på organisationsnivå, samma nivå som MASSIV+. Ny här? Läs [introduktionen](../../introduktion.md) först.

GHG Protocol och MASSIV+ svarar på olika frågor. GHG Protocol är världens dominerande ramverk för företags klimatredovisning - Corporate Standard (Scope 1-2) och Scope 3 Standard (värdekedjeutsläpp) - och svarar på frågan *"vad är bolaget X:s totala fotavtryck?"*. Det enskilda bolaget är central enhet: varje företag mäter sina egna Scope 1-2 och skattar Scope 3 uppdelat i 15 kategorier, ofta med EEIO-schabloner (EEIO = miljöutvidgad input-output-analys - branschgenomsnitt från ekonomisk statistik) eller spenddatabaser (utsläpp skattade från inköpsbelopp) som grund. Uppskattningar och leverantörsdata summeras till ett totalt Scope 3-värde. Standarden kräver att företaget för varje kategori redovisar hur stor andel av utsläppen som beräknats med data från leverantörer eller andra partner i värdekedjan, men andelen följer inte med talet när nästa led använder det.¹

MASSIV+ svarar på en annan fråga: *"vad är detta flödes utsläpp genom värdekedjan?"*. Standarden utgår från ett nätverk av noder snarare än ett enskilt bolag. Utsläpp propageras matematiskt längs faktiska leverantörsrelationer istället för att skattas kategorivis per bolag. Faktisk data (A) och okänt (U) hålls strikt åtskilda och kvantifieras via Coverage-måttet - U är ett täckningsunderlag som visar hur stor del av emissionsbilden som ännu saknar faktisk grund. För Scope 1 och 2 använder alla noder ett gemensamt, fastställt set av emissionsfaktorer per bränsle och energibärare - vilket eliminerar den godtycklighet i emissionsfaktorval som är ett känt problem i GHG Protocol-rapportering.² Scope 1- och Scope 2-data enligt GHG Protocol är direkt användbar som ingångsvärde i MASSIV+-noder - systemen är komplementära och förstärker varandra.

GHG Protocols nivåer rangordnar hur specifik beräkningen är för leverantören och produkten. MASSIV+ skiljer det som en namngiven leverantör faktiskt har mätt och deklarerat från det som fortfarande är okänt, och redovisar hur stor andel som är faktisk.

Scope 3-vägledningen har fyra metoder för inköpta varor och tjänster, ordnade efter hur specifik datan är: leverantörsspecifik, där leverantören lämnar ett vagga-till-grind-avtryck för produkten, till exempel en EPD eller PCF; hybrid; genomsnittsdata per fysisk enhet; och spendbaserad med EEIO-faktorer. Vägledningen skiljer själv på specificitet och exakthet: data från en leverantör är inte automatiskt mer exakt än ett branschsnitt, bland annat eftersom leverantörens utsläpp måste fördelas på de produkter den säljer.³

MASSIV+ utgår från hybridmetoden. Dess första del är "collecting allocated scope 1 and scope 2 emission data directly from suppliers",³ och det är vad faktisk data (A) är. Skillnaden är att MASSIV+ gör samma sak i varje led, så att också resten av uppströmsledet består av leverantörernas egna allokerade tal i stället för uppskattningar. När varje led är en nod, energileverantörerna inräknade, är allt leverantörsspecifikt och vilar på mätningar hos namngivna aktörer. Med GHG Protocols definition av primärdata, som omfattar utsläppsdata som leverantören räknat fram för sin egen verksamhet, är A primärdata.⁴

Vägen dit går genom organisationer som fördelar sina utsläpp på kunderna, inte genom en produktmodell. MASSIV+ blir därför en egen kategori vid sidan om den leverantörsspecifika metoden snarare än ett steg i samma trappa. Mot en EPD eller PCF är varje led deklarerat av en namngiven aktör, med gemensamma faktorer och massbalans, och talen uppdateras varje period. Produkten har däremot ett eget tal i en EPD, medan MASSIV+ fördelar nodens hela börda med en nyckel. Det som ännu inte är deklarerat kvantifieras som okänt (U) med bästa tillgängliga metod, och där kan GHG Protocols övriga metoder användas (se [specifikationen §2](../../standard/specifikation.md#2-utsläppskomponenter-per-nod)).

Eftersom mottagarens Scope 3 är leverantörens faktiska Scope 1+2, allokerad längs den faktiska affärsrelationen, bär underlaget per konstruktion den specifika motpartens data. Relevansen kommer alltså av vidareledningen längs relationen, inte enbart av att datan är faktisk. Det skiljer ut två kvalitetsaxlar: Coverage mäter andelen faktisk data, medan relevansen styrs av nodgranulariteten - hur nära det faktiska A-värdet ligger just den leverans mottagaren tar emot. GHG Protocol bedömer datakvalitet med fem separata indikatorer och rangordnar leverantörsdata efter nivå, från produkt via process, anläggning och affärsenhet till koncern. Nodgranulariteten motsvarar den rangordningen.⁵

| Dimension | GHG Protocol | MASSIV+ |
|---|---|---|
| Frågan som besvaras | "Vad är bolaget X:s totala fotavtryck?" | "Vad är detta flödes utsläpp genom värdekedjan?" |
| Output | Bolagsinventering, redovisning | Operativ flödesdata |
| Central enhet | Enskilt bolag | Nod i ett nätverk |
| Scope 3-hantering | 15 kategorier, skattas per bolag | Flödespropagering längs leverantörsrelationer |
| Okänd datas roll | Blandas in i Scope 3-värdet som uppskattning | Strukturellt åtskild från faktisk data (U mot A); U kvantifieras som täckningsunderlag, inte utsläppsanspråk |
| Emissionsfaktorer S1+S2 | Aktören väljer källa, för Scope 2 inom en rekommenderad hierarki (Scope 2 Guidance, tabell 6.2-6.3); ingen gemensam uppsättning | Standardiserat gemensamt set för alla noder |
| Datakvalitetstransparens | Fem datakvalitetsindikatorer och andel leverantörsdata per kategori | Coverage-mått per nod, propageras nedströms |
| Krav för att starta | Alla Scope 3-utsläpp ska redovisas, undantag ska motiveras (Scope 3 Standard, avsnitt 6.2) | Kan starta med partiell täckning |
| Datarelevans | Metoder ordnade efter specificitet, med leverantörens produktavtryck överst, i praktiken sällan nått | Hybridmetoden i varje led: faktisk data deklarerad av varje leverantör; relevans styrs av nodgranularitet |

¹ GHG Protocol, Corporate Value Chain (Scope 3) Accounting and Reporting Standard (2011), avsnitt 7.3, s. 75, och avsnitt 11.1, s. 119: "For each scope 3 category, the percentage of emissions calculated using data obtained from suppliers or other value chain partners." [PDF](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard_041613.pdf)
² Jämför GHG Protocol, Scope 2 Guidance (2015), avsnitt 1.3, s. 6, om leverantörsspecifika emissionsfaktorer: "Supplier disclosure requirements and calculation methodology differ, making it difficult for consumers to consistently use this type of information." Bristande jämförbarhet mellan Scope 3-inventeringar lyfts också av flera inlämnare i den pågående revisionen (GHG Protocol, Summary of Scope 3 Proposals, mars 2024, avsnitt 4, s. 19). [PDF](https://ghgprotocol.org/sites/default/files/2024-03/Scope-3-Proposals-Summary-Draft.pdf)
³ GHG Protocol, Technical Guidance for Calculating Scope 3 Emissions (2013), kategori 1 (Purchased Goods and Services): metoderna s. 20-21, hybridmetoden s. 21 och Box 1.1 "The difference between data specificity and data accuracy" s. 22. [PDF](https://ghgprotocol.org/sites/default/files/standards/Scope3_Calculation_Guidance_0.pdf)
⁴ GHG Protocol, Corporate Value Chain (Scope 3) Accounting and Reporting Standard (2011), avsnitt 7.2, tabell 7.3 och efterföljande text, s. 70-71: "Primary data includes data provided by suppliers or other value chain partners related to specific activities in the reporting company's value chain. Such data may take the form of primary activity data, or emissions data calculated by suppliers that are specific to suppliers' activities."
⁵ GHG Protocol, Corporate Value Chain (Scope 3) Accounting and Reporting Standard (2011), avsnitt 7.3, tabell 7.6 "Data quality indicators", s. 76, och avsnitt 7.4, tabell 7.7 "Levels of data (ranked in order of specificity)", s. 80.
