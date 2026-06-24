---
layout: default
title: "Produktstandarder"
nav_order: 5
---

# MASSIV+ och produktnivåstandarderna

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

De fem produktnivåstandarderna delar ett gemensamt perspektiv på MASSIV+. Texten börjar med den generella relationen som gäller dem alla, och behandlar sedan var och en för sig.

---

## Den generella relationen

ISO 14040/14044, ISO 14067, EPD/ISO 14025, PACT och Catena-X delar ett gemensamt perspektiv: produkten är den centrala analysenheten. Utsläpp beräknas per deklarerad enhet (kg CO₂e per kg stål, per bil, per kWh) längs en definierad livscykel. MASSIV+ spårar också flöden i värdekedjan men på *organisationsnivå* snarare än produktnivå. Allokeringen är till kunder snarare än till deklarerade enheter, och beräkningen är per nod snarare än per produkt.

MASSIV+ bygger på etablerad allokeringsmetodik. ISO 14044:s allokeringshierarki - undvik via subdivision eller systemexpansion, annars fysiska samband (massa, energi, kvantitet), annars ekonomiskt värde - är ärvd av ISO 14067, EPD och GHG Protocol Product Standard och utgör en sedan länge etablerad standard för *vilken princip* allokeringen ska följa. MASSIV+ importerar denna hierarki rakt av i sitt val av allokeringsregel per nod (se [specifikationen §3](../../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Det nya är tillämpningsnivån, inte principen: allokeringen sker på organisation/nod → kund som propageringssteg, snarare än mellan biprodukter inom en process per deklarerad produktenhet. Det är denna logiska nivå - leverantörens fördelning av sina totala Scope 1+2 mellan sina kunder - som varken ISO, GHG Protocol eller EU:s rapporteringsstandarder hittills har standardiserat.

Det innebär att systemen mäter olika saker och inte konvergerar mot samma svar. De är komplementära snarare än konkurrerande. Relationen är konkret och praktisk i två riktningar:

**Produktdata in i MASSIV+.** En leverantör med en verifierad PCF (ISO 14067, PACT, Catena-X, EPD) besitter faktisk primärdata som kan matas in i en MASSIV+-nod och ger Coverage nära 1 - förutsatt att PDS (Primary Data Share) är hög. PDS och Coverage är konceptuellt identiska mått: båda anger andelen faktisk primärdata i det rapporterade värdet.

**MASSIV+-data in i produktberäkningar.** En nod med hög Coverage och faktiska Scope 1+2-data producerar leverantörsspecifik organisationsdata som kan användas som indata i PCF-beräkningar enligt alla produktstandarderna - som ett bättre alternativ till sekundärdatabaser när leverantörsspecifik PCF saknas. Data är allokerad efter en konsistent regel snarare än kopplad till en specifik deklarerad enhet, vilket ska dokumenteras i mottagarens PDS-beräkning.

En komplikation kvarstår: MASSIV+ kräver standardiserade emissionsfaktorer för Scope 1+2; produktstandarderna tillåter aktören att välja egna. Data från de två systemen är därmed inte direkt jämförbara utan en notering om vilka EF:er som använts.

### ISO 14040/14044

ISO 14040 och ISO 14044 är de internationella grundstandarderna för livscykelanalys. ISO 14040 definierar principerna och ramverket; ISO 14044 specificerar kraven och riktlinjerna. Alla produktrelaterade miljöstandarder nedan - ISO 14067, EPD/ISO 14025, PACT, Catena-X - bygger på dessa som metodologisk grund. Standarderna täcker alla miljöpåverkanskategorier (inte bara klimat) och hela livscykeln vagga till grav, men föreskriver inga specifika beräkningsmetoder.

MASSIV+ är en propageringsansats med en annan domän än LCA. Standarderna definierar hur produkters miljöpåverkan ska *beräknas* med vetenskaplig noggrannhet; MASSIV+ definierar hur utsläpp ska *propageras* i ett nodnätverk. En nod kan ha ISO 14040/44-kompatibel LCA i botten och därmed bidra med idealisk primärdata; alternativt räcker direkt rapportering av Scope 1+2 enligt MASSIV+.

| Dimension | ISO 14040/14044 | MASSIV+ |
|---|---|---|
| Syfte | Metodram för fullständig produktLCA | Propagering av utsläppsflöden i nodnätverk |
| Miljöpåverkan | Alla kategorier (klimat, vatten, ekotoxicitet m.fl.) | Enbart klimat (CO₂e) |
| Livscykelgräns | Vagga till grav | Scope 1+2 + allokerade uppströmsflöden |
| Metodkrav | Fullständig LCA-kompetens | Scope 1+2-rapportering per nod |

### ISO 14067

ISO 14067 specificerar principer och krav för att kvantifiera ett produkts koldioxidavtryck (PCF) - en tillämpningsstandard som bygger direkt på ISO 14040/14044 men begränsar sig till klimatpåverkan, cradle-to-gate per deklarerad enhet. Det är den standard Catena-X primärt bygger på och som PACT/Pathfinder är anpassat till.

Relationen till MASSIV+ är tydlig: ISO 14067 definierar hur ett PCF ska *beräknas* per produkt och deklarerad enhet; MASSIV+ definierar hur utsläpp ska *propageras* och allokeras mellan organisatoriska noder. De verkar på olika nivåer och är komplementära i båda riktningar - se den generella relationen ovan.

| Dimension | ISO 14067 | MASSIV+ |
|---|---|---|
| Syfte | Kvantifiera produkters koldioxidavtryck | Propagera utsläppsflöden i nodnätverk |
| Centralt objekt | Produkt (per deklarerad enhet, cradle-to-gate) | Nod (organisatorisk enhet) |
| Metodkrav | LCA-kompetens, fullständig inventering | Scope 1+2-rapportering per nod |

### EPD / ISO 14025

En EPD (Environmental Product Declaration) är en typ III-miljödeklaration enligt ISO 14025 - ett tredjepartsverifierat dokument som redovisar en produkts miljöpåverkan baserat på LCA. ISO 14025 kräver att beräkningarna görs enligt ISO 14040/14044 och att produktkategorispecifika regler (PCR) specificerar beräkningsmetodik: systemgränser, cut-off-kriterier, allokeringsregler och datakvalitetskrav. Sektoriella tillämpningar som EN 15804 (byggprodukter) lägger ytterligare krav ovanpå detta. EN 15804+A2 har därutöver krav på datakvalitetsbedömning och dokumentation av primärdataandel; andra PCR varierar i hur explicit de behandlar detta. Distinktionen *primärdata vs sekundärdata* är alltså etablerad i EPD-systemet, men hanteras som metadata bredvid ett enskilt rapporterat värde per produkt. EPD-systemet är metodologiskt föreskrivande för *beräkningarna* - men det EPD saknar är definitionen av hur utsläpp ska fördelas och propageras längs en värdekedja. Det är precis vad MASSIV+ tillhandahåller.

Båda är B2B-verktyg, men fyller olika funktioner. En EPD *deklarerar* vad en produkt presterar vid ett givet tillfälle och används i upphandling och leverantörsdialog. MASSIV+ skapar ett *operativt flödessystem* där kunder löpande kan se hur stor andel av inkommande utsläpp som är faktabaserade och därigenom rikta krav och incitament mot rätt leverantörer. En leverantör med publicerad EPD har per definition genomfört en verifierad LCA - det är precis den primärdata som gör Coverage-värdet högt i MASSIV+. EPD är input; MASSIV+ är systemet som gör inputens kvalitet synlig längs hela kedjan.

**Räcker det inte med EPDer?**

En vanlig invändning är att MASSIV+ inte behövs eftersom organisationer redan arbetar med att samla in EPDer från sina leverantörer. Argumentet bygger på en missuppfattning: EPDer är värdefull indata, men utgör inget värdekedjesystem. Fyra begränsningar gör en ren EPD-strategi otillräcklig:

- **Täckning.** EPDer finns för en bråkdel av en typisk leverantörsbas - framförallt inom bygg där EN 15804 driver fram dem, marginellt i andra sektorer. En EPD-strategi har inget svar för den stora delen av leverantörsspenden där ingen EPD finns.
- **Bakar in det okända i ett samlat värde.** EPD adresserar datakvalitet via metadata (DQR enligt EN 15804, primärdataandelar) och fallback till sekundärdatabaser, men kombinerar detta i ett enskilt rapporterat värde per produkt. MASSIV+:s U/A-distinktion håller i stället okänt och faktiskt strukturellt åtskilt **på värdenivå**, så att andelen kan följas, propageras separat nedströms, och stegvis konverteras till primärdata utan att modellen behöver räknas om.
- **Ingen koherens mellan EPDer.** Olika EPDer använder olika emissionsfaktorer, systemgränser och PCR. Att samla 40 EPDer ger 40 punktdeklarationer, inte en koherent värdekedjebild - och inget strukturellt skydd mot gränsöverlapp eller över-allokering mellan dem.
- **Statisk vs operativ.** En EPD är en ögonblicksbild giltig 3-5 år; MASSIV+ är ett operativt flödessystem där värden uppdateras löpande.

Den operativa karaktären har en konkret styrningskonsekvens som EPD-strategin saknar. Eftersom Coverage och utsläppsvärden uppdateras löpande kan organisationen sätta **KPI:er för kontinuerlig utsläppsminskning** - år för år eller kvartalsvis om man vill - både för den egna verksamheten och som krav eller incitament mot leverantörer. När en leverantör förbättrar sin primärdata syns effekten omedelbart i mottagarnas nästa rapporteringscykel utan att tidigare rapporter behöver räknas om. Det förvandlar utsläppsdata från en årlig rapporteringsbörda till ett operativt styrinstrument.

EPD och MASSIV+ är därför komplementära och fyller olika funktioner. En leverantör med publicerad EPD bidrar med idealisk primärdata till sin nod, men mottagaren behöver ändå ett system för att hantera leverantörer utan EPD, garantera massbalans, och göra datakvaliteten synlig och styrbar nedströms. Det är vad MASSIV+ tillhandahåller.

| Dimension | EPD / ISO 14025 | MASSIV+ |
|---|---|---|
| Systemtyp | Deklarationsformat | Propageringssystem |
| Miljöpåverkan | Multipla kategorier | Enbart klimat (CO₂e) |
| Verifiering | Tredjepartsverifierad, obligatorisk | Ej specificerat |
| B2B-funktion | Deklarera produktens miljöprestanda | Göra datakvalitet synlig och handlingsbar |
| Relation | EPD-data är idealisk primärindata i MASSIV+-nod | Komplementärt |

### PACT / Pathfinder Framework

PACT (WBCSD) är ett tvärsindustriellt initiativ vars kärna är Pathfinder Framework - metodologisk vägledning för att beräkna och utbyta produktkoldioxidavtryck (PCF) längs värdekedjan, byggd på GHG Protocol och ISO 14067. Varje aktör beräknar sitt cradle-to-gate-PCF per deklarerad enhet och skickar det vidare; konsistens uppnås via gemensamma beräkningsregler, inte via matematisk konservering. Fel propageras nedströms utan systemvarning. Teknologilagret Pathfinder Network möjliggör interoperabelt datautbyte via API:er.

En tydlig parallell: PACT:s *Primary Data Share* (PDS) - andelen PCF baserad på primärdata - är konceptuellt identisk med MASSIV+:s Coverage-mått. Båda systemen delar designambitionen att göra datakvaliteten synlig och driva andelen faktisk data uppåt. Skillnaden är att PDS beräknas per produkt i LCA-kontext; Coverage per nod i ett propageringssystem. PACT kräver LCA-kompetens, intern produktspårbarhet och oberoende tredjepartsverifiering. MASSIV+ kräver Scope 1+2-rapportering per nod - utan LCA-krav eller produktspårning.

| Dimension | PACT / Pathfinder | MASSIV+ |
|---|---|---|
| Centralt objekt | Produkt (PCF, cradle-to-gate) | Nod |
| Konsistensgrund | Gemensam beräkningsmetodik | Massbalans och konserveringsregler |
| Datakvalitetsmått | Primary Data Share (PDS) | Coverage - konceptuellt identiskt |
| Massbevarande | Inte strukturellt garanterat | Inbyggt via massbalansen |
| Datakrav | LCA-metodik, produktspårbarhet | Scope 1+2 per nod |
| Emissionsfaktorer S1+S2 | Primärdata prioriteras, sekundärdatabaser som fallback | Standardiserat gemensamt set för alla noder |
| Verifiering | Kräver oberoende tredjepartsgranskning | Ej specificerat |

### Catena-X

CX-PCF Rulebook bygger primärt på **ISO 14067** och **ISO 14040/14044**, med nära anpassning till Pathfinder Framework. Sektoriella riktlinjer (TFS, worldsteel, International Aluminium) kan användas som drop-in standards med specificerade tilläggskrav. Varje aktör beräknar sitt cradle-to-gate PCF per deklarerad enhet och utbyter det till nästa led - konsistens via regelbok, inte via matematisk konservering.

Det centrala datakravet skiljer dem åt: Catena-X kräver intern produktspårbarhet och LCA-kompetens som de flesta aktörer utanför de största koncernerna saknar. En Catena-X-aktör med verifierad PCF och hög PDS kan bidra med data som ger Coverage nära 1 i en MASSIV+-nod - den mest mogna änden av datamognadskurvan. En aktör med lägre PDS ger proportionellt lägre Coverage och är inte per definition fullständig primärdata i MASSIV+-termer.

Konceptuellt är PDS och Coverage parallella mått: båda anger andelen primärdata i det rapporterade värdet och båda propagerar genom kedjan. Skillnaden ligger i hanteringen av icke-primär data - Catena-X tillåter sekundärdatabaser med representativitetskriterier medan MASSIV+ markerar saknad data som U (okänt) utan att fylla luckan med databasvärden. Det är en strukturellt skarpare position som syftar till att hålla osäkerhet synlig snarare än bortskattad.

Catena-X har därutöver ett Data Quality Rating (DQR) med tre representativitetsindikatorer (teknisk, temporal, geografisk) på 1-5-skala. MASSIV+ har inget motsvarande extra lager, vilket är en avsiktlig förenkling: när alla noder använder ett gemensamt standardiserat emissionsfaktorset på organisationsnivå adresserar standardisering det som DQR:s representativitetspoäng vill kvantifiera, vilket gör det extra lagret onödigt för MASSIV+:s syfte.

| Dimension | Catena-X | MASSIV+ |
|---|---|---|
| Metodologisk bas | ISO 14067 + 14040/14044, anpassad till Pathfinder | Eget nodbaserat flödessystem |
| Centralt objekt | Produkt (PCF, cradle-to-gate) | Nod |
| Konsistensgrund | Regelbok (ISO 14067 + Catena-X-krav) | Massbalans |
| Datakvalitet-mått | DQR (TeR/TiR/GeR, 1-5) + PDS | Coverage = A/(A+U) |
| Hantering av icke-primär data | Sekundärdatabaser med hierarki + representativitetskriterier | U-markör (okänt) - ingen fallback till databaser |
| Datakrav | LCA-metodik, intern produktspårbarhet | Scope 1+2 per nod |
| Industritäckning | Fordonsindustri | Industri- och storleksagnostiskt |
