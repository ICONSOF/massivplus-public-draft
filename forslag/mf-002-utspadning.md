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

> **Status:** Utkast, 2026-10-30, reviderat 2026-11-04. Ingår inte i standarden. Berör §8. Författare: Birger Löfgren. Diskussion: [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> [MF-004](mf-004-nodindelning.md) anger vad som får vara en nod och [MF-005](mf-005-allokeringsposter.md) vad organisationer lämnar till varandra. Förslagen kan bedömas vart för sig.

En nod samlar sina egna utsläpp och de utsläpp den tar emot från leverantörer, och fördelar summan vidare till sina mottagare ([specifikationen](../standard/specifikation.md) §1-4). Den del av de inkommande utsläppen som har faktisk grund heter A och den okända delen U. Coverage anger hur stor andel av nodens utsläpp som har faktisk grund (§8). Förslaget inför ett andra mått, D, som visar hur mycket fördelningen av de inkommande utsläppen till mottagarna avviker från en fördelning som organisationen har dokumenterat som den mest rättvisande. [MF-004](mf-004-nodindelning.md) visar med ett exempel hur en nod som samlar flera inflöden kan jämna ut skillnaderna mellan dem. D gör den utjämningen synlig som ett tal.

## Förslag till standardtext

Följande föreslås som ett nytt avsnitt i §8. Definitionerna av Coverage och uppströms-Coverage står kvar. Beteckningarna nedan gäller bara D.

### D: avvikelse från en referensfördelning

D ska redovisas vid sidan av Coverage för ett angivet mätområde. D visar hur fördelningen av områdets inkommande utsläpp till mottagarna avviker från en dokumenterad referensfördelning. Om D inte kan beräknas ska det redovisas som ej beräknat, med skälet.

Mätområdet, B, kan vara en nod, en del av verksamheten som är stabil över tid eller hela organisationen. När olika nodindelningar jämförs ska följande vara detsamma:

1. Områdets gräns och rapporteringsperiod.
2. De inkommande A och U, med underlagets version.
3. Mottagarna och hur fint de delas upp, till exempel per kundrelation, mottagande nod eller leveransgrupp.
4. Referensfördelningen, vad den ska visa och vilken metodversion den följer.

D räknas bara på utsläpp som kommer in från leverantörer. Områdets egna Scope 1+2 ingår inte, inte heller när de passerar interna noder och där räknas som Actual. Underlaget ska hålla isär de egna utsläppen och de inkommande.

Referensen ska vara den fördelning till mottagarna som bäst passar syftet och som går att motivera med uppgifter som finns eller rimligen kan tas fram. Relevanta uppgifter som redan finns, till exempel om leverantör, artikelgrupp och leverans, ska användas. Väljs en grövre referens ska valet motiveras. Underlag, antaganden och begränsningar ska dokumenteras.

Referensen ska bestämmas före jämförelsen och användas på samma sätt i alla indelningar som jämförs. Det ska framgå vad i referensen som bygger på registrerade leveranskopplingar, vad som bygger på avtal och vad som är modellerat. Ändringar av referens eller metod ska versionshanteras, och det ska anges hur de påverkar jämförelsen med tidigare perioder. Referensen får vara densamma som den fördelning som faktiskt används, om den följer av en metod som är motiverad i sig.

För varje mottagare r används följande, i samma enhet, till exempel ton CO2e:

| Beteckning | Betydelse |
|---|---|
| a_r, u_r | A respektive U som området fördelar till mottagaren |
| a_ref,r, u_ref,r | A respektive U som mottagaren skulle få enligt referensen |
| E | Områdets inkommande A + U för perioden |

Både fördelningen och referensen ska summera till områdets inkommande A och U, var för sig. En obalans ska utredas innan D beräknas och får inte döljas genom att talen skalas om. Inga tal får vara negativa.

```
L_r = |a_r - a_ref,r| + |u_r - u_ref,r|
D_B = sum_r L_r / (2E)
```

D_B ligger mellan 0 och 1. Noll betyder att varje mottagare får lika mycket A och lika mycket U som referensen anger. Om E är noll går D_B inte att beräkna.

Varje mottagare som tilldelas något, eller har något i referensen, ska också få ett eget värde:

```
D_B,r = L_r / (a_r + u_r + a_ref,r + u_ref,r)
```

Även D_B,r ligger mellan 0 och 1. Mottagaren ska få veta vad den tilldelats, vad referensen anger och skillnaden, med riktning och med A och U var för sig, och vilket område och vilken referens jämförelsen gäller.

D visar avvikelsen från den angivna referensen. Ett högt D betyder inte att en fördelningsnyckel som §3 tillåter är fel. D-värden som räknats med olika områden, referenser eller uppdelning av mottagarna går inte att jämföra med varandra. D gäller fördelningen inom området och visar inte om leverantörerna längre upp i kedjan har bevarat skillnaderna.

## Varför ett mått till?

Coverage visar hur stor andel av utsläppen som har faktisk grund. §8 påpekar också att två fördelningar kan ha Coverage 1 och ändå ge kunden olika stöd: ett snitt för hela bolaget och en fördelning för just den linje som levererar till kunden. D mäter en del av den skillnaden, nämligen hur långt fördelningen ligger från en motiverad referens.

Mer faktisk data höjer Coverage, men det hjälper inte kunden om skillnaderna mellan inflödena jämnas ut på vägen. D kompletterar Coverage på den punkten. Det är inget samlat betyg på datakvaliteten.

## Exempel: en grossist med två kunder

En grossist köper 100 ton material från vardera av två leverantörer. Materialet från den första bär 40 ton CO2e, koldioxidekvivalenter, och materialet från den andra 200 ton. Kund X får materialet från den första leverantören och kund Y från den andra. Grossistens egna utsläpp är 5 ton och delas lika. Alla inkommande utsläpp är A. Talen är påhittade.

En gemensam nod som fördelar efter vikt ger båda kunderna 122,5 ton. Om grossisten håller isär inflödena får X 42,5 och Y 202,5 ton. Referensen är här den kända kopplingen mellan inköp och kund.

Om D räknades inom varje nod för sig skulle en nod med bara en mottagare alltid få D = 0. Grossisten skulle kunna dela den gemensamma noden i två kundnoder som var och en får samma snitt som förut och då få D = 0, utan att någon kund fått ett bättre tal. Därför räknas D över ett område som hålls fast när noderna delas om:

| Indelning inom samma område | X får totalt | Y får totalt | D_B | X:s D_B,r | Y:s D_B,r |
|---|---:|---:|---:|---:|---:|
| En nod, fördelning efter vikt | 122,5 | 122,5 | 0,333 | 0,500 | 0,250 |
| Två kundnoder med samma snitt | 122,5 | 122,5 | 0,333 | 0,500 | 0,250 |
| Inflödena hålls isär | 42,5 | 202,5 | 0 | 0 | 0 |

D räknas på de 240 ton som kommer in från leverantörerna. Totalerna i tabellen innehåller också de egna 5 tonnen. Att noderna delas om ändrar inte D, det gör bara en ändrad fördelning till kunderna.

Mätområdet behöver inte vara hela bolaget. En nod som är stabil över tid kan vara området.

## Ett lågt D för området kan dölja en stor avvikelse för en kund

Anta att referensen ger X 8 och Y 360 ton. En fördelning efter vikt, där X köper 10 procent och Y 90 procent, ger i stället X 36,8 och Y 331,2 ton. Områdets D är cirka 0,078. X får ändå 28,8 ton mer än referensen, och X:s eget värde är cirka 0,643. Y får 28,8 ton mindre, och Y:s värde är cirka 0,042.

X:s värde betyder inte att 64 procent av X:s utsläpp är fel. Det visar hur stor avvikelsen är i förhållande till X:s egna tal. Därför ska mottagaren också få avvikelsen i ton och åt vilket håll den går.

Områdets D är ett vägt medel av mottagarnas värden. Varje mottagare väger efter hur stor del av de inkommande utsläppen den har i fördelningen och i referensen:

```
w_r = (a_r + u_r + a_ref,r + u_ref,r) / (2E)
```

Vikterna summerar till 1. En mottagare som varken tilldelas något eller har något i referensen väger noll.

## A och U jämförs var för sig

Referensen kan ge X 100 ton A och Y 100 ton U. En gemensam nod ger i stället båda 50 ton A och 50 ton U. Båda får fortfarande 100 ton totalt, så om bara totalerna jämförs blir D = 0. När A och U jämförs var för sig blir D = 0,5, både för området och för varje kund.

Områdets Coverage är 0,5 i båda fallen. För kunderna ändras Coverage från 1 och 0 till 0,5 för båda. D visar alltså en förändring som områdets Coverage inte visar. U är fortfarande det okända enligt §2. Ändras U-underlaget kan D ändras, och därför ska underlagets version anges.

## Hur fint mottagarna delas upp påverkar D

Om X och Y i föregående exempel i stället är två leveransgrupper till samma kund blir D = 0,5 när grupperna jämförs var för sig. Slås de ihop till en total för kunden blir D noll, eftersom kunden totalt får lika mycket A och U som referensen anger.

Hur fint mottagarna delas upp är alltså en del av mätningen. Förslaget hindrar att en intern omindelning av noderna sänker D, men D beror fortfarande på hur mottagarna avgränsas. Uppdelningen ska passa syftet och underlaget och anges för mottagaren.

## Valet av referens

I exemplet med grossisten följer referensen den kända kopplingen mellan inköp och kunder. Om grossisten i stället fördelar efter intäkt, och X står för 60 procent av intäkten och Y för 40, får X 144 och Y 96 ton av de inkommande utsläppen. Mot referensen 40 och 200 blir D cirka 0,433.

Har grossisten och kunderna i stället avtalat en fördelning på 144 och 96, och är avtalet motiverat i sig, kan avtalet vara referensen. Då blir D noll med samma fördelning, vilket visar att fördelningen följer avtalet. Exemplet visar hur mycket valet av referens betyder, inte vilken referens som passar en viss verksamhet.

En referens som bygger på varornas ursprung kan visa att en fördelning efter intäkt ger mer utsläpp till en dyrare vara, också när den varan hade lägre utsläpp i inköp. §3 tillåter fortfarande intäktsnyckeln, men D gör följden synlig. Förslaget anger därför ingen gräns för vad som är ett godkänt D.

En grossist som redan har uppgifter om leverantör, artikelgrupp och leverans ska använda dem i referensen. En grövre referens kan vara motiverad av vad det kostar att ta fram uppgifterna, men motiveringen ska framgå. Bolaget behöver inte kartlägga varje väg genom hela leveranskedjan för att börja använda D.

När flöden blandas fysiskt, som el i ett elnät, kan referensen bygga på en dokumenterad modell, om modellen är motiverad för syftet. D visar då hur väl fördelningen stämmer med modellen. Finns ingen motiverad referens redovisas D som ej beräknat.

### ISO 14044:s ordning för allokering

ISO 14044, standarden för livscykelanalys, anger en ordning för allokering (avsnitt 4.3.4.2). I första hand undviks allokering, till exempel genom att dela upp processen. I andra hand fördelas utsläppen efter fysiska samband, och först därefter efter andra samband, som ekonomiskt värde. Ordningen gäller livscykelanalys och inte MASSIV+, men den pekar åt samma håll som kravet att använda relevanta uppgifter som redan finns. Förslaget hämtar ingen regel för D från ISO.

## Jämförbarhet och begränsningar

D mäter fördelningen inom området. Skillnader kan redan ha jämnats ut hos leverantören, och två olika ursprung kan ge samma A och U till kunderna. D = 0 hos en grossist betyder därför inte att hela kedjan har bevarat skillnaderna.

Förslaget säger inget om hur leverantörernas D ska föras vidare eller läggas ihop. Mottagaren får veta vilket område D gäller. Ska en jämförelse omfatta ett tidigare led behövs ett underlag och en referens för just det ledet.

Ett byte av referens, område, uppdelning av mottagarna eller U-underlag kan ändra D fast utsläppen är desamma. Därför ska D versionshanteras och jämföras på samma grund över tid. [MF-004](mf-004-nodindelning.md) beskriver hur nodindelningen hålls stabil och hur metodbyten redovisas.

## Alternativ och beräkningskontroll

Tre enklare sätt att räkna D räcker inte:

1. Ett D per intern nod. En nod med en enda mottagare får alltid noll, så en uppdelning i kundnoder ger ett sken av förbättring.
2. Bara ett D för hela bolaget. En liten kund kan få en stor avvikelse som inte syns i bolagets värde.
3. Ett D på A och U tillsammans. Det missar när fördelningen blandar ihop det kända och det okända.

Förslaget hanterar de tre fallen, men kräver mer underlag än Actual och Unknown som skickas till kunden.

Räknefallen kan räknas om med [d-fast-avgransning.py](../assets/berakningar/d-fast-avgransning.py), som räknar med exakta bråk. Skriptet kontrollerar balansen, att D ligger mellan 0 och 1, hur mottagarnas värden vägs ihop, att de egna utsläppen hålls utanför och att D inte ändras när noderna delas om, också för 100 slumpade fördelningar. Det visar att formlerna har de egenskaperna, inte att en viss verksamhets referens är väl vald.

## Beslut

Inte behandlat. Förslaget gäller ett nytt mått i §8 och kräver ett eget beslut.
