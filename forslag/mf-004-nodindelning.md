---
layout: default_banner
title: "MF-004 Nodindelning och interna beräkningsenheter"
parent: "Förslag"
nav_order: 4
forslag_id: MF-004
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§1, §5"
forslag_forfattare: Birger Löfgren
forslag_diskussion: https://github.com/ICONSOF/massivplus-public-draft/discussions/62
---

# MF-004 Nodindelning och interna beräkningsenheter

> **Status:** Utkast, 2026-10-30, språket förenklat 2026-11-04. Ingår inte i standarden. Berör §1 och §5. Författare: Birger Löfgren. Diskussion: [#62](https://github.com/ICONSOF/massivplus-public-draft/discussions/62).
>
> Förslaget tar över nodreglerna som tidigare låg i MF-002. [MF-002](mf-002-utspadning.md) handlar nu om fördelningsmåttet D och [MF-005](mf-005-allokeringsposter.md) om vad organisationer lämnar till varandra. Förslagen kan bedömas vart för sig.

En nod samlar sina egna utsläpp och de utsläpp den tar emot från leverantörer, och fördelar summan vidare till sina mottagare ([specifikationen](../standard/specifikation.md) §1-4). Summan kallas T. Den del som har faktisk grund heter Actual när den skickas och A när den tagits emot. Den okända delen heter på samma sätt Unknown och U. Förslaget anger vilka delar av en verksamhet som får vara en nod.

## Förslag till standardtext

### §1: komplettera definitionen av organisatorisk enhet

En nod är en dokumenterad beräkningsenhet som tillhör en rapporteringsentitet. Den kan vara en fysisk anläggning eller en tydligt avgränsad del av verksamheten, till exempel ett område för inköp och försäljning. Gränsen får dras med hjälp av uppgifter om leverantörer, kunder och artiklar, också när området har flera leverantörer.

Utöver de fyra kraven i §1, heltäckning, ingen överlapp, intern konsistens och konsekvens över tid, gäller följande:

1. Rapporteringsentiteten ansvarar för noden och dokumenterar vilken verksamhet den omfattar, var gränsen går och hur den räknas.
2. Det ska finnas dokumenterade regler för vilka inköp, inkommande utsläpp, egna och delade utsläpp och utgående leveranser som hör till noden. Kopplingar som finns registrerade i verksamhetens system ska gå att skilja från kopplingar som är beräknade med en fördelningsnyckel. Om en inkommande post delas mellan noder ska delarna summera till postens hela Actual och hela Unknown, var för sig.
3. Varje egen utsläppskälla ska ingå i exakt en nod. En gemensam resurs får vara en egen nod enligt §1, Hantering av delade resurser. En nod får ha noll egna Scope 1+2 om den saknar egna utsläppskällor och de gemensamma resurserna ligger i andra noder.
4. Nodens hela T för perioden ska beräknas och fördelas med en dokumenterad proportionell regel enligt §2-4, med Actual och Unknown var för sig.
5. Nodens definition ska versionshanteras. När indelningen ändras ska det redovisas vad som ändrats och hur det påverkar jämförelsen med tidigare perioder. Föregående period ska räknas om med den nya indelningen när underlaget räcker. Går det inte ska det redovisas, tillsammans med det som är känt om hur metodbytet påverkar talen.

En grupp blir en nod när den uppfyller kraven ovan som en del av rapporteringsentitetens verksamhet. Ett namn eller en beteckning räcker inte. Ett artikelnummer som flera organisationer använder gör dem inte till en gemensam nod.

### §5: ersätt stycket under Individuation av allokeringsenheten

En allokering mellan två noder ska gälla en affärsrelation som går att identifiera: vem som skickar, vem som tar emot, vilken period och vad den omfattar. Omfattningen kan vara en hel kundrelation, en leverans eller en grupp leveranser av en viss kvalitet. Artikeluppgifter får användas för att avgränsa omfattningen och avsändarens nod.

Det som deklareras ska vara en del av avsändarnodens T och ska gå att stämma av mot avsändarens beräkning. Mottagaren bokför det och räknar sedan fram sin egen nods allokering enligt §2-4. Ett värde per artikel som följer med varan oförändrat, oavsett hur mottagaren räknar, är en produktallokering. Produktallokering är som tidigare tillåten bara vid terminering mot en sänka, enligt reglerna ovan i §5.

Om en allokering är en produktallokering avgörs av vem som ansvarar för den, vilken period och omfattning den gäller, om den kan stämmas av och om mottagaren räknar vidare med den. Att flera mottagare får samma kvot per ton avgör det inte.

## Syftet med avgränsningen

MASSIV+ ligger mellan bolagstal, som är för grova för vissa beslut, och produktberäkningar, som kräver mer data än många verksamheter kan hålla uppdaterad ([introduktionen](../introduktion.md) och specifikationens syftesavsnitt). Nodindelningen ska ge underlag för konkreta beslut med en rimlig datainsats. Finast möjliga indelning är därför inget mål i sig.

Det tidigare utkastet av MF-002 sa att en nod skulle avgränsas av motpart eller fysisk enhet, aldrig av godset. Det här förslaget ersätter den regeln med krav som går att pröva, både på noden och på det som deklareras till nästa led. Det är ett förslag till ändring av §1 och §5, inte en tolkning av texten som redan gäller.

## Bakgrund: Helens Rör och de EPD:er som redan finns

I dialogen med Helens Rör och andra bolag har vi sett en risk som behöver utredas: att MASSIV+ jämnar ut skillnader som bolaget redan kan visa sina kunder med EPD:er, miljövarudeklarationer. Skillnaden mellan två inköpsalternativ skulle då bli mindre synlig när kunden väljer. Det är en synpunkt från bolagen, inte resultatet av en mätning.

Risken gäller standardens syfte, att ge underlag för beslut. Två saker kan hända samtidigt: mer faktisk data höjer Coverage, medan en grövre fördelning gör det svårare att se skillnaden mellan två inköp. De två behöver prövas var för sig.

Värden från EPD:er får som tidigare användas för att skatta U (§2). En finare nodindelning gör dem inte till A, eftersom A kräver en MASSIV+-deklaration från leverantören. Exemplet nedan jämför olika sätt att fördela samma inkommande utsläpp. Hur en EPD:s tal förhåller sig till en MASSIV+-deklaration prövas inte här.

## Vad ett bolag känner till och vad det lämnar vidare

Varje bolag känner bara sina egna noder, på samma sätt som varje bolag bara känner sin egen bokföring ([bokföringsanalogin](../fordjupningar/bokforingsanalogin.md)). Bolaget vet hur det delat in sig i noder och vilka inköp som gått till vilka leveranser, i den mån det finns registrerat, till exempel i en stycklista. Leverantören ansvarar för sin egen indelning och för det den deklarerar. Kunden behöver inte se leverantörens noder.

Ett leverantörsbolag kan ha flera noder. Om Ovako har en nod för ett sortiment med lägre utsläpp och en annan för ett med högre, och deklarerar dem var för sig, kan Helens hålla isär dem. Har Helens i stället en nod per **leverantörsbolag** blandas Ovakos två sortiment i den noden innan de fördelas vidare. Det är där skillnaden jämnas ut.

På samma sätt behöver det vara klart vilken nod hos kunden som tar emot. En kund kan ta emot flera poster i olika egna noder eller samla dem i en. §5 tillåter redan flera leveransgrupper inom samma kundrelation. [MF-005](mf-005-allokeringsposter.md) beskriver hur avsändare och mottagare stämmer av samma post utan att visa sina interna nätverk.

## Ett genomräknat exempel

Helens köper två artikelgrupper från både Ovako och SSAB, här kallade grön och brun. Namnen är bara etiketter, inga certifieringar eller påståenden om bolagens verkliga sortiment. **Alla mängder och utsläppstal är påhittade.**

Exemplet bygger på fem antaganden:

1. Leverantörerna har var sin nod för grönt och brunt, alltså fyra noder, och deklarerar till Helens från var och en.
2. Alla deklarerade utsläpp har faktisk grund. Fallet med en okänd del kommer längre ned.
3. Helens vet hur mycket av varje inflöde som gått till Sandvik och till kund Y.
4. Hallens egna utsläpp, 10 ton, ligger i en egen nod för den gemensamma resursen. Hallen fördelar dem till Helens övriga noder efter hur mycket material de hanterar.
5. Alla noder fördelar vidare efter vikt, med en massnyckel: varje mottagare får lika stor andel av utsläppen som av den levererade vikten. Andra dokumenterade proportionella nycklar är tillåtna enligt §3.

| Avsändande nod | Material till Helens, ton | Utsläpp, ton CO2e | Sandvik köper, ton | Kund Y köper, ton |
|---|---:|---:|---:|---:|
| Ovako, grön grupp | 40 | 16 | 32 | 8 |
| SSAB, grön grupp | 60 | 48 | 48 | 12 |
| Ovako, brun grupp | 60 | 120 | 12 | 48 |
| SSAB, brun grupp | 40 | 96 | 8 | 32 |
| **Summa** | **200** | **280** | **100** | **100** |

Helens fördelar totalt 280 + 10 = 290 ton CO2e. Det som går mellan Helens egna noder, som hallens andel, räknas inte en gång till.

### Samma total, olika fördelning

| Helens interna indelning | Sandvik får, ton CO2e | Kund Y får, ton CO2e |
|---|---:|---:|
| En gemensam nod | 145,00 | 145,00 |
| En nod per leverantörsbolag | 145,48 | 144,52 |
| En nod per inkommande leverantörsnod | 99,40 | 190,60 |
| En nod per artikelgrupp över båda leverantörerna | 99,40 | 190,60 |
| En nod per leverantörsbolag och artikelgrupp | 99,40 | 190,60 |
| En nod per kund, med den kända inflödesfördelningen | 99,40 | 190,60 |

Med en nod per leverantörsbolag får Ovakos nod 141 ton (16 + 120 + 5 från hallen) och SSAB:s 149. Sandvik köper 44 procent av Ovakos material och 56 procent av SSAB:s och får 62,04 + 83,44 = 145,48. Kunderna får nästan lika mycket, eftersom grönt och brunt redan har blandats i varje leverantörsnod.

En nod per artikelgrupp betyder att Helens räknar alla gröna inköp och leveranser i en nod, från både Ovako och SSAB, och alla bruna i en annan. Den gröna noden får 69 ton inklusive sin del av hallen, den bruna 221. Sandvik köper 80 procent av det gröna och 20 procent av det bruna och får 55,2 + 44,2 = 99,4 ton. Kund Y får resten.

Totalen, 290 ton, är det Helens fördelar vidare. Nodindelningen avgör vilka inflöden som räknas ihop. Fördelningsnyckeln avgör sedan hur varje sådan summa delas mellan kunderna. Det är två olika steg.

En nod per kund ger samma resultat som de finare indelningarna, men bara för att Helens använder vetskapen om vilket inflöde som gått till vilken kund när kundnoderna fylls. Får båda kundnoderna i stället ett genomsnitt blir resultatet ett genomsnitt. En kund som köper både grönt och brunt får dessutom en enda summa, om leveranserna inte delas i grupper.

### När kunden ändrar sitt inköp

Anta att Sandvik byter sina 20 ton brunt mot grönt från samma leverantörer, medan kund Y köper som förut. Utsläppen per ton i varje inflöde är desamma som i grundfallet. Helens fördelar nu 258 ton, hallen inräknad.

| Indelning | Sandvik före | Sandvik efter | Kund Y före | Kund Y efter |
|---|---:|---:|---:|---:|
| En gemensam nod | 145,00 | 129,00 | 145,00 | 129,00 |
| Per leverantörsbolag | 145,48 | 129,86 | 144,52 | 128,14 |
| Per artikelgrupp | 99,40 | 67,67 | 190,60 | 190,33 |
| Per inkommande leverantörsnod | 99,40 | 67,40 | 190,60 | 190,60 |

En grov indelning ger också kund Y en del av minskningen, fast Y inte ändrat något. Med artikelgrupper hamnar nästan hela minskningen hos Sandvik. Att Sandvik får 67,67 i stället för 67,40 beror på att den gröna gruppen fortfarande blandar Ovako och SSAB.

### När leverantören förbättrar sig eller byts ut

Anta i stället att Ovakos gröna produktion halverar sina utsläpp, från 16 till 8 ton. Helens fördelar då 282 ton. En gemensam nod ger 141 ton till var och en av kunderna. Artikelgrupper eller separata inkommande noder ger Sandvik 93 och Y 189. Vem som får del av förbättringen beror alltså på indelningen.

Anta sedan att 20 ton av det gröna köps från Ovako i stället för från SSAB. Utsläppen per ton är oförändrade, och varje grönt inflöde går som förut till 80 procent till Sandvik och 20 procent till Y. Totalen blir också då 282. Artikelgrupperna ger åter 93 och 189, medan en nod per leverantörsbolag ger 141 till var och en. Att totalen sjunker säger alltså inte vem som får del av minskningen.

### Artikelgrupper bevarar inte alla skillnader mellan leverantörer

I grundfallet köper Sandvik 32 ton grönt från Ovako och 48 från SSAB. Anta i stället att Sandvik köper 40 från vardera och att kund Y:s 20 ton grönt kommer helt från SSAB. Varje kund köper lika mycket grönt och brunt som förut, och leverantörerna levererar lika mycket totalt.

Artikelgrupperna ger fortfarande 99,4 och 190,6 ton, medan separata inkommande noder ger 96,2 och 193,8. En nod som samlar flera leverantörer kan alltså hålla isär grönt och brunt men jämna ut skillnaden mellan leverantörerna inom samma grupp.

## Vad som går att göra med den data som finns

Vilken indelning som går att använda beror på tre slags data: om leverantörerna deklarerar sina delar var för sig, vilka kopplingar mellan inköp och leveranser Helens själv har registrerat, och underlaget för egna och gemensamma resurser. De behöver bedömas tillsammans.

Om Ovako bara lämnar en total på 136 ton och SSAB en på 144 kan Helens dela upp dem internt. Men då har leverantörerna inte deklarerat grönt och brunt var för sig. Fördelar Helens bolagstotalerna på artikelgrupperna efter vikt blir resultatet 145,48 till Sandvik och 144,52 till Y, samma som med en nod per leverantörsbolag. Fler grupper skapar inte information som saknas.

Där registrerade kopplingar saknas får mottagaren fördela med dokumenterade antaganden. Det ska framgå vilka kopplingar som är registrerade och vilka som är fördelade. Actual som mottagaren delar upp i sin bokföring förblir Actual, men uppdelningen är mottagarens egen och säger inget om vad avsändaren mätt. EPD-värden som används för att skatta U förblir U.

Olika delar av beräkningen kan ha olika detaljnivå. Hallens utsläpp kan fördelas från en egen nod samtidigt som leverantörernas inflöden hålls isär.

## Coverage och fördelningsnyckeln visar annat

Anta att SSAB:s utsläpp i grundfallet är okända, alltså U, medan Ovakos och hallens har faktisk grund. Med artikelgrupper får Sandvik då 41,8 ton Actual och 57,6 ton Unknown, Coverage cirka 0,421. Y får 104,2 Actual och 86,4 Unknown, Coverage cirka 0,547. Samma fördelning av T kan alltså ge mottagarna olika andel faktisk data.

Valet av nyckel påverkar också resultatet. Om allt ligger i en nod och grönt kostar dubbelt så mycket per ton som brunt står Sandvik för 60 procent av Helens intäkt. En intäktsnyckel ger då Sandvik 174 ton och Y 116, i stället för massnyckelns 145 och 145. Båda nycklarna är tillåtna enligt §3.

D-måttet i [MF-002](mf-002-utspadning.md) är tänkt att visa hur mycket fördelningen avviker från en motiverad referens. Nodkraven gäller oavsett vad D visar.

## Var gränsen mot produktallokering går

En artikelgrupp hos Helens gör det möjligt att räkna fram periodens utsläpp för en avgränsad del av verksamheten. Gruppen kan ha en egen inköpsansvarig, egna inflöden i bokföringen, egna kundrelationer och en dokumenterad andel av de gemensamma resurserna. Den behöver varken egen chef eller egen elmätare.

Om gruppen har en eller två leverantörer ändrar inte vad den är, och båda fallen bedöms efter samma krav. De kan däremot ge olika underlag för beslut, som räknefallen visar.

§5 säger i dag att talet ska variera med motparten och inte med varan. Men en produktionslinje, som enligt §1 får vara en nod, kan tillverka en enda artikel. Med massnyckel får då alla linjens kunder samma kvot per ton. Att talen är lika kan därför inte ensamt avgöra om det är en produktallokering.

Förslaget drar i stället gränsen vid vad som deklareras och hur det används. En leverantör deklarerar en bestämd mängd utsläpp till en verklig mottagare, för en viss omfattning och period. Mottagaren räknar in den i sin nod och fördelar sedan nodens hela T vidare. Ett värde per artikel som följer med varan oförändrat fungerar på ett annat sätt.

## Stabilitet över tid

En grupp bör avgränsas så att den går att behålla från period till period. Om leverantörer, inköpsvolymer eller kundmix ändras inom samma definition är det ingen ny nodindelning. Om definitionen ändras ska ändringen versionshanteras och jämförbarheten bedömas.

Föregående period kan räknas om med den nya indelningen när underlaget finns. Annars ska det synas vad metodbytet kan ha påverkat och var jämförelsen brister. Ett sjunkande utsläppstal eller D får inte tolkas som att verksamheten förbättrats utan en sådan bedömning.

Förslaget låter organisationen välja en indelning som stöder dess beslut och som den kan hålla uppdaterad med den data som finns. Det kräver dokumentation, full täckning och avstämning även för interna grupper. En finare indelning kan bevara viktiga skillnader men kostar mer att förvalta, och den sänker inte i sig utsläppen.

## Alternativ och beräkningskontroll

Tre andra regler har prövats:

1. Bara fysiska anläggningar som noder. Det är enkelt, men kan jämna ut skillnader i inköp som redan går att följa.
2. Förbud mot att använda artikelinformation. Det skulle också utesluta verksamhetsgrupper vars flöden går att följa i bokföringen.
3. Krav på finast möjliga indelning. Det skulle ta bort användarens avvägning mot datainsatsen.

Förslaget ställer i stället dokumenterade krav på vad noden ska klara.

[helens-nodindelning.py](../assets/berakningar/helens-nodindelning.py) räknar om alla exemplen med exakta bråk. Skriptet kontrollerar att inflöden och utflöden stämmer, att totalen och U går ihop och de viktigaste jämförelserna, för sex scenarier och sex indelningar och för fallen med U och intäktsnyckel. Exemplen visar hur fördelningen påverkas under de angivna antagandena. De visar inte vilken indelning som passar ett visst bolag bäst.

## Beslut

Inte behandlat. Den föreslagna standardtexten ändrar §1 och §5 och kräver ett eget beslut.
