---
layout: default_banner
title: "PACT"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 10
---

# MASSIV+ och PACT Methodology

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Den gemensamma ingången för produktstandarderna finns i [den generella relationen](produktstandarder.md#den-generella-relationen). Ny här? Läs [introduktionen](../../introduktion.md) först.

PACT (Partnership for Carbon Transparency) är ett tvärsindustriellt initiativ inom WBCSD. Dess metodstandard PACT Methodology anger hur produktkoldioxidavtryck (PCF) beräknas och utbyts längs värdekedjan och bygger på GHG Protocol, ISO-standarderna för livscykelanalys och klimatavtryck samt produkt- och sektorsspecifika regler (avsnitt 1.3 och 3.1). Gällande version är 3.0 från 2025, som ersätter version 2.0 från 2023 (då kallad Pathfinder Framework). Varje aktör beräknar sitt cradle-to-gate-PCF per deklarerad enhet och skickar det vidare; konsistens uppnås via gemensamma beräkningsregler, inte via matematisk konservering. Ett fel i en leverantörs PCF följer med in i kundens beräkning, och PACT hanterar det med datakvalitetsmått och verifiering snarare än med en balanskontroll. Utbytet sker via PACT Network, där PACT Technical Specifications anger datamodell och API (avsnitt 6.2).

En tydlig parallell: PACT:s *Primary Data Share* (PDS) - andelen PCF baserad på primärdata - är analog med MASSIV+:s Coverage-mått. Båda systemen delar designambitionen att göra datakvaliteten synlig och driva andelen faktisk data uppåt. Måtten räknar på olika grund: i PDS är en datapunkt primär när både aktivitetsdata och emissionsfaktor är primära, medan A i MASSIV+ är det som en ansvarig avsändare har deklarerat. El som räknats med en gemensam listfaktor är därför faktisk data i MASSIV+ men sekundärdata i PDS (avsnitt 4.2.2; tabell 6 och 9). Skillnaden är att PDS beräknas per produkt i LCA-kontext; Coverage per nod i ett propageringssystem. Från 2027 kompletteras PDS med ett andra mått, Data Quality Rating (DQR), som bedömer teknisk, geografisk och tidsmässig representativitet på en skala från 1 till 5 (avsnitt 4.2.1 och 4.2.3).

PACT förutsätter i praktiken LCA-metodik, eftersom metoden är en attributionell livscykelanalys (avsnitt 3.2.1), och att aktivitetsdata i första hand är företagsspecifika, även när emissionsfaktorerna hämtas ur databaser; proxydata och utgiftsbaserade data är en reserv (avsnitt 4.1.3.1). Verifiering ska göras av oberoende tredje part (tabell 3). Fram till 2030 granskas företagets beräkningsmodell med begränsad säkerhet, från 2030 certifieras hela PCF-programmet, och små och medelstora företag får två års längre tid (avsnitt 5.3-5.4). Ett PCF får utbytas innan verifieringen är klar (avsnitt 5.2.2, fotnot 76). MASSIV+ kräver Scope 1+2-rapportering per nod - utan LCA-krav eller produktspårning.

| Dimension | PACT | MASSIV+ |
|---|---|---|
| Centralt objekt | Produkt (PCF, cradle-to-gate) | Nod |
| Konsistensgrund | Gemensam beräkningsmetodik | Massbalans och konserveringsregler |
| Datakvalitetsmått | Primary Data Share (PDS), från 2027 även Data Quality Rating (DQR) | Coverage - analogt med PDS, räknat på annan grund |
| Massbevarande | Inte strukturellt garanterat | Inbyggt via massbalansen |
| Datakrav | LCA-metodik, produktspårbarhet | Scope 1+2 per nod |
| Emissionsfaktorer S1+S2 | Primärdata prioriteras, sekundärdatabaser som fallback | Standardiserat gemensamt set för alla noder |
| Verifiering | Oberoende tredje part: beräkningsmodellen 2025-2030, certifiering av PCF-programmet från 2030 | Ej specificerat |

## Källor

- WBCSD, *PACT Methodology: Methodology for Calculating and Exchanging Cradle-to-Gate Product Carbon Footprints*, version 3.0 (2025). Tabell 1 (s. 13-14) sammanfattar ändringarna mot version 2.0 (2023). [WBCSD](https://www.wbcsd.org/resources/pact-methodology-version-3/)
