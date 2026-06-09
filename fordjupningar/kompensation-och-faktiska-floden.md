# Kompensation och faktiska flöden: köpt energi, certifikat och upptag

> **Syfte:** Att visa hur MASSIV+ behandlar köpt energi, energicertifikat och permanenta upptag inom samma princip - att kompensationstransaktioner hålls strukturellt åtskilda från faktiska bruttoflöden. Texten härleder hur en leverantörsspecifik energifaktor uppstår legitimt i modellen, var gränsen mot köpta attribut går, och hur positionen förhåller sig till GHG Protocol och ISO 14064-1.

Den här texten kan läsas fristående. Den förutsätter en grundläggande bild av hur MASSIV+ fungerar - läs [introduktionen](../introduktion.md) eller [specifikationen](../standard/specifikation.md) först om du inte är bekant med ramverket.

---

## 1. Frågan

Omställningen till netto noll drivs inte bara av energieffektivisering. En lika viktig hävstång är att köpa energi med lägre utsläpp, ibland för att den dessutom är billigare. För att den åtgärden ska synas i redovisningen måste en nod kunna få en leverantörsspecifik och trovärdig emissionsfaktor för sin köpta energi att slå igenom i sin Scope 2.

Det möter vid första anblick en spänning med MASSIV+:s princip om **standardiserade emissionsfaktorer**, som föreskriver att alla noder använder ett gemensamt fastställt set och inte väljer egna faktorer för Scope 1 och 2 ([specifikationen §2](../standard/specifikation.md#standardiserade-emissionsfaktorer-för-scope-1-och-2)). Läst rakt av skulle en nod som köper lågutsläppsel ändå tvingas räkna sin S2 med standardfaktorn, och förbättringen skulle inte synas.

Spänningen är skenbar. Lösningen kräver ingen ny mekanism, utan är två principer MASSIV+ redan har, tillämpade på energileverantören: **"ditt Scope 1+2 är mitt Scope 3"** och **replacement rule**. Men den tvingar fram en distinktion som är avgörande för standardens trovärdighet: skillnaden mellan att köpa faktisk lågutsläppsenergi och att köpa ett attribut som påstår den.

## 2. Två marknader som kopplades isär

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
- **Tveksam additionalitet.** En garanti från ett befintligt vattenkraftverk som ändå hade producerat ger ingen ytterligare klimatnytta. Marknaden för lösa garantier är dessutom tunn och billig, så priset signalerar knappt någon ny förnybar utbyggnad.

## 3. Köpt energi i MASSIV+: leverantören som uppströmsnod

Energileverantören är en uppströmsnod som alla andra. Köpt energi följer därmed samma A/U-logik som övriga uppströmsflöden, med två datatillstånd.

**Utan leverantörsdeklaration räknas standardiserad S2 som faktisk data (A).** Argumentet är paritet med Scope 1. En nods S1 räknas redan som faktisk data trots att den använder en standardiserad bränslefaktor - en diesel-emissionsfaktor är också ett genomsnitt. Uppmätt MWh multiplicerad med standardens energibärarfaktor är exakt samma konstruktion: uppmätt aktivitet gånger fastställd faktor ger faktisk S2. Standarden drar redan gränsen på rätt ställe för detta, eftersom distinktionen mellan A och U *"handlar om ansvarig avsändare, inte om numerisk kvalitet"* ([specifikationen §2](../standard/specifikation.md#separation-av-faktisk-och-okänd-data)). Noden är ansvarig avsändare för sin egen uppmätta förbrukning.

**Med leverantörsdeklaration ersätter leverantörens faktiska data baslinjen.** När energileverantören är en nod och deklarerar, allokerar den sin faktiska S1+2 till köparen. Det flödet bär med sig både A och U, eftersom leverantörens egen uppström kan vara delvis okänd. Det ersätter den standardiserade baslinjen via replacement rule ([specifikationen §6](../standard/specifikation.md#6-replacement-rule---progressiv-dataförbättring)). Statusen ändras inte i bytet: noden går från en A, sin standardiserade, till en annan A, leverantörens mer specifika, och får på köpet leverantörens U synlig.

Det är så en låg energisiffra ska uppstå i MASSIV+: genom att köpa från en leverantör vars *faktiska* allokerade utsläpp är låga, inte genom att noden själv väljer en lägre faktor.

**El är ett specialfall som skärper meningen.** För bränslen och de flesta material finns ett fysiskt flöde till en bestämd mottagare, och resonemanget håller rakt av. För nätel gör det inte det: elektronerna poolas i elområdet, och det finns sällan någon fysisk leverans till en enskild konsument - det är just därför certifikat uppstod. Den ärliga fysiska A-siffran för nätel är därför location-based-faktorn själv, och en lägre leverantörsspecifik siffra vilar nästan alltid på ett kontraktuellt instrument (PPA eller ursprungsgaranti), utom vid genuin direktleverans bakom mätaren.

Den fysiska spaken försvinner inte för el, den flyttar. När nätredovisningen går mot tim- och elområdesupplösning blir location-based-faktorn själv tids- och platsberoende, och då uppstår en genuint fysisk åtgärd som inte kräver ett enda certifikat: att förlägga förbrukning till tider och elområden där nätmixen faktiskt är ren sänker den verkliga location-based-A:n. Den logiska konsekvensen är att MASSIV+:s standardiserade EF-set bör utvecklas mot temporal och geografisk granularitet - från årlig nationell faktor mot timvis per elområde - så att standardfaktorn blir ärligare utan att noden väljer den. Var den granulariteten ska läggas är ett normativt val för standardens förvaltning (se avsnitt 10).

> **Honest wrinkle.** Coverage kan sjunka när en nod byter från standardfaktor till leverantörsdata. Standardfaktorn låtsades implicit vara fullt känd, medan leverantören ärligt redovisar sin okända uppström. Det är ett önskat beteende - systemet blir mer ärligt, inte sämre - men kontraintuitivt, och bör förklaras så att en sjunkande Coverage inte misstolkas som en försämring.

## 4. Gränsen mot kompensation

> **Offsets / klimatkompensation** är samlingsnamnet för att köpa en klimatåtgärd utanför den egna verksamheten för att väga upp sina utsläpp. Två typer ryms under begreppet: *undvikande- eller reduktionskrediter*, där någon annan släpper ut mindre, och *upptag* (eng. *removals*), där koldioxid faktiskt plockas bort ur luften och lagras - det Stockholm Exergi gör med infångning vid kraftvärmeverket i Hjorthagen. "Permanenta upptag" eller "minusutsläpp" är den varaktiga änden av skalan. Energicertifikat (ursprungsgarantier) är strikt sett ett annat instrument - ett påstående om hur el producerades, inte en köpt klimatåtgärd - men MASSIV+ behandlar alla strukturellt likadant: de är **köpta anspråk** som hålls åtskilda från de faktiska flödena.

Mekanismen i avsnitt 3 får bara släppa in faktiska flöden från en faktisk producentnod i A. Den får inte släppa in köpta attribut. Annars blir den en kanal för att vika in offsets i bruttosiffran - exakt det problem köpta upptag och certifikat reser, ett steg tidigare i värdekedjan.

Två olika saker kallas båda *att köpa klimatneutral energi*:

| | Fysisk lågutsläppsleverans | Marknadsbaserat certifikat |
|---|---|---|
| Vad köparen får | El från en faktisk lågutsläppsproducent | Ursprungsgaranti, attributet avskilt från elektronerna |
| Fysiska utsläpp | Faktiskt låga | Nätmix som vanligt |
| I MASSIV+-termer | A-flöde från leverantörsnod | Kontraktuell transaktion, inte ett flöde |

Den skarpa linjen är: **A från köpt energi förutsätter att attributet motsvarar en faktisk fysisk leverans från en producent som deklarerar sin egen uppmätta S1+2.** En lös ursprungsgaranti uppfyller inget av kraven - varken fysisk leverans eller deklarerande motpart - och hör därför hemma i ett separat kompensationslager, samma fack som permanenta upptag.

**Var den fysiska A-vägen faktiskt finns skiljer sig mellan energibärare**, och det är värt att vara konkret med, eftersom den för nätel i praktiken är tom. Elektronerna poolas i elområdet, och ett elhandelsbolag som blir nod allokerar i praktiken elområdets mix, alltså ungefär location-based-faktorn; en siffra under det kräver ett kontraktuellt instrument och hör till kompensationslagret. Den fysiska A-vägen för köpt energi gäller i stället främst **värme, ånga och kyla samt on-site- eller direktledd el**, där leveransen sker via ett lokalt, spårbart nät och producenten kan deklarera sin egen S1+2 och allokera. Det är ingen hypotes: det är precis den mekanism [avfallsförbränningsfördjupningen](avfallsforbranning-och-allokering.md) beskriver för fjärrvärme, där förbränningsanläggningen allokerar sina faktiska utsläpp till värmekunderna.

| Energibärare | Fysisk A-väg | Annars |
|---|---|---|
| Fjärrvärme, ånga, kyla | Ja - lokalt nät, producenten deklarerar och allokerar | - |
| On-site eller direktledd el | Ja, men nisch | - |
| Nätel | I praktiken nej | Granulär location-based som A, kontraktuella anspråk i kompensationslagret |

## 5. Tre register, inte två

Det leder till en modell med tre register, där location-based och market-based får sin plats utan att bryta propageringen:

1. **A/U - fysisk brutto, propagerar.** Detta är den fysiska linjen, byggd nerifrån av faktisk data. Den motsvarar i princip location-based: standardiserad nät-EF som baslinje, ersatt av fysisk leverantörsnods faktiska data när den finns. U är den okända delen av samma linje.
2. **Kompensationslagret - kontraktuella anspråk, propagerar inte.** Lösa certifikat och permanenta upptag. Anspråk noden håller, strukturellt likt ett köpt upptag.
3. Vid rapporteringsgränsen rekonstrueras båda GHG-talen ur de två registren.

Den viktiga insikten är att **GHG Protocols market-based-hink inte är en enda sak i MASSIV+.** Den blandar ihop två ting modellen medvetet håller isär: bundlad fysisk leverans från en deklarerande producent (ett fysiskt flöde, hör hemma i A) och obundet attribut (ett kontraktuellt anspråk, hör hemma i kompensationslagret). MASSIV+:s naturliga axel är därför inte location vs market, utan **fysiskt flöde, som propagerar som A/U, mot kontraktuellt anspråk, som inte propagerar.** Den axeln skär rakt igenom market-based-talet och delar det i två.

## 6. Varför två tal inte propageras

En naturlig fråga är om MASSIV+ borde införa GHG:s dual reporting fullt ut och alltid propagera både ett location-based och ett market-based tal genom nätverket. Svaret är nej, av ett strukturellt skäl.

Market-based-talet är per konstruktion ett **nettotal**: fysiska utsläpp minus de kontraktuella instrument köparen håller. Det är samma slags pre-nettade siffra som ett fotavtryck minus offsets. Hela MASSIV+ är byggt för att aldrig låta något pre-nettat propagera. Det propagerande ämnet - A och U - måste vara brutto och fysiskt, annars ärver varje nedströmsnod en Scope 3 som redan är tvättad med någon annans certifikatköp, mot en motpart den inte kan se. Det är just det massbalansen och regeln om en bokföring mot en namngiven motpart finns för att förhindra.

GHG:s dual reporting lever på inventarienivå, där de två talen står bredvid varandra och ingen propagerar dem vidare. MASSIV+ propagerar. Asymmetrin - att bara det fysiska propagerar - är priset för att vara ett flödessystem snarare än ett inventarium. Informationen går inte förlorad: båda GHG-talen kan rekonstrueras vid gränsen, men bruttolinjen hålls ren genom kedjan.

## 7. Gråzonen: virtuella PPA och additionalitet

Gränsen bundlat mot obundet är inte knivskarp. Ett fysiskt PPA med en deklarerande producentnod är klart A. En lös ursprungsgaranti är klart kompensation. Däremellan sitter det **finansiella eller virtuella PPA:t** (VPPA): en kontraktuell prissäkring utan fysisk leverans, där köparen får certifikaten men elektronerna går till det lokala nätet. Ett VPPA har inget fysiskt flöde, men kan vara genuint additionellt - den nya vindparken byggdes för att avtalet fanns.

Här finns ett genuint vägval:

- **Strikt fysiskt kriterium.** Ingen fysisk leverans innebär kompensationslager, oavsett additionalitet. Renast mot massbalansen och regeln om namngiven motpart, och fullt verifierbart.
- **Additionalitetskriterium.** Tillåt anspråket om finansieringen kan visas ha drivit ny kapacitet. Mer generöst, men öppnar för bedömningsfrågor som är svåra att verifiera och granska - precis den godtycklighet MASSIV+ är konstruerat för att undvika.

Den linje som ligger närmast standardens övriga design är det strikta fysiska kriteriet, eftersom det är verifierbart: antingen finns en deklarerande leverantörsnod med faktisk leverans, eller så är det kompensation. Additionalitet är ett äkta klimatvärde, men hör hemma som en egenskap på posten *i* kompensationslagret, inte som en biljett in i A. Var exakt linjen ska dras är ett normativt val som hör hemma i standardens förvaltning.

## 8. Positionering mot etablerade ramverk

MASSIV+ intar här ingen avvikande hållning, utan operationaliserar en position som standarderna redan delvis tar.

**ISO 14064-1** är det närmaste ankaret. Annex E (normativ) föreskriver location-based som default för importerad el och tillåter marknadsbaserat *som tilläggsinformation under kontraktskvalitetskriterier*. Tre-register-modellen är den operativa formen av exakt detta: location-based som A/U, marknadsbaserat som tilläggslager.

**GHG Protocol Scope 2 Guidance** kräver *dual reporting* - bolag med kontraktuella instrument rapporterar både ett location-based och ett market-based tal - och ställer en uppsättning kvalitetskriterier på instrument för att de ska få räknas market-based, bland annat unik claim utan dubbelräkning, retirering eller annullering, vintage nära konsumtionsperioden, och att de kommer från samma marknad. MASSIV+ är en strängare men kompatibel position: där GHG släpper in en kriterie-godkänd lös garanti i market-based-talet, vägrar MASSIV+ släppa in den i det propagerande A och routar den till kompensationslagret. Standarden bryter inte mot dual reporting utan levererar in i det, eftersom båda talen kan produceras vid gränsen.

**Den pågående Scope 2-revisionen pekar åt MASSIV+:s håll.** GHG Protocol driver den första större översynen av Scope 2 sedan 2015, genom fyra tekniska arbetsgrupper. Det offentliga samrådet öppnade i oktober 2025 och stängde 31 januari 2026; ett reviderat utkast väntas senare under 2026, följt av en andra samrådsrunda, med en slutlig text omkring 2027 och stegvis implementering troligen från 2028. En statusförändring värd att notera är att dokumentet siktar på att bli en *Standard* snarare än dagens *Guidance*, vilket gör det mer bindande för de ramverk som hänvisar till det.

Tre föreslagna ändringar träffar precis de svagheter modellen pekar ut:

- **Timmatchning.** Certifikat ska utfärdas och annulleras för samma timme som energin förbrukades, istället för att kvittas mot årsförbrukning. Det angriper den tidsupplösning garantierna idag saknar.
- **Deliverability.** Certifikat ska komma från produktion som bedöms levererbar till den förbrukande lasten, istället för var som helst inom "samma marknad" (i praktiken nationsgränser). Det riktar sig mot att en avlägsen garanti grönmärker förbrukning den inte fysiskt når.
- **Bibehållen dubbelrapportering, skärpt location-based.** Strukturen med både location-based och market-based behålls, och location-based skärps med en uppdaterad faktorhierarki och krav på de mest precisa tillgängliga faktorerna.

Eftersom timmatchning är dyrt och komplext föreslås övergångsåtgärder: lastprofiler, undantagströsklar för mindre organisationer under en ännu inte fastställd förbrukningsgräns, en legacy-klausul för befintliga kontrakt, och en flerårig utrullning. De trösklarna är centrala för mindre aktörer, som initialt ofta hamnar under det fulla timkravet men ändå behöver förstå riktningen.

Riktningen bekräftar MASSIV+:s grundinstinkt: rörelsen går från löst attribut mot faktisk fysisk, temporal och geografisk koppling. Och eftersom MASSIV+ aldrig bakat in det omstridda instrumentet i den propagerande substansen är positionen robust oavsett var revisionen landar - den fysiska A/U-linjen står stilla medan certifikatreglerna ändras, och MASSIV+ kan mappa mot vilket utfall som helst vid gränsen. Att GHGP-uppdateringar dessutom inte automatiskt flödar in i de ramverk som hänvisar till dem (IFRS S2, ESRS/CSRD, Kaliforniens SB 253) utan en formell revidering innebär en fördröjning innan de slår igenom i regelefterlevnad - en fördröjning som en fysik-först-hållning är okänslig för.

**EU rör sig parallellt, och snabbare på vissa punkter.** Två spår driver granulära ursprungsgarantier: lagstiftning (RED III) och teknisk standard (CEN-EN 16325). RED III uppmuntrar tidsstämpling och fastställer att en garanti har standardstorleken 1 MWh men får delas i fraktioner ned till multiplar av 1 Wh, och uppmuntrar medlemsstater att utfärda mer tidsupplösta garantier. EECS-reglerna och utkastet till reviderad EN 16325 är redan kompatibla med timmatchning, så flaskhalsen är nationell implementering hos utfärdande organ, inte teknik eller EU-juridik.

Det skarpaste konkreta kravet gäller datacenter. Kommissionens utkast till delegerad förordning för hållbarhetsklassning av datacenter - samrådet stängde 23 april 2026, antagande planerat under Q2 2026 - föreslår 15-minuters, location-based matchning: garantier ska motsvara de 15-minutersperioder som sammanfaller med förbrukningen och komma från samma budområde som datacentret, villkorat av att sådana granulära garantier finns i medlemsstaten. Utkastet inför också ett additionalitetsliknande krav: garantierna ska komma från anläggningar tagna i drift högst tio år före rapportåret, med undantag för långsiktiga PPA:er med buntade garantier på plats senast 15 maj. EU:s 15-minutersupplösning är därmed finkornigare än GHGP:s timupplösning, och bindande tidigare - vilket kan forma marknaden för granulära garantier innan den globala redovisningsstandarden hunnit ikapp.

**En terminologisk fallgrop** är värd att markera. *Supplier-specific emission factor* betyder olika saker i de två världarna. I GHG och produktstandarderna inkluderar begreppet ofta leverantörens kontraktuella produktmix inklusive dess egna ursprungsgarantier. I MASSIV+ betyder leverantörsspecifik enbart leverantörens faktiska uppmätta fysiska S1+2, allokerad till köparen, inte dess certifikatjusterade siffra. Samma ord, olika referent.

**Produktstandarderna** (ISO 14067, PACT, Catena-X, EPD) låter aktören välja egna emissionsfaktorer och tillämpa marknadsbaserade instrument enligt sin egen produktkategoriregel. Arbetsdelningen mot MASSIV+ är ren: MASSIV+ levererar den fysiska bruttosiffran på organisationsnivå, och PCF-utföraren avgör enligt sin PCR om och hur marknadsbaserade instrument läggs på i sitt eget lager. Det gör MASSIV+-data till ett *bättre* underlag, eftersom det kommer oförnettat. Den notering om vilka emissionsfaktorer som använts som redan krävs vid överföring till en PCF behöver då utvidgas till att också ange om kontraktuella instrument är nettade eller inte.

## 9. Enkelhet: komplexiteten ligger i systemet, inte hos användaren

En elegant lösning får inte bli svår att använda. Tre-register-modellen ser ut att lägga till struktur, men för noden som rapporterar är den medvetet enklare än alternativet, eftersom komplexiteten absorberas av systemet och inte skjuts över på användaren.

Vad noden faktiskt gör är litet:

- **Rapportera uppmätt energi.** Standardfaktorn ger automatiskt A-baslinjen. Användaren behöver inte välja emissionsfaktor eller grubbla över location kontra market - valet är redan gjort på standardnivå.
- **Ingenting extra när leverantören ansluter.** Blir energileverantören en nod flödar dess faktiska data in via replacement rule, hanterat av verktyget. Noden räknar inte om något.
- **Bara registrera kontraktuella instrument, inte räkna med dem.** En lös ursprungsgaranti antecknas som ett anspråk noden håller. Användaren nettar ingenting och avgör inte själv hur det ska redovisas.

Det svåra - dual reporting, location kontra market, rekonstruktionen av båda GHG-talen - sker vid rapporteringsgränsen, i verktygslagret, inte i nodens dagliga arbete. Det följer standardens befintliga arbetsdelning: stränga regler för *att* bokföra, lokal frihet och verktygsstöd i *hur* (se [avfallsförbränningstexten, avsnitt 5](avfallsforbranning-och-allokering.md#5-standard-och-implementation-två-olika-lager)).

Linjeringen med befintliga standarder är i sig en enkelhetsegenskap. Eftersom MASSIV+ intar ISO 14064-1:s location-default och producerar underlag som matar in i GHG:s dual reporting, behöver användaren inte lära sig eller stämma av ett parallellt system - MASSIV+:s utdata faller in i den rapportering organisationen redan gör.

Den pågående GHG-revisionen gör den här poängen konkret. När Scope 2 rör sig mot timmatchning och geografisk matchning blir market-based-redovisning *mer* krävande för användaren, och en stor del av dagens certifikat kan förlora giltighet. En MASSIV+-nod är skyddad: dess fysiska A/U-linje står stilla medan certifikatreglerna ändras. Komplexiteten i en marknad i förändring landar i gränssnittslagret, inte i den enskilda nodens grunddata, som inte behöver räknas om varje gång reglerna för kontraktuella instrument skrivs om.

## 10. Var gränsen går

Som med allokeringsfrågan löser standarden och dess förvaltning olika saker, och det är värt att vara tydlig med vad som är avgjort och vad som återstår.

Avgjort i sak:

- Standardiserad S2 räknas som A, med paritet mot S1 som grund.
- Leverantörsdeklaration ersätter baslinjen via replacement rule och bär in både A och U.
- Kontraktuella instrument hålls i ett separat register och propagerar inte.
- Den fysiska bruttolinjen är det enda som propagerar; GHG-talen rekonstrueras vid gränsen.

Återstår som normativa val för standardens förvaltning:

- Det exakta verifieringskravet för att en leverantörsdeklaration ska räknas som A.
- Placeringen av virtuella PPA:er - strikt fysiskt kriterium eller additionalitetskriterium.
- Den närmare utformningen av kompensationslagret som en del av standarden.
- Granulariteten på det standardiserade EF-setet för el - årlig nationell faktor mot timvis per elområde, i takt med att nätredovisningen och regelverken blir mer tidsupplösta.

---

## Källor

- [Om ursprungsgarantier - Energimyndigheten](https://www.energimyndigheten.se/ursprungsgarantier)
- [GHG Protocol Scope 2 Guidance](https://ghgprotocol.org/scope-2-guidance)
- [GHG Protocol - publika konsultationer om Scope 2 och konsekvensbaserad elredovisning](https://ghgprotocol.org/blog/release-ghg-protocol-opens-public-consultations-scope-2-and-electricity-sector-consequential)
- [ISO 14064-1:2018 - Greenhouse gases, Part 1](https://www.iso.org/standard/66453.html)
- [EU Renewable Energy Directive - targets and rules](https://energy.ec.europa.eu/topics/renewable-energy/renewable-energy-directive-targets-and-rules_en)
- [EU draft sets granular GOO rules for data centres - Argus Media](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2818021-eu-draft-sets-granular-goo-rules-for-data-centres)

---

*Sammanställd juni 2026 baserat på dialog i MASSIV+-projektet. Den normativa utformningen av kompensationslagret och gränsdragningen för virtuella PPA:er behandlas vidare i arbetsgruppen.*
