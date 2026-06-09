---
layout: default
title: "Avfallsförbränning och allokering"
nav_order: 5
---

# Avfallsförbränning och allokering: ett fall ur fjärrvärmesektorn

> **Syfte:** Att visa hur ett konkret och omdebatterat redovisningsproblem i fjärrvärmesektorn - fördelningen av utsläpp från avfallsförbränning mellan värmekunder och avfallsaktörer - är en direkt instans av MASSIV+:s allokeringsfråga. Sektorn har prövat två vägar för att lösa det: Värmemarknadskommitténs parallella informationsspår och den nordiska koalitionens förslag om *reverse cut-off* till GHG Protocol. Texten visar att båda försöker nå samma sak som MASSIV+ ger som standardfall, varför ingen särskild undantagsregel behövs, och var gränsen går mellan vad standarden löser och vad ett implementerande system löser.

Den här texten kan läsas fristående. Den förutsätter en grundläggande bild av hur MASSIV+ fungerar - läs [introduktionen](../introduktion.md) eller [specifikationen](../standard/specifikation.md) först om du inte är bekant med ramverket.

---

## 1. Problemet idag

En avfallskraftvärmeanläggning eldar restavfall och gör värme av det. Det fossila innehållet i avfallet ger klimatpåverkan.

Två frågor kan ställas om dessa utsläpp, och båda handlar om bokföringen. Den ena är hos vilken motpart de ska bokföras. Den andra, som MASSIV+ lägger avgörande vikt vid, är om den motpart de hamnar hos också är den som har **rådighet** att påverka dem - om den som faktiskt kan minska utsläppet ser det i sina egna böcker. Det etablerade ramverket - GHG Protocol, med sin uppdelning i Scope 1, 2 och 3 - ger ett utförligt svar på den första frågan, men det svar det landar i lämnar den andra obesvarad. Det är där dagens problem för fjärrvärmesektorn ligger, och det är så sektorn själv formulerar det: Avfall Sverige beskriver att klimatbördan hamnar hos fjärrvärmekunderna, *"som har låg rådighet att påverka mängden avfall som lämnas till förbränning."*

Svaret på den första frågan är följande. Förbränningen är direkta utsläpp hos fjärrvärmebolaget som driver anläggningen, alltså bolagets Scope 1, och de ligger kvar där i bolagets egen redovisning. Det omdebatterade gäller kundsidan. Samma utsläpp följer med den värme bolaget säljer som en del av fjärrvärmens emissionsfaktor, så att den som köper värmen - hyresgäster och fastighetsägare - redovisar dem som sin Scope 2 för köpt energi. Att ett och samma utsläpp är Scope 1 hos producenten och Scope 2 hos köparen är inte dubbelräkning, utan så köpt energi är tänkt att fungera i GHG Protocol. Värmemarknadskommittén (VMK) sammanfattar utgångsläget som: *"den totala klimatpåverkan läggs på produkten fjärrvärme."*

Den fördelning som är omdebatterad är alltså den nedströms: ska de fossila utsläppen bäras av värmekundens Scope 2, eller föras till de aktörer vars avfall gav upphov till dem? Idag förs de inte dit på något etablerat sätt. Tvärtom motverkar redovisningslogiken det. Den nordiska koalitionen som lyft frågan i GHG Protocols pågående Scope 3-revision beskriver att dagens vägledning för kategori 5 i praktiken **nollställer** avfall-till-energi på avfallssidan: om ett företag både köper energi från en anläggning och skickar avfall dit, skulle en post både uppströms och nedströms riskera att dubbelräkna samma utsläpp. Lösningen i nuvarande praxis blir att förbränningens utsläpp inte tas upp i avfallslämnarens kategori 5, och att hela lasten i stället bärs av energin via Scope 2. En avfallslämnare som ändå vill redovisa förbränningen är hänvisad till generiska emissionsfaktorer som den applicerar själv, inte till anläggningens faktiska och allokerade siffra, och i praktiken utelämnas posten ofta. Den faktiska informationen om vad det egna avfallet gav upphov till saknar alltså en kanal.

Storleksordningen gör frågan tung. Energiåtervinning av restavfall utgör ungefär 20 % av bränslemixen i svensk fjärrvärme men står för den dominerande delen av sektorns produktionsutsläpp - Naturvårdsverket anger avfallsförbränning till omkring 81 % av utsläppen från el och fjärrvärme 2024. När övriga fossila bränslen fasas ut blir avfallet den dominerande och svåraste posten kvar.

Tre egenskaper hos dagens fördelning skaver:

- **Rådigheten ligger inte där utsläppet redovisas.** Den som kan minska utsläppen sitter uppströms: producenter som sätter fossil plast på marknaden, konsumenter, och avfallsledet. Värmekunden, som bär utsläppen i sin redovisning, har låg rådighet över avfallets sammansättning. Signalen når alltså inte den som kan påverka.
- **Belastningen kan vara importerad.** De fjärrvärmenät som har avfallsförbränning får bära klimatbelastningen från hushåll och företag vars avfall kommer från andra kommuner eller länder. Kunden bär då utsläpp som saknar koppling till den lokala verksamheten, och klimatvärdena blir svårjämförbara mellan nät beroende på om de har avfallsförbränning eller inte - med sämre förutsättningar för hållbar finansiering som följd.
- **Incitamentet uteblir.** Den siffra avfallsaktören eventuellt redovisar är en egen generisk schablon, frikopplad från den verkliga förbränningen. En sådan siffra rör sig inte när aktören minskar mängden eller det fossila innehållet i sitt avfall, så drivkraften uppströms blir svag.

## 2. Två vägar sektorn prövat

Sektorn har inte stått stilla. Två svar har vuxit fram, på två olika nivåer, och båda strävar mot samma sak: att föra utsläppsinformationen till avfallsaktören.

**Värmemarknadskommitténs parallellspår (Sverige).** I december 2022 utökades miljööverenskommelsen med ett *avfallsperspektiv* vid sidan av energiperspektivet, och en rekommendation om ett parallellt informationsspår genom avfallskedjan:

- **Fastighetsägaren** begär utsläppsdata från sin avfallsentreprenör och redovisar utsläppet från energiåtervinning av det egna avfallet separat, utanför Scope 3.
- **Förbränningsanläggningen** behåller fullt ansvar i den nationella statistiken men lämnar utsläppsdata på avfallsfakturan.

Konstruktionen riktar utsläppsinformationen till avfallsaktören. Begränsningen ligger i att den är ett spår vid sidan av den ordinarie redovisningen. Utsläppet ligger kvar på fjärrvärmen i den officiella bokföringen *och* redovisas separat hos avfallsaktören. Det blir två register som ska hållas i synk för hand, utan en gemensam regel som garanterar att de summerar till varandra och utan att flödet bokförs en gång mot en namngiven motpart.

**Reverse cut-off (GHG Protocol).** En nordisk koalition - bland dem Göteborg Energi, Fortum, Stockholm Exergi, Sysav, Mälarenergi och Tekniska verken - har i GHG Protocols pågående Scope 3-revision föreslagit en regel som kallas *reverse cut-off*. Förslaget innebär att förbränningens utsläpp allokeras till den som genererat avfallet i stället för till energiåtervinningen: förbränning ses primärt som en avfallsbehandlingstjänst, och energin redovisas som noll. Motivet är *polluter pays* - den som orsakade avfallet ska bära lasten. (Detta är ett inkommet förslag i revisionsprocessen, inte en antagen ändring.)

Termen är upplysande. Den behöver ordet "reverse" därför att GHG Protocols logik har en default-riktning given av materialets väg - avfallet flödar *in*, alltså är avfallslämnaren uppströms - som man sedan måste *vända* för att lägga lasten där den hör hemma. Reverse cut-off är med andra ord en föreslagen undantagsregel mot standardens egen grundlogik. Det är just den kampen mot grundlogiken som gör förslaget svårt att få igenom.

## 3. Samma problem i MASSIV+:s termer

I MASSIV+ är detta en **allokeringsfråga** - en av de tre frågor standarden uttryckligen tar sig an (se [specifikationen, avsnitt 3](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Mer precist är förbränningsanläggningen en **multi-output-nod**, som också är det allra vanligaste fallet i praktiken.

Kärnan i hur MASSIV+ reder i fallet är en enda definition: **nedströms bestäms av kundrelationen, inte av materialflödets fysiska riktning.** I en flödesbaserad modell är avfallslämnaren uppströms, eftersom avfallet flödar in till anläggningen. I MASSIV+:s relationsmodell är avfallslämnaren nedströms - den är **kund** hos anläggningen och köper en avfallsbehandlingstjänst (en gate fee).

Anläggningen är alltså en nod som rapporterar sina egna Scope 1+2 och har minst två utflöden, alltså två kundrelationer:

- värmen som levereras till fjärrvärmenätet och dess kunder, och
- avfallstjänsten som levereras till dem som lämnar avfallet.

"Den som lämnar avfallet" är konkret en kedja, inte en enskild part. Anläggningens direkta motpart är oftast den kommunala avfallsverksamheten för hushållens restavfall, eller en privat avfallsentreprenör för verksamhetsavfall. Ett led längre upp sitter den som ger upphov till avfallet: ett bostadsbolag, en livsmedelskedja, en tillverkande verksamhet. Längst upp finns producenterna som sätter den fossila plasten på marknaden. MASSIV+ allokerar till den direkta motparten, och andelen propagerar sedan uppåt led för led mot dem som har rådighet att minska mängden och det fossila innehållet.

Att avfallstjänsten räknas som ett utflöde kan verka bakvänt, eftersom avfallet fysiskt rör sig in till anläggningen. Men ett utflöde i MASSIV+ är den produkt eller tjänst noden säljer, inte det material den tar emot. Den enkla testfrågan är vem som betalar: den som betalar är kund, den som får betalt är leverantör. Bostadsbolaget betalar anläggningen för att bli av med sitt avfall, precis som fjärrvärmekunden betalar för värme. Båda är alltså kunder, och anläggningen är leverantör i båda relationerna. Utsläppsdatan flödar därför från leverantör till kund i båda fallen, och avfallsbehandling hamnar i avfallslämnarens uppströms Scope 3 (kategori 5), i linje med GHG Protocol.

| | Anläggningen säljer värme | Anläggningen säljer behandling |
|---|---|---|
| Leverantör (får betalt) | Anläggningen | Anläggningen |
| Kund (betalar) | Fjärrvärmekunden | Avfallslämnaren |
| Materialet rör sig | anläggning → kund | kund → anläggning |
| Utsläppsdata (Scope 1 → Scope 3) | anläggning → kund | anläggning → kund |

Bara materialets riktning skiljer relationerna åt. Leverantör- och kundrollerna, och därmed utsläppsdatans riktning, är desamma.

**Därför behöver MASSIV+ ingen reverse cut-off.** Det som i GHG Protocol kräver en särskild undantagsregel för att "vända pilen" faller i MASSIV+ ut direkt ur riktningsdefinitionen - pilen var aldrig vänd, eftersom riktningen aldrig gavs av materialet. Behovet av ordet "reverse" är ett symptom på flödestänkande: man måste vända något bara om man har en default-riktning given av materialet. När riktningen i stället ges av affären finns ingen pil att vända; det blir bara ett vanligt *cut* där affärsrelationen slutar, åt det håll affären pekar. Den krångliga terminologin är alltså inte ett tecken på att problemet är svårt, utan på att det beskrivs i fel koordinatsystem. MASSIV+ byter koordinatsystem, och då försvinner krångligheten. Avfallsförbränning behöver ingen branschspecifik paragraf - samma regel som för en stålleverans gäller.

> I MASSIV+ är nedströms inte dit materialet flödar, utan vilka som är ens kunder. Avfallslämnaren köper en behandlingstjänst och är därmed en nedströmskund hos förbränningsnoden - trots att avfallet fysiskt flödar in. Reverse cut-off behövs därför inte som undantagsregel; den faller ut direkt ur riktningsdefinitionen.

Noden fördelar sin totala utsläppsmassa proportionellt över dessa utflöden med en dokumenterad metod, tillämpad konsekvent inom perioden. Varje motpart får sin andel som faktisk Scope 3 (A), bokförd en gång mot en identifierad motpart. Massbalansen garanterar att summan av de utgående flödena motsvarar nodens totala utsläpp - varken över- eller underallokering uppstår (se [specifikationen, avsnitt 5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)).

Det är viktigt att vara tydlig med vad som *inte* är skillnaden mot de befintliga svaren. VMK:s parallellspår ger redan avfallsaktören faktisk, allokerad data från anläggningen, inte en schablon, och reverse cut-off riktar utsläppet rätt. Riktningen och den faktiska siffran delar MASSIV+ med dem. Det MASSIV+ tillför ligger i strukturen runt siffran:

- **En bokföring i stället för två.** I VMK ligger utsläppet kvar på fjärrvärmen i den ordinarie redovisningen *och* redovisas separat hos avfallsaktören utanför Scope 3 - två parallella register. I MASSIV+ är allokeringen själva bokföringen: nodens utsläpp delas över utflödena och varje andel räknas en gång, i den ordinarie redovisningen.
- **Massbalans som garanti.** Summan av andelarna motsvarar nodens totala utsläpp, så ingenting dubbelräknas eller faller bort. VMK:s två register har ingen invariant som binder dem till varandra, och det dubbelräkningsproblem som motiverar dagens nollställning i GHG Protocol uppstår aldrig, eftersom varje andel per konstruktion räknas exakt en gång.
- **Samma valuta genom kedjan.** Avfallsaktörens andel uttrycks i samma standardiserade form som alla andra noders och kan propagera vidare till aktörens egna kunder. VMK:s spår är en branschintern notering för fjärrvärmeledet, inte en post som rör sig vidare i värdekedjan.

Det möter också en återkommande invändning mot avfallsperspektivet: att flytta utsläppen bort från värmen skulle låta fastighetsägare dölja sin klimatpåverkan. I MASSIV+ kan utsläppet inte döljas, eftersom massbalansen kräver att nodens hela utsläpp fördelas och att varje andel bokförs mot en namngiven motpart. Utsläppet byter motpart, men det försvinner inte ur systemet.

### Illustration

> En anläggning släpper ut 1000 ton CO₂ under perioden och har två utflöden: värme till fjärrvärmenätet, och en behandlingstjänst till dem som lämnar avfall (totalt 2000 ton).
>
> **Steg 1 - dela mellan utflödena.** Anläggningen fördelar sina 1000 ton mellan de två utflödena med en dokumenterad metod. Hur stor del som hamnar på respektive utflöde är metodvalet (energi- kontra avfallsperspektiv) och avgörs inte av standarden i sig. Olika branscher kan ha olika sätt att luta sig mot praxis - och egna stödsystem för att hjälpa till med det praktiskt. Säg att 600 ton läggs på behandlingstjänsten och 400 ton på värmen.
>
> **Steg 2 - dela inom varje utflöde.** Behandlingstjänstens 600 ton fördelas på avfallslämnarna efter avfallsmängd. Ett bostadsbolag som via den kommunala avfallsverksamheten lämnat 100 ton, 5 % av mängden, får 5 % × 600 = 30 ton, bokförda som dess faktiska Scope 3 (kategori 5) mot anläggningen. Värmens 400 ton fördelas på fjärrvärmekunderna efter levererad MWh.
>
> **Det centrala:** 600 + 400 = 1000. Inget skapas och inget försvinner. I dagens system skulle hela 1000 ton ligga på värmen. I MASSIV+ flyttas 600 ton till dem som lämnat avfallet, och fjärrvärmekundernas andel sjunker i exakt samma grad. De 30 ton bostadsbolaget tar på sig är 30 ton som fjärrvärmekunderna inte längre bär. Samma utsläpp räknas en gång, mot rätt motpart.

## 4. Kommersiell relation, inte fysisk kausalitet

Riktningspoängen i avsnitt 3 vilar på ett medvetet designval som är värt att göra explicit, eftersom det är just här avfallsfallet blir principiellt intressant. MASSIV+ följer **kommersiella relationer, inte fysisk kausalitet.** I de allra flesta fall sammanfaller de två: leverantören säljer stål, och både materialet och fakturan går åt samma håll. Avfallsfallet är lärorikt just för att de *divergerar* - materialet och pengarna går åt motsatt håll.

Det betyder att MASSIV+ och reverse cut-off-förespråkarna landar i samma resultat av två olika skäl:

- *"Polluter pays"* är ett **kausalt** argument: den som orsakade avfallet ska bära lasten.
- MASSIV+ levererar samma utfall via ett **kommersiellt** argument: den som köpte behandlingstjänsten bär lasten.

Att de sammanfaller här är lyckligt, men de vilar på olika grund. Det är en styrka att vara öppen med det, inte en svaghet att dölja. Designvalet - att följa den kommersiella relationen - bör vara medvetet, eftersom det är det som gör att MASSIV+ kan luta sig mot bokföringens befintliga begreppsapparat hela vägen i stället för att behöva mäta fysisk kausalitet.

Gränsfallet att tänka igenom är när de två faller isär utan att en affär finns däremellan: gratis biprodukter och restströmmar som någon tar emot utan att betala. Utan en kommersiell relation finns ingen nedströmskant i MASSIV+, men det kan finnas ett tydligt kausalt flöde. Hur sådana vederlagsfria strömmar ska hanteras är ett öppet gränsfall som ramverket bör adressera uttryckligen snarare än att lämna implicit.

## 5. Standard och implementation: två olika lager

En viktig precisering: standarden och de system som implementerar den löser olika saker.

- **Standarden** håller sig medvetet metodneutral. Den kräver att noden väljer en dokumenterad, proportionell metod och tillämpar den konsekvent, men den pekar inte ut vilken metod som ska användas för ett visst fall. Detta är samma designlinje som att cirkularitet och automatisering lämnas till verktygen: stränga regler för *att* bokföra, lokal frihet i *hur* fördelningen görs.
- **Ett system byggt på MASSIV+** kan ge betydligt mer stöd. Det kan föreslå en lämplig fördelningsmetod för en viss sektor, sätta vettiga förval, hämta in vikt- eller energidata, räkna fram fördelningen och utföra själva nodfördelningen åt användaren. Verktyget kan alltså i praktiken guida en anläggning eller avfallsaktör hela vägen från rådata till bokförd post.

Distinktionen är en arbetsfördelning. Standarden definierar vad som är en giltig allokering och säkrar konsistensen mellan motparter. Implementationen gör metodvalet och beräkningen hanterbara i praktiken.

Här finns ett uppslag som följer direkt av att utsläpp i MASSIV+ rör sig som intäkter och kostnader. Om utsläppsfördelningen följer affären, ligger den redan latent i bolagets befintliga ekonomiska system: förbränningsnoden vet redan exakt vad den fakturerar för gate fees och för värme, kund för kund. Fördelningsnyckeln behöver då inte uppfinnas i ett separat mätsystem - en stor del av den finns i huvudboken. En billig och upplysande sak att undersöka är därför om en MASSIV+-allokering kan härledas direkt ur den ekonomiska redovisning en anläggning redan har, utan att bygga ett parallellt flödesbaserat mätsystem. Det demonstrerar samtidigt precis det som skiljer MASSIV+ från flödesansatserna.

## 6. Relation till E-liability

Den närmaste strukturella grannen till MASSIV+ är **E-liability** (Kaplan & Ramanna; med institutionellt momentum genom Carbon Measures Coalition, 2025). Också E-liability följer transaktioner snarare än fysiska flöden, och löser avfallsfallet i samma anda. Skillnaden i hur är upplysande för båda.

E-liability spårar utsläpp på **produktnivå**: varje produkt bär ett netto från vagga till grind, och reverse cut-off blir där en allokeringsregel på flödesnivå. Det är på sätt och vis en renare lösning på just avfallsfallet. Men produktspåret tvingar fram en fråga MASSIV+ aldrig behöver ställa: "vilken produkt orsakade vilket utsläpp?" - och i det ögonblicket kommer fysisk kausalitet in bakvägen igen.

MASSIV+ stannar på **organisationsnivå** (nod, inte produkt) och behöver därför bara fråga "vilka är nodens kunder?". Det är en enklare fråga, och dessutom samma fråga som redovisningsavdelningen redan besvarar dagligen. Organisationsnivån är därför inte en begränsning jämfört med E-liability - den är förutsättningen för att bokföringsanalogin ska hålla hela vägen, och för att affärslogiken ska kunna bära riktningen utan att man tvingas ned i produktallokering.

Tre skillnader är värda att hålla isär:

- **Enhet:** produkt (E-liability) mot organisatorisk nod (MASSIV+).
- **Aggregering:** global aggregerbarhet via ett gemensamt masterledger (E-liability) mot lokal disciplin utan någon helhetsvy, "god's view" (MASSIV+).
- **Struktur:** ett netto från vagga till grind per produkt (E-liability) mot bevarad Scope-struktur där "ditt Scope 1+2 = mitt Scope 3" (MASSIV+, interoperabelt med GHG Protocol).

Att MASSIV+ löser riktningen strukturellt men lämnar fördelningsnyckeln som ett deklarerat gränssnittsval är ett ärligt designval, konsistent med principen om strikta gränssnitt och lokal tolerans.

## 7. Var gränsen går

MASSIV+ avgör inte normativt hur utsläppen ska delas mellan värme och avfallshantering. Valet mellan energiperspektiv och avfallsperspektiv, och mellan massbaserad, energibaserad eller annan fördelning, förblir ett metodval som någon måste göra. Det är samma val som VMK:s två perspektiv ställer upp, och MASSIV+ ersätter inte den diskussionen.

Det är värt att hålla isär två påståenden av olika styrka, eftersom det är där gränsen mellan det säkra och det öppna går:

- Att **affären ger riktningen** - att en andel av utsläppen ska till avfallslämnaren därför att den är nedströmskund - är robust och i grunden oomtvistligt. Det är detta som bär hela resonemanget i avsnitt 3.
- Att **affären också ger fördelningsnyckeln**, exempelvis via intäktsandel, är ett starkare och mer omstritt påstående. En maximalt stram bokföringsanalogi skulle innebära intäktsandel som default-nyckel, men det är ett val att överväga, inte en självklarhet. Det hör hemma som en gemensam forskningsfråga (jämför avsnitt 5), inte som en slutsats att hävda.

Att hålla isär de två är vad som gör resonemanget tåligt: det säkra bär budskapet, det öppna blir en genuin fråga snarare än en svaghet.

Det standarden tillför är alltså strukturen att representera en överenskommen fördelning på ett konsekvent och spårbart sätt: en gång, mot identifierad motpart, under massbalans. I VMK:s modell kräver avfallsaktörens andel ett separat informationsspår; i GHG Protocol kräver den en föreslagen undantagsregel; i MASSIV+ följer den av att en nod allokerar sina utsläpp till sina kunder.

Avfallsförbränningen illustrerar därmed allokeringsfrågan i ett konkret fall. Både VMK:s parallellspår och reverse cut-off motsvarar i sak den bokföring MASSIV+ utför som standardfall - men utfört manuellt vid sidan av den ordinarie redovisningen, respektive som en undantagsregel mot en standards grundlogik.

---

## Källor

### Reverse cut-off och GHG Protocol

- GHG Protocol, *Summary of Scope 3 Proposals* (mars 2024) - avsnitt 3.3 om avfallsbehandling och återvinning, med den nordiska koalitionens förslag och formuleringen "reverse cut-off". (Sammanställning av inkomna förslag, inte en antagen revision.) [PDF](https://ghgprotocol.org/sites/default/files/2024-03/Scope-3-Proposals-Summary-Draft.pdf)
- GHG Protocol, *Technical Guidance for Calculating Scope 3 Emissions*, kapitel 5 (kategori 5) - nuvarande logik för avfall-till-energi och dubbelräkning. [PDF](https://ghgprotocol.org/sites/default/files/2022-12/Ch5_GHGP_Tech.pdf)

### Svensk debatt och metodik

- [Värmemarknadskommittén överens om perspektiv på avfallsförbränning - Sveriges Allmännytta](https://www.sverigesallmannytta.se/allmannyttans-klimatinitiativ/klimatinitiativets-inrapporteringsverktyg/varmemarknadskommitten-overens-om-perspektiv-pa-avfallsforbranning/)
- [Miljövärdering av fjärrvärme - Energiföretagen Sverige](https://www.energiforetagen.se/statistik/fjarrvarmestatistik/miljovardering-av-fjarrvarme/)
- [Klimat - Avfall Sverige](https://www.avfallsverige.se/for-medlemmar/vagledning-och-stod/klimat/)
- [Vem är förorenare? Allokering av utsläpp från energiåtervinning (2017) - Avfall Sverige](https://www.avfallsverige.se/aktuellt/nyhetsarkiv/artikel/vem-ar-fororenare-allokering-av-utslapp-fran-energiatervinning/)
- [Korrekt redovisning styr incitamenten för att minska utsläppen - Aktuell Hållbarhet](https://www.aktuellhallbarhet.se/opinion/debatt/replik-korrekt-redovisning-styr-incitamenten-for-att-minska-utslappen/)
- [Ursprungsmärkning fjärrvärme - Mälarenergi](https://www.malarenergi.se/om-malarenergi/miljo-och-hallbar-utveckling/ursprungsmarkning/ursprungsmarkning-fjarrvarme/)
- [Utsläpp av växthusgaser från el och fjärrvärme - Naturvårdsverket](https://www.naturvardsverket.se/data-och-statistik/klimat/vaxthusgaser-utslapp-fran-el-och-fjarrvarme/)

### E-liability (närmaste strukturella granne)

- [What are E-ledgers? - E-ledgers Institute (Kaplan & Ramanna)](https://e-ledgers.institute/what-are-e-ledgers/)
- Ramanna, Holloway m.fl. & Kaplan, *A Proto-Standard for Carbon Accounting and Auditing using the E-Liability Method* (v.2, sept 2025), [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5427956)
- Kaplan & Ramanna, *E-ledgers Carbon Accounting* (aug 2025), [HBS Working Paper 26-004](https://www.hbs.edu/ris/download.aspx?name=26-004.pdf)
- [E-Ledgers vs. GHG Protocol Approaches to Emissions Reporting - WRI](https://www.wri.org/technical-perspectives/e-liabilities-vs-ghg-protocol-emissions-reporting)
- [Carbon Measures Coalition signals growing momentum for ledger-based carbon accounting (nov 2025)](https://www.insideenergyandenvironment.com/2025/11/carbon-measures-coalition-signals-growing-momentum-for-ledger-based-carbon-accounting/)
