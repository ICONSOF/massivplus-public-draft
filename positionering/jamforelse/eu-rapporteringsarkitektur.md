---
layout: default
title: "EU:s rapporteringsarkitektur"
nav_order: 8
---

# MASSIV+ och EU:s rapporteringsarkitektur (CSRD/ESRS, Voluntary Standard)

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

CSRD/ESRS, Voluntary Standard ("VSME") och CSDDD är rapporterings- och tillsynsregimer som vilar på beräkningsstandarderna i de övriga jämförelserna - inte beräkningsstandarder i sig. Omnibus I-paketet våren 2026 reviderar denna arkitektur väsentligt och berör MASSIV+ på två sätt: dels genom att skapa en explicit *legal* roll för en frivillig värdekedjekonvention, dels genom att lämna ett operativt utrymme öppet som MASSIV+ är konstruerat att fylla.

## Tre lager, tre olika roller

- **Voluntary Standard, Basic Module (B3)** är dataminimum för bolag <1000 anställda. B3 kräver "estimated absolute gross GHG emissions" - Scope 1 + location-based Scope 2 - utan föreskriven EF-källa, utan datakvalitetsdeklaration och utan kundallokering. Det är ett *datafloor*, inte ett fullt operativt rapportsystem.
- **MASSIV+** ligger som operativt skikt ovanpå B3: samma underliggande Scope 1+2-data, gjord användbar genom (a) ett gemensamt EF-set som gör data jämförbara mellan noder, (b) kundallokering som propageringssteg och (c) A/U-separation med Coverage som datakvalitetsmått. MASSIV+ uppfinner inte rapporteringsplikt - det specificerar hur B3:s datafloor blir användbart i en värdekedja.
- **ESRS E1** är ramverket för det rapporterande bolaget (det stora bolaget i CSRD-scope). ESRS hänvisar till GHG Protocol Corporate Standard som metodbas, tillåter både primärdata från motparter och estimat/proxies för värdekedjedata (§65), men prioriterar verksamhetsspecifik, tidsaktuell och verifierad data (AR 24). MASSIV+-data flödar in som högkvalitativ primärinput i det rapporterande bolagets significant Scope 3 categories.

## Value chain cap - vad MASSIV+ ligger inom och utom

Reviderade ESRS inför en *value chain cap*: stora CSRD-bolag får inte begära mer värdekedjedata av leverantörer <1000 anställda än vad Voluntary Standard kräver, *när syftet är CSRD-rapportering*. Capens omfattning är entity-level Scope 1 + location-based Scope 2 - alltså B3.

Det här bromsar den direkta regulatoriska efterfrågan på detaljerad värdekedjedata, men MASSIV+ ligger utanför capen i fyra led:

- **Frivilligt sektorgemensamt protokoll.** Recital 12 i Omnibus I-direktivet undantar uttryckligen "information som vanligen delas mellan aktörer i en sektor" och "tillämpning av hållbarhetskriterier i upphandling". En sektorsadoption av MASSIV+ faller per definition utanför capen.
- **GHG management snarare än rapportering.** Capen täcker rapporteringsfrågor; data som samlas in för operativ utsläppsminskning ligger utanför.
- **Parallella regimer.** CSDDD-impact assessments har egna proportionalitetskrav (informationsförfrågningar mot partners <5000 anställda får endast göras när information inte rimligen kan inhämtas på annat sätt) men ingen value chain cap som motsvarar CSRD:s. Frivillig riskhantering är formellt separat med egen logik.
- **Banker och försäkringsbolag.** CRD VI / CRR III / EBA/GL/2024/01 ger finansinstitut en *standalone* skyldighet att samla in klimatdata från låntagare för prudential risk - helt fri från CSRD-capen. Det är samma kanal som PCAF, och MASSIV+:s primärdata är direkt användbar där (se [jämförelsen med PCAF](pcaf.md)).

Konsekvensen är att MASSIV+ inte ska positioneras som något stora CSRD-bolag *kräver* av sina leverantörer - det skulle bryta mot capen - utan som en frivillig, sektorgemensam konvention för datadelning som löser det operativa hål ESRS och Voluntary Standard medvetet lämnar öppet.

| Dimension | Voluntary Standard B3 | MASSIV+ | ESRS E1 |
|---|---|---|---|
| Roll | Datafloor för SME i CSRD-värdekedja | Operativt skikt ovanpå B3 | Rapporteringsram för CSRD-bolag |
| Scope 1+2 | "Estimated", location-based S2 | Standardiserade EFs, fördelade per kund | GHG Protocol-baserad, location + market-based S2 |
| Scope 3 | Ej i Basic | Byggs nedifrån via propagering | Per significant category; primärdata prioriteras, estimat tillåtna |
| Datakvalitet | Ingen formell deklaration | Coverage = A / (A+U) per nod | "Significant uncertainties" ska redovisas |
| Allokering till kunder | Saknas | Standardiserad propageringsregel | Endast på mottagarsidan; avsändarens fördelning är inte standardiserad |
| Legalt utrymme | Frivilligt komplement, gränsat av cap | Frivilligt sektorgemensamt protokoll (Recital 12) | Obligatoriskt från FY2027 |

**Ett modernt prejudikat: momsen.** Den bilaterala konsistenslogiken i MASSIV+ - säljarens utgående post är köparens ingående, kedjan terminerar hos slutkonsumenten - är samma som mervärdesskattens. Momsen är värd att hålla framme för en specifik egenskap: den togs från idé till global standard på ett par decennier (Sverige införde moms 1969) och är idag fundamentet för statsfinanser i över 170 länder. En bilateral redovisningsstandard kan alltså etableras på decennier snarare än sekel, när problemet är skarpt nog och principen fast nog.
