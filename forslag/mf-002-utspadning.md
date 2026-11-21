---
layout: default_banner
title: "MF-002 Utspädning och fördelningsmåttet D"
parent: "Förslag"
nav_order: 2
forslag_id: MF-002
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§8"
forslag_forfattare: Birger Löfgren
forslag_diskussion: https://github.com/ICONSOF/massivplus-public-draft/discussions/49
---

# MF-002 Utspädning och fördelningsmåttet D

> **Status:** Utkast, omarbetat 2026-10-30, språket förenklat 2026-11-21. Ingår inte i standarden. Berör §8. Författare: Birger Löfgren. Diskussion: [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> Vad som får vara en nod behandlas i [MF-004](mf-004-nodindelning.md), och vad som lämnas till nästa organisation i [MF-005](mf-005-allokeringsposter.md).

Coverage (faktisk andel, om [MF-008](mf-008-namnbyte.md) antas) visar hur stor del av en nods utsläpp som har faktisk grund. Det visar inte om noden har jämnat ut skillnader mellan sina inflöden. En grossist som köper från en leverantör med låga utsläpp och en med höga, och ger alla kunder samma snitt, kan ha Coverage 1 och ändå dölja skillnaden.

Förslaget inför måttet D, som visar hur mycket fördelningen till kunderna avviker från en dokumenterad referens.

## Förslag till standardtext

Ett nytt delavsnitt i §8. Definitionerna av Coverage och uppströms-Coverage står kvar.

### D: avvikelse från en referensfördelning

**D ska redovisas vid sidan av Coverage för ett angivet mätområde.** D visar hur fördelningen av områdets inkommande uppströmsmängder avviker från en dokumenterad referens. Kan D inte beräknas redovisas det som ej beräknat, med orsak.

Mätområdet B kan vara en nod, en stabil del av verksamheten eller en rapporteringsentitet. Följande ska anges, och hållas lika när olika interna nodindelningar jämförs:

1. Verksamhetsgräns och rapporteringsperiod.
2. Inkommande A och U från externa leverantörer, med underlagets version.
3. Mottagarna och deras detaljnivå, till exempel kundrelation, mottagande nod eller leveransgrupp.
4. Referensfördelningen, dess syfte och metodversion.

Områdets egna Scope 1+2 räknas inte in i D, inte heller när de passerar interna noder och då ingår i Actual. Underlaget ska hålla isär egna utsläpp och inkommande uppströmsmängder.

**Referensen ska vara den fördelning som bäst passar syftet och som kan motiveras med information som finns eller rimligen kan tas fram.** Underlag, antaganden och detaljnivå dokumenteras. Finare uppgifter som redan finns och är relevanta ska användas, och ett grövre val ska motiveras.

Referensen bestäms före jämförelsen och används konsekvent. Registrerade leveranskopplingar, avtalade fördelningar och modellerade samband ska gå att skilja åt. Ändringar av referens eller metod versionshanteras, och det anges hur de påverkar jämförbarheten. Referensen får vara densamma som allokeringen om den har en egen motivering.

För varje mottagare r används följande mängder, i samma enhet:

| Beteckning | Betydelse |
|---|---|
| a_r, u_r | Inkommande faktiska respektive okända mängder som området fördelar till mottagaren |
| a_ref,r, u_ref,r | Samma mängder enligt referensen |
| E | Den inkommande A + U som området fördelar under perioden. Utan lagerkonto är det områdets inkommande A + U. Med lagerkonto enligt [MF-001](mf-001-lagerhantering.md) är det inkommande A + U minus lagerförändringen |

De fördelade mängderna och referensmängderna ska var för sig summera till den A och den U som området fördelar, alltså till E. En obalans ska utredas och får inte döljas genom normalisering.

Med lagerkonto fördelas inte allt som kommer in under perioden. Får området in 240 ton och lägger 40 ton i lagerkontot fördelas 200 ton. Fördelningen, referensen och E avser då alla 200 ton.

D förutsätter att mängderna inte är negativa, och det är därför D ligger mellan 0 och 1. En rättelse som enligt [MF-006](mf-006-periodregel.md) bokförs i nästa period kan ge negativa mängder. Bokfördes 100 ton som U för en leverantör vars post sedan visade 97 ton A, förs −100 U och +97 A till nästa period. Sådana rättelser räknas inte in i D utan redovisas bredvid.

```
L_r = |a_r - a_ref,r| + |u_r - u_ref,r|
D_B = sum_r L_r / (2E)
```

D_B ligger mellan 0 och 1. Noll betyder att fördelningen sammanfaller med referensen för alla mottagare. När E är noll är D_B odefinierat.

För varje mottagare med en fördelad mängd eller en referensmängd över noll redovisas också relationsvärdet:

```
D_B,r = L_r / (a_r + u_r + a_ref,r + u_ref,r)
```

D_B,r ligger mellan 0 och 1 och är odefinierat när nämnaren är noll. Mottagaren får de fördelade mängderna, referensmängderna och skillnaden, med riktning och med A och U var för sig, och uppgift om område och referens.

D mäter avvikelse från referensen. Ett högt värde betyder inte att en allokeringsnyckel som §3 tillåter är fel. D med olika områden, referenser eller mottagarnivåer får inte jämföras med varandra. D gäller fördelningen inom området och säger inget om vad som hänt längre upp i kedjan.

## Varför ett mått till

§8 skiljer redan mellan två egenskaper: hur stor del som är faktisk (Coverage) och hur relevant den faktiska delen är för kunden. Ett bolagssnitt och en linjespecifik allokering kan båda ha Coverage 1 men ge kunden olika underlag. D mäter en del av relevansen: hur mycket fördelningen avviker från en motiverad fördelning av samma inflöden.

## Exempel: kundnoder

En grossist köper 100 ton material från vart och ett av två leverantörsflöden. Det ena bär 40 ton CO2e, det andra 200. Kund X får materialet från det första flödet och kund Y från det andra. Grossistens egna utsläpp är 5 ton och delas lika. Allt har faktisk grund. Talen är påhittade.

En gemensam nod med massnyckel ger båda kunderna 122,5 ton. Hålls inflödena isär får X 42,5 och Y 202,5 ton.

Den tidigare formeln för D jämförde andelar inom varje nod, och en nod med en enda mottagare fick alltid noll. Två nya kundnoder kunde därför få D = 0 trots att båda fick samma utjämnade snitt. Den fasta avgränsningen fångar det:

| Beräkning inom samma område | X får | Y får | D_B | D_B,r för X | D_B,r för Y |
|---|---:|---:|---:|---:|---:|
| En nod, massnyckel | 122,5 | 122,5 | 0,333 | 0,500 | 0,250 |
| Två kundnoder med samma snitt | 122,5 | 122,5 | 0,333 | 0,500 | 0,250 |
| Inflödenas fördelning bevaras | 42,5 | 202,5 | 0 | 0 | 0 |

D räknas på de 240 inkommande tonnen, eftersom grossisten inte har något lagerkonto. Tabellens totaler innehåller också de egna 5 tonnen. Nya interna nodnamn ändrar inte D, men en ändrad faktisk fördelning gör det.

## Exempel: ett lågt D kan dölja en kunds avvikelse

Referensen ger X 8 ton och Y 360 ton. En massnyckel på 10/90 ger i stället X 36,8 och Y 331,2. Områdets D_B är cirka 0,078. X får ändå 28,8 ton mer än referensen, med D_B,r cirka 0,643. Y får 28,8 ton mindre, med D_B,r cirka 0,042.

Relationsvärdet visar avvikelsens storlek. Det betyder inte att 64,3 procent av X:s utsläpp är fel, och därför behövs också mängd och riktning.

D_B är ett viktat medelvärde av relationsvärdena, med vikten:

```
w_r = (a_r + u_r + a_ref,r + u_ref,r) / (2E)
```

Vikterna summerar till 1. Mottagare där båda mängderna är noll har vikt noll.

## Exempel: A och U jämförs var för sig

Referensen ger X 100 ton A och Y 100 ton U. En gemensam nod ger i stället båda 50 A och 50 U. Båda får 100 ton, så en jämförelse av bara totalerna ger D = 0. Jämförs A och U var för sig blir D_B = 0,5, och D_B,r = 0,5 för båda.

Områdets Coverage är 0,5 i båda fallen, men kundernas Coverage går från 1 och 0 till 0,5 för båda. D visar en förändring som områdets Coverage inte visar. Ändras U-underlaget kan D:s viktning ändras, och därför versionsanges underlaget.

## Mottagarnivån påverkar D

Är X och Y i stället två leveransgrupper till samma kund är D_B fortfarande 0,5 när grupperna jämförs separat. Slås de ihop till en kundtotal blir D_B noll.

Hur mottagarna avgränsas är alltså en del av mätningen. Förslaget hindrar att en intern omindelning sänker D, men D beror fortfarande på hur de externa mottagarna avgränsas. Detaljnivån ska passa syftet och anges för mottagaren.

## Valet av referens

I det första exemplet följer referensen den kända kopplingen mellan inköp och kunder. Med intäkt som allokeringsnyckel och intäktsandelarna 60/40 får X 144 och Y 96 ton av de inkommande mängderna. Mot den fysiska referensen 40/200 blir D_B cirka 0,433. Mot en motiverad avtalsreferens på 144/96 blir D_B noll med samma fördelning.

Referensen avgör alltså vad D visar. En fysisk referens kan visa att en intäktsnyckel ger en dyrare vara mer utsläpp än dess inflöden motiverar. D får ingen gräns för godkänt resultat i detta förslag.

En grossist som redan har uppgifter om leverantör, artikelgrupp och leverans ska använda dem i referensen. Ett grövre underlag kan motiveras med datainsatsen, men motiveringen ska framgå. Ingen behöver kartlägga varje fysisk väg genom kedjan för att börja.

Vid fysisk blandning, till exempel i ett elnät, kan en dokumenterad modell användas som referens. D visar då överensstämmelse med modellen. Går ingen referens att motivera redovisas D som ej beräknat.

[JRC:s vägledning för LCA](https://eplca.jrc.ec.europa.eu/uploads/ILCD-Handbook-General-guide-for-LCA-DETAILED-GUIDANCE-12March2010-ISBN-fin-v1.0-EN.pdf) beskriver en ordning för allokering enligt ISO 14044: först undersöks om allokering kan undvikas, sedan fysiska samband, sedan andra. Den ordningen gäller LCA. Förslaget hämtar tanken att valet ska motiveras, men tillskriver inte ISO någon regel för D.

## Begränsningar

D mäter fördelningen inom området. Skillnader kan redan ha jämnats ut hos leverantören, och två olika källor kan ge samma A och U till kunderna. Ett lokalt D = 0 visar därför inte att kedjan som helhet har bevarat skillnaderna. Förslaget har ingen regel för att föra leverantörernas D vidare.

Byte av referens, område, mottagarnivå eller U-underlag kan ändra D utan att utsläppen har ändrats. Därför behövs versionskontroll när D följs över tid. Nodindelningens stabilitet behandlas i MF-004.

## Alternativ och beräkningskontroll

- Den tidigare formeln per intern nod. Avvisad, eftersom en uppdelning i kundnoder kunde ge ett skenbart bättre resultat.
- Enbart ett D för hela företaget. Avvisat, eftersom en liten kund kan påverkas mycket utan att det syns.
- Ett mått på bara A + U. Avvisat, eftersom det missar utjämning mellan faktisk och okänd del.
- En generell övre uppskattning av D när ingen referens finns, som i ett tidigare utkast. Avvisad, eftersom en grov uppskattning inte är visad vara en övre gräns för alla tillåtna nycklar.

Den föreslagna konstruktionen kräver mer underlag än den vanliga posten med Actual och Unknown.

Räkneexemplen kan upprepas med [d-fast-avgransning.py](../assets/berakningar/d-fast-avgransning.py), som räknar med exakta bråk. Programmet kontrollerar balans, gränsvärden, viktningen av relationsvärden, att egna utsläpp hålls utanför och att D inte ändras vid omindelning, med 100 varierade fördelningar. Kontrollen visar formlernas egenskaper. Den avgör inte om en viss verksamhets referens är väl vald.

## Beslut

Inte behandlat. Förslaget avser ett nytt mått i §8 och kräver separat beslut.
