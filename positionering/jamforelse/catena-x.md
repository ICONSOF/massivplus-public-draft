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

Reglerna för hur detta ska gå till finns i **CX-PCF Rulebook** - en gemensam regelbok som säkerställer att alla aktörer beräknar på samma sätt. Regelboken bygger primärt på **ISO 14067** och **ISO 14040/14044**, med nära anpassning till Pathfinder Framework. Sektoriella riktlinjer (TFS, worldsteel, International Aluminium) kan användas som drop-in standards med specificerade tilläggskrav. Varje aktör beräknar sitt cradle-to-gate-PCF per deklarerad enhet och utbyter det till nästa led - konsistens uppnås via regelboken, inte via matematisk konservering.

## Samma grundidé, olika räkneobjekt

Grundidén är densamma som i MASSIV+: verklig utsläppsdata ska flöda genom värdekedjan, från leverantör till kund, i stället för att varje företag skattar sina uppströmsutsläpp med schabloner. Skillnaden ligger i vad man räknar på. Catena-X räknar per **produkt** - varje artikel får ett eget PCF, vilket kräver att företaget kan spåra material och energi ned på produktnivå och behärskar LCA-metodik. MASSIV+ räknar per **nod** - företaget rapporterar sina samlade Scope 1+2-utsläpp och fördelar dem proportionellt på sina kunder, utan LCA-krav och utan produktspårning.

Det gör att trösklarna skiljer sig markant: Catena-X kräver intern produktspårbarhet och LCA-kompetens som de flesta aktörer utanför de största koncernerna saknar, medan MASSIV+ kräver Scope 1+2 per nod. De två kan samtidigt samverka. En Catena-X-aktör med verifierad PCF och hög PDS har allt som krävs för att också utfärda en MASSIV+-deklaration och därmed bidra med data som ger Coverage nära 1 i en MASSIV+-nod - den mest mogna änden av datamognadskurvan. En aktör med lägre PDS ger proportionellt lägre Coverage och är inte per definition fullständig primärdata i MASSIV+-termer.

## Datakvalitet: PDS och Coverage

Båda systemen mäter hur stor del av ett rapporterat värde som vilar på verklig data. I Catena-X heter måttet *Primary Data Share* (PDS) - andelen av PCF-värdet som bygger på primärdata. I MASSIV+ heter motsvarigheten Coverage. Konceptuellt är de parallella mått: båda anger andelen primärdata i det rapporterade värdet och båda propagerar genom kedjan.

Skillnaden ligger i vilken status icke-primär data får. Catena-X tillåter sekundärdatabaser med representativitetskriterier som del av själva PCF-värdet. MASSIV+ använder också sekundärdata - spend, fysisk volym, sektordata, databasvärden eller annan rimlig proxy - men enbart för att kvantifiera U-underlaget, dvs. den del av emissionsbilden som ännu saknar faktisk datagrund. Underlaget behövs för att beräkna Coverage och möjliggöra allokering, men räknas aldrig som faktisk data (A) och ersätts när faktisk data tillkommer. Ett verifierat Catena-X-PCF kan på samma sätt användas som grund för ett välunderbyggt U-underlag hos en MASSIV+-mottagare, men räknas som A först när leverantören själv utfärdar en MASSIV+-deklaration - distinktionen handlar om ansvarig avsändare, inte om numerisk kvalitet. Det är fortfarande en strukturellt skarpare position, men skärpan ligger i statusseparationen: osäkerheten hålls synlig på värdenivå i stället för att bäddas in i det rapporterade talet.

Catena-X har därutöver ett Data Quality Rating (DQR) med tre representativitetsindikatorer (teknisk, temporal, geografisk) på 1-5-skala. MASSIV+ har inget motsvarande extra lager, vilket är en avsiktlig förenkling: när alla noder använder ett gemensamt standardiserat emissionsfaktorset på organisationsnivå adresserar standardisering det som DQR:s representativitetspoäng vill kvantifiera, vilket gör det extra lagret onödigt för MASSIV+:s syfte.

## Jämförelse i sammandrag

| Dimension | Catena-X | MASSIV+ |
|---|---|---|
| Metodologisk bas | ISO 14067 + 14040/14044, anpassad till Pathfinder | Eget nodbaserat flödessystem |
| Centralt objekt | Produkt (PCF, cradle-to-gate) | Nod |
| Konsistensgrund | Regelbok (ISO 14067 + Catena-X-krav) | Massbalans |
| Datakvalitet-mått | DQR (TeR/TiR/GeR - teknisk/temporal/geografisk representativitet, 1-5) + PDS | Coverage = A/(A+U) |
| Hantering av icke-primär data | Sekundärdatabaser med hierarki + representativitetskriterier, del av PCF-värdet | Kvantifierar U-underlaget (proxy/sekundärdata tillåten) - räknas aldrig som faktisk data (A) |
| Datakrav | LCA-metodik, intern produktspårbarhet | Scope 1+2 per nod |
| Industritäckning | Fordonsindustri | Industri- och storleksagnostiskt |
