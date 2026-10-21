---
layout: default_banner
title: "Vad massbalansen bevarar"
parent: "Fördjupningar"
nav_order: 13
---

# Vad massbalansen bevarar

> **Poäng:** Massbalansen i MASSIV+ handlar inte om materia. Den bevarar ansvaret för utsläpp som redan har skett, på samma sätt som bokföringsekvationen bevarar pengar mellan debet och kredit. Därför följer den affärerna och inte godset, och därför går gränsen mellan det tillåtna och det otillåtna vid om en minskning hos en part bokförs som en ökning hos en annan.

Texten förutsätter en grundläggande bild av MASSIV+. Läs [introduktionen](../introduktion.md) först om du inte är bekant med ramverket.

---

## 1. Vad principen säger

För varje nod gäller att summan av de utgående flödena är lika med nodens totala utsläpp ([specifikationen §5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)):

```
Σⱼ Tᵢⱼ = Tᵢ
```

Noden för vidare allt den har, varken mer eller mindre. Den kan inte skicka ut mer än den har, och den kan inte tappa något på vägen. Regeln gäller per nod och per period, och varje nod håller den själv utan att någon behöver se hela nätverket.

---

## 2. Vad som bevaras

Namnet antyder att något fysiskt rör sig genom kedjan. Så är det inte. När en ståltillverkare har släppt ut 100 ton koldioxid finns de i atmosfären. Ingenting av dem följer med stålet till kunden.

Det som följer med är ansvaret för utsläppen. Ståltillverkaren redovisar dem som sin Scope 1, och kunderna redovisar sina andelar som Scope 3. Massbalansen ser till att andelarna tillsammans blir exakt 100 ton, så att varje ton redovisas en gång i varje led.

Den närmaste motsvarigheten är bokföringsekvationen. En faktura bokförs som intäkt hos säljaren och som kostnad hos köparen, och beloppet är detsamma på båda sidor. I MASSIV+ bokförs varje flöde som Scope 1+2 hos avsändaren och som Scope 3 hos mottagaren (se [bokföringsanalogin](bokforingsanalogin.md)).

---

## 3. Ordet betyder olika saker

Massbalans förekommer i minst fyra betydelser i de ramverk MASSIV+ jämförs med:

| Var | Vad det betyder | Vad som går ihop |
|---|---|---|
| EU:s utsläppshandel, ISO 14064-1 Annex C | Ett sätt att räkna fram processutsläpp ur kolet som går in i och ut ur en process | Kolatomer |
| ISO 14044 (LCA) | En kontroll av att data för en enhetsprocess går ihop | Material och energi |
| ISO 22095 | En spårbarhetsmodell där material med och utan en egenskap blandas och egenskapen fördelas genom bokföring | Mängden egenskap |
| MASSIV+ | Bevarande per nod | Ansvaret för utsläpp |

De två första gäller fysisk materia. ISO 22095 och MASSIV+ gäller bokföring, men av olika saker. Mer om ISO 22095 finns i [jämförelsen](../positionering/jamforelse/iso-22095.md).

Att ordet lätt läses fel är skälet till att namnet prövas i [diskussion #56](https://github.com/ICONSOF/massivplus-public-draft/discussions/56).

---

## 4. Vad den garanterar och inte garanterar

Massbalansen garanterar intern konsistens. Inga utsläpp skapas eller försvinner i propageringen, och ingenting räknas två gånger.

Den garanterar inte att talen stämmer. En nod som rapporterar för låga egna utsläpp för felet vidare nedströms med full precision. Och för att kontrollera en nods massbalans utifrån måste man se alla dess kunder och volymer, alltså det som konfidentialiteten skyddar. Båda frågorna behandlas i [metodologiska risker](metodologiska-risker.md).

---

## 5. Vad den tillåter och förbjuder

MASSIV+ följer affärsrelationen, inte godset (se [koordinatbytet](koordinatbytet.md)). Massbalansen frågar därför inte vart molekylerna tog vägen. Den frågar om allt som noden har är bokfört en gång mot en namngiven motpart.

Det ger utrymme för flera sätt att fördela:

- En nod väljer sin nyckel, till exempel massa, energi, kvantitet eller värde ([§3](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)).
- En organisation väljer hur den delas upp i noder, till exempel en nod per leverantör, per kund eller per anläggning ([§1](../standard/specifikation.md#1-systemdefinition---värdekedjan-som-nätverk)).

### Exempel: en anläggning som blandar råvara

En kemisk anläggning köper två sorters råvara och blandar dem i samma process. Den fossila råvaran bär 450 ton uppströmsutsläpp och står för 90 procent av volymen. Den biobaserade bär 10 ton och står för 10 procent. Anläggningens egna Scope 1+2 är 500 ton. Totalt har anläggningen 960 ton.

Tre kunder köper produkten: X tar 10 procent, Y och Z 45 procent var. X har köpt en produkt som säljs som biobaserad.

| Fördelning | X | Y | Z | Summa |
|---|---|---|---|---|
| En nod, massa som nyckel | 96 | 432 | 432 | 960 |
| En nod per kund, den biobaserade råvaran bokförd på X | 60 | 450 | 450 | 960 |

I den andra raden får X sin andel av de egna utsläppen (50 ton) och den biobaserade råvarans 10 ton. Y och Z delar resten. X:s tal sjunker med 36 ton och Y:s och Z:s stiger med 18 ton var. Summan är densamma.

Det andra sättet motsvarar mass balance i ISO 22095:s mening, och det håller massbalansen i MASSIV+. Utsläppen är anläggningens egna och verkliga, varje del är bokförd en gång mot en namngiven kund, och det X får mindre får Y och Z mer. Att X:s produkt fysiskt innehåller samma blandning som de andras spelar ingen roll, eftersom MASSIV+ inte följer godset.

### Det som bryter massbalansen

Ett certifikat fungerar annorlunda. En ursprungsgaranti för el, ett certifikat för biogas eller ett certifikat för lågutsläppsstål som köps skilt från leveransen låter köparen räkna bort utsläpp. Men ingen annan bokför dem i stället. Minskningen hos köparen motsvaras inte av en ökning hos någon annan, och summan går inte längre ihop.

Detsamma gäller ett tal som har nettats mot klimatkompensation innan det skickas vidare. Det som propageras ska vara brutto (se [kompensation och faktiska flöden](kompensation-och-faktiska-floden.md) och [ursprungsgarantier](ursprungsgarantier-kritik-och-regelverk.md)).

Gränsen går alltså inte mellan fysiskt och bokfört. Den går mellan en omfördelning inom bokföringen, där summan är densamma, och ett avdrag utanför den, där summan minskar.

---

## 6. Öppna frågor

- **Namnet.** Om principen ska heta massbalans, bevarandeprincipen eller något annat prövas i [#56](https://github.com/ICONSOF/massivplus-public-draft/discussions/56).
- **Att redovisa en avtalsstyrd fördelning.** I exemplet stiger Y:s och Z:s tal utan att något har ändrats för deras del. Om en sådan fördelning ska redovisas särskilt, så att de ser varför, hör till förslaget om [utspädning i genomströmningsnoder](../forslag/mf-002-utspadning.md).
- **Relation eller vara.** Talet ska variera med motparten, inte med varan ([§5](../standard/specifikation.md#individuation-av-allokeringsenheten)). En nod per kund uppfyller det. Om anläggningen i stället sätter ett lägre tal på en produktsort, så att varje köpare av sorten får det, följer talet varan. Var gränsen går i praktiken är oprövat (se [produktnivå-invändningen](produktniva-invandningen.md)).
