---
layout: default
title: "Jämförelse med andra ramverk"
nav_order: 3
---

# Jämförelse med andra ramverk

> **Poäng:** Hur MASSIV+ förhåller sig till de etablerade ramverk som redan finns på fältet - GHG Protocol, ISO 14064-1, EPD, PACT, Catena-X, DPP, BEAst och PCAF. Den korta versionen: relationen är komplementär, inte konkurrerande.

Den här sidan ger den övergripande jämförelsetabellen och den sammanfattande positioneringen. De detaljerade jämförelserna ligger som egna texter per kategori, länkade i [listan nedan](#de-detaljerade-jämförelserna). Läs [introduktionen](../introduktion.md) först om du inte är bekant med MASSIV+.

---

## Översikt

Tabellen ställer samtliga ramverk bredvid varandra på de dimensioner som är mest informativa tvärs kategorierna. Den fördjupade jämförelsen per ramverk - med en egen tabell var - ligger i delfilerna nedan.

| Ramverk | Central enhet | Systemtyp | Datakvalitetsmått | Relation till MASSIV+ |
|---|---|---|---|---|
| GHG Protocol | Bolag | Redovisningsramverk | Data quality indicators | Grund för Scope 1+2; MASSIV+ adderar det operativa flödeslagret |
| ISO 14064-1 | Organisation (kat 1-6) | Redovisningsstandard + verifieringsstack | Primärdata vs sekundärdata | Samma nivå; en nod kan vara en 14064-1-organization |
| ISO 14040/14044 | Produkt | Metodstandard (LCA) | Datakvalitetskrav per fas | LCA i botten ger idealisk primärdata till noden |
| ISO 14067 | Produkt (PCF) | Metodstandard | Datakvalitetskrav | PCF som primärdata in; verkar på olika nivåer |
| EPD / ISO 14025 | Produkt | Deklarationsformat | Verifierad LCA (DQR) | Idealisk primärindata; MASSIV+ gör kvaliteten propagerbar |
| PACT / Pathfinder | Produkt (PCF) | Beräknings- och utbytesramverk | Primary Data Share (PDS) | PDS motsvarar Coverage; produktdata in i noden |
| Catena-X | Produkt (PCF) | Regelbok + dataplattform | DQR + PDS | Mogen primärdata in; MASSIV+ är sektoragnostiskt |
| DPP | Produkt | Decentraliserat dataobjekt (bärarstandard EN 1821x) | Koldioxidfältet: PEF / ISO 14067 (jämförbarhet ej garanterad) | Bärare; MASSIV+ matar uppströms primärdata till avtrycksberäkningen |
| BEAst | Affärstransaktion | Transaktions- och utbytesstandard | Saknas (köpare kan begära detalj) | Bär MASSIV+-flöden på den bilaterala transaktionen |
| PCAF | Finansiell portfölj | Portföljallokeringsmetod | PCAF score (1-5) | MASSIV+ är primärinput, höjer score 4-5 till 1-2 |
| CSRD/ESRS, VSME | Rapporteringsregim | Rapporterings- och tillsynsregim | "Significant uncertainties" redovisas | MASSIV+ operativt skikt; primärinput i Scope 3 |
| **MASSIV+** | **Nod (org.enhet)** | **Propageringssystem** | **Coverage = A/(A+U)** | **(referensramen)** |

## De detaljerade jämförelserna

Jämförelserna är grupperade enligt standardernas metodologiska arvsordning: från organisationsperspektivet via produktstandarderna till infrastruktur- och transaktionslagret och finansvärldens PCAF, med EU:s rapporteringsarkitektur som ett regulatoriskt lager ovanpå beräkningsstandarderna.

- **[Organisationsnivåstandarderna](jamforelse/organisationsstandarder.md)** - GHG Protocol och ISO 14064-1.
- **[Produktnivåstandarderna](jamforelse/produktstandarder.md)** - ISO 14040/14044, ISO 14067, EPD/ISO 14025, PACT, Catena-X.
- **[Infrastruktur- och transaktionslagret](jamforelse/infrastruktur-och-transaktion.md)** - DPP och BEAst.
- **[PCAF](jamforelse/pcaf.md)** - finanssektorns standard för financed emissions.
- **[EU:s rapporteringsarkitektur](jamforelse/eu-rapporteringsarkitektur.md)** - CSRD/ESRS och Voluntary Standard ("VSME").

---

## Sammanfattande positionering

MASSIV+ är en **öppen standard för beräkning och propagering av utsläppsdata på organisationsnivå** - utformad för det utrymme där produktnivådata är otillgänglig men bolagsnivådata är för grov. Relationerna till omgivande standarder är komplementära. GHG Protocol är grunden för Scope 1+2-värdena, och produktstandarderna och MASSIV+ utbyter data i båda riktningar. DPP är en databärare (bärarstandarderna EN 1821x publicerade 2026, med data decentraliserad hos aktörerna) vars koldioxidfält följer PEF/ISO 14067 - ett fält vars jämförbarhet passet inte garanterar, vilket är den lucka MASSIV+ adresserar med standardiserade faktorer och Coverage - och dit MASSIV+ levererar uppströms primärdata. Byggsektorns BEAst-standard kan bära MASSIV+-flöden på den bilaterala transaktionen mellan leverantör och kund, och PCAF får i MASSIV+ den primärdata på kundnivå som dagens financed-emissions-rapportering (utsläpp knutna till lån och investeringar) saknar. I förhållande till EU:s reviderade rapporteringsarkitektur (CSRD/ESRS, Voluntary Standard) är MASSIV+ det operativa skikt som gör Voluntary Standards Scope 1+2-datafloor (ett obligatoriskt dataminimum - ett golv för vad som ska rapporteras) användbart i en värdekedja - och flödar in som högkvalitativ primärinput i det rapporterande bolagets Scope 3.
