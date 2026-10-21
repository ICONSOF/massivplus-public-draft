---
layout: default_banner
title: "Massbalansen i MASSIV+"
parent: "Fördjupningar"
nav_order: 13
---

# Massbalansen i MASSIV+

> **Poäng:** Massbalansen i MASSIV+ bevarar ansvaret för utsläpp som redan har skett, inte materia, på samma sätt som bokföringsekvationen bevarar pengar mellan debet och kredit. Därför följer den affärerna, och därför går gränsen mellan det tillåtna och det otillåtna vid om en minskning hos en part bokförs som en ökning hos en annan.

Texten förutsätter en grundläggande bild av MASSIV+. Läs [introduktionen](../introduktion.md) först om du inte är bekant med standarden.

---

## 1. Vad principen säger

För varje nod gäller att summan av de utgående flödena är lika med nodens totala utsläpp ([specifikationen §5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)):

```
Σⱼ Tᵢⱼ = Tᵢ
```

Noden för vidare allt den har, varken mer eller mindre. Regeln gäller per nod och per period, och varje nod håller den själv utan att någon behöver se hela nätverket.

---

## 2. Vad som bevaras

Namnet antyder att något fysiskt rör sig genom kedjan, men när en ståltillverkare har släppt ut 100 ton koldioxid finns de redan i atmosfären.

Det som följer med till kunden är ansvaret för utsläppen. Ståltillverkaren redovisar dem som sin Scope 1, och kunderna redovisar sina andelar som Scope 3. Massbalansen ser till att andelarna tillsammans blir exakt 100 ton, så att varje ton redovisas en gång hos avsändaren och en gång hos mottagarna.

Den närmaste motsvarigheten är bokföringsekvationen. En faktura bokförs som intäkt hos säljaren och som kostnad hos köparen, och beloppet är detsamma på båda sidor. I MASSIV+ bokförs varje flöde som Scope 1+2 hos avsändaren och som Scope 3 hos mottagaren (se [bokföringsanalogin](bokforingsanalogin.md)).

---

## 3. Ordet betyder olika saker

Massbalans förekommer i minst fyra betydelser i de ramverk MASSIV+ jämförs med:

| Var | Vad det betyder | Vad som går ihop |
|---|---|---|
| EU:s utsläppshandel, ISO 14064-1 Annex C | Ett sätt att räkna fram processutsläpp ur kolet som går in i och ut ur en process | Kolatomer |
| ISO 14044 (LCA) | En kontroll av att data för en enhetsprocess, en enskild process i LCA-modellen, går ihop | Material och energi |
| ISO 22095 | En spårbarhetsmodell där material med och utan en egenskap blandas och egenskapen fördelas genom bokföring | Mängden egenskap |
| MASSIV+ | Bevarande per nod | Ansvaret för utsläpp |

De två första gäller fysisk materia. ISO 22095 och MASSIV+ gäller bokföring, men av olika saker. Mer om ISO 22095 finns i [jämförelsen](../positionering/jamforelse/iso-22095.md).

Att ordet lätt läses fel är skälet till att namnet prövas i [diskussion #56](https://github.com/ICONSOF/massivplus-public-draft/discussions/56).

---

## 4. Vad den garanterar

Massbalansen garanterar intern konsistens. Inga utsläpp skapas eller försvinner i propageringen, och ingenting räknas två gånger.

Att talen stämmer garanterar den inte. En nod som rapporterar för låga egna utsläpp för felet vidare nedströms med full precision. Och för att kontrollera en nods massbalans utifrån måste man se alla dess kunder och volymer, alltså det som sekretessen skyddar. Båda frågorna behandlas i [metodologiska risker](metodologiska-risker.md).

---

## 5. Vad den tillåter och förbjuder

MASSIV+ följer affärsrelationen, inte godset (se [koordinatbytet](koordinatbytet.md)). Massbalansen frågar därför om allt noden har är bokfört en gång mot en namngiven motpart, oavsett vart godset tog vägen.

Det ger utrymme för flera sätt att fördela:

- En nod väljer sin nyckel, till exempel massa, energi, kvantitet eller värde ([§3](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)).
- En organisation väljer hur den delas upp i noder, till exempel en nod per leverantör, per kund eller per anläggning ([§1](../standard/specifikation.md#1-systemdefinition---värdekedjan-som-nätverk)).

### Exempel: en anläggning som blandar råvara

Med påhittade siffror: en kemisk anläggning köper två sorters råvara och blandar dem i samma process. Den fossila råvaran bär 450 ton uppströmsutsläpp och står för 90 procent av volymen. Den biobaserade bär 10 ton och står för 10 procent. Anläggningens egna Scope 1+2 är 500 ton. Totalt har anläggningen 960 ton.

Tre kunder köper produkten: X tar 10 procent, Y och Z 45 procent var. X har köpt en produkt som säljs som biobaserad.

| Fördelning | X | Y | Z | Summa |
|---|---|---|---|---|
| En nod, massa som nyckel | 96 | 432 | 432 | 960 |
| En nod per kund, den biobaserade råvaran bokförd på X | 60 | 450 | 450 | 960 |

I den andra raden får X sin andel av de egna utsläppen (50 ton) och den biobaserade råvarans 10 ton. Y och Z delar resten. X:s tal sjunker med 36 ton och Y:s och Z:s stiger med 18 ton var.

Det andra sättet motsvarar mass balance i ISO 22095:s mening, och det håller massbalansen i MASSIV+. Utsläppen är anläggningens egna och verkliga, varje del är bokförd en gång mot en namngiven kund, och det X får mindre får Y och Z mer.

Det X får är en mängd utsläpp för relationen under perioden, inte ett tal per kilo produkt. Köper X både den biobaserade och den vanliga produkten under perioden ingår båda i samma mängd. Ett tal per enhet som följer med varan uppstår först när kedjan når en slutkonsument ([§5](../standard/specifikation.md#individuation-av-allokeringsenheten)).

### Det som bryter massbalansen

Ett certifikat bryter massbalansen. En ursprungsgaranti för el, ett certifikat för biogas eller ett certifikat för lågutsläppsstål som köps skilt från leveransen låter köparen räkna bort utsläpp som ingen annan tar över, och summan minskar.

Detsamma gäller ett tal där köpt klimatkompensation redan har dragits av innan det skickas vidare. Det som propageras ska vara brutto (se [kompensation och faktiska flöden](kompensation-och-faktiska-floden.md) och [ursprungsgarantier](ursprungsgarantier-kritik-och-regelverk.md)).

Gränsen går alltså mellan en omfördelning inom bokföringen, där summan är densamma, och ett avdrag utanför den, där summan minskar, inte mellan fysiskt och bokfört.

---

## 6. Öppna frågor

- **Namnet.** Om principen ska heta massbalans, bevarandeprincipen eller något annat prövas i [#56](https://github.com/ICONSOF/massivplus-public-draft/discussions/56).
- **Att redovisa en avtalsstyrd fördelning.** I exemplet stiger Y:s och Z:s tal utan att något har ändrats för deras del. Om en sådan fördelning ska redovisas särskilt, så att de ser varför, hör till förslaget om [utspädning i genomströmningsnoder](../forslag/mf-002-utspadning.md).
