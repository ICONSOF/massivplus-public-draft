---
layout: default_banner
title: "Metodologiska risker"
parent: "Fördjupningar"
nav_order: 4
---

# Metodologiska risker och begränsningar

> **Poäng:** Var MASSIV+ är strukturellt svagt, hur svagheterna hanteras, och vad som ännu är öppet. En öppen genomgång av riskerna är förutsättningen för att standarden ska kunna granskas och vidareutvecklas på sina egna villkor.

Den här texten kan läsas fristående. Den förutsätter en grundläggande bild av hur MASSIV+ fungerar - läs [introduktionen](../introduktion.md) eller [specifikationen](../standard/specifikation.md) först om du inte är bekant med ramverket. För uppstartsfasens praktiska friktion, se [uppstartsfriktion](uppstartsfriktion.md); här behandlas det principiella.

Varje risk anges med en status: **mitigerad** (hanterad av en regel i standarden), **hanterad i riktning** (lösningsväg vald men ännu inte normerad i specifikationen), eller **öppen**. Flera av riskerna delas med etablerade ansatser - LCA, EPD, GHG Protocol Scope 3. Där så är fallet sägs det: en risk som är oförändrad eller mildare än i dagens praxis är fortfarande värd att redovisa, men den är inte ett argument mot bytet.

---

## Verifiering och förtroende

### Konsistens är inte korrekthet

Massbalansen garanterar att inget skapas eller försvinner i propageringen - den garanterar inte att indata är sanna. En nod som underrapporterar sin Scope 1 propagerar felet nedströms med full matematisk precision, och en A-deklaration vilar på att avsändaren står bakom den. Systemets trovärdighet beror alltså på något utanför modellen: att indata går att lita på.

**Hanterad i riktning:** en trappad verifieringsstruktur. Mindre aktörer självdeklarerar enligt standarden - samma modell som CE-märkning, där tillverkarens egenförsäkran mot en harmoniserad standard bär ansvaret. Större aktörer certifieras av tredje part. Var gränsen går, och det exakta verifieringskravet för att en leverantörsdeklaration ska räknas som A (se [köpt energi, avsnitt 10](kompensation-och-faktiska-floden.md#10-var-gränsen-går)), är normativa val som återstår att fastställa.

### Konfidentialitet mot revision

Att granska en nods massbalans kräver insyn i nodens samtliga relationer och volymer - exakt det data konfidentialiteten skyddar. Spänningen är mekanisk, inte abstrakt: systemets bärande invariant kan inte kontrolleras utifrån utan att röja det som gör att leverantörer vågar delta.

**Hanterad i riktning:** samma modell som finansiell revision alltid använt. Granskaren ser hela huvudboken under tystnadsplikt; marknaden ser bara revisionsberättelsen. Verifieringstrappan ovan bär denna roll.

### Cirkularitet och verktygskonsistens

Ömsesidiga leveransrelationer hanteras via matrisinversion eller tidssegmentering (se [specifikationen, avsnitt 7](../standard/specifikation.md#7-cirkulära-flöden)). Risken är att olika verktyg implementerar detta inkonsekvent, så att samma nätverk ger olika tal beroende på systemval.

**Hanterad i riktning:** central certifiering av systemlösningar - förvaltningsorganisationen certifierar att implementationer räknar rätt, på samma sätt som verifieringstrappan certifierar att noder rapporterar rätt.

---

## Manipulerbarhet

### U-kvantifieringen och Coverage-måttet

Coverage = (S1 + S2 + A) / T, där T = S1 + S2 + A + U, och U kvantifieras med en proxy. Om proxyvalet är fritt kan en nod välja ett lågt U-underlag och få både högre Coverage och lägre totalbild i ett drag - kvalitetsmåttet blir känsligt för just den godtycklighet i skattningar som standarden eliminerar på A-sidan.

**Hanterad i riktning:** standardisera proxykällan. U kvantifieras top-down med EEIO-data (miljöutvidgad input-output-analys, till exempel Exiobase): billigt, enkelt och medvetet konservativt. Det låser nämnaren så att spel blir meningslöst, håller arbetsinsatsen på U minimal - U är en platshållare som ska ersättas, inte förfinas - och konservatismen gör att faktisk data nästan alltid är lägre än schablonen, vilket i sig skapar incitamentet att ersätta U med A.

### Allokeringsnyckeln

Standarden tillåter allokering per massa, energi, kvantitet eller monetärt värde men pekar inte ut vilken nyckel som gäller för vilket fall. En nod med en premiumprodukt och en lågmarginalbiprodukt kan flytta börda mellan kundgrupper genom nyckelvalet, och byte av nyckel mellan perioder kräver dokumentation men har ännu ingen spärr.

Här är läget detsamma som i de etablerade ramverken: varken ISO 14044 eller GHG Protocol dikterar nyckeln, utan kräver att valet motiveras och tillämpas konsekvent (för GHG Protocol se Scope 3 Standard, avsnitt 8.3 med figur 8.2, s. 88-89) - MASSIV+ följer samma princip (fysiska samband före ekonomiska). Två saker skiljer ändå åt. Massbalansen tvingar varje omfördelning att landa hos en annan namngiven motpart som ser sitt tal - ett granskningstryck en privat LCA-studie saknar. Och den väg EPD-världen valt, att låsa nyckeln per produktkategori genom PCR:er, står öppen även här: sektorvisa konventioner och verktygsförval kan fylla vägledningen utan att standarden själv blir sektorspecifik (se [avfallsförbränning, avsnitt 5](avfallsforbranning-och-allokering.md#5-standard-och-implementation-två-olika-lager)).

**Öppen:** normativ nyckelvägledning per falltyp återstår och väntas växa fram som sektorpraxis. Läget är inte sämre än dagens praxis.

### Nodgranularitet och partitionering

En nod kan vara en koncern, en anläggning eller en linje. Det ger två risker: noder på olika aggregeringsnivå är svåra att jämföra, och partitioneringen kan i princip väljas strategiskt - finkornig där det smickrar, grov där det inte gör det.

Vad standarden redan spärrar är döljande. Kravet på fullständig täckning utan överlapp betyder att hela organisationens utsläpp måste vara någonstans: en partition kan omfördela, men aldrig gömma. Jämför selektiv EPD-publicering, där enbart den gynnsammaste produkten får en deklaration och resten förblir orapporterat - den formen av döljande är omöjlig i MASSIV+.

**Mitigerad** vad gäller döljande, genom täckningskravet. **Öppen** vad gäller jämförbarhet mellan nivåval och vägledning för granularitetsval - frågor som belyses bäst av tidiga piloter (se [uppstartsfriktion, avsnitt 3](uppstartsfriktion.md#3-nodgranularitet-är-en-oavgjord-designfråga)).

---

## Signalens integritet

### Verklig förändring mot dataförbättring

När en nods tal ändras mellan två perioder kan det bero på tre saker:

1. **Verklig förändring.** Utsläppen har minskat eller ökat.
2. **Bättre data.** Ett okänt värde har ersatts av ett faktiskt (den regel standarden kallar replacement rule, se [specifikationen, avsnitt 6](../standard/specifikation.md#6-replacement-rule---progressiv-dataförbättring)).
3. **Ändrade definitioner.** Noden eller en leverantör har ändrat nodindelning ([§1](../standard/specifikation.md#krav-på-noddefiniering)), allokeringsregel ([§3](../standard/specifikation.md#krav-på-allokeringsregeln)) eller version av emissionsfaktorerna.

En kund som ser leverantörens siffra falla kan inte utan vidare skilja "de blev bättre" från "de blev bättre mätta" eller "de räknar på ett annat sätt" - och för ett system vars syfte är operativ signal är den skillnaden central. Frågan har ställts i [diskussion #39](https://github.com/ICONSOF/massivplus-public-draft/discussions/39): en ny nodindelning eller allokeringsmetod kan ge en ny total som felaktigt tas till intäkt för en minskning.

**Hanterad i riktning:** dekomponering i tre delar. Eftersom A och U hålls strukturellt åtskilda kan ett verktyg mekaniskt dela upp en periodförändring i förändring inom A (verklig) och effekten av U→A-byten (datarevision) - samma mönster som "jämförbara enheter" i finansiell rapportering. Den tredje delen kräver att föregående period räknas om med de nya definitionerna, vilket [MF-004](../forslag/mf-004-nodindelning.md) föreslår för nodindelningen. Skillnaden mellan det omräknade och det ursprungliga talet är effekten av definitionsbytet. Allokeringsposten anger allokeringsregel och standardversion ([MF-005](../forslag/mf-005-allokeringsposter.md)), så att mottagaren kan se när en leverantör har bytt.

Omräkningen görs för jämförelsens skull och ändrar inte de poster som redan skickats till kunderna. Bokföringen gör på samma sätt: jämförelsetalen räknas om när en redovisningsprincip ändras, men fakturorna skickas inte om. [MF-006](../forslag/mf-006-periodregel.md) föreslår att en ny version av en post alltid räknas med de definitioner som gällde för perioden. Dekomponeringen behöver bli en rapporteringskonvention; underlaget finns redan i strukturen.

### Icke-deltagande mellanled

Affärsrelationskoordinaten kräver att varje led deltar för att faktisk data ska propagera. En flödesansats kan hoppa över ett handelsled - en EPD kan refereras genom en grossist - men i MASSIV+ blir en producents deklaration synlig nedströms först när mellanledet (grossist, distributör, handelsbolag) självt är en nod. Tills dess fyller U hålet, ärligt men informationsfattigt.

**Öppen:** en strukturell egenskap snarare än ett fel, men med en praktisk konsekvens: handels- och distributionsled är oproportionerligt värdefulla att ansluta, och adoptionsarbetet bör prioritera dem. Elhandelsnoden är specialfallet av samma mönster (se [ursprungsgarantier, avsnitt 6](ursprungsgarantier-kritik-och-regelverk.md#6-var-massiv-landar)).

### Tidsdimensionen

Fyra besläktade frågor är underspecificerade. Noder med olika rapporteringsperioder (kalenderår, brutet år, kvartal) propagerar mot varandra utan synkroniseringsregel, och en leverantörs post har ofta inte kommit när kunden stänger sin period. En nods egna aktivitetsdata, till exempel periodens sista elfaktura, kan också saknas vid stängningen. Utsläpp uppstår vid produktion men allokeras vid försäljning, så lageruppbyggnad och lageravveckling förskjuter börda mellan perioder. Och när det standardiserade EF-setet revideras kan en kunds Scope 3 blanda leverantörstal beräknade under olika faktorversioner, vilket stör jämförbarheten över tid.

**Hanterad i riktning** för periodsynkronisering och egna data: [MF-006](../forslag/mf-006-periodregel.md) föreslår att en post gäller avsändarens period, att det som saknas vid stängningen bokförs som U och ersätts med en ny version när posten kommer, och ett avräkningsfönster för när en period är slutlig. [MF-007](../forslag/mf-007-egna-data-vid-stangning.md) föreslår samma behandling av egna aktivitetsdata. Varför tiden blir en fråga i MASSIV+ och vad periodregeln betyder i djupa kedjor behandlas i [Tiden i kedjan](tiden-i-kedjan.md). **Öppen** för lagerhantering. Versionskontrollen av EF-setet finns, och posten anger vilken version den bygger på.

---

## Gränsfall och tolkning

### Koordinatens gränsfall

Två erkända gränsfall följer direkt av valet att följa affären i stället för flödet. **Vederlagsfria strömmar** - gratis biprodukter och restströmmar som tas emot utan betalning - saknar affärsrelation och därmed nedströmskant, trots ett tydligt kausalt flöde (se [avfallsförbränning, avsnitt 4](avfallsforbranning-och-allokering.md#4-kommersiell-relation-inte-fysisk-kausalitet), och för skrot och återvunnet material [återvinning och cirkulära materialflöden, avsnitt 5](atervinning-och-cirkulara-materialfloden.md#5-priset-avgör-riktningen)). Och vid **sänkan** måste sista noden lösa upp sin organisationsbörda på enskilda enheter, så allokeringsfrågan återkommer exakt där gate-talet ska bära externa policymekanismer; individuationskriteriet som håller koordinaten ren är logiskt skarpt men operativt oprövat i gränsfall (se [produktnivå-invändningen, avsnitt 5-7](produktniva-invandningen.md)).

**Öppen** i båda fallen: uttryckligen erkända, och lämpliga att pröva i pilot.

### Köpt energi och Scope 2

Ett kluster av normativa val är identifierat men inte avgjort: placeringen av virtuella PPA:er (power purchase agreements, långsiktiga elköpsavtal) (strikt fysiskt kriterium eller additionalitet), kompensationslagrets närmare utformning, EF-setets tids- och geografiska granularitet för el, och residualmixens förhållande till U.

**Öppen:** förvaltningsval som återstår att fastställa. Frågorna, och varför grundpositionen står stabil oavsett var de landar, behandlas i [köpt energi, avsnitt 10](kompensation-och-faktiska-floden.md#10-var-gränsen-går).

### Dubbelräkning av okända utsläpp

Om en nod inkluderar okända utsläpp för leverantörers leverantörer utanför sin direkta kedja kan samma utsläppsmassa hamna i systemet två gånger. Att flera direkta kunder var för sig rapporterar U för samma leverantör är däremot *inte* ett problem - de räknar var sin andel.

**Mitigerad:** standarden tillåter enbart att direkta leverantörsrelationer deklareras. En nod får bara rapportera U för en leverantör den faktiskt köper av.

### Regulatorisk och tolkningsrisk

Konventionella GHG-ramverk summerar uppskattningar och faktisk data till ett samlat Scope 3-värde, och GHG Protocol redovisar andelen leverantörsdata per kategori vid sidan av talet (Scope 3 Standard, avsnitt 11.1, s. 119); MASSIV+ särhåller dem i varje värde. Risken är att systemet missuppfattas som att det jämställer okänd data med mätdata, avviker från etablerad GHG-praxis, eller utger sig för att ersätta produktnivåberäkning (PCF). Till detta kommer en regulatorisk kant: CSRD:s value chain cap (gränsen för hur mycket data stora bolag får kräva av mindre leverantörer) innebär att stora bolag inte får *kräva* mer än Voluntary Standard-nivån av mindre leverantörer - MASSIV+ är därför utformad som en frivillig sektorgemensam konvention och ligger utanför capen (se [EU:s rapporteringsarkitektur](../positionering/jamforelse/eu-rapporteringsarkitektur.md)).

**Mitigerad:** strikt A/U-separation, transparent Coverage, tydlig kommunikation om att U är temporärt, och aktiv positionering som komplement till befintliga ramverk (se [jämförelse med andra ramverk](../positionering/jamforelse-med-andra-ramverk.md)). Positioneringen mot capen är gjord; disciplinen att hålla den är löpande.
