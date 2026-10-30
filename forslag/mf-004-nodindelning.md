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

> **Status:** Utkast, 2026-10-30. Ingår inte i standarden. Berör §1 och §5. Författare: Birger Löfgren. Diskussion: [#62](https://github.com/ICONSOF/massivplus-public-draft/discussions/62).
>
> Förslaget utvecklar nodregler som tidigare låg i MF-002. [MF-002](mf-002-utspadning.md) behandlar nu fördelningsmåttet D och [MF-005](mf-005-allokeringsposter.md) informationsutbytet mellan organisationer. Varje förslag kan bedömas separat.

En nod är enligt [specifikationen](../standard/specifikation.md) en enhet som samlar egna och inkommande utsläppsbelopp och fördelar dem vidare. T betecknar nodens hela belopp. Actual är den faktiska delen i en utgående allokering och Unknown den okända delen. Hos mottagaren blir de A respektive U. Förslaget nedan preciserar vilka verksamhetsdelar som får utgöra sådana enheter.

## Förslag till standardtext

### §1: komplettera definitionen av organisatorisk enhet

En nod är en dokumenterad beräkningsenhet inom en ansvarig rapporteringsentitet. Enheten kan motsvara en fysisk anläggning eller en konsekvent avgränsad del av organisationens verksamhet, exempelvis ett inköps- och försäljningsområde. Leverantörs-, kund- och artikelinformation får användas vid avgränsningen, även när verksamhetsområdet omfattar flera leverantörer.

För en sådan enhet gäller följande, tillsammans med kraven på heltäckning, ingen överlapp, intern konsistens och konsekvens över tid:

1. Rapporteringsentiteten ansvarar för enheten och dokumenterar dess verksamhet, gräns och beräkningsregler.
2. Inköp, inkommande utsläppsunderlag, egna och delade utsläpp samt utgående leveranser ska kunna hänföras enligt dokumenterade regler. Registrerade samband ska kunna skiljas från fördelningar med nyckel. En uppdelad inkommande post ska stämmas av till postens hela Actual och Unknown var för sig.
3. Varje egen utsläppskälla ska ingå i exakt en nod. Gemensamma resurser får hanteras genom en nod för delad resurs. En mottagande beräkningsnod får ha noll egna Scope 1+2 när dess egna utsläppskällor saknas och de gemensamma resurserna är täckta av partitionen.
4. Nodens hela utsläppsmassa för perioden ska beräknas och allokeras med en dokumenterad proportionell regel enligt §2-4, med faktisk och okänd del separat.
5. Nodens definition och förändringar ska versionshanteras. Vid ändrad indelning ska ändringen och dess betydelse för jämförbarheten redovisas. Föregående period ska räknas om till gemensam grund när underlaget medger detta. Om omräkning inte är möjlig ska begränsningen och tillgängliga uppgifter om metodeffekten redovisas.

Att en grupp fått en viss beteckning är inte tillräckligt för att den ska utgöra en nod. Gruppen ska uppfylla kraven ovan som del av rapporteringsentitetens verksamhet. En gemensam artikelbeteckning över flera organisationer bildar inte i sig en gemensam nod.

### §5: ersätt stycket under Individuation av allokeringsenheten

En allokering i ett nod-till-nod-flöde ska avse en identifierbar affärsrelation mellan ansvarig avsändare och mottagare, för en angiven period och en definierad omfattning. Omfattningen får vara exempelvis en kundrelation, en leverans eller en grupp leveranser med viss kvalitet. Artikelinformation får användas för att definiera omfattningen och den interna beräkningsenheten.

Det deklarerade beloppet ska vara en avstämningsbar tilldelning av den avsändande nodens beräknade utsläppsmassa till mottagaren. Mottagaren bokför beloppet och beräknar sin egen nods fortsatta allokering enligt §2-4. Ett fristående artikelvärde som tillskrivs varan och förs vidare som samma egenskap oberoende av mottagarens beräkning är en produktallokering. Produktupplösning vid terminering mot sänka följer fortsatt reglerna ovan i §5.

Lika beräknade kvoter för olika mottagare avgör inte i sig om allokeringen är en produktallokering. Avsändaransvar, period, omfattning, avstämning och användning i nästa leds beräkning ska vara bestämmande.

## Syftet med avgränsningen

[Introduktionen](../introduktion.md) och specifikationens syftesavsnitt placerar MASSIV+ mellan bolagsdata som är för grov för vissa beslut och produktberäkningar som kräver mer data än många verksamheter kan upprätthålla. Nodindelningen ska ge stöd för konkreta åtgärder med en realistisk datainsats. Den finaste möjliga indelningen är därför inget självändamål.

Det tidigare MF-002-utkastet föreslog att en nod skulle avgränsas av motpart eller fysisk enhet, aldrig av godset. Detta förslag ersätter den begränsningen med prövbara krav på den interna beräkningsenheten och på den deklaration som lämnas till nästa led. Det är en föreslagen ändring och precisering av §1 och §5, inte en redan fastställd tolkning.

## Bakgrund: Helens rör och befintlig beslutsinformation

Helens rör har i dialog, återgiven av förslagsställaren, uttryckt oro för att en tillämpning av MASSIV+ skulle jämna ut bättre uppgifter som bolaget redan kan ge sina kunder med hjälp av EPD:er, miljövarudeklarationer. Oron gäller att skillnaden mellan inköpsalternativ skulle bli mindre användbar i kundens beslut. Detta är en återgiven intressentsynpunkt, ingen verifierad mätning av en faktisk tillämpning.

Invändningen är relevant för standardens syfte. Mer faktisk data kan ge högre Coverage samtidigt som en grövre fördelning försämrar stödet för ett visst inköpsbeslut. De två egenskaperna behöver prövas var för sig.

EPD-tal får fortsatt användas som U-underlag enligt §2. De blir inte A genom en finare nodindelning. A förutsätter ansvarig leverantörs MASSIV+-deklaration. Prövningen nedan jämför olika fördelningar av samma inkommande underlag. En jämförelse av totalsummorna i en EPD och en MASSIV+-deklaration kräver en separat analys av omfattning och metod.

## Vad ett bolag känner till och vad som lämnas vidare

Bolaget känner sin egen nodindelning och de kopplingar mellan inköp, interna beräkningar och kundernas leveranser som det faktiskt har registrerat. Leverantören ansvarar för sin egen indelning och för de allokeringar den lämnar. Hela leverantörens nätverk behöver inte vara synligt för kunden.

Ett leverantörsbolag kan ha flera noder. Om Ovako redan deklarerar separata mängder från en nod för ett sortiment med lägre utsläpp och en annan nod för ett sortiment med högre utsläpp kan Helens hålla posterna isär. En egen Helens-nod per **leverantörsbolag** skulle däremot samla båda posterna innan de fördelas vidare. Det är i det senare steget skillnaden kan jämnas ut. Leverantörsnoder blandar alltså inte generellt samma leverantörs olika leveranser.

Även kopplingen till mottagarens nod behöver vara entydig. En kund kan ta emot flera poster till olika egna noder eller samla dem i samma nod. Flera leveransgrupper inom en kundrelation är möjliga enligt §5. [MF-005](mf-005-allokeringsposter.md) preciserar hur samma post kan stämmas av utan att hela det interna nätverket lämnas ut.

## Ett genomräknat exempel

Anta att Helens köper två artikelgrupper från Ovako och SSAB. I exemplet kallas grupperna grön och brun för att hålla isär alternativen. Beteckningarna är inga certifieringar eller påståenden om bolagens faktiska sortiment. **Alla mängder och utsläppstal är påhittade.**

Leverantörerna antas ha fyra separata avsändande noder och deklarera följande mängder till Helens. Alla belopp har i grundfallet faktisk grund. Underlaget innehåller också kopplingen till kundernas inköp:

| Avsändande nod | Material till Helens, ton | Uppströmsbelopp, ton CO2e | Sandvik köper, ton | Kund Y köper, ton |
|---|---:|---:|---:|---:|
| Ovako, grön grupp | 40 | 16 | 32 | 8 |
| SSAB, grön grupp | 60 | 48 | 48 | 12 |
| Ovako, brun grupp | 60 | 120 | 12 | 48 |
| SSAB, brun grupp | 40 | 96 | 8 | 32 |
| **Summa** | **200** | **280** | **100** | **100** |

Helens hall har 10 ton egna utsläpp i en separat nod för delad resurs. Hallen fördelar dem till verksamhetens mottagande noder efter hanterad materialmassa. De noderna fördelar sedan hela sitt T vidare efter levererad massa. Egna och inkommande utsläpp räknas därmed en gång vid områdets externa gräns: 280 + 10 = 290 ton. Interna överföringar adderas inte ännu en gång till detta totalbelopp.

Med en **massnyckel** får varje mottagare samma andel av utsläppsbeloppet som dess andel av den levererade vikten. Andra dokumenterade proportionella nycklar är fortsatt tillåtna enligt §3.

### Samma total, olika fördelning

| Helens interna indelning | Sandvik får, ton CO2e | Kund Y får, ton CO2e |
|---|---:|---:|
| En gemensam nod | 145,00 | 145,00 |
| En nod per leverantörsbolag | 145,48 | 144,52 |
| En nod per inkommande leverantörsnod | 99,40 | 190,60 |
| En nod per artikelgrupp över båda leverantörerna | 99,40 | 190,60 |
| En nod per leverantörsbolag och artikelgrupp | 99,40 | 190,60 |
| En nod per kund, med den kända inflödesfördelningen | 99,40 | 190,60 |

En nod per artikelgrupp betyder här att Helens räknar alla sina inköp och leveranser i den gröna gruppen tillsammans i en egen beräkningsenhet. Både Ovako och SSAB ingår. Den bruna gruppen hanteras på samma sätt i en annan enhet.

Den gröna enheten får totalt 69 ton inklusive sin del av hallen. Den bruna får 221. Sandvik får 80 procent av den gröna enhetens belopp och 20 procent av den brunas: 55,2 + 44,2 = 99,4. Kund Y får resten.

En bolagssumma på 290 säger hur mycket Helens ska fördela vidare totalt. Nodindelningen bestämmer vilka inkommande belopp som först räknas tillsammans. Allokeringsnyckeln bestämmer därefter hur varje sådan summa delas mellan mottagarna. Dessa är olika steg i beräkningen.

En nod per kund kan återskapa den kända fördelningen i exemplet eftersom just det underlaget används när inflödena hänförs. Om båda kundnoderna först får ett genomsnitt blir resultatet i stället genomsnittet. Kunden som köper både grönt och brunt får dessutom fortfarande en kundsumma om inga separata leveransgrupper används.

### När kunden ändrar sitt inköp

Anta att Sandvik byter sina 20 ton brunt mot grönt från samma leverantörer. Kund Y:s inköp är oförändrade. Alla ursprungliga utsläppskvoter per inflöde hålls fasta i räknefallet. Totalbeloppet blir nu 258 ton inklusive hallen.

| Indelning | Sandvik före | Sandvik efter | Kund Y före | Kund Y efter |
|---|---:|---:|---:|---:|
| En gemensam nod | 145,00 | 129,00 | 145,00 | 129,00 |
| Per leverantörsbolag | 145,48 | 129,86 | 144,52 | 128,14 |
| Per artikelgrupp | 99,40 | 67,67 | 190,60 | 190,33 |
| Per inkommande leverantörsnod | 99,40 | 67,40 | 190,60 | 190,60 |

En grov indelning ger även Y del av minskningen, trots oförändrat inköp. Artikelgrupperna bevarar en större del av förändringen hos Sandvik. Skillnaden mot separata inkommande noder beror på att den gröna gruppen fortfarande räknar Ovako och SSAB tillsammans.

### När leverantören förbättrar eller byts

Om Ovakos gröna produktion i grundfallet halverar sitt utsläppsbelopp från 16 till 8 ton blir totalen 282. En gemensam nod ger 141 ton till vardera kunden. Artikelgrupper eller separata inkommande noder ger Sandvik 93 och Y 189. Fördelningen av förbättringen beror alltså på indelningen.

Om 20 ton grönt i stället flyttas från SSAB till Ovako, med oförändrade ursprungliga kvoter och med samma fördelning 80/20 till kunderna inom varje grönt inflöde, blir totalen också 282. Artikelgrupperna ger åter 93 och 189. En nod per leverantörsbolag ger då 141 till vardera kunden. Ett lägre totalbelopp visar inte ensamt vem som får del av förändringen.

### Artikelgrupper bevarar inte alla leverantörsskillnader

I grundfallet köper Sandvik 32 ton grönt från Ovako och 48 från SSAB. Anta i stället 40 från vardera, medan Y:s 20 gröna ton kommer helt från SSAB. Totalmängderna per kund och artikelgrupp är oförändrade, liksom alla leverantörernas totala inflöden.

Artikelgrupperna ger fortfarande 99,4 och 190,6 ton. Separata inkommande noder ger 96,2 och 193,8. Gruppering över leverantörer kan alltså bevara skillnaden mellan grupperna och samtidigt jämna ut skillnader inom en grupp.

## Vad underlaget faktiskt medger

En praktisk indelning beror på tre slags data: leverantörernas separata deklarationer, Helens egna kopplingar mellan inköp och leveranser samt underlaget för egna och gemensamma resurser. De behöver bedömas tillsammans.

Om Ovako endast lämnar en total på 136 ton och SSAB en total på 144 kan Helens fördela dessa internt. Men leverantörerna har då inte lämnat separata deklarationer för de gröna och bruna delarna. En massfördelning av bolagstotalerna till artikelgrupper ger i grundfallet 145,48 till Sandvik och 144,52 till Y. Fler etiketter skapar inte den finare information som saknas.

Mottagaren får använda dokumenterade fördelningsantaganden där registrerade kopplingar saknas. Det ska framgå vilka samband som observerats och vilka som fördelats. En bokföringsmässig uppdelning av mottagen Actual behåller denna status; den påstår inte att avsändaren har mätt eller deklarerat samma uppdelning. EPD-underlag som används för att beräkna U behåller däremot sin status som U.

Olika detaljnivå i olika delar kräver inte att allt förs upp till bolagsnivå. Hallens gemensamma utsläpp kan exempelvis fördelas från en resursnod samtidigt som leverantörernas mer detaljerade inflöden hålls isär.

## Coverage och allokeringsnyckeln visar andra egenskaper

Om SSAB:s belopp i grundfallet är U medan Ovako och hallen har faktisk grund får artikelgruppernas Sandvikstilldelning 41,8 ton Actual och 57,6 ton Unknown. Coverage blir cirka 0,421. Y får 104,2 Actual och 86,4 Unknown, med Coverage cirka 0,547. Samma T-fördelning kan alltså ha olika faktisk andel hos mottagarna.

Allokeringsnyckeln kan också ändra utfallet. Om allt samlas i en nod och grönt säljs till dubbla priset per ton jämfört med brunt får Sandvik 60 procent av intäkten. En intäktsnyckel ger då 174 ton till Sandvik och 116 till Y. Detta är en annan fördelning än massnyckelns 145/145, inom §3:s tillåtna metodval.

Det föreslagna D-måttet i MF-002 ska göra avvikelsen mot en motiverad referens synlig. D är ingen grund för att tillåta en nod som annars inte uppfyller nodkraven.

## Artikelgräns och produktallokering

En intern artikelgrupp gör det möjligt att beräkna periodens samlade utsläpp för en avgränsad del av bolagets verksamhet. Den kan ha ansvarig inköpsorganisation, bokförbara inflöden, egna kundrelationer och en dokumenterad andel av gemensamma resurser. Gruppen behöver varken egen chef eller egen elmätare för att kunna uppfylla dessa krav.

Att lägga till en andra leverantör förändrar inte i sig enhetens organisatoriska karaktär. En dokumenterad grupp med en leverantör och samma verksamhetsgrupp med två leverantörer bör bedömas efter samma krav. De kan däremot ge olika beslutsinformation, vilket räknefallen visar.

Den nuvarande formuleringen i §5 säger att talet ska variera med motparten och inte med varan. En produktionslinje, som uttryckligen får vara en nod enligt §1, kan samtidigt tillverka en enda artikel. Med massnyckel kan alla linjens kunder få samma kvot per ton. Numerisk likhet kan därför inte ensam avgöra om en produktallokering har uppstått.

Förslaget drar gränsen vid det som deklareras och hur det används. En leverantör deklarerar en bestämd mängd till en verklig mottagare för en angiven omfattning och period. Mottagaren tar in den i sin egen beräkning och fördelar sin egen nods hela T vidare. En lös artikelkvot som förs vidare som varans oförändrade egenskap har en annan funktion.

## Stabilitet över tid och praktiska konsekvenser

En grupp bör definieras så att den kan upprätthållas mellan perioder. Att leverantör, inköpsvolym eller kundmix ändras inom en oförändrad definition är inte automatiskt ett byte av nodpartition. Om själva definitionen ändras ska ändringen versionshanteras och jämförbarheten bedömas.

En omräkning av föregående period till den nya grunden är användbar när underlaget finns. Där den inte kan göras ska metodförändringens kända effekter och jämförelsens begränsningar synas. Ett fallande utsläppstal eller D får inte utan sådan bedömning tillskrivas en verksamhetsförbättring.

Förslaget ger organisationen utrymme att välja en nivå som stöder beslut och kan upprätthållas med tillgänglig data. Det kräver dokumentation, full täckning och avstämning även för interna grupper. En finare indelning kan bevara relevanta skillnader, men kostar mer att förvalta och garanterar ingen viss utsläppsnivå.

## Alternativ och beräkningskontroll

Enbart fysiska anläggningar skulle vara en enkel avgränsning men kan jämna ut skillnader i inköp som redan går att följa. Ett generellt förbud mot artikelinformation skulle även utesluta dokumenterade verksamhetsgrupper med bokförbara flöden. Ett krav på finaste möjliga indelning skulle å andra sidan minska användarens avvägning mot datainsatsen. Förslaget väljer dokumenterade funktionskrav för enheten.

[helens-nodindelning.py](../assets/berakningar/helens-nodindelning.py) reproducerar räknefallen med exakta bråk. Det kontrollerar inflödes- och utflödesmängder, extern totalbalans, U-balans och centrala jämförelser för sex scenarier och sex indelningar samt fallen med U och intäktsnyckel. Räknefallen visar fördelningseffekter under angivna antaganden. De bevisar inte att en viss grupp alltid är den lämpligaste organisatoriska enheten.

## Beslut

Inte behandlat. Föreslagen standardtext ovan kräver separat beslut om ändring av §1 och §5.
