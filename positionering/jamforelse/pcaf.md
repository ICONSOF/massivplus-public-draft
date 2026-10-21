---
layout: default_banner
title: "PCAF"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 14
---

# MASSIV+ och PCAF

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

PCAF är finanssektorns standard för finansierade utsläpp, alltså de utsläpp en bank eller investerare bär via sin utlåning och sina innehav. Den är en egen kategori: en portföljallokeringsmetod som behöver kunddata MASSIV+ kan leverera.

---

## MASSIV+ vs. PCAF

PCAF (Partnership for Carbon Accounting Financials) tar fram finanssektorns standarder för utsläpp kopplade till lån och investeringar (del A), kapitalmarknadstjänster (del B) och försäkringar (del C). Tredje utgåvan av del A (december 2025) täcker tio tillgångsklasser: noterade aktier och företagsobligationer, företagslån och onoterade aktier, projektfinansiering, kommersiella fastigheter, bolån, fordonslån, strukturer med öronmärkt låneändamål, värdepapperiseringar och strukturerade produkter, statsskuld samt skuld hos offentliga organ under nationell nivå (PCAF 2025, tabell 5-1, s. 37-38). Standarden fördelar låntagarens eller investeringsobjektets utsläpp till finansiella aktörer proportionellt mot deras finansieringsandel via en *attribution factor*. För aktier, obligationer och företagslån är den utestående belopp dividerat med EVIC (Enterprise Value Including Cash, bolagsvärde inklusive kassa) för noterade bolag, eller med summan av eget kapital och skulder för onoterade (avsnitt 5.1 och 5.2, s. 41-44 och 56-57). Övriga tillgångsklasser har egna nämnare, till exempel fastighetens värde vid lånetillfället. De finansierade utsläppen är vad finansiella aktörer rapporterar som sin Scope 3 kategori 15.

Sedan rapporter publicerade 2025 ska finansiella aktörer redovisa låntagarens och investeringsobjektets Scope 1, Scope 2 *och* Scope 3 för alla sektorer, med Scope 3 redovisat separat (avsnitt 5.1, ruta 5.1-1, s. 40). PCAF har ett eget data quality score från 1 till 5 (tabell 5.1-2, s. 46): score 1 är rapporterade utsläpp som beräknats enligt GHG Protocol och verifierats av tredje part, score 2 är overifierade rapporterade utsläpp eller utsläpp som banken beräknar från bolagets uppmätta energianvändning (det senare bara för Scope 1 och 2), score 3 är utsläpp beräknade från bolagets produktionsdata, och score 4-5 är skattningar från ekonomisk aktivitet, alltså branschgenomsnittliga emissionsfaktorer per intäkts- eller tillgångskrona, ofta hämtade ur EEIO-tabeller (EEIO = miljöutvidgad input-output-analys - branschgenomsnitt från ekonomisk statistik). PCAF konstaterar att jämförbarheten, täckningen, transparensen och tillförlitligheten i Scope 3-data fortfarande varierar kraftigt mellan sektorer och datakällor (s. 41). I praktiken landar de flesta bank-PCAF-värden idag på score 4-5.

MASSIV+ adresserar det datagap PCAF har på scope 3-sidan. Standarden producerar verifierbar primärdata med Coverage-mått hos låntagaren eller investeringsobjektet, vilket banken kan använda direkt som indata till sin PCAF-beräkning. Var en MASSIV+-deklaration hamnar i PCAF:s skala beror på om den uppfyller PCAF:s villkor. Rapporterade utsläpp ger score 1 eller 2 bara om de är beräknade enligt GHG Protocol, och score 1 kräver dessutom verifiering av tredje part (s. 44, fotnot 49-50). Nodens Scope 1+2-aktivitetsdata med gemensamma emissionsfaktorer motsvarar annars PCAF:s alternativ 2a, score 2, som bara gäller Scope 1 och 2 (s. 46, fotnot 53). PCAF tillhandahåller *attribution-metoden* (hur banken fördelar kundens utsläpp till sin portfölj); MASSIV+ tillhandahåller *kunddatan* (vad kundens utsläpp är, med transparent datakvalitet). De är komplementära - PCAF förblir bankens standard för portföljallokering, medan MASSIV+ kan höja datakvaliteten på de underliggande emissionsvärdena från EEIO-schabloner (PCAF score 4-5) till företagsspecifika underlag (score 1-2 under PCAF:s villkor).

| Dimension | PCAF | MASSIV+ |
|---|---|---|
| Centralt objekt | Finansiell portfölj | Värdekedjenod |
| Räckvidd | 10 tillgångsklasser för lån och investeringar (försäkringar i del C) | Värdekedjenoder (alla branscher och organisationsstorlekar) |
| Allokeringsmetod | Attribution factor (finansieringsandel) | Massbalans + allokeringsregel per nod |
| Datakällor | Kundens egna data, fallback till EEIO-baserade schabloner per intäkt eller tillgång | Standardiserad Scope 1+2 + propagering nedifrån |
| Datakvalitetsmått | PCAF data quality score (1-5) | Coverage = (S1+S2+A)/T |
| Relation | PCAF är bankens portföljmetod | MASSIV+-data kan vara primärinput till PCAF (kan ersätta schabloner, score 4-5, med företagsspecifika data, score 1-2 under PCAF:s villkor) |

---

## Källor

- PCAF (2025), *The Global GHG Accounting and Reporting Standard Part A: Financed Emissions*, Third Edition, december 2025. [PCAF](https://carbonaccountingfinancials.com/en/standard)
