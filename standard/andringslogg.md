---
layout: default_banner
title: "Versioner och ändringslogg"
parent: "Standard"
nav_order: 3
---

# Versioner och ändringslogg

Specifikationen ändras bara genom släppta versioner. Varje version beslutas på ett releasemöte, och vad som ingår redovisas här. Hur det går till beskrivs i [Så utvecklas standarden](../sa-utvecklas-standarden.md).

**Numrering.** Versionerna numreras `0.1`, `0.2` och så vidare. Andra siffran ökar vid varje release med ändringar i sak. En redaktionell rättelse mellan två releaser, som språk eller en trasig länk, kan få en tredje siffra (`0.2.1`) om den behöver gå att hänvisa till. Version 1.0 reserveras för den första version som antas av ett formellt tekniskt råd.

**Hänvisa till en version.** Sidan [Specifikation](specifikation.md) visar alltid den gällande versionen. Ersatta versioner ligger kvar under `/standard/versioner/` med sitt nummer i adressen, och varje version har en tagg och en release på [GitHub](https://github.com/{{ site.massiv.repo }}/releases).

**På väg in i nästa version.** Ändringar som väntar på releasemötet {{ site.massiv.nasta_releasemote }} syns under [Förslag](../forslag/) och som öppna pull requests under [milstolpen för version {{ site.massiv.nasta_version }}](https://github.com/{{ site.massiv.repo }}/milestones).

---

## 0.1 - antagen {{ site.massiv.antagen }}

Första versionen. Den samlar specifikationen som den har vuxit fram sedan publiceringen, till och med uppdelningen i två Coverage-mått (Coverage över nodens hela massa och uppströms-Coverage) i oktober 2026. Ändringarna före 0.1 finns i [commit-historiken](https://github.com/{{ site.massiv.repo }}/commits/main/standard/specifikation.md).
