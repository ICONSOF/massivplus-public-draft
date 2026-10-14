---
layout: default_banner
title: "Mall för ett förslag"
parent: "Förslag"
nav_order: 99
---

# Mall för ett förslag

Ett förslag är en fil i mappen `forslag/` med namnet `mf-nnn-kort-titel.md`. Kopiera mallen, fyll i fälten överst och skriv avsnitten. Fälten styr statusrutan på förslagets sida och listan på [Förslag](README.md).

```markdown
---
layout: default_banner
title: "MF-003 Kort titel"
parent: "Förslag"
nav_order: 3
forslag_id: MF-003
forslag_status: Utkast          # Utkast, Under diskussion, Beredd, Antagen, Avvisad, Parkerad
forslag_mal: "0.3"              # versionen förslaget siktar på
forslag_beror: "§2"             # avsnitt i specifikationen
forslag_forfattare: Förnamn Efternamn
forslag_diskussion: https://github.com/{{ site.massiv.repo }}/discussions/NN
forslag_pr: NN                  # pull requesten med textändringen, när den finns
---

# MF-003 Kort titel

## Problem
Vad standarden inte hanterar, eller hanterar fel. Gärna med ett fall från fältet.

## Förslag
Den konkreta ändringen, formulerad som text i specifikationen.

## Konsekvenser
Vad ändras för en nod som redan rapporterar? Ändras några siffror?
Påverkas massbalansen, Coverage eller propageringen?
Vad blir svårare att tillämpa, och kan ett verktyg bära det?
Vad behöver prövas i en pilot innan förslaget antas?

## Alternativ som övervägts
Och varför de valdes bort.

## Öppna frågor

## Beslut
Fylls i på releasemötet: antagen i version X, avvisad eller parkerad, med motivering.
```
