---
layout: default
title: "Ursprungsgarantier: kritiken och regelverket"
nav_order: 7
---

# Ursprungsgarantier: kritiken och regelverket

> **Syfte:** En fördjupning i kritiken mot ursprungsgarantier, det regelverk som nu skärper dem, och hur MASSIV+:s hantering av köpt energi förhåller sig till båda. Texten är fristående och icke-normativ. För själva mekanismen - hur MASSIV+ hanterar Scope 2 och köpt energi - se [Köpt energi och Scope 2](kompensation-och-faktiska-floden.md).

Texten bygger på distinktionen mellan faktiska flöden och köpta anspråk som [Köpt energi och Scope 2](kompensation-och-faktiska-floden.md) etablerar, och fördjupar varför den lösa ursprungsgarantin hör hemma på anspråkssidan.

---

## 1. Två marknader som kopplades isär

För el finns två separat handlbara ting, som historiskt såldes ihop men har skilts åt:

- **Den fysiska energin** - kilowattimmarna, som handlas på spotmarknaden och fysiskt går ut på nätet.
- **Attributet** - påståendet att en viss MWh producerades från en viss källa. En separat, handlbar rättighet.

En **ursprungsgaranti** (eng. *Guarantee of Origin*, GO) representerar attributet för 1 MWh producerad el, med uppgift om energikälla och anläggning. Inom EU utfärdas den under förnybartdirektivet, i Sverige av Energimyndigheten, och är giltig en begränsad tid efter produktionstillfället. Ett historiskt faktum förklarar mycket av dess problematik: ursprungsgarantin konstruerades för *fuel mix disclosure* - för att tala om för konsumenten hur stor andel förnybart elen innehöll - och lånades först senare in i klimatbokföringen via GHG Protocols Scope 2 Guidance. Ett upplysningsinstrument används alltså som om det vore en utsläppsmätning.

Eftersom de två marknaderna är åtskilda kan producenten sälja elektronen och garantin till olika köpare. Det ger två fall:

- **Bundlad.** Garantin följer med den fysiska leveransen från samma producent. Köper du el via ett avtal som inkluderar garantierna pekar fysisk leverans och anspråk på samma flöde.
- **Lös (obunden).** Garantin säljs avskild från elen. De fysiska elektronerna går ut på nätet och konsumeras som residualmix, medan garantin säljs separat till någon som vill kunna hävda förnybart. Köparen har ingen fysisk koppling till anläggningen.

Tre egenskaper gör den lösa garantin till en kompensationstransaktion snarare än en fysisk minskning:

- **Ingen fysisk förändring.** Köpet flyttar inte en elektron. Du drar samma nätmix som innan; bara bokföringssiffran ändras.
- **Residualmix gör det till nollsummespel.** När förnybara attribut strippas av och säljs som garantier blir den fysiska mix som blir kvar för alla andra smutsigare. Det du drar av läggs på någon annan. Systemets totala fysiska utsläpp är oförändrade.
- **Tveksam additionalitet.** En garanti från ett befintligt vattenkraftverk som ändå hade producerat ger ingen ytterligare klimatnytta. Marknaden för lösa garantier är dessutom tunn och billig, så priset signalerar knappt någon ny förnybar utbyggnad (se avsnitt 4).

## 2. Dotzauers kritik

Erik Dotzauer (Stockholm Exergi) har formulerat en samlad kritik mot ursprungsgarantier som i sak är korrekt för det system som råder idag. Invändningarna i korthet:

1. **Omfördelning utan ny förnybar el.** Systemet flyttar statistik snarare än att öka mängden förnybar produktion. Handeln är frikopplad från det fysiska elflödet.
2. **Geografisk frikoppling.** En garanti från Island kan användas i Sverige trots att elsystemen saknar fysisk koppling.
3. **Tidsmässig frikoppling.** Årsavräkning gör att en garanti från en sommarnatt med överskott kan täcka förbrukning en vindstilla vinterkväll.
4. **Additionalitet saknas.** Utbyggnaden drivs av starkare styrmedel (utsläppsrättshandel, skatter, stöd). Garantipremien är för svag för att påverka investeringar.
5. **Risk att styra fel.** Tillgodoräknat grönt värde i beslutsunderlag, exempelvis vid nybyggnation, kan dölja hög elanvändning vid topplast och leda till felaktiga konstruktionsval.

Invändningarna 1 till 3 är symptom på en gemensam rotorsak: attributet handlas separat från relationen. Det är möjligt enbart därför att redovisningen vilar på ett flödes- och attributkoordinat.

## 3. Möter MASSIV+ kritiken?

MASSIV+ löser inte garantiproblemet på elmarknadens egna villkor. Ansatsen byter ut det koordinatsystem som gör frikopplingen möjlig - och det avgör vilka invändningar som biter.

**Omfördelningskritiken (1, 2) biter inte, eftersom det inte finns något separat attribut att omfördela.** I MASSIV+ är en nods Scope 2 dess faktiska elförbrukning beräknad med standardens gemensamma emissionsfaktorer. Det finns ingen mekanism för att köpa ett fristående attribut som skriver om det värdet. Det som propagerar nedströms enligt principen *ditt Scope 1+2 är mitt Scope 3* är elproducentens eller elhandelsnodens faktiska utsläpp i relationen till just denna kund, inte en annullerad garanti hämtad från en annan tid och plats. Ett attribut som korsar 30 länder utan fysisk koppling bryter mot just den invariant massbalansen upprätthåller: summan ut ska vara lika med summan in per nod.

**Topplastsignalen (3, 5) adresseras i den mån nodens tidsupplösning tillåter.** Dotzauers skarpaste exempel - att garantier i byggnaders beslutsunderlag döljer förbrukning vid hög nätbelastning - hanteras bättre i MASSIV+ än av årsbaserade garantier, men inte automatiskt fullständigt. Avgörande är nodens granularitet i tid: om en elhandelsnod allokerar samma genomsnittliga emissionsfaktor över hela året återinförs en utslätning som liknar garantiernas. För att fånga topplastsignalen krävs att nodens Scope 2 och dess nedströmsallokering har tillräcklig tidsupplösning - samma riktning som GHG Protocols föreslagna timmatchning rör sig mot, men uppnådd genom relationens upplösning snarare än ett tidsstämplat certifikat.

**Additionalitet (4) ligger utanför vad standarden gör anspråk på.** Dotzauers djupaste poäng är att utbyggnaden drivs av andra styrmedel, inte av garantierna. MASSIV+ är ett redovisnings- och propageringssystem, inte ett styrmedel som finansierar ny produktion. Standarden löser additionalitetsproblemet i en svag mening - genom att inte skapa det, eftersom det inte finns något grönt mervärde att felaktigt tillgodoräkna. Men den driver inte i sig utbyggnad, och det vore ett överklaim att hävda annat. Det MASSIV+ däremot gör är att göra faktiska minskningar synliga: en elproducents övergång till fossilfri produktion sänker dess faktiska Scope 1+2 och syns i alla kundnoders Scope 3 nästa rapporteringsperiod. Det är en signaleffekt, inte en finansieringsmekanism.

### En tredje position

Det placerar MASSIV+ vid sidan av den vanliga axeln location mot market:

- Den **market-based**-metoden vilar på det fristående kontraktuella attributet. MASSIV+ har inget sådant attribut.
- Den **location-based**-metoden vilar på nätgenomsnittet. MASSIV+:s koordinat är inte nätmixen utan affärsrelationen mellan två parter.

MASSIV+ delar alltså location-baseds motvilja mot kontraktuell omskrivning, men vilar inte på nätgenomsnittet utan på den faktiska relationen. Baslinjen utan leverantörsdeklaration sammanfaller i praktiken med location-based (standardiserad nät-EF), men så snart en leverantörsnod deklarerar sin faktiska S1+2 ersätts genomsnittet av relationens verkliga siffra. Det är den rörelsen - från nätgenomsnitt till faktisk relation - som gör MASSIV+ till en tredje position snarare än en variant av någon av de två.

## 4. Prisbilden

Additionalitetsinvändningen vilar på en empirisk observation om prissignalen, och den står sig 2026:

- **Före 2021:** i snitt under 1 EUR/MWh, stort utbud, svag efterfrågan.
- **2022 till 2023:** kraftig topp på grund av torka och låg vattenkraftsproduktion i kombination med stigande företagsefterfrågan - nordisk vattenkraft noterades omkring 9,8 EUR/MWh i slutet av november 2022.
- **2024 och framåt:** nordisk vattenkraft åter omkring 1 EUR/MWh (Cal26 omkring 1,4), äldre årgångar med betydande rabatt.

Även under toppen drevs prisuppgången av hydrologi, inte av att systemet plötsligt fått styrverkan. Vid cirka 1 EUR/MWh är intäkten per producerad MWh för låg för att ensam påverka ett investeringsbeslut. Det bekräftar Dotzauers empiriska kärnpåstående. Samtidigt är det här de granulära garantierna kan ändra spelplanen: om timstämplade garantier skapar en väsentligt högre premie för el levererad vid knappa timmar kan signalen bli stark nog att påverka investeringar i lagring och flexibilitet. Den effekten är ännu inte påvisad i marknadsdata.

## 5. Det framväxande regelverket

Kritiken är inte avfärdad utan på väg att institutionaliseras: både GHG Protocol och EU rör sig mot de skärpningar som adresserar invändningarna.

### GHG Protocol, Scope 2-revisionen

Den första större översynen av Scope 2 sedan 2015, genom fyra tekniska arbetsgrupper. Det offentliga samrådet öppnade i oktober 2025 och stängde 31 januari 2026; ett reviderat utkast väntas senare under 2026, följt av en andra samrådsrunda, med en slutlig text omkring 2027 och stegvis implementering troligen från 2028. En statusförändring värd att notera är att dokumentet siktar på att bli en *Standard* snarare än dagens *Guidance*, vilket gör det mer bindande för de ramverk som hänvisar till det.

Tre föreslagna ändringar träffar precis de svagheter kritiken pekar ut:

- **Timmatchning.** Certifikat ska utfärdas och annulleras för samma timme som energin förbrukades, istället för att kvittas mot årsförbrukning. Angriper den tidsupplösning garantierna idag saknar (invändning 3 och 5).
- **Deliverability.** Certifikat ska komma från produktion som bedöms levererbar till den förbrukande lasten, istället för var som helst inom "samma marknad" (i praktiken nationsgränser). Riktar sig mot den geografiska frikopplingen (invändning 2).
- **Bibehållen dubbelrapportering, skärpt location-based.** Strukturen med både location-based och market-based behålls, och location-based skärps med en uppdaterad faktorhierarki och krav på de mest precisa tillgängliga faktorerna.

Eftersom timmatchning är dyrt och komplext föreslås övergångsåtgärder: lastprofiler, undantagströsklar för mindre organisationer under en ännu inte fastställd förbrukningsgräns, en legacy-klausul för befintliga kontrakt, och en flerårig utrullning. De trösklarna är centrala för mindre aktörer.

GHG Protocol ligger till grund för IFRS S2, EU:s ESRS/CSRD och Kaliforniens SB 253. Uppdateringar flödar dock inte automatiskt in i dessa ramverk utan kräver formell revidering, vilket innebär en fördröjning innan de slår igenom i regelefterlevnad.

### EU, granulära ursprungsgarantier

EU rör sig parallellt och snabbare på vissa punkter. RED III uppmuntrar tidsstämpling och fastställer att en garanti har standardstorleken 1 MWh men får delas i fraktioner ned till multiplar av 1 Wh. EECS-reglerna och utkastet till reviderad CEN-standard EN 16325 är redan kompatibla med timmatchning, så flaskhalsen är nationell implementering hos utfärdande organ, inte teknik eller EU-juridik.

Det skarpaste konkreta kravet gäller datacenter. Kommissionens utkast till delegerad förordning för hållbarhetsklassning av datacenter - samrådet stängde 23 april 2026, antagande planerat under Q2 2026 - föreslår 15-minuters, location-based matchning: garantier ska motsvara de 15-minutersperioder som sammanfaller med förbrukningen och komma från samma budområde som datacentret, villkorat av att sådana granulära garantier finns i medlemsstaten. Utkastet inför också ett additionalitetsliknande krav: garantierna ska komma från anläggningar tagna i drift högst tio år före rapportåret, med undantag för långsiktiga PPA:er med buntade garantier på plats senast 15 maj. EU:s 15-minutersupplösning är därmed finkornigare än GHGP:s timupplösning, och bindande tidigare.

## 6. Var MASSIV+ landar

Riktningen i både GHG Protocol och EU bekräftar MASSIV+:s grundinstinkt: rörelsen går från löst attribut mot faktisk fysisk, temporal och geografisk koppling. Regleringen försöker laga det attributsbaserade systemet inifrån - timmatchning, deliverability, tioårsregeln - och varje sådan reparation återinför en koppling till verkligheten som det ursprungliga koordinatet hade lossat. MASSIV+ behöver inte reparera den kopplingen eftersom det aldrig bröt den: relationen mellan två parter är fysiskt och ekonomiskt verklig från början.

Eftersom MASSIV+ aldrig bakat in det omstridda instrumentet i den propagerande substansen är positionen robust oavsett var revisionen landar. Den fysiska A/U-linjen står stilla medan certifikatreglerna ändras, och båda GHG-talen kan rekonstrueras vid rapporteringsgränsen (se [Köpt energi och Scope 2, avsnitt 5-6](kompensation-och-faktiska-floden.md#5-tre-register-inte-två)).

Några frågor återstår, och de är genuint öppna:

- **Elhandelsnoden.** Bör elhandelsbolaget modelleras som en egen nod mellan producent och förbrukare, och hur allokeras i så fall producenternas faktiska Scope 1+2 genom en handelsnod som blandar många källor?
- **Residualmix mot U.** Om en förbrukarnod saknar A-data uppströms och faller tillbaka på U - hur förhåller sig den hanteringen till residualmix-begreppet i location-based-metoden? I location-based bär de som strippar garantier ansvaret för en smutsigare residual; i MASSIV+ är fallbacken okänt (U), inte en omfördelad mix.
- **Nodens tidsupplösning.** Vid vilken granularitet bör en elhandelsnod allokera Scope 2 nedströms för att topplastsignalen ska bevaras?

---

## Källor

- Erik Dotzauer, "Ursprungsgarantier för el riskerar att styra fel", Second Opinion (Energiföretagen Sverige).
- [Om ursprungsgarantier - Energimyndigheten](https://www.energimyndigheten.se/ursprungsgarantier)
- [GHG Protocol Scope 2 Guidance](https://ghgprotocol.org/scope-2-guidance)
- [GHG Protocol - publika konsultationer om Scope 2 och konsekvensbaserad elredovisning](https://ghgprotocol.org/blog/release-ghg-protocol-opens-public-consultations-scope-2-and-electricity-sector-consequential)
- [EU Renewable Energy Directive - targets and rules](https://energy.ec.europa.eu/topics/renewable-energy/renewable-energy-directive-targets-and-rules_en)
- [EU draft sets granular GOO rules for data centres - Argus Media](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2818021-eu-draft-sets-granular-goo-rules-for-data-centres)
- CEN-EN 16325 (utkast) samt branschsammanställningar (Bird & Bird, GSI Environmental, Future Energy Go) av Scope 2-revisionen och GO-priser.

---

*Fristående fördjupning, sammanställd juni 2026. Bygger på dialog i MASSIV+-projektet och offentliga källor om den pågående regleringen. Motargument i debatten (bl.a. om en positiv grön premie räcker som investeringssignal) finns men är ännu inte vägda; de behandlas i det interna underlaget.*
