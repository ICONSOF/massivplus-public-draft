---
layout: default_banner
title: "MF-004 Vad som får vara en nod"
parent: "Förslag"
nav_order: 4
forslag_id: MF-004
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§1, §5"
forslag_forfattare: Birger Löfgren
forslag_diskussion: https://github.com/ICONSOF/massivplus-public-draft/discussions/62
---

# MF-004 Vad som får vara en nod

> **Status:** Utkast, 2026-10-30, reviderat 2026-11-04. Ingår inte i standarden. Berör §1 och §5. Författare: Birger Löfgren. Diskussion: [#62](https://github.com/ICONSOF/massivplus-public-draft/discussions/62).
>
> [MF-002](mf-002-utspadning.md) handlar om fördelningsmåttet D och [MF-005](mf-005-allokeringsposter.md) om vad organisationer lämnar till varandra. Förslagen kan bedömas vart för sig.

En nod samlar sina egna utsläpp och de utsläpp den tar emot från leverantörer, och fördelar summan vidare till sina mottagare ([specifikationen](../standard/specifikation.md) §1-4). Summan kallas T. Den del som har faktisk grund heter Actual när den skickas och A när den tagits emot. Den okända delen heter på samma sätt Unknown och U. Förslaget anger vilka delar av en verksamhet som får vara en nod. Bakgrunden är att en nod som samlar flera inflöden kan jämna ut skillnaderna mellan dem, så att kunden inte ser skillnaden mellan två inköp.

## Förslag till standardtext

### §1: komplettera definitionen av organisatorisk enhet

En nod kan vara en fysisk anläggning eller en avgränsad del av verksamheten, till exempel ett område för inköp och försäljning. Gränsen får dras med hjälp av uppgifter om leverantörer, kunder och artiklar, också när området har flera leverantörer. En nod ligger alltid inom en och samma organisation.

Utöver de fyra kraven i §1, heltäckning, ingen överlapp, intern konsistens och konsekvens över tid, gäller följande:

1. Organisationen ansvarar för noden och dokumenterar vilken verksamhet den omfattar, var gränsen går och hur den räknas.
2. Det ska finnas dokumenterade regler för vilka inköp, inkommande utsläpp, egna och delade utsläpp och utgående leveranser som hör till noden. Kopplingar som finns registrerade i verksamhetens system ska gå att skilja från kopplingar som är beräknade med en fördelningsnyckel. Om en inkommande post delas mellan noder ska delarna summera till postens hela Actual och hela Unknown, var för sig.
3. Varje egen utsläppskälla ska ingå i exakt en nod. En gemensam resurs får vara en egen nod enligt §1, Hantering av delade resurser. En nod får ha noll egna Scope 1+2 om den saknar egna utsläppskällor och de gemensamma resurserna ligger i andra noder.
4. Nodens hela T för perioden ska beräknas och fördelas med en dokumenterad proportionell regel enligt §2-4, med Actual och Unknown var för sig.
5. Nodens avgränsning ska versionshanteras. När indelningen ändras ska det redovisas vad som ändrats och hur det påverkar jämförelsen med tidigare perioder. Föregående period ska räknas om med den nya indelningen när underlaget räcker. Går det inte ska det redovisas, tillsammans med det som är känt om hur metodbytet påverkar talen.

### §5: ersätt stycket under Individuation av allokeringsenheten

En allokering mellan två noder ska gälla en affärsrelation som går att identifiera: vem som skickar, vem som tar emot, vilken period och vad den omfattar. Omfattningen kan vara en hel kundrelation, en leverans eller en grupp leveranser av en viss kvalitet. Artikeluppgifter får användas för att avgränsa omfattningen och avsändarens nod.

Det som deklareras ska vara en del av avsändarnodens T. Avsändaren bokför det som utgående och mottagaren samma Actual och Unknown som ingående. Mottagaren räknar in det i sin egen nod och räknar fram sin egen allokering enligt §2-4. Det gäller också när flera mottagare får samma tal per ton från samma nod.

Följer talet i stället med varan oförändrat vidare till mottagarens kunder är det en produktallokering. Reglerna i §5 om produktallokering vid leverans till en sänka gäller oförändrade.

## Syfte

MASSIV+ ligger mellan bolagstal, som är för grova för vissa beslut, och produktberäkningar, som kräver mer data än många verksamheter kan hålla uppdaterad ([introduktionen](../introduktion.md) och specifikationens syftesavsnitt). Nodindelningen ska ge underlag för konkreta beslut med en rimlig datainsats. Finast möjliga indelning är därför inget mål i sig.

## Bakgrund: när en nod jämnar ut skillnader mellan inflöden

I dialogen med bolag i MASSIV+ har vi sett en risk som behöver utredas: att en nod som samlar flera inflöden jämnar ut skillnaderna mellan dem. Skillnaden mellan två inköpsalternativ blir då mindre synlig när kunden väljer. Bolagen ser det i dag med EPD:er, miljövarudeklarationer, som visar att ett stål har lägre utsläpp än ett annat. Samma sak gäller när leverantörerna deklarerar enligt MASSIV+.

Risken gäller standardens syfte, att ge underlag för beslut. Två saker kan hända samtidigt: mer faktisk data höjer Coverage, medan en grövre fördelning gör det svårare att se skillnaden mellan två inköp. De två behöver prövas var för sig.

Förslaget utgår från ett handelsled, som en grossist, där nästan alla utsläpp kommer med det inköpta materialet. En verksamhet med stor egen produktionsenergi måste också fördela den energin mellan sina noder. Det kan göras på samma sätt som med hallen i exemplet, med en egen nod för energin och en nyckel som speglar hur mycket energi varje artikelgrupp kräver. Den frågan avgränsas från det här förslaget.

Exemplet nedan räknar med MASSIV+-deklarationer, alltså A, och jämför olika sätt att fördela samma inkommande utsläpp. Värden från EPD:er får användas för att skatta U enligt §2, och en finare nodindelning gör dem inte till A.

## Vad ett bolag känner till och vad det lämnar vidare

Varje bolag känner bara sina egna noder, på samma sätt som varje bolag bara känner sin egen bokföring ([bokföringsanalogin](../fordjupningar/bokforingsanalogin.md)). Bolaget vet hur det delat in sig i noder och vilka inköp som gått till vilka leveranser, i den mån det finns registrerat, till exempel i en stycklista. Leverantören ansvarar för sin egen indelning och för det den deklarerar. Kunden behöver inte se leverantörens noder.

Ett leverantörsbolag kan ha flera noder. Om en leverantör har en nod för ett sortiment med lägre utsläpp och en annan för ett med högre, och deklarerar dem var för sig, kan kunden hålla isär dem. Har kunden i stället en nod per **leverantörsbolag** blandas de två sortimenten i den noden innan de fördelas vidare. Det är där skillnaden jämnas ut.

På samma sätt behöver det vara klart vilken nod hos kunden som tar emot. En kund kan ta emot flera poster i olika egna noder eller samla dem i en. §5 tillåter redan flera leveransgrupper inom samma kundrelation. [MF-005](mf-005-allokeringsposter.md) beskriver hur avsändare och mottagare stämmer av samma post utan att visa sina interna nätverk.

## Ett genomräknat exempel

**Exemplet är hypotetiskt.** Grossisten, de två stålverken, Verkstaden och kund Y är påhittade, liksom inköpen, mängderna och utsläppen.

Exemplet prövar fyra frågor:

1. Jämnar nodindelningen ut skillnaden mellan inköpsalternativ?
2. Når en förändring rätt kund?
3. Hur fin kan indelningen vara, och vad kräver den av data?
4. Är Coverage och fördelning olika saker?

Grossisten köper två artikelgrupper från både Stålverk A och Stålverk B, här kallade grön och brun. Beteckningarna är bara etiketter. Exemplet bygger på fem antaganden:

1. Leverantörerna har var sin nod för grönt och brunt, alltså fyra noder, och deklarerar till Grossisten från var och en.
2. Leverantörerna deklarerar enligt MASSIV+, så allt Grossisten tar emot är A. Fallet där en del är okänd, U, kommer under fråga 4.
3. Grossisten vet hur mycket av varje inflöde som gått till Verkstaden och till kund Y.
4. Grossistens hall har 10 ton egna utsläpp, som ligger i en egen nod för den gemensamma resursen. Hallen fördelar dem till Grossistens övriga noder efter hur mycket material de hanterar.
5. Alla noder fördelar vidare efter vikt, med en massnyckel: varje mottagare får lika stor andel av utsläppen som av den levererade vikten. Andra dokumenterade proportionella nycklar är tillåtna enligt §3.

| Avsändande nod | Material till Grossisten, ton | Utsläpp, ton CO2e | Utsläpp per ton material | Verkstaden köper, ton | Kund Y köper, ton |
|---|---:|---:|---:|---:|---:|
| Stålverk A, grön grupp | 50 | 20 | 0,4 | 40 | 10 |
| Stålverk B, grön grupp | 50 | 40 | 0,8 | 40 | 10 |
| Stålverk A, brun grupp | 50 | 100 | 2,0 | 10 | 40 |
| Stålverk B, brun grupp | 50 | 120 | 2,4 | 10 | 40 |
| **Summa** | **200** | **280** | | **100** | **100** |

Verkstaden köper alltså mest grönt och kund Y mest brunt. Grossisten fördelar totalt 280 + 10 = 290 ton CO2e. Det som går mellan Grossistens egna noder, som hallens andel, räknas inte en gång till.

### 1. Jämnar nodindelningen ut skillnaden?

| Grossistens indelning | Verkstaden får, ton CO2e | Kund Y får, ton CO2e |
|---|---:|---:|
| En gemensam nod | 145 | 145 |
| En nod per leverantörsbolag | 145 | 145 |
| En nod per artikelgrupp | 97 | 193 |
| En nod per inkommande leverantörsnod | 97 | 193 |

Med en gemensam nod får kunderna hälften var, fast Verkstaden köper mest grönt. En nod per leverantörsbolag ger samma resultat. Noden för Stålverk A får 20 + 100 ton därifrån och 5 ton av hallens utsläpp, eftersom Stålverk A:s material är hälften av det hallen hanterar, totalt 125. Noden för Stålverk B får 40 + 120 + 5 = 165. Verkstaden köper hälften av varje leverantörs material och får 62,5 + 82,5 = 145. Grönt och brunt har blandats i leverantörsnoden, och skillnaden är borta.

En nod per artikelgrupp håller isär grönt och brunt. Det går här av två skäl. Leverantörerna deklarerar grönt och brunt var för sig, så utsläppen kommer in uppdelade. Och Grossisten vet vilka leveranser till kunderna som är gröna och vilka som är bruna, till exempel genom att inköpsartikeln går att knyta till försäljningsartikeln. Saknas något av det går det inte, vilket fråga 3 visar. Den gröna noden får 60 ton från leverantörerna och 5 ton av hallens utsläpp, totalt 65. Den bruna får 220 + 5 = 225. Verkstaden köper 80 procent av det gröna och 20 procent av det bruna och får 52 + 45 = 97. Kund Y får 13 + 180 = 193.

Nodindelningen avgör vilka inflöden som räknas ihop. Fördelningsnyckeln avgör sedan hur varje sådan summa delas mellan kunderna. Det är två olika steg, och det är i det första som skillnaden går förlorad.

### 2. Når en förändring rätt kund?

Anta att Verkstaden byter sina 20 ton brunt mot grönt, 10 ton från varje leverantör, medan kund Y köper som förut. Grossisten fördelar nu 258 ton, hallens utsläpp inräknade.

| Indelning | Verkstaden före | Verkstaden efter | Kund Y före | Kund Y efter |
|---|---:|---:|---:|---:|
| En gemensam nod | 145 | 129 | 145 | 129 |
| En nod per leverantörsbolag | 145 | 129 | 145 | 129 |
| En nod per artikelgrupp | 97 | 65 | 193 | 193 |

Med en gemensam nod eller en nod per leverantörsbolag får kund Y hälften av minskningen, fast Y inte har ändrat något. Med artikelgrupper hamnar hela minskningen, 32 ton, hos Verkstaden.

Samma sak gäller när en leverantör förbättrar sig. Om Stålverk A halverar utsläppen i sin gröna produktion, från 20 till 10 ton, ger en gemensam nod båda kunderna 5 ton mindre, 140 var. Med artikelgrupper får Verkstaden 8 ton mindre, 89, och kund Y 2 ton mindre, 191, i proportion till hur mycket grönt de köper.

### 3. Hur fin kan indelningen vara?

Artikelgrupperna håller isär grönt och brunt, men inte Stålverk A:s gröna stål från Stålverk B:s. Det spelar roll när leverantörerna inom en artikelgrupp skiljer sig åt, och i exemplet har Stålverk A:s gröna stål halva Stålverk B:s utsläpp per ton.

Anta att Verkstaden köper allt Stålverk A:s gröna, 50 ton, och 30 ton grönt från Stålverk B. Kund Y:s 20 ton grönt kommer då från Stålverk B. Varje kund köper lika mycket grönt och brunt som förut. Artikelgrupperna ger fortfarande 97 och 193, eftersom den gröna noden räknar Stålverk A och Stålverk B tillsammans. En nod per inkommande leverantörsnod ger 93 och 197. Att Verkstaden valt det gröna stålet med lägst utsläpp syns först när varje leverantörs gröna hålls isär.

Hur fin indelningen kan vara beror på vad leverantörerna deklarerar. Om Stålverk A och Stålverk B bara lämnar en total var, 120 och 160 ton, vet Grossisten inte hur den fördelar sig på grönt och brunt. Delar Grossisten upp totalerna på artikelgrupperna efter vikt blir resultatet 145 och 145, samma som med en gemensam nod. Fler grupper skapar inte information som saknas.

En nod per kund ger 97 och 193, men bara för att Grossisten redan vet vilket inflöde som gått till vilken kund. Det är den kunskapen som ger resultatet, inte kundnoden.

Där registrerade kopplingar saknas får mottagaren fördela med dokumenterade antaganden. Det ska framgå vilka kopplingar som är registrerade och vilka som är fördelade. Actual som mottagaren delar upp i sin bokföring förblir Actual, men uppdelningen är mottagarens egen och säger inget om vad avsändaren mätt. EPD-värden som används för att skatta U förblir U.

### 4. Är Coverage och fördelning olika saker?

I grundfallet deklarerar båda leverantörerna enligt MASSIV+, och allt Grossisten fördelar har faktisk grund: Coverage är 1. Ändå får kunderna 145 var med en gemensam nod. Om Stålverk B i stället inte deklarerar skattar Grossisten Stålverk B:s utsläpp som U, med samma tal som förut, och Coverage sjunker till cirka 0,45. Med artikelgrupper får kunderna ändå 97 och 193, precis som när allt var känt.

| Fall | Coverage för Grossisten | Verkstaden får, ton CO2e | Kund Y får, ton CO2e |
|---|---:|---:|---:|
| Båda leverantörerna deklarerar, en gemensam nod | 1 | 145 | 145 |
| Stålverk B deklarerar inte, en nod per artikelgrupp | 0,45 | 97 | 193 |

Hög Coverage hindrar alltså inte att skillnaden jämnas ut, och låg Coverage hindrar inte att den bevaras. Coverage visar hur stor del som har faktisk grund. Indelningen avgör om skillnaderna mellan inflödena följer med till kunderna. [MF-002](mf-002-utspadning.md) föreslår ett mått, D, för det andra: hur mycket fördelningen avviker från en motiverad referens.

## Hur långt mot produkten?

Med en nod per artikelgrupp får Verkstaden i exemplet utsläpp från den gröna noden för det gröna stål Verkstaden har köpt. Det liknar ett tal per produkt, men det är Grossistens utsläpp under perioden, fördelade på det Verkstaden köpt. Talet följer med leveransen till Verkstaden, och att det motsvarar just det gröna stålet beror på att noden bara innehåller grönt. Längre än så följer det inte stålet. Verkstaden räknar in talet i sin egen nod, lägger till sina egna utsläpp och fördelar vidare, så Verkstadens kunder får Verkstadens tal och inte Grossistens. Det är vad introduktionen menar med att enheten är [affärsrelationens avtryck under en period](../introduktion.md#en-fråga-att-ta-med-sig).

En allokering kan gälla så lite som en enskild leverans av en viss kvalitet till en viss kund. Talet blir ändå aldrig finare än noden det kommer från, och hur fin noden kan vara begränsas i praktiken av tre saker: vad leverantörerna deklarerar (fråga 3 i exemplet), om de egna utsläppen går att knyta till noden, och att indelningen ska gå att dokumentera och behålla från period till period. En nod för en enda leverans klarar sällan det sista.

Talet från den gröna noden blir lika träffsäkert som ett tal per produkt om noden inte blandar grönt med brunt, om den egna energin går att knyta till det gröna, och om stålet levereras samma period som det köps in ([produktnivåinvändningen](../fordjupningar/produktniva-invandningen.md)).

Det blir en produktallokering först om talet följer med varan oförändrat, så att Verkstadens kunder får samma tal per ton som Grossisten räknade fram. Enligt §5 i dag är det tillåtet bara vid leverans till en sänka, till exempel en privatperson. Det här förslaget ändrar inte den regeln.

Förslaget ändrar hur §5 skiljer en allokering till en mottagare från en produktallokering. I dag ska talet variera med motparten och inte med varan. Men i exemplet får Verkstaden och kund Y samma tal per ton grönt stål, eftersom båda köper från samma gröna nod. Det är ändå ingen produktallokering, för båda räknar in talet i sina egna noder. Därför prövar förslaget vad mottagaren gör med talet i stället för om talet är lika för alla.

## Stabilitet över tid

En nod bör avgränsas så att den går att behålla från period till period. Om leverantörer, inköpsvolymer eller kunder ändras men noden avgränsas på samma sätt, till exempel att den gröna noden fortfarande omfattar allt grönt stål, är det ingen ny nodindelning. Om avgränsningen ändras ska ändringen versionshanteras och jämförbarheten bedömas.

Föregående period kan räknas om med den nya indelningen när underlaget finns. Annars ska det synas vad metodbytet kan ha påverkat och var jämförelsen brister. Ett sjunkande utsläppstal eller D får inte tolkas som att verksamheten förbättrats utan en sådan bedömning.

Förslaget låter organisationen välja en indelning som stöder dess beslut och som den kan hålla uppdaterad med den data som finns. Det kräver dokumentation, full täckning och avstämning även för noder som är en del av verksamheten och inte en egen anläggning. En finare indelning kan bevara viktiga skillnader men kostar mer att förvalta, och den sänker inte i sig utsläppen.

## Alternativ och beräkningskontroll

Tre andra regler har prövats:

1. Bara fysiska anläggningar som noder. Det är enkelt, men kan jämna ut skillnader i inköp som redan går att följa.
2. Förbud mot att använda artikelinformation. Det skulle också utesluta delar av verksamheten vars flöden går att följa i bokföringen.
3. Krav på finast möjliga indelning. Det skulle ta bort användarens avvägning mot datainsatsen.

Förslaget ställer i stället dokumenterade krav på vad noden ska klara.

[mf-004-nodindelning.py](../assets/berakningar/mf-004-nodindelning.py) räknar om alla exemplen med exakta bråk. Skriptet kontrollerar att inflöden och utflöden stämmer, att totalen och U går ihop och de viktigaste jämförelserna, för fem scenarier och sex indelningar och för fallet med U. Exemplen visar hur fördelningen påverkas under de angivna antagandena. De visar inte vilken indelning som passar ett visst bolag bäst.

## Beslut

Inte behandlat. Den föreslagna standardtexten ändrar §1 och §5 och kräver ett eget beslut.
