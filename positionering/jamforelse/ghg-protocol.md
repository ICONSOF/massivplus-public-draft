---
layout: default_banner
title: "GHG Protocol"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 4
---

# MASSIV+ vs. GHG Protocol

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. GHG Protocol och [ISO 14064-1](iso-14064-1.md) verkar på organisationsnivå, samma nivå som MASSIV+. Ny här? Läs [introduktionen](../../introduktion.md) först.

GHG Protocol och MASSIV+ svarar på olika frågor. GHG Protocol är världens dominerande ramverk för företags klimatredovisning - Corporate Standard (Scope 1-2) och Scope 3 Standard (värdekedjeutsläpp) - och svarar på frågan *"vad är bolaget X:s totala fotavtryck?"*. Det enskilda bolaget är central enhet: varje företag mäter sina egna Scope 1-2 och skattar Scope 3 uppdelat i 15 kategorier, ofta med EEIO-schabloner (EEIO = miljöutvidgad input-output-analys - branschgenomsnitt från ekonomisk statistik) eller spenddatabaser (utsläpp skattade från inköpsbelopp) som grund. Uppskattningar blandas in i det totala Scope 3-värdet utan att andelen osäker data alltid är transparent nedströms.

MASSIV+ svarar på en annan fråga: *"vad är detta flödes utsläpp genom värdekedjan?"*. Standarden utgår från ett nätverk av noder snarare än ett enskilt bolag. Utsläpp propageras matematiskt längs faktiska leverantörsrelationer istället för att skattas kategorivis per bolag. Faktisk data (A) och okänt (U) hålls strikt åtskilda och kvantifieras via Coverage-måttet - U är ett täckningsunderlag som visar hur stor del av emissionsbilden som ännu saknar faktisk grund. För Scope 1 och 2 använder alla noder ett gemensamt, fastställt set av emissionsfaktorer per bränsle och energibärare - vilket eliminerar den godtycklighet i emissionsfaktorval som är ett känt problem i GHG Protocol-rapportering. Scope 1- och Scope 2-data enligt GHG Protocol är direkt användbar som ingångsvärde i MASSIV+-noder - systemen är komplementära och förstärker varandra.

GHG Protocols nivåer rangordnar hur specifik beräkningen är för leverantören och produkten. MASSIV+ skiljer det som en namngiven leverantör faktiskt har mätt och deklarerat från det som fortfarande är okänt, och redovisar hur stor andel som är faktisk.

Scope 3-vägledningen har fyra metoder för inköpta varor och tjänster, ordnade efter hur specifik datan är: leverantörsspecifik, där leverantören lämnar ett vagga-till-grind-avtryck för produkten, till exempel en EPD eller PCF; hybrid; genomsnittsdata per fysisk enhet; och spendbaserad med EEIO-faktorer. Vägledningen skiljer själv på specificitet och exakthet: data från en leverantör är inte automatiskt mer exakt än ett branschsnitt, bland annat eftersom leverantörens utsläpp måste fördelas på de produkter den säljer.¹

MASSIV+ utgår från hybridmetoden. Dess första steg är "collecting allocated scope 1 and scope 2 emission data directly from suppliers", och det är vad faktisk data (A) är. Skillnaden är att MASSIV+ gör samma sak i varje led, så att också resten av uppströmsledet består av leverantörernas egna allokerade tal i stället för uppskattningar. När varje led är en nod, energileverantörerna inräknade, är allt leverantörsspecifikt och vilar på mätningar hos namngivna aktörer. Med GHG Protocols definition av primärdata, som omfattar utsläppsdata som leverantören räknat fram för sin egen verksamhet, är A primärdata.²

Vägen dit går genom organisationer som fördelar sina utsläpp på kunderna, inte genom en produktmodell. MASSIV+ blir därför en egen kategori vid sidan om den leverantörsspecifika metoden snarare än ett steg i samma trappa. Mot en EPD eller PCF är varje led deklarerat av en namngiven aktör, med gemensamma faktorer och massbalans, och talen uppdateras varje period. Produkten har däremot ett eget tal i en EPD, medan MASSIV+ fördelar nodens hela börda med en nyckel. Det som ännu inte är deklarerat kvantifieras som okänt (U) med bästa tillgängliga metod, och där kan GHG Protocols övriga metoder användas (se [specifikationen §2](../../standard/specifikation.md#2-utsläppskomponenter-per-nod)).

Eftersom mottagarens Scope 3 är leverantörens faktiska Scope 1+2, allokerad längs den faktiska affärsrelationen, bär underlaget per konstruktion den specifika motpartens data. Relevansen kommer alltså av vidareledningen längs relationen, inte enbart av att datan är faktisk. Det skiljer ut två kvalitetsaxlar som annars buntas i ett samlat datakvalitetsbetyg: Coverage mäter andelen faktisk data, medan relevansen styrs av nodgranulariteten - hur nära det faktiska A-värdet ligger just den leverans mottagaren tar emot.

| Dimension | GHG Protocol | MASSIV+ |
|---|---|---|
| Frågan som besvaras | "Vad är bolaget X:s totala fotavtryck?" | "Vad är detta flödes utsläpp genom värdekedjan?" |
| Output | Bolagsinventering, redovisning | Operativ flödesdata |
| Central enhet | Enskilt bolag | Nod i ett nätverk |
| Scope 3-hantering | 15 kategorier, skattas per bolag | Flödespropagering längs leverantörsrelationer |
| Okänd datas roll | Blandas in i Scope 3-värdet som uppskattning | Strukturellt åtskild från faktisk data (U mot A); U kvantifieras som täckningsunderlag, inte utsläppsanspråk |
| Emissionsfaktorer S1+S2 | Aktören väljer själv | Standardiserat gemensamt set för alla noder |
| Datakvalitetstransparens | Data quality indicators per kategori | Coverage-mått per nod |
| Krav för att starta | Fullständig kategoribedömning förväntas | Kan starta med partiell täckning |
| Datarelevans | Metoder ordnade efter specificitet, med leverantörens produktavtryck överst, i praktiken sällan nått | Hybridmetoden i varje led: faktisk data deklarerad av varje leverantör; relevans styrs av nodgranularitet |

¹ GHG Protocol, Technical Guidance for Calculating Scope 3 Emissions (2013), kapitel 1, inklusive Box 1.1 "The difference between data specificity and data accuracy".
² GHG Protocol, Corporate Value Chain (Scope 3) Accounting and Reporting Standard (2011), kapitel 7, i anslutning till tabell 7.3: "Primary data includes data provided by suppliers or other value chain partners related to specific activities in the reporting company's value chain. Such data may take the form of primary activity data, or emissions data calculated by suppliers that are specific to suppliers' activities."
