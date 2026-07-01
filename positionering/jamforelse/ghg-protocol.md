---
layout: default
title: "GHG Protocol"
nav_order: 4
---

# MASSIV+ vs. GHG Protocol

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. GHG Protocol och [ISO 14064-1](iso-14064-1.md) verkar på samma nivå som MASSIV+ - organisationen snarare än produkten. Ny här? Läs [introduktionen](../../introduktion.md) först.

GHG Protocol och MASSIV+ svarar på olika frågor. GHG Protocol är världens dominerande ramverk för företags klimatredovisning - Corporate Standard (Scope 1-2) och Scope 3 Standard (värdekedjeutsläpp) - och svarar på frågan *"vad är bolaget X:s totala fotavtryck?"*. Det enskilda bolaget är central enhet: varje företag mäter sina egna Scope 1-2 och skattar Scope 3 uppdelat i 15 kategorier, ofta med EEIO-schabloner (EEIO = miljöutvidgad input-output-analys - branschgenomsnitt från ekonomisk statistik) eller spenddatabaser (utsläpp skattade från inköpsbelopp) som grund. Uppskattningar blandas in i det totala Scope 3-värdet utan att andelen osäker data alltid är transparent nedströms.

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
