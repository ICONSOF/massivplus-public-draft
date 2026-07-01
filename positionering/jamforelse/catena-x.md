---
layout: default_banner
title: "Catena-X"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 11
---

# MASSIV+ och Catena-X

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Den gemensamma ingången för produktstandarderna finns i [den generella relationen](produktstandarder.md#den-generella-relationen). Ny här? Läs [introduktionen](../../introduktion.md) först.

CX-PCF Rulebook bygger primärt på **ISO 14067** och **ISO 14040/14044**, med nära anpassning till Pathfinder Framework. Sektoriella riktlinjer (TFS, worldsteel, International Aluminium) kan användas som drop-in standards med specificerade tilläggskrav. Varje aktör beräknar sitt cradle-to-gate PCF per deklarerad enhet och utbyter det till nästa led - konsistens via regelbok, inte via matematisk konservering.

Det centrala datakravet skiljer dem åt: Catena-X kräver intern produktspårbarhet och LCA-kompetens som de flesta aktörer utanför de största koncernerna saknar. En Catena-X-aktör med verifierad PCF och hög PDS kan bidra med data som ger Coverage nära 1 i en MASSIV+-nod - den mest mogna änden av datamognadskurvan. En aktör med lägre PDS ger proportionellt lägre Coverage och är inte per definition fullständig primärdata i MASSIV+-termer.

Konceptuellt är PDS och Coverage parallella mått: båda anger andelen primärdata i det rapporterade värdet och båda propagerar genom kedjan. Skillnaden ligger i hanteringen av icke-primär data - Catena-X tillåter sekundärdatabaser med representativitetskriterier medan MASSIV+ markerar saknad data som U (okänt) utan att fylla luckan med databasvärden. Det är en strukturellt skarpare position som syftar till att hålla osäkerhet synlig snarare än bortskattad.

Catena-X har därutöver ett Data Quality Rating (DQR) med tre representativitetsindikatorer (teknisk, temporal, geografisk) på 1-5-skala. MASSIV+ har inget motsvarande extra lager, vilket är en avsiktlig förenkling: när alla noder använder ett gemensamt standardiserat emissionsfaktorset på organisationsnivå adresserar standardisering det som DQR:s representativitetspoäng vill kvantifiera, vilket gör det extra lagret onödigt för MASSIV+:s syfte.

| Dimension | Catena-X | MASSIV+ |
|---|---|---|
| Metodologisk bas | ISO 14067 + 14040/14044, anpassad till Pathfinder | Eget nodbaserat flödessystem |
| Centralt objekt | Produkt (PCF, cradle-to-gate) | Nod |
| Konsistensgrund | Regelbok (ISO 14067 + Catena-X-krav) | Massbalans |
| Datakvalitet-mått | DQR (TeR/TiR/GeR - teknisk/temporal/geografisk representativitet, 1-5) + PDS | Coverage = A/(A+U) |
| Hantering av icke-primär data | Sekundärdatabaser med hierarki + representativitetskriterier | U-markör (okänt) - ingen fallback till databaser |
| Datakrav | LCA-metodik, intern produktspårbarhet | Scope 1+2 per nod |
| Industritäckning | Fordonsindustri | Industri- och storleksagnostiskt |
