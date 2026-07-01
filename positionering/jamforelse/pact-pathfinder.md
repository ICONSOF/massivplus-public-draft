---
layout: default_banner
title: "PACT / Pathfinder"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 10
---

# MASSIV+ och PACT / Pathfinder Framework

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Den gemensamma ingången för produktstandarderna finns i [den generella relationen](produktstandarder.md#den-generella-relationen). Ny här? Läs [introduktionen](../../introduktion.md) först.

PACT (WBCSD) är ett tvärsindustriellt initiativ vars kärna är Pathfinder Framework - metodologisk vägledning för att beräkna och utbyta produktkoldioxidavtryck (PCF) längs värdekedjan, byggd på GHG Protocol och ISO 14067. Varje aktör beräknar sitt cradle-to-gate-PCF per deklarerad enhet och skickar det vidare; konsistens uppnås via gemensamma beräkningsregler, inte via matematisk konservering. Fel propageras nedströms utan systemvarning. Teknologilagret Pathfinder Network möjliggör interoperabelt datautbyte via API:er.

En tydlig parallell: PACT:s *Primary Data Share* (PDS) - andelen PCF baserad på primärdata - är konceptuellt identisk med MASSIV+:s Coverage-mått. Båda systemen delar designambitionen att göra datakvaliteten synlig och driva andelen faktisk data uppåt. Skillnaden är att PDS beräknas per produkt i LCA-kontext; Coverage per nod i ett propageringssystem. PACT kräver LCA-kompetens, intern produktspårbarhet och oberoende tredjepartsverifiering. MASSIV+ kräver Scope 1+2-rapportering per nod - utan LCA-krav eller produktspårning.

| Dimension | PACT / Pathfinder | MASSIV+ |
|---|---|---|
| Centralt objekt | Produkt (PCF, cradle-to-gate) | Nod |
| Konsistensgrund | Gemensam beräkningsmetodik | Massbalans och konserveringsregler |
| Datakvalitetsmått | Primary Data Share (PDS) | Coverage - konceptuellt identiskt |
| Massbevarande | Inte strukturellt garanterat | Inbyggt via massbalansen |
| Datakrav | LCA-metodik, produktspårbarhet | Scope 1+2 per nod |
| Emissionsfaktorer S1+S2 | Primärdata prioriteras, sekundärdatabaser som fallback | Standardiserat gemensamt set för alla noder |
| Verifiering | Kräver oberoende tredjepartsgranskning | Ej specificerat |
