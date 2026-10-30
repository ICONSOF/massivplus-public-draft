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

> **Status:** Utkast, omarbetat 2026-10-30. Ingår inte i standarden. Berör §8. Författare: Birger Löfgren. Diskussion: [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> Avsikten med D vid sidan av Coverage behålls. Den tidigare formeln per föränderlig intern nod ersätts av en jämförelse över ett fast område. Nodreglerna i det tidigare utkastets punkt 1-2 behandlas i [MF-004](mf-004-nodindelning.md). Informationsutbytet behandlas i [MF-005](mf-005-allokeringsposter.md).

Enligt [specifikationen](../standard/specifikation.md) samlar varje nod egna Scope 1+2 och inkommande uppströmsbelopp. A betecknar den faktiska uppströmsdelen och U den okända delen. Coverage anger andelen med faktisk grund. D föreslås beskriva en annan egenskap: hur dessa inkommande belopp fördelas till mottagarna.

## Förslag till standardtext

Följande föreslås som ett nytt delavsnitt i §8. Befintliga definitioner av Coverage och uppströms-Coverage behålls. Beteckningarna nedan gäller D-beräkningen.

### D: avvikelse från en dokumenterad referensfördelning

**D ska redovisas vid sidan av Coverage för ett deklarerat mätområde.** D visar hur fördelningen av områdets externt mottagna uppströmsbelopp avviker från en dokumenterad referensfördelning. Saknas underlag för beräkning ska detta anges tillsammans med orsaken. Frånvaro av underlag redovisas som ej beräknat.

Mätområdet B kan vara en nod, en stabil verksamhetsdel eller en rapporteringsentitet. Följande ska anges och hållas lika när alternativa interna nodindelningar jämförs:

1. Verksamhetsgräns och rapporteringsperiod.
2. Externt inkommande A- och U-underlag, inklusive underlagets version.
3. Mottagaruppsättning och mottagarnas detaljnivå, exempelvis kundrelation, mottagande nod eller leveransgrupp.
4. Referensfördelning, dess syfte och metodversion.

Områdets egna Scope 1+2 ska hållas utanför D. Detta gäller även när de passerar interna noder och därför ingår i Actual i senare interna led. Beräkningsunderlaget ska särskilja dessa bidrag från externt mottagna uppströmsbelopp.

**Referensen ska väljas så att den bäst representerar den fördelning mellan mottagarna som är relevant för det angivna syftet och kan motiveras med information som finns eller rimligen kan tas fram.** Underlag, antaganden, begränsningar och vald detaljnivå ska dokumenteras. Redan tillgängliga finare uppgifter som är relevanta för syftet ska beaktas; ett grövre val ska motiveras.

Referensen ska fastställas före jämförelsen och tillämpas konsekvent. Registrerade leveranskopplingar, avtalade fördelningar och modellerade samband ska kunna skiljas åt i redovisningen. Referens- och metodändringar ska versionshanteras och deras påverkan på jämförbarheten anges. Referensen får sammanfalla med den använda allokeringen när detta följer av en självständigt motiverad metod.

För varje mottagare r används följande belopp, i samma utsläppsenhet:

| Beteckning | Betydelse |
|---|---|
| a_r, u_r | Externt mottagna faktiska respektive okända belopp som områdets beräkning tilldelar mottagaren |
| a_ref,r, u_ref,r | Motsvarande belopp enligt referensen |
| E | Områdets totala externt mottagna A + U för perioden |

Utgående belopp och referensbelopp ska vardera summera till områdets inkommande A respektive U. Obalans ska utredas före beräkningen och får inte döljas genom normalisering. Definitionen gäller icke-negativa belopp med full avstämning för perioden.

```
L_r = |a_r - a_ref,r| + |u_r - u_ref,r|
D_B = sum_r L_r / (2E)
```

D_B ligger mellan 0 och 1. Noll betyder att båda komponenterna sammanfaller med referensen för samtliga mottagare på den angivna detaljnivån. När E är noll är D_B odefinierat.

För varje mottagarrelation med positivt tilldelat belopp eller referensbelopp ska även relationvärdet redovisas:

```
D_B,r = L_r / (a_r + u_r + a_ref,r + u_ref,r)
```

Även D_B,r ligger mellan 0 och 1. När nämnaren är noll är relationvärdet odefinierat. Mottagaren ska få tilldelade belopp, referensbelopp och skillnader i utsläppsenheten, med riktning och med faktisk respektive okänd del separat, samt uppgift om vilket område och vilken referens jämförelsen gäller.

D är ett avvikelsemått mot den angivna referensen. Ett högt värde avgör inte om en allokeringsnyckel som tillåts i §3 är felaktig. D med olika områden, referenser eller mottagarnivåer får inte jämföras som om jämförelsegrunden vore densamma. Måttet avser fördelningen inom området; det intygar inte att information har bevarats genom hela uppströmskedjan.

## Varför ett mått till?

Coverage visar hur stor andel av utsläppsunderlaget som har faktisk grund. Specifikationens §8 beskriver också en relevansdimension: ett bolagssnitt och en linjespecifik allokering kan båda ha Coverage 1, samtidigt som de ger olika stöd för kundens beslut. D föreslås mäta en avgränsad del av denna dimension, nämligen avvikelsen från en motiverad fördelning av samma uppströmsunderlag.

Detta svarar mot MASSIV+:s syfte att göra löpande inköps- och verksamhetsbeslut möjliga med data som praktiskt går att samla in. Ett högre Coverage ersätter inte behovet att bevara relevanta skillnader mellan inflöden. D kompletterar därför Coverage utan att bli ett allmänt betyg på all datakvalitet.

## Grundfallet och problemet med kundnoder

En grossist köper 100 ton material från vardera av två leverantörsflöden. De bär 40 respektive 200 ton CO2e, koldioxidekvivalenter. Kund X får materialet från det första flödet, kund Y från det andra. Grossistens egna utsläpp är 5 ton och delas lika. Alla uppströmsbelopp har här faktisk grund. Talen är påhittade.

En gemensam nod som fördelar efter materialets massa ger båda kunderna 122,5 ton. Om inflödena hålls isär får X 42,5 och Y 202,5 ton. Massnyckeln är ett exempel; §3 tillåter också andra dokumenterade proportionella nycklar.

Den tidigare D-formeln jämförde mottagarnas andelar inom varje enskild nod. En nod med bara en mottagare fick alltid noll. Två nybildade kundnoder kunde därför få D = 0 även om de först hade tilldelats samma utjämnade genomsnitt. Den föreslagna fasta avgränsningen fångar skillnaden:

| Beräkning inom samma område | X får totalt | Y får totalt | D_B | X:s D_B,r | Y:s D_B,r |
|---|---:|---:|---:|---:|---:|
| En nod, massnyckel | 122,5 | 122,5 | 0,333 | 0,500 | 0,250 |
| Två kundnoder med samma genomsnitt | 122,5 | 122,5 | 0,333 | 0,500 | 0,250 |
| Inflödenas fördelning bevaras | 42,5 | 202,5 | 0 | 0 | 0 |

D räknas på de externa 240 tonnen, medan tabellens totaler även innehåller de egna 5 tonnen. Enbart nya interna nodnamn ändrar inget D. En ändrad faktisk tilldelning kan göra det.

Mätområdet behöver inte vara hela bolaget. Om en nod utgör ett lämpligt stabilt område kan D_B vara den nodens D. Kunden behöver dessutom relationvärdet för sin del. Området och referensen ligger kvar när interna noder ritas om i en jämförelse.

## Ett lågt samlat D kan dölja kundens avvikelse

Anta att referensen ger X 8 och Y 360 ton CO2e. En massnyckel på 10/90 ger i stället X 36,8 och Y 331,2. Områdets D_B är cirka 0,078. X får ändå 28,8 ton mer än referensen, med D_B,r cirka 0,643. Y får 28,8 ton mindre, med D_B,r cirka 0,042.

Relationvärdet anger avvikelsens storlek med den föreslagna normaliseringen. Det betyder inte att 64,3 procent av X:s utsläpp är fel. Därför behövs även belopp och riktning.

De två nivåerna hänger ihop matematiskt. D_B är det viktade medelvärdet av relationvärdena, med vikten:

```
w_r = (a_r + u_r + a_ref,r + u_ref,r) / (2E)
```

Vikterna summerar till 1. Relationer där båda beloppen är noll har vikt noll och ingår inte med något relationvärde.

## A och U måste jämföras separat

Referensen kan ge X 100 ton A och Y 100 ton U. En gemensam nod ger i stället båda 50 A och 50 U. Båda får fortfarande totalt 100, så en jämförelse av enbart totalsummorna ger D = 0. Den föreslagna komponentvisa jämförelsen ger D_B = 0,5 och D_B,r = 0,5 för båda.

Områdets Coverage är 0,5 i båda fallen. Kundernas Coverage förändras från 1 respektive 0 till 0,5 för båda. Här visar D en förändring som områdets Coverage inte visar. U behåller sin innebörd som numeriskt underlag för det okända enligt §2. Ändrade U-underlag kan ändra D:s viktning och ska därför versionsanges.

## Samma kund kan behöva flera mottagarrelationer

Om X och Y i föregående exempel i stället är två leveransgrupper till samma kund är D_B fortfarande 0,5 när grupperna jämförs separat. Slås de ihop till en enda kundtotal sammanfaller utfall och referens och D_B blir noll.

Mottagarnivån är alltså en del av själva mätningen. Förslaget skyddar mot att enbart intern omindelning sänker D. Det gör inte D oberoende av hur externa mottagarrelationer avgränsas. Detaljnivån ska motsvara syftet och underlaget och anges för mottagaren.

## Referensvalet är ett redovisat metodval

I grundfallet följer referensen den kända kopplingen mellan inköp och kunder. Med intäkt som allokeringsnyckel och intäktsandelarna 60/40 får X 144 och Y 96 ton externt uppströmsunderlag. D_B mot den fysiskt baserade referensen 40/200 blir cirka 0,433.

Om en självständigt motiverad avtalsreferens i stället är 144/96 blir D_B noll med samma utfall. Det visar överensstämmelse med avtalsfördelningen. Exemplet visar referensens betydelse; det avgör inte vilken referens som är lämplig för en viss verksamhet.

En fysisk referens kan synliggöra att en intäktsnyckel ger mer utsläppsunderlag till en vara med prispåslag, även när dess uppströmsbelopp är lägre. Det gör konsekvensen synlig utan att upphäva §3:s metodval. D får därför ingen generell gräns för godkänt resultat i detta förslag.

För en grossist som redan har relevanta uppgifter om leverantör, artikelgrupp och leverans behöver de beaktas vid referensvalet. Ett grövre underlag kan vara motiverat av realistisk datainsats, men motiveringen ska framgå. Ett företag behöver inte kartlägga varje fysisk väg genom hela leveranskedjan för att börja använda måttet.

Vid fysisk blandning, exempelvis i ett elnät, kan en dokumenterad modell av relevanta samband användas om den kan motiveras för syftet. D anger då överensstämmelse med modellen. Om ingen motiverad referens kan tas fram redovisas D som ej beräknat. Det tidigare förslaget om en generell övre uppskattning utgår; en grov approximation är inte visad vara en övre gräns för alla tillåtna nycklar.

### Förhållandet till ISO:s allokeringsprinciper

Verksamhetsanpassning och motivering är användbara utgångspunkter för MASSIV+:s referensval. Den föreslagna regeln ska samtidigt bedömas på egna meriter. ISO 14044:s allokeringsprinciper innebär inte ett fritt val mellan likvärdiga nycklar. [JRC:s officiella LCA-vägledning](https://eplca.jrc.ec.europa.eu/uploads/ILCD-Handbook-General-guide-for-LCA-DETAILED-GUIDANCE-12March2010-ISBN-fin-v1.0-EN.pdf) beskriver en ordning där möjligheten att undvika allokering undersöks före fysiska och därefter andra samband. Den ordningen avser LCA-allokering. Detta förslag tillskriver inte ISO någon regel för D.

## Jämförbarhet och begränsningar

D mäter beloppsfördelningen inom det deklarerade området. Information kan redan ha jämnats ut hos leverantören. Två olika källfördelningar kan också ge samma A/U-belopp till kunderna. Ett lokalt D = 0 intygar därför varken källidentitet, framtida förbättringars fördelning eller hela kedjans upplösning.

Förslaget inför ingen regel för att propagera eller summera leverantörernas D. Mottagaren får uppgift om det område där måttet beräknats. Om en jämförelse behöver omfatta ett tidigare led krävs ett motsvarande avgränsat underlag och en referens för den jämförelsen.

Byte av referens, mätområde, mottagarnivå eller U-underlag kan påverka D utan att verksamhetens utsläpp ändrats. Versionskontroll och jämförelse på gemensam grund behövs därför även när D redovisas över tid. Nodindelningens stabilitet och redovisning av metodbyten behandlas vidare i MF-004.

## Prövade alternativ och beräkningskontroll

Den tidigare formeln per intern nod utgår eftersom en uppdelning i kundnoder kunde ge ett missvisande förbättringsresultat. Enbart ett företagsgemensamt D räcker heller inte, eftersom en liten kund kan påverkas mycket. Ett mått på enbart A + U missar utjämning av faktisk och okänd del. Den föreslagna konstruktionen hanterar dessa tre fall men kräver mer underlag än den vanliga utgående Actual/Unknown-summan.

Räknefallen kan reproduceras med [d-fast-avgransning.py](../assets/berakningar/d-fast-avgransning.py), som använder exakta bråk. Programmet kontrollerar balans, gränsvärden, viktningen av relationvärden, egenutsläppens avskiljning och invarians vid omindelning, inklusive 100 varierade fördelningar. Beräkningskontrollen verifierar formlernas egenskaper under de angivna villkoren; den avgör inte om en viss verksamhets referens är väl vald.

## Beslut

Inte behandlat. Förslaget avser ett nytt mått i §8; antagande kräver separat beslut.
