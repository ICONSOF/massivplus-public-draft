---
layout: default_banner
title: "Bokföringsanalogin"
parent: "Fördjupningar"
nav_order: 2
---

# MASSIV+ och dubbel bokföring: en utvecklad analogi

> **Syfte:** Att utveckla parallellen mellan MASSIV+ och finansiell bokföring som ett positioneringsverktyg och som ett analytiskt raster för att bedöma vad standarden faktiskt levererar - med netto noll-acceleration som yttersta måttstock.

---

## 1. Den grundläggande strukturella analogin

Dubbel bokföring bygger på en lokal invariant per transaktion: debet = kredit. Ingen central revisor behöver se hela världsekonomin för att en enskild transaktion ska vara korrekt bokförd hos båda parter. Lokala regler bär den globala konsistensen.

MASSIV+ har en strukturellt identisk egenskap: varje flöde mellan två noder bokförs hos båda parter - som Scope 1+2 hos avsändaren och som Scope 3-input hos mottagaren. Principen *"ditt Scope 1+2 är mitt Scope 3"* är samma typ av bilateral invariant som *"min kredit är din debet"*. Massbalansen per nod motsvarar bokföringsekvationen per företag.

Detta är samma matematiska struktur - inte en lös metafor.

**Familjen av system med samma emergenta egenskap:**

| System | Invariant |
|---|---|
| Dubbel bokföring | Aritmetisk per transaktion |
| Moms (VAT) | Aritmetisk + bilateral per transaktion, termineras hos konsument |
| MASSIV+ | Aritmetisk + bilateral per flöde |
| Content-addressed grafer (Git, Merkle, blockchain) | Kryptografisk per länk |

I alla fyra fallen är det den lokala regeln som bär den globala egenskapen. Vad systemen garanterar är *intern konsistens*, inte *korrekthet* - sanningshalten kommer från indata.

Värt att notera om dubbel bokföring som prejudikat: den lokala invarianten var aldrig slutmålet. Den blev grunden för en hel uppsättning institutionella funktioner som idag tas för givna - revision, ansvar, kreditmarknader, delegering, koordinering mellan aktörer som inte känner varandra. Strukturen kom först; institutionerna växte fram över tid eftersom strukturen gjorde dem möjliga. Det är värt att hålla framme när man bedömer vad MASSIV+ kan vara på sikt - inte som löfte, utan som referenspunkt för vad lokal invariant historiskt har möjliggjort när den fått tid att bära.

Den bilaterala konsistenslogiken finns inte bara i dubbel bokföring. Moms är ett yngre och mer medvetet konstruerat exempel på samma princip: säljarens utgående moms motsvarar köparens ingående moms, dubbelbeskattning förhindras via avdragsrätt, kedjan terminerar hos slutkonsumenten som inte kan dra av. Det är samma bilaterala bokföring med samma terminering vid konsument som MASSIV+ konstruerar. Och momsen är värd att hålla framme för en specifik egenskap: den togs från idé till global standard på ett par decennier (Sverige införde moms 1969), och är idag fundamentet för statsfinanser i över 170 länder.

---

## 2. Tankeexperimentet: bokföring som klimatberäkning

Om finansiell bokföring idag fungerade som klimatberäkning gör, skulle den ha följande egenskaper:

**Företaget skulle bokföra åt sina motparter.** När du betalade en faktura skulle du själv uppskatta hur mycket leverantören tjänade på affären, baserat på branschgenomsnitt för marginaler. Du skulle inte vänta på motpartens faktura - du skulle skatta deras intäkt utifrån en databas som säger "tillverkare i denna sektor har typiskt 12% marginal". Detta är precis hur Scope 3 ofta beräknas idag via EEIO (miljöutvidgad input-output-analys - utsläpp skattade från branschers ekonomiska statistik) eller spenddata (utsläpp skattade från inköpsbelopp).

**Olika företag skulle använda olika valutaomräkningar för samma transaktion.** Du bokför i SEK enligt din egen kurs; leverantören i EUR enligt sin egen kurs; ingen koherens krävs. Motsvarar att två bolag i samma kedja får använda olika emissionsfaktorer för samma bränsle.

**Samma krona skulle räknas i flera bolags resultat.** Om en konsult fakturerar tre kunder för samma timme skulle alla tre bokföra hela kostnaden - och konsulten dessutom bokföra full intäkt från var och en. GHG Protocol erkänner uttryckligen att Scope 3 dubbelräknas mellan bolag och accepterar det som oundvikligt.

**Årsredovisningar skulle uppdateras vart tredje år.** 2023 års vinst skulle deklareras baserat på en beräkning gjord 2020, eftersom det är dyrt att räkna om. Det motsvarar EPD-cykeln.

**Skatteverket skulle acceptera att 60% av siffrorna är schabloner från en branschdatabas** så länge "estimated" stod bredvid - utan krav på att den uppskattade andelen särredovisas. Ingen Coverage-motsvarighet (andelen som vilar på faktisk, deklarerad data) finns idag i klimatredovisning på det sätt MASSIV+ kräver.

**Momsen skulle fungera som dagens Scope 3-rapportering.** Säljaren skulle inte fakturera moms till köparen - istället skulle köparen själv uppskatta hur mycket moms säljaren *borde* ha tagit ut, baserat på branschgenomsnitt. Två köpare av samma vara skulle uppskatta olika belopp. Säljaren skulle uppskatta sin egen momsskuld oberoende av köparnas uppskattningar. Skatteverket skulle få in en summa som varken stämmer med säljarens eller köparens redovisning, och ingen skulle tycka det var konstigt - för att alla vet att momssystemet är "metodologiskt komplext" och att exakta siffror är "en orealistisk ambition i värdekedjor med många led". Det är ungefär så Scope 3 hanteras idag.

**Motpartsidentitet skulle saknas.** Du bokför "inköp från transportsektorn: 50 000 kr" snarare än "inköp från Schenker AB: 50 000 kr". Vilket är precis vad spendbaserad Scope 3 gör - utsläpp tillskrivs en kategori, inte en identifierad motpart.

**Ingen skulle revidera grannoden.** Om din leverantörs bokföring var helt felaktig skulle det inte påverka din - du har redan skattat deras siffror själv, oberoende av vad de redovisar.

### Det som blir synligt genom övningen

Finansiell bokföring tog flera hundra år att utveckla till sin nuvarande form. De principer som idag känns självklara - att varje transaktion bokförs av båda parter, att motparten är identifierad, att summorna måste stämma över tid, att uppskattningar måste särredovisas, att samma krona inte räknas dubbelt - är *exakt* de principer som klimatredovisning saknar. MASSIV+ kan beskrivas som ett försök att importera dessa principer till klimatdomänen.

---

## 3. Var analogin är stark och var den bryter

**Stark:** Den matematiska strukturen är genuint identisk. Bilateral bokföring per transaktion, lokal invariant, emergent global konsistens utan central koordinator, identifierad motpart, ersättningsprincip när bättre data blir tillgänglig (analogt med rättelser i bokföring).

**Delvis stark:** Att A-data - faktisk, deklarerad data (A), till skillnad från ännu okänd (U) - kräver att leverantören själv utfärdar deklarationen är analogt med att man inte bokför åt sina motparter i finansiell redovisning. Replacement rule (faktisk data ersätter okänd, ackumuleras inte) speglar hur korrigeringar hanteras i bokföring.

**Bryter:** Pengar är fungibla på ett sätt som utsläpp inte är. En transaktion har en entydig motpart medan ett kilo CO₂ inte har det utan en allokeringsregel. Allokering har ingen verklig motsvarighet i bokföring. MASSIV+ ärver den matematiska strukturen men inte den institutionella infrastrukturen - revisorer, ackrediteringssystem, lagstiftning bakom GAAP/IFRS, professionsstrukturer.

Just därför är jämförelsen användbar som *positionering*: den visar inte att klimatberäkning är trivial och att man bara behöver kopiera bokföring, utan att det fält som ofta beskrivs som "omöjligt att lösa exakt" har en stark prejudikat i ett annat fält där det löstes - inte perfekt, men tillräckligt väl för att hela den globala ekonomin vilar på det.

---

## 4. Bokföringsanalogin testad mot netto noll-syftet

Det yttersta syftet är att stimulera snabb utveckling mot netto noll. Designval bör testas mot detta, inte mot intern elegans. Finansiell bokföring är värdefull inte för att den är vacker utan för att den gör *ekonomiska beslut handlingsbara*. Den frågan ger följande analys för klimatdomänen:

### Tre beslutstyper som driver netto noll

**Inköpsbeslut.** En inköpschef som väljer mellan två leverantörer behöver veta vilken som faktiskt har lägre utsläpp - inte vilken som har skickligast hållbarhetsavdelning. Dagens system gör detta svårt: olika emissionsfaktorer, olika systemgränser, olika rapporteringsår, schabloner blandade med primärdata utan markering. MASSIV+ gör jämförelse möjlig eftersom alla leverantörer rapporterar enligt samma regler och Coverage visar hur mycket av siffran som är primärdata. Leverantörer med högre Coverage och lägre absolut värde vinner affärer.

**Investeringsbeslut.** En aktör som överväger utsläppsminskande investering behöver veta att investeringen *syns* nedströms - annars saknas affärscaset. I dagens system kan en ståltillverkare investera i elektrifierad masugn, sänka utsläppen med 90%, och fortfarande se att kunderna räknar med EPD-siffror från 2022 i tre år framåt. Investeringssignalen dämpas. MASSIV+ propagerar förändringen i nästa rapporteringsperiod till alla nedströmsnoder.

**Regulatoriska beslut.** CBAM, EU ETS, CSRD, framtida produktkrav - alla bygger på att man kan tillskriva utsläpp till en identifierad aktör utan dubbelräkning. Här är dagens praxis strukturellt svag: olika ramverk ger olika svar, dubbelräkning är erkänd och accepterad. MASSIV+ ger en konsistent grund som kan understödja regulatorisk rapportering snarare än ersätta den. För aktörer som redan rapporterar under EU ETS finns en envägsbrygga in - verifierad ETS-data kan användas direkt som Scope 1 i MASSIV+ - vilket gör adoption särskilt billig för ETS-anläggningar.

### Standarden som tre lager - inte som monolit

En produktiv distinktion: MASSIV+ kan antas stegvis - det är en stege där varje steg har sitt eget netto noll-värde och sin egen implementeringskostnad. Tre lager kan urskiljas:

**Lager 1: Standardiserad Scope 1+2-rapportering per nod.** Gemensamma emissionsfaktorer, identifierad rapporterande enhet, deklarerad metodik, definierad nodgränsdragning. Inget krav på kunskap om uppströmsutsläpp. Detta är vad ett bolag kan göra ensamt, utan beroende av sina leverantörer. Värdet uppstår med en gång och stannar hos den rapporterande aktören: internt beslutsstöd om var i verksamheten utsläppen ligger, en konsistent grund över tid för egna investeringsbeslut, jämförbarhet med andra aktörer på samma nivå, auditerbar metodik som tål CSRD-granskning, och trovärdighet i leverantörsdialog. För aktörer som redan rapporterar verifierade utsläpp under EU ETS kan dessa värden användas direkt som Scope 1 i MASSIV+ istället för standardens emissionsfaktorer - en envägsbrygga som ger ETS-aktörer en låg tröskel in i standarden. Lägst tröskel - och därför det lager där flest aktörer kan börja.

**Lager 2: Allokering och bilateralt utbyte mellan noder.** Avsändaren allokerar sin Scope 1+2 till mottagarna enligt standardens regler och deklarerar detta bilateralt. Mottagaren rapporterar faktiskt uppströms Scope 3 (A) för den relationen, eller markerar U om leverantören inte rapporterar. Detta är den genuint bilaterala bokföringen - där *"din kredit är min debet"* faktiskt realiseras - och det är här bokföringsanalogin verkligen biter. Det är också den minsta möjliga propageringen: ett steg, från en nod till nästa. Värdet uppstår även om bara den ena parten har anammat standarden: en leverantör som rapporterar enligt MASSIV+ erbjuder sina kunder en kvalitativt bättre datapost än branschschabloner, vilket stärker positionen i upphandlingar oavsett om kunden själv rapporterar enligt standarden. För det specifika kund-leverantörsparet ger lager 2 dessutom matematisk konsistens i utbytet, strukturellt utesluten dubbelräkning, och motpartsidentitet bevarad genom kedjan.

**Lager 3: Flerstegspropagering genom värdekedjan.** Den fullständiga modellen där A/U-information och utsläppsvärden ackumuleras genom hela kedjan, och där förändringar i en nods Scope 1+2 propagerar nedströms i nästa rapporteringsperiod. Värdet: dynamisk signalspridning där investeringar i utsläppsminskning syns flera led nedströms utan att varje mellanled gör egen utredning.

### Vad detta innebär för positionering och adoption

De tre lagren bär olika tunga argument. Lager 1 levererar netto noll-värde via *inköp och regulering* - bättre data för beslut som redan tas idag. Lager 2 är där MASSIV+ faktiskt skiljer sig metodologiskt från GHG Protocol, PACT och Catena-X, eftersom det är där den bilaterala konsistensen mellan motparter konstrueras. Lager 3 levererar det specifika tilläggsvärde som propagering ger: signaler som rör sig i samma takt som de beslut de ska påverka.

Det gör adoptionen mindre binär. En aktör kan börja med lager 1 och successivt lägga till lager 2 när leverantörsrelationerna är redo. Lager 3 förutsätter i sin tur att tillräckligt många noder i en given kedja har implementerat lager 2 - annars finns inget att propagera. Det är en naturlig sekvens, inte ett allt-eller-inget-åtagande.

Det gör att varje lagers värde står på egna ben. Den vanligaste invändningen mot MASSIV+ - att flerstegspropagering är komplicerad och otrygg i tidig adoption - rår inte på lager 1 och 2, som ändå bär en stor del av netto noll-värdet. Standarden är därmed en stege snarare än en monolit: den kan antas ett lager i taget.

---

## 5. Funktionsförskjutningen: från rapportering till operativ signal

En observation som ligger latent i propageringsargumentet men förtjänar att skrivas ut: MASSIV+ representerar inte bara en metodologisk förbättring av befintlig klimatredovisning - det representerar en *funktionsförskjutning* i vad klimatdata är till för.

Dagens dominerande klimatredovisning är retrospektiv. GHG Protocol-rapportering, EPD-deklarationer och CSRD-bilagor sammanställs en gång om året (eller mer sällan), oftast med flera månaders eftersläpning, för att svara på frågan *"vilka utsläpp hade vi förra perioden?"*. Funktionen är primärt compliance: att visa rapporteringspliktig data för en avgränsad period.

MASSIV+ är konstruerat så att utsläppsdata kan fungera som *operativ signal* - något som faktiskt påverkar beslut i den period då data uppstår. Det är inte en revolutionerande omformulering, men det är en betydelsefull funktionsförskjutning som syns tydligt i tabellen nedan:

| Dimension | Etablerad klimatrapportering | MASSIV+ |
|---|---|---|
| Primär funktion | Compliance | Beslutsstöd |
| Tidsperspektiv | Retrospektiv | Periodaktuell |
| Beslutsstöd | Begränsat | Strukturellt inbyggt |
| Förhållande till förbättringar | Synliggör i nästa rapport | Propagerar i nästa period |
| Riktning för data | Uppåt mot rapportmottagare | Mellan affärsparter |

Förskjutningen är inte total. MASSIV+-data kan användas för compliance-rapportering precis som GHG Protocol-data - funktionerna utesluter inte varandra. Men *konstruktionsändamålet* skiljer sig: MASSIV+ är designat för att stödja beslut i värdekedjan, inte primärt för att fylla rapporteringskrav.

Detta är sannolikt det djupare *varför* bakom propageringen. Propageringens värde ligger i att den gör data till en signal som rör sig genom systemet i samma takt som besluten den ska påverka - inte i propageringen i sig.

### Lokal nätverkseffekt - och vad som ger värde oberoende av andra

Värdet av MASSIV+ uppstår inte uniformt med adoption. De olika lagren beter sig olika:

- **Lager 1 ger värde med en gång**, oberoende av om någon annan i kedjan rapporterar enligt standarden. Det är intern data för intern användning, plus en konsistent grund för rapportering uppåt.
- **Lager 2 ger värde med en gång för den part som rapporterar**, även om motparten inte gör det. En leverantör som deklarerar sin allokerade andel till en kund erbjuder en datapost som är kvalitativt bättre än branschschabloner - det stärker leverantörens position i upphandling och kunddialog oavsett om kunden själv är på MASSIV+. För kunden uppstår fullt värde först när någon av leverantörerna rapporterar, men en enda rapporterande leverantör räcker för att A-andelen i kundens uppströms Scope 3 ska börja byggas.
- **Lager 3 är där den lokala nätverkseffekten faktiskt biter.** Värdet av flerstegspropagering växer med antalet noder *i en given kedja* som har implementerat lager 2 - det är först då en investering hos en uppströmsaktör syns flera led nedströms utan att varje mellanled gör egen utredning.

Detta skiljer sig från det vanliga adoptionsargumentet kring nätverksstandarder. Värdet på lager 1 och 2 är reellt från dag ett, så MASSIV+ kräver inte att hela värdekedjan följer med för att de första aktörerna ska få nytta. Det är *flerstegseffekten* som är beroende av kedjeadoption, inte standarden som helhet.

Det är inte heller en global nätverkseffekt av Metcalfe-typ där värdet växer kvadratiskt med antalet noder. Det är något mer specifikt: lager 3-värdet växer med antalet noder *i en given kedja*, och de kedjor där flera aktörer adopterar parallellt vinner mest. Skillnaden spelar roll - den förklarar varför adoption i sektorer med koncentrerade värdekedjor (stål, kemi, bygg) kan ge stor effekt även med begränsad global spridning.

---

## 6. Den infrastrukturella ramningen

Det starkaste netto noll-argumentet för bokföringsanalogin är kanske *infrastrukturellt* snarare än tekniskt. Det tog hundratals år att bygga finansiell redovisning till sin nuvarande form, och under den tiden har den möjliggjort sällsynt effektiv allokering av kapital över miljarder transaktioner per dag.

Klimatdomänen har inte 400 år. Men det betyder också att man inte behöver återuppfinna principerna - de finns redan, beprövade, i en angränsande domän. Att importera dem är inte ett tekniskt äventyr utan ett institutionellt arbete.

Momsen är värd att hålla framme just här som tidsmässigt prejudikat. Den togs från idé till global standard på ett par decennier - Sverige införde moms 1969, och idag är systemet fundamentet för statsfinanser i över 170 länder. En bilateral redovisningsstandard kan etableras snabbt när problemet är skarpt nog och lösningen principfast nog. MASSIV+ behöver inte vänta 400 år för att fungera; den behöver bara följa samma logik som ett system som mänskligheten redan har byggt en gång, medvetet och i modern tid.

**Den produktiva ramningen:** MASSIV+ är en *översättning* av en mogen institutionell praxis till en ung domän där tiden är knapp - inte en innovation i metodologi. Tiden är knapp just för att netto noll inte väntar på att nya principer ska uppfinnas från scratch.

---

## 7. Var analogin bär och var den brister

Analogin fungerar som positioneringsverktyg snarare än som anspråk på ny metodologi. MASSIV+ är en översättning av etablerad institutionell praxis till en ung domän - ett svagare men mer trovärdigt anspråk än "ny metodologi", och ett som knyter standarden till en mogen tradition.

Den bär olika starkt i standardens tre lager. Lager 1 (Scope 1+2-rapportering per nod) ger jämförbarhet och regulatorisk grund; lager 2 (bilateralt utbyte med allokering) ger den bilaterala konsistens som skiljer MASSIV+ från andra ramverk; lager 3 (flerstegspropagering) ger dynamisk signalspridning. Analogin träffar starkast i lager 2, där "din kredit är min debet" realiseras som bilateral bokföring mellan identifierade motparter - lager 1 är förberedelse, lager 3 är konsekvens. Värdet uppstår redan på lager 1 och 2, oberoende av hur många motparter som anslutit; endast flerstegspropageringen är beroende av kedjeadoption. Det motsäger invändningen att en nätverksstandard är värdelös innan tillräckligt många följer med.

Analogin har tydliga brytpunkter. Pengar är inte CO₂, allokering har ingen motsvarighet i bokföring, och den institutionella infrastruktur som dubbel bokföring bär växte fram över tid - den ärvs inte med strukturen. Inom dessa gränser beskriver analogin en distinkt funktionell ambition: MASSIV+ är data som rör sig i samma takt som besluten den ska påverka, snarare än förbättrad compliance-rapportering.
