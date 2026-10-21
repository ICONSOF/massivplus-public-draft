---
layout: default_banner
title: "Catena-X"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 11
---

# MASSIV+ och Catena-X

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Den gemensamma ingången för produktstandarderna finns i [den generella relationen](produktstandarder.md#den-generella-relationen). Ny här? Läs [introduktionen](../../introduktion.md) först.

## Vad är Catena-X?

Catena-X är fordonsindustrins gemensamma datanätverk - ett europeiskt samarbete, initierat av tyska fordonstillverkare och deras leverantörer, för att utbyta data genom hela leverantörskedjan på ett standardiserat sätt. Ett av användningsområdena är klimatdata: varje leverantör beräknar sin produkts klimatavtryck - ett *Product Carbon Footprint* (PCF) - och skickar värdet vidare till sin kund, som räknar in det i sin egen beräkning. Så byggs ett fordons totala avtryck upp länk för länk av leverantörernas egna siffror, i stället för av branschgenomsnitt.

Reglerna för hur detta ska gå till finns i **CX-PCF Rulebook** - en gemensam regelbok som gör att alla aktörer beräknar på samma sätt. Regelboken (version 3, augusti 2024) bygger på ISO 14067 och ISO 14040/14044 och är nära anpassad till WBCSD:s Pathfinder Framework, som i dag heter PACT Methodology (avsnitt 3.1). Sektorsriktlinjer från worldsteel (LCI-metodiken, 2017), International Aluminium Institute (2021), European Aluminium (2023) och Together for Sustainability (TfS, 2022) är godkända i angivna versioner och kan användas direkt med regelbokens tilläggskrav (bilaga A2-A6). Varje aktör beräknar sitt cradle-to-gate-PCF - från vaggan till fabriksgrind, alltså utan användningsfas och slutligt omhändertagande men med avfallet från den egna produktionen (avsnitt 4.2) - per deklarerad enhet och utbyter det till nästa led - konsistensen vilar på regelboken.

## Samma grundidé, olika räkneobjekt

Grundidén är densamma som i MASSIV+: verklig utsläppsdata ska flöda genom värdekedjan, från leverantör till kund, i stället för att varje företag skattar sina uppströmsutsläpp med schabloner. Skillnaden ligger i vad man räknar på. Catena-X räknar per **produkt** - varje artikel får ett eget PCF enligt en attributionell LCA-ansats (avsnitt 4). Det förutsätter LCA-metodik och att material och energi kan knytas till produkten; saknas produktspecifika mätningar ska anläggnings- eller företagsspecifika data användas (avsnitt 6.1). MASSIV+ räknar per **nod** - företaget rapporterar sina samlade Scope 1+2-utsläpp och fördelar dem proportionellt på sina kunder, utan LCA-krav och utan produktspårning.

Det gör att trösklarna skiljer sig markant. Regelboken konstaterar själv att PCF-beräkning främst görs i stora företag och att mindre företag kan sakna resurser eller kunskap för den (avsnitt 1.3), medan MASSIV+ kräver Scope 1+2 per nod. De två kan samtidigt samverka. En Catena-X-aktör med verifierad PCF och hög PDS har allt som krävs för att också utfärda en MASSIV+-deklaration och därmed bidra med data som ger Coverage nära 1 i en MASSIV+-nod. En aktör med lägre PDS ger proportionellt lägre Coverage och är inte per definition fullständig primärdata i MASSIV+-termer.

## Datakvalitet: PDS och Coverage

Båda systemen mäter hur stor del av ett rapporterat värde som vilar på verklig data. I Catena-X heter måttet *Primary Data Share* (PDS) - andelen av PCF-värdet som bygger på primärdata. I MASSIV+ heter motsvarigheten Coverage. Konceptuellt är de parallella mått: båda anger hur stor andel av det rapporterade värdet som vilar på faktisk data, och båda propagerar genom kedjan. Måtten räknar på olika grund: i PDS är en datapunkt primär när både aktivitetsdata och emissionsfaktor är primära, medan A i MASSIV+ är det som en ansvarig avsändare har deklarerat. El som räknats med en gemensam listfaktor är därför faktisk data i MASSIV+ men sekundärdata i PDS; regelboken använder själv elfaktorn från en nationell utsläppsinventering som exempel på en sekundär emissionsfaktor (avsnitt 6.1 och 7.2.4).

Skillnaden ligger i vilken status icke-primär data får. Catena-X tillåter sekundärdatabaser med representativitetskriterier som del av själva PCF-värdet, och skattningen ska vara konservativ så att sekundärdata inte ger ett lägre PCF än primärdata skulle ha gett (avsnitt 6.2). MASSIV+ använder också sekundärdata - spend, fysisk volym, sektordata, databasvärden eller annan rimlig proxy - men enbart för att kvantifiera U-underlaget, dvs. den del av emissionsbilden som ännu saknar faktisk datagrund. Underlaget behövs för att beräkna Coverage och möjliggöra allokering, men räknas aldrig som faktisk data (A) och ersätts när faktisk data tillkommer. Ett verifierat Catena-X-PCF kan på samma sätt användas som grund för ett välunderbyggt U-underlag hos en MASSIV+-mottagare, men räknas som A först när leverantören själv utfärdar en MASSIV+-deklaration - distinktionen handlar om ansvarig avsändare, inte om numerisk kvalitet. Skillnaden ligger i statusseparationen: osäkerheten hålls synlig på värdenivå i stället för att bäddas in i det rapporterade talet.

Catena-X har därutöver ett Data Quality Rating (DQR) med tre representativitetsindikatorer (teknisk, temporal, geografisk) på 1-5-skala. Enligt regelboken ska DQR vara obligatoriskt efter övergångsperioden, som löpte till slutet av 2025 (avsnitt 2.4 och 7.2.5.1). MASSIV+ har inget motsvarande extra lager, vilket är en avsiktlig förenkling: när alla noder använder ett gemensamt standardiserat emissionsfaktorset på organisationsnivå täcker standardiseringen det som DQR:s representativitetspoäng vill kvantifiera.

## Jämförelse i sammandrag

| Dimension | Catena-X | MASSIV+ |
|---|---|---|
| Metodologisk bas | ISO 14067 + 14040/14044, anpassad till Pathfinder Framework (i dag PACT) | Eget nodbaserat flödessystem |
| Centralt objekt | Produkt (PCF, cradle-to-gate) | Nod |
| Konsistensgrund | Regelbok (ISO 14067 + Catena-X-krav) | Massbalans |
| Datakvalitet-mått | DQR (TeR/TiR/GeR - teknisk/temporal/geografisk representativitet, 1-5) + PDS | Coverage = (S1+S2+A)/T |
| Hantering av icke-primär data | Sekundärdatabaser med hierarki + representativitetskriterier, del av PCF-värdet | Kvantifierar U-underlaget (proxy/sekundärdata tillåten) - räknas aldrig som faktisk data (A) |
| Datakrav | LCA-metodik, produktspecifika data (anläggnings- eller företagsspecifika som reserv) | Scope 1+2 per nod |
| Industritäckning | Fordonsindustri | Industri- och storleksagnostiskt |

## Källor

- Catena-X, *Catena-X Product Carbon Footprint Rulebook (CX-PCF Rules)*, version 3 (augusti 2024). Avsnitt 3.1-3.2 (grund och hierarki), 4.2-4.3 (systemgräns och deklarerad enhet), 6.1-6.2 (primär- och sekundärdata), 7.2.4 (PDS), 7.2.5 (DQR) och bilaga A2 (godkända sektorsriktlinjer).
