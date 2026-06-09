---
layout: default
title: "Metodologiska risker"
nav_order: 4
---

# Metodologiska risker och begränsningar

> **Poäng:** Var MASSIV+ är strukturellt svagt, och hur svagheterna hanteras. En öppen genomgång av riskerna är förutsättningen för att standarden ska kunna granskas och vidareutvecklas på sina egna villkor.

Den här texten kan läsas fristående. Den förutsätter att du har en grundläggande bild av hur MASSIV+ fungerar - läs [introduktionen](../introduktion.md) eller [specifikationen](../standard/specifikation.md) först om du inte är bekant med ramverket.

---

## Dubbelräkning av okända utsläpp

Om en nod inkluderar okända utsläpp för leverantörers leverantörer utanför sin direkta kedja kan samma utsläppsmassa hamna i systemet två gånger - dels via leverantörens egen U-rapportering nedströms, dels via nodens egen U-rapportering som hoppar över ett led. Att flera direkta kunder var för sig rapporterar U för samma leverantör är *inte* ett problem - de räknar var sin andel av samma leverantörs okända utsläpp.

**Mitigering:** standarden tillåter enbart att direkta leverantörsrelationer deklareras. Det vill säga: en nod får bara rapportera U för en uppströmsleverantör som den faktiskt köper av, inte för leverantörens leverantör.

## Cirkularitet

Ömsesidiga leveransrelationer hanteras av verktyg som implementerar standarden via matrisinversion eller tidssegmentering (se [specifikationen, avsnitt 7](../standard/specifikation.md#7-cirkulära-flöden)). En risk kvarstår om verktyg implementerar detta inkonsekvent - vilket understryker vikten av att standarden specificerar godkända metoder och att förvaltningsorganisationen certifierar implementationer.

## Regulatorisk och tolkningsrisk

Konventionella GHG-ramverk blandar okänd och faktisk data i ett samlat Scope 3-värde. MASSIV+ särhåller dem explicit via A- och U-komponenterna. Risken är att systemet missuppfattas som om det:

- jämställer okänd data med mätdata,
- avviker från etablerad GHG-praxis, eller
- utger sig för att vara ett substitut för produktnivåberäkning (PCF).

**Mitigering:** strikt separation av A och U, transparent Coverage-rapportering, tydlig kommunikation om att U är temporärt och att A alltid prioriteras, samt aktiv positionering av standarden som komplement till befintliga ramverk - inte ersättning. Se [jämförelse med andra ramverk](../positionering/jamforelse-med-andra-ramverk.md) för hur relationen till GHG Protocol, ISO 14064-1, EPD, PACT, Catena-X och PCAF konkret ser ut.

---

*Källa: Utdrag ur MASSIV+ teknisk specifikation, 2026-05-06.*
