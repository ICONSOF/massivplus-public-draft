---
layout: default_banner
title: "Specifikation"
parent: "Standard"
nav_order: 2
---

# MASSIV+ - Teknisk specifikation

Den här texten är den fullständiga tekniska specifikationen av MASSIV+. För en mjukare ingång rekommenderas [introduktionen](../introduktion.md). För positionering mot andra ramverk och affärsvärde, se [positionering/](../positionering/); för konceptuella fördjupningar och metodologiska risker, se [fordjupningar/](../fordjupningar/).

---

## Sammanfattning

**MASSIV+ är en öppen standard för beräkning och propagering av utsläppsdata i värdekedjor på organisationsnivå.** Standarden adresserar ett praktiskt tomrum mellan dagens alternativ: bolagsnivådata är för grov för att vägleda åtgärder, medan produktnivåberäkning (PCF) kräver en datainfrastruktur som de flesta aktörer saknar.

Värdekedjan modelleras som ett riktat nätverk av noder. Varje nod rapporterar sina egna Scope 1- och Scope 2-utsläpp med ett gemensamt, fastställt set av emissionsfaktorer, och allokerar dem proportionellt vidare till sina kunder. Mottagaren bygger därmed sin Scope 3 nedifrån av faktisk data, snarare än uppifrån med branschschabloner.

Standarden vilar på tre principer: **(1) ditt Scope 1+2 är mitt Scope 3**; **(2) faktisk data eller okänt** - ingen uppskattning får samma status som faktisk data, och datakvalitet kvantifieras via ett Coverage-mått; **(3) standardiserade emissionsfaktorer** som gör data jämförbara mellan aktörer. Massbalansen per nod säkerställer att utsläppsmassa varken skapas eller försvinner i propageringen, och okända värden ersätts progressivt av faktisk data utan att modellen behöver rekonstrueras.

Resultatet är ett operativt flödessystem som möjliggör KPI:er för kontinuerlig utsläppsminskning - år för år eller kvartalsvis - både internt och som krav eller incitament mot leverantörer. För inköparen blir det ett upphandlingsverktyg där krav kan riktas exakt mot leverantörer med låg datakvalitet; för leverantören räcker en deklaration mot samtliga kunder utan att exponera affärsdata.

En central praktisk egenskap är att standarden **kan tillämpas unilateralt**. Ett enskilt bolag kan börja rapportera idag utan att invänta att leverantörer eller kunder ansluter - leverantörer som ännu inte deltar bokförs som okänt (U) och konverteras till faktisk data (A) när de senare börjar rapportera. Nyttan ökar med varje aktör som ansluter, men värde uppstår redan från första dagen.

MASSIV+ kompletterar etablerade ramverk (GHG Protocol, ISO 14064-1, ISO 14067, EPD, PACT, Catena-X, DPP, PCAF) genom att tillföra det operativa flödeslager som idag saknas - en spårbar koppling mellan utsläpp och leverans i värdekedjan. Andras data är primärdata in i MASSIV+-noder, och MASSIV+-data kan användas som primärdata i deras beräkningar och rapporter.

---

## Bakgrund och syfte

Klimatomställningen är i grunden en handlingsfråga: den kräver att organisationer aktivt minskar sina utsläpp. Många bolag har idag uttalade netto-noll-mål, men för att nå dem måste de veta var utsläppen faktiskt uppstår och vad som kan göras för att minska dem. Utan den kunskapen, och utan handgripliga sätt att agera på den, sker omställningen inte.

Faktisk, verklig klimatdata är förutsättningen - inte uppskattningar baserade på branschgenomsnitt eller schabloniserade emissionsfaktorer. Det är skillnaden mellan att veta var utsläppen faktiskt uppstår och att tro sig veta det. Utan verklig data kan man inte fatta välgrundade beslut om var insatser ger störst effekt.

I praktiken stöter de flesta aktörer på ett strukturellt dilemma när det gäller granularitetsnivån på klimatdata:

**Bolagsnivå är för bred.** Årsredovisningar och aggregerade hållbarhetsrapporter på koncern- eller bolagsnivå - även när de följer GHG Protocol och CSRD-krav - kan ofta visa vilka kategorier som driver utsläppen, men inte vilka delar inom kategorin - vilka anläggningar, flöden eller leverantörsrelationer - som är de faktiska källorna. Gapet mellan kategori- och åtgärdsnivå gör att data inte är operativt användbar för konkret klimatåtgärd.

**Produktnivå är för svårt.** I andra änden av spektrumet finns den detaljerade produktkoldioxidberäkningen (PCF - Product Carbon Footprint), som spårar utsläpp per enskild produkt längs hela värdekedjan. Det är metodologiskt precist, men i praktiken oåtkomligt för de flesta aktörer. Hindren är flera: tid (en PCF-analys är ett betydande arbete), kompetens (LCA-expertis är en specialiserad färdighet), och faktisk data (många företag producerar sina produkter i flera steg fördelade på olika anläggningar och spårar helt enkelt inte produktnivådata internt). Tillsammans gör de att PCF kräver en datainsamlings- och kompetensinfrastruktur som de flesta saknar.

Däremellan finns ett praktiskt tomrum: data på **anläggnings- eller organisationsenhetsnivå** är ofta tillräckligt detaljerat för att vara operativt meningsfullt, och tillräckligt aggregerat för att vara realistiskt att samla in. Det är just i detta tomrum MASSIV+ är utformat att verka.

En första observation är att värde uppstår redan på enskild nod-nivå. Att en organisation börjar mäta och rapportera sina egna Scope 1+2-utsläpp - även utan koppling till värdekedjan ovanför eller nedanför - är ett självständigt värdeskapande steg. Det ger organisationen den kunskapsbas som krävs för att börja agera. Värdekedjepropageringen som MASSIV+ möjliggör kommer in i nästa skede: när det handlar om att *visa* effekten av åtgärderna, både inåt mot ledning och utåt mot kunder och regleringsmyndigheter. Värdet ligger i båda lagren - kunskapsbasen som möjliggör handling, och värdekedjepropageringen som gör effekten synlig och verifierbar.

Ramverket är konstruerat kring en tydlig dikotomi: antingen finns faktisk, primär data - eller så är utsläppen **okända**. MASSIV+ använder medvetet inte begreppet "uppskattning", eftersom det antyder en kvalificerad gissning med implicit precision. Okända utsläpp är okända - de hanteras som temporära platshållare som successivt ska ersättas av faktisk data, men utan att ge dem en precision de inte har.

Den mest grundläggande operativa principen i MASSIV+ är att **ditt Scope 1 och 2 är mitt Scope 3**. Istället för att varje bolag självständigt försöker uppskatta sina leverantörers utsläpp - vilket är GHG Protocols Scope 3-logik - fokuserar MASSIV+ på att varje nod etablerar sina faktiska Scope 1- och Scope 2-utsläpp och delar dessa nedströms. Scope 3 byggs upp nedifrån med faktisk data snarare än skattas uppifrån med schabloner. Det är det som gör systemet meningsfullt: varje förbättring i en leverantörs Scope 1+2-rapportering förbättrar direkt kvaliteten på kundens Scope 3-bild.

Den djupare logiken bakom denna princip är att flytta informationsarbetet dit data faktiskt finns. Under traditionell Scope 3-rapportering gissar köparen uppifrån trots att leverantören är den enda som har relevant data - och leverantören har samtidigt negativt incitament att dela den eftersom detaljerade volyms- och energidata kan användas i prisförhandlingar. MASSIV+ inverterar ordningen: leverantören gör sin egen beräkning, allokerar enligt en standardiserad regel, och delar bara den färdiga siffran. Det är samma princip som etablerade produktnivåstandarder (EPD, ISO 14067, PACT) tillämpar för enskilda produkter - MASSIV+ generaliserar den till organisationsnivå.

En direkt konsekvens av denna princip är kravet på **standardiserade emissionsfaktorer**. Om Scope 1+2-data ska vara jämförbara och meningsfulla som Scope 3 hos mottagaren måste de vara beräknade med samma underlag. MASSIV+ tillhandahåller därför ett gemensamt, fastställt set av emissionsfaktorer per bränsleslag och energibärare som samtliga noder är skyldiga att använda. Det eliminerar den godtycklighet i emissionsfaktorval som annars gör Scope 1+2-data ojämförbara tvärs aktörer och sektorer.

MASSIV+ är en **öppen standard för beräkning och propagering av utsläppsdata i värdekedjor**. Standarden definierar reglerna - hur Scope 1+2 beräknas, vilka emissionsfaktorer som gäller, hur utsläpp allokeras och propageras mellan noder, och hur faktisk och okänd data hålls isär. Ovanpå standarden kan ett ekosystem av verktyg och tjänster byggas av kommersiella aktörer. Standarden förvaltas av en central organisation som ansvarar för metodinnehåll, emissionsfaktorer och versionskontroll. Teknisk infrastruktur för peer-to-peer datadelning mellan aktörer - baserad på data spaces-arkitektur - ingår i den tekniska visionen men beskrivs i separata tekniska dokument.

---

## 1. Systemdefinition - värdekedjan som nätverk

MASSIV+ modellerar värdekedjan som ett **riktat nätverk av noder**. Att nätverket är *riktat* innebär att varje koppling har en bestämd riktning: utsläppsflöden rör sig från uppström till nedström, från leverantör mot kund. En nod tar emot flöden från sina leverantörer och skickar flöden till sina kunder, aldrig i omvänd ordning inom samma beräkningssteg. Riktningen är vad som möjliggör propagering med bevarad massbalans. En nod är den minsta organisatoriska enhet som:

- Mäter sina egna Scope 1- och Scope 2-utsläpp
- Tar emot allokerade utsläppsflöden från uppströmsnoder
- Allokerar utsläppsflöden vidare till nedströmsnoder

Begreppet "organisatorisk enhet" är medvetet generiskt. En nod kan vara ett helt bolag, en produktionsanläggning, en produktionslinje, en avdelning, en fordonsflotta, eller vilken annan konsekvent definierad enhet som helst. Standarden är agnostisk till nivå. Granularitetsvalet är samtidigt relevansspaken: en finare nod låter A-värdet spegla den faktiska leveransen närmare, medan en grövre nod ger ett mer utslätat snitt. Avvägningen mot insamlingsbördan är användarens.

### Krav på noddefiniering

Granulariteten är användarens val, men nodpartitionen måste uppfylla fyra krav:

1. **Heltäckning.** Varje S1+S2-utsläpp i organisationen tillhör exakt en nod. Inget utsläpp får ligga utanför nätverket. Administrativa byggnader, lager, testanläggningar och transportflottor inkluderas precis som produktionsanläggningar.
2. **Ingen överlapp.** Ingen utsläppskälla får ligga i mer än en nod.
3. **Intern konsistens per nod.** En nods granularitet är enhetlig inom noden. Mellan olika noder kan granulariteten variera: huvudfabriken kan vara modellerad på linjenivå medan administrationen utgör en enda nod.
4. **Konsekvent över tid.** Nodpartitionen ändras inte mellan rapporteringsperioder utan explicit versionskontroll, och hela uppdelningen ska vara dokumenterad.

Rapporteringsentiteten (juridisk person, koncern, division eller annan enhet som heltäckningskravet gäller för) ska deklareras explicit och hållas konsekvent över tid. Standarden överlåter åt rapporterande organisation att välja entitet, men kräver att valet är dokumenterat och inte ändras mellan perioder utan versionskontroll.

### Hantering av delade resurser

Krav: när en nods granularitet är finare än vissa försörjningsflöden ska de delade utsläppen täckas av nodpartitionen utan att hamna utanför nätverket eller dubbelräknas mellan noder.

**Exempel på lösningar:**

- *Aggregera upp:* välj en nodnivå som rymmer den delade resursen, så att exempelvis hela fabriken inklusive central ventilation utgör en enda nod istället för en nod per produktionslinje.
- *Egen nod för delad resurs:* den delade resursen blir en separat nod som mäter sina egna S1+S2 och allokerar dem internt till de förbrukande noderna med samma allokeringslogik som mellan externa leverantörer och kunder.

---

## 2. Utsläppskomponenter per nod

För varje nod *i* definieras fyra grundläggande komponenter:

| Beteckning | Beskrivning |
|---|---|
| **S1ᵢ** | Scope 1 - direkta utsläpp |
| **S2ᵢ** | Scope 2 - indirekta utsläpp från inköpt energi |
| **Aᵢ** | Upstream Actual - uppströmsutsläpp baserade på faktisk data |
| **Uᵢ** | Upstream Unknown - okända uppströmsutsläpp |

Nodens totala utsläppsmassa beräknas som:

```
Tᵢ = S1ᵢ + S2ᵢ + Aᵢ + Uᵢ
```

### Standardiserade emissionsfaktorer för Scope 1 och 2

Eftersom ditt Scope 1 och 2 är andras Scope 3 är det avgörande att S1+S2-data är beräknad på ett enhetligt och jämförbart sätt. MASSIV+ tillhandahåller därför ett gemensamt, fastställt set av emissionsfaktorer per bränsleslag och energibärare som samtliga noder är skyldiga att använda - inga egna emissionsfaktorer tillåts för dessa komponenter. Det gör att S1 och S2 är fullt jämförbara mellan noder, sektorer och länder, och att den godtycklighet i emissionsfaktorval som annars gör Scope 3-data inkonsistent är eliminerad i systemets kärna. Emissionsfaktorerna förvaltas centralt, uppdateras periodiskt och är publikt dokumenterade.

### Separation av faktisk och okänd data

En central princip i MASSIV+ är att **Aᵢ och Uᵢ aldrig aggregeras utan attribution**. Skiljelinjen är strikt: Aᵢ är emissionsdata med faktisk grund; Uᵢ är ett kvantifierat täckningsunderlag för den del av uppströmsflödet där sådan grund saknas. Modellen behandlar A och U matematiskt lika för att kunna beräkna Coverage och upprätthålla massbalans i propageringen - men håller dem isär i syfte att möjliggöra transparens, spårbarhet och progressiv förbättring. Uᵢ är alltså inte ett utsläppsanspråk med antagen precision, utan en markering av att denna del av emissionsbilden ännu inte är etablerad som faktisk data.

Det praktiska värdet av denna separation är att mottagaren av ett utsläppsflöde alltid kan se *hur stor del av det inkommande värdet som är grundat i faktisk mätning*, och därmed fatta informerade beslut om datakrav och osäkerhetsmarginaler.

A-värden förutsätter att leverantören själv har utfärdat en MASSIV+-deklaration för sina Scope 1+2. Externa primärdatakällor (EPD, PCF, PACT/Catena-X) kan användas som grund för mer välunderbyggda U-underlag hos mottagaren, men räknas inte som A - distinktionen handlar om ansvarig avsändare, inte om numerisk kvalitet.

### U-värdets roll

För att Coverage ska kunna beräknas krävs ett numeriskt underlag även för den del av uppströmsflödet som ännu inte har faktisk datagrund. Detta underlag kan tas fram med bästa tillgängliga metod - exempelvis spend, fysisk volym, produktdata, sektordata eller annan rimlig proxy - men dess roll i MASSIV+ är begränsad.

U-värdet används för att:

- beräkna Coverage, dvs. andelen faktisk data i relation till total känd + okänd emissionsmassa
- visa var primärdata saknas och var datainsamling bör prioriteras
- möjliggöra konsekvent allokering och replacement rule när faktisk data senare tillkommer

U-värdet används inte för att hävda att utsläppen faktiskt uppgår till det numeriska underlagets belopp. Underlaget är medlet för att kvantifiera avsaknaden av faktisk data; den centrala MASSIV+-informationen är A-värdet och Coverage. När MASSIV+-data används i en CSRD-, ESRS- eller GHG Protocol-kontext kan U-värdet eller en separat residualberäkning användas som uppskattad residual, men den ska då redovisas som estimat enligt det externa ramverkets regler och inte blandas in i MASSIV+-deklarationens A-komponent.

---

## 3. Allokering - att fördela utsläpp till mottagare

Varje nod väljer en proportionell allokeringsmetod baserad på utflödets fysiska eller ekonomiska egenskaper. Följande metoder är tillåtna:

- **Massbaserad allokering** - fördelning efter vikt
- **Energibaserad allokering** - fördelning efter energiinnehåll
- **Kvantitetsbaserad allokering** - fördelning efter antal enheter eller volym
- **Monetärbaserad allokering** - fördelning efter intäkt eller värde
- **Annan dokumenterad proportionell metod**

### Krav på allokeringsregeln

Allokeringsregeln gäller för nodens hela utsläppsmassa Tᵢ, och ska tillämpas konsekvent inom en rapporteringsperiod. Regeln får uppdateras mellan perioder, men ej retroaktivt utan explicit versionskontroll och flaggning.

---

## 4. Allokeringsformel - matematisk definition

Om nod *i* levererar till kund *j* med andelen **Shareᵢⱼ**, beräknas utsläppsflödet som:

```
Tᵢⱼ = Tᵢ × Shareᵢⱼ
```

Faktiska och okända utsläpp allokeras separat:

```
Actualᵢⱼ  = (S1ᵢ + S2ᵢ + Aᵢ) × Shareᵢⱼ
Unknownᵢⱼ = Uᵢ × Shareᵢⱼ
```

Den mottagande noden *j* uppdaterar sina ackumulerade värden:

```
Aⱼ += Actualᵢⱼ
Uⱼ += Unknownᵢⱼ
```

Denna formel garanterar tre egenskaper: strikt massbalans, separat propagering av faktiska och okända utsläpp, samt frånvaro av över-allokering inom systemet.

---

## 5. Massbalansprincipen - systemets invarians

Massbalansen är systemets **centrala invariansregel**. För varje nod *i* gäller att summan av alla utgående flöden ska motsvara nodens totala utsläppsmassa:

```
Σⱼ (Tᵢⱼ) = Tᵢ
```

Enkelt uttryckt: *det som går ut måste motsvara det som finns inne*.

Massbalansen är en *konserveringsprincip*: utsläppsmassa varken skapas eller försvinner i propageringen. Den förhindrar både *över-allokering* (Σ Share > 1, där en nod skickar ut mer än den har) och *under-allokering* (Σ Share < 1, där en nod tappar utsläpp på vägen). Allt som finns i en nod kommer ut, varken mer eller mindre.

Massbalansen är en lokal disciplinregel per nod. Den förutsätter inte central överblick över nätverket - varje nod upprätthåller sin balans oberoende av om nedströms noder existerar eller hämtar data.

MASSIV+ skiljer mellan två typer av utgående flöden. Ett nod-till-nod-flöde är ett flöde till en mottagande nod som kan ta emot och propagera utsläppsvärdet vidare - det allokerade värdet blir Scope 3 hos mottagaren. Ett nod-till-konsument-flöde är ett flöde till slutkonsument utanför systemet - kedjan terminerar och inget Scope 3 genereras hos en mottagande nod. Båda flödestyperna lyder under samma allokeringslogik och samma massbalansregel. Noder som enbart levererar till slutkonsumenter är ett normalfall i MASSIV+, inte ett undantag.

### Från affärsrelation (B2B) till produktinformation (B2C)

MASSIV+ följer affärsrelationen genom kedjan. Så länge en leverans går från företag till företag (B2B) bär mottagaren en organisationsallokerad börda och propagerar den vidare. När leveransen når en slutkonsument (B2C) terminerar kedjan, och först då översätts den ackumulerade bördan till produktinformation. Resten av avsnittet definierar denna gräns och den upplösning som sker vid den.

Propageringen fortsätter så länge mottagaren är en nod och avslutas när mottagaren inte är det. En mottagare som saknar eget Scope 1+2 och nedströms affärsrelation - typiskt en privatkonsument - är en *sänka*, och vid en sänka terminerar kedjan. Gränsen för propageringen är alltså gränsen mellan nod och icke-nod, inte en produktgräns.

Vid terminering mot en sänka löser den sista noden upp sin utgående allokering till den levererade enheten: den inkommande organisationsallokerade bördan plus nodens eget Scope 1+2 fördelas på de enskilda enheter som levereras till sänkan, eftersom en sänka inte kan ta emot en organisationsallokering. Denna produktupplösning är avgränsad till terminerande flöden mot en sänka. I nod-till-nod-flöden allokeras alltid till mottagande nod, aldrig till produkt.

### Individuation av allokeringsenheten

En nods allokering per affärsrelation (§3) får vara godtyckligt finkornig - per kund, per leverans, per kvalitet - och förblir i organisationskoordinaten så länge det allokerade talet är en egenskap hos *relationen* och inte hos den fysiska artefakten. Det operativa kriteriet är individuation: talet ska variera med motparten, inte med godset. Ett tal som sätts på en fysisk enhet och följer med den oavsett köpare är en produktallokering, och en sådan tillåts endast vid terminering mot en sänka enligt ovan.

---

## 6. Replacement Rule - progressiv dataförbättring

När en uppströmsleverantör etablerar faktisk primärdata för utsläpp som tidigare var okända tillämpas följande procedur:

1. Det okända värdet tas bort från **Uᵢ**
2. Det faktiska värdet läggs till i **Aᵢ**
3. Nodens totala utsläpp **Tᵢ** uppdateras i enlighet med detta
4. Uppdaterade värden propageras och allokeras i efterföljande rapporteringsperioder

Faktisk data *ersätter* okända värden - den läggs inte ovanpå dem. Förbättringen sker i praktiken när ett bolag successivt får tillgång till mer verklig primärdata: när en leverantör börjar mäta sina egna utsläpp, när en anläggning installerar mätning, eller när ett avtal specificerar rapporteringskrav.

Att etablera A-värdet kräver primärdata och kompetens hos den nod som tar steget, eftersom det är där den verkliga datan finns. När detta är gjort sker propageringen mekaniskt enligt standardens regler: okänt värde tas bort från U, faktiskt värde läggs till i A, ackumulerade totaler och Coverage omberäknas, och uppdaterade värden propageras till nedströms noder i efterföljande perioder. Att processen är välspecificerad gör att den kan automatiseras av verktygsimplementationer, men automatiseringen är en implementationsfråga och inte del av standardens specifikation.

Den praktiska konsekvensen är att ett bolag kan **börja rapportera idag med de data som finns** - inklusive okända utsläpp för leverantörer som ännu inte rapporterar - och gradvis ersätta dessa med faktisk data i takt med att den blir tillgänglig. Varje förbättring förbättrar direkt den bild som syns nedströms i kedjan.

### Konsekvenser av replacement rule

- **Ingen ackumulering** - okända värden ersätts, läggs inte ovanpå
- **Dynamisk förbättring** - datakvaliteten förbättras utan att modellstrukturen behöver rekonstrueras
- **Progressiv precisering av Scope 3** - den okända andelen konverteras gradvis till faktisk data

Replacement rule höjer andelen faktisk data. En andra form av progressiv förbättring sker när nodgranulariteten förfinas: ett bolagssnitt ersätts av linje- eller produktfamiljsdata för den faktiska leveransen, under nodpartitionens versionskontroll (§1). Den första klättringen gör bilden mer faktisk, den andra mer relevant.

---

## 7. Cirkulära flöden

I verkliga värdekedjor förekommer ömsesidiga leveransrelationer - nod A köper av nod B och nod B köper av nod A. Detta är ett normalt inslag - inte ett undantag - i industriella nätverk som kemi, stål och energi. MASSIV+ tillåter sådana relationer utan att användaren behöver justera sin noddefinition eller ta hänsyn till om en kund också är leverantör.

Cirkuläritet uppstår beräkningsmässigt när utsläppsvärdet för nod A beror på nod B:s värde, som i sin tur beror på nod A:s värde. En enkel sekventiell propagering nod för nod saknar en startpunkt och fastnar. Det är ett tekniskt beräkningsproblem - inte ett användarens problem - och standarden kräver att det hanteras transparent utan att användaren behöver agera.

MASSIV+ specificerar två tillåtna metoder för att lösa cirkulära beroenden:

**Matrisinversion.** De noder som ingår i det cirkulära beroendet sätts upp som ett linjärt ekvationssystem och löses simultant. Ger exakt svar för den aktuella perioden utan tidsfördröjning. Tekniskt välbeprövat - används i LCA-verktyg och input-output-analys.

**Tidssegmentering.** Det cirkulära ledet bryts via föregående rapporteringsperiods data. Enklare att implementera; introducerar en ett-periods fördröjning i det cirkulära ledet, vilket i praktiken är acceptabelt givet att rapportering är periodisk.

Valet mellan metoderna är en teknisk implementeringsfråga för verktyg som bygger på standarden, och specificeras i separata tekniska dokument. Från användarens perspektiv är beteendet detsamma: deklarera relationer och volymer - beräkningen hanteras av verktyget.

---

## 8. Coverage - mått på datakvalitet

För varje nod *i* definieras ett **Coverage-mått** som anger andelen utsläpp som baseras på faktisk primärdata:

```
Coverageᵢ = Aᵢ / (Aᵢ + Uᵢ)
```

Coverage indikerar **datakvalitet**, inte utsläppsnivå. Det är en viktig distinktion: ett högt Coverage-värde innebär att en stor andel av emissionsbilden har faktisk datagrund - inte att utsläppen är låga. Omvänt innebär lågt Coverage att en stor del av emissionsbilden ännu saknar faktisk grund. Det numeriska U-underlaget behövs för att beräkna andelen, men det är Coverage-värdet - inte U-underlaget i sig - som är den primära datakvalitetssignalen.

Coverage mäter en axel: andelen utsläpp med faktisk grund. Relevansen hos den faktiska delen ligger på en andra axel, som styrs av nodgranulariteten (§1). Ett bolagssnitt allokerat per intäkt och en linjespecifik allokering för just den linje som betjänar kunden kan båda ha Coverage 1,0, medan den senare ligger närmare den faktiska affären och därmed är mer relevant för mottagaren. Ju finare nod, desto närmare ligger A-värdet den faktiska leveransen. Relevansaxeln kan i en kommande version ges ett eget mått; redan nu bör den läsas som en andra kvalitetsdimension vid sidan av Coverage.

I praktiken används Coverage-måttet för att prioritera var insatser på datainsamling ger störst effekt: en nod med lågt Coverage som svarar för en stor andel av systemets totala utsläppsmassa är där förbättring av primärdata ger störst genomslag.

---

## 9. Sammanfattning av standarden

MASSIV+ är en öppen standard för beräkning och propagering av utsläppsdata i värdekedjor. Standarden vilar på tre grundläggande principer:

- **Ditt Scope 1+2 är mitt Scope 3.** Varje nod etablerar sina egna faktiska Scope 1- och Scope 2-utsläpp och delar dessa nedströms. Scope 3 byggs upp nedifrån av faktisk data, inte skattas uppifrån med schabloner.
- **Faktisk data eller okänt.** Ingen uppskattning får samma status som faktisk data. Antingen finns faktisk primärdata (A) eller så är utsläppen okända (U). Dessa hålls alltid åtskilda och kvantifieras via Coverage-måttet.
- **Standardiserade emissionsfaktorer.** Alla noder använder samma gemensamma set av emissionsfaktorer för Scope 1+2 - per bränsleslag och energibärare - vilket gör data jämförbara tvärs aktörer och sektorer.

Standardens tekniska regler säkerställer:

| Egenskap | Mekanism |
|---|---|
| Massbevarande | Massbalansprincipen: summan av allokerade flöden = nodens totala utsläpp |
| Datakvalitet är synlig | Coverage = Aᵢ/(Aᵢ+Uᵢ) per nod, propageras nedströms |
| Progressiv förbättring | Replacement rule: okända värden ersätts av faktisk data |
| Cirkulära relationer hanteras | Matrisinversion eller tidssegmentering enligt teknisk specifikation |
| Nodsymmetri | Samma regler gäller alla aktörer oavsett storlek eller sektor |

Standarden förvaltas av en central organisation. Verktyg och tjänster som implementerar standarden kan byggas och säljas av kommersiella aktörer. Teknisk infrastruktur för datadelning mellan noder beskrivs i separata tekniska dokument.

---

## 10. Vidare läsning

Tre teman som tidigare ingick i den här texten ligger numera i egna dokument under [positionering/](../positionering/) och [fordjupningar/](../fordjupningar/), eftersom var och en bär en självständig poäng och kan läsas fristående:

- **[Metodologiska risker och begränsningar](../fordjupningar/metodologiska-risker.md)** - var standarden är strukturellt svag (dubbelräkning av okända utsläpp, cirkularitet, regulatorisk och tolkningsrisk) och hur svagheterna hanteras.
- **[Jämförelse med andra ramverk](../positionering/jamforelse-med-andra-ramverk.md)** - hur MASSIV+ förhåller sig till GHG Protocol, ISO 14064-1, ISO 14040/44, ISO 14067, EPD/ISO 14025, PACT, Catena-X, DPP och PCAF. Innehåller även den övergripande jämförelsetabellen.
- **[Positionering och affärsvärde](../positionering/positionering-och-affarsvarde.md)** - varför detta är värt att göra för inköpare, leverantör, stor och liten, och var i landskapet av befintliga ramverk MASSIV+ sitter.

Övriga fördjupningar som inte var del av tidigare versioner av denna specifikation:

- **[Bokföringsanalogin](../fordjupningar/bokforingsanalogin.md)** - den strukturella parallellen till dubbel bokföring som positioneringsverktyg.
- **[Exempel: grönt stål i fordonsvärdekedjan](../fordjupningar/exempel-gront-stal.md)** - konkret illustration av principerna i en verklig kedja.
- **[MASSIV+ vs processbaserad LCA](../positionering/massiv-vs-ecoinvent.md)** - är en MASSIV+-nod "bara" ett cradle-to-gate-dataset?
- **[Koordinatbytet](../fordjupningar/koordinatbytet.md)** - varför brottet mot livscykeltraditionen är ett byte av grundkoordinat (affärsrelation i stället för fysiskt flöde), inte en skillnad i hållning.
- **[Produktnivå-invändningen](../fordjupningar/produktniva-invandningen.md)** - argumentet bakom terminering mot sänka och individuation ovan: varför produktupplösning uppstår emergent vid sänkan i stället för som en andra koordinat genom kedjan.
- **[Incitament och konsumtionsled](../fordjupningar/incitament-och-konsumtionsled.md)** - var incitamentet att välja lägre uppströmspåverkan bor, och hur gate-talet vid sänkan förhåller sig till konsumtionsledsmekanismer.


