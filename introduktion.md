---
layout: default
title: "Introduktion"
---

# Introduktion till MASSIV+

> En 10-minuters genomgång av vad MASSIV+ är, vilket problem det löser, och varför det är konstruerat som det är.

---

## Det grundläggande problemet

Klimatomställningen är en handlingsfråga, inte en rapporteringsfråga. För att ett bolag ska kunna minska sina utsläpp behöver det veta var utsläppen faktiskt uppstår och vad som kan göras åt dem. Den kunskapen kräver verklig data: faktiska mätvärden från faktiska anläggningar och flöden, inte schabloner från branschdatabaser.

Här uppstår ett strukturellt problem. Dagens klimatredovisning erbjuder två primära granulariteter: bolagsnivå (typiskt en årsredovisning med Scope 1, 2 och 3) eller produktnivå (en PCF-beräkning per artikel). Båda har sina begränsningar.

**Bolagsnivå är för grov.** En rapport på koncernnivå kan visa att en kategori står för stor del av utsläppen, men inte vilka anläggningar, leverantörsrelationer eller flöden inom kategorin som är de faktiska källorna. Skillnaden mellan *"vår Scope 3 är 80 % av totalen"* och *"anläggning B i Stockholm står för X kton"* är skillnaden mellan att veta att man har ett problem och att veta var åtgärden ska sättas in.

**Produktnivå är för svårt.** En PCF (Product Carbon Footprint) per artikel kräver LCA-kompetens, intern produktspårbarhet och primärdata från hela värdekedjan. De största industrikoncernerna kan klara det för enstaka produkter. För de allra flesta organisationer - inklusive små och medelstora företag, men också större bolag som producerar i flera anläggningar utan systematisk produktspårning - är PCF i praktiken oåtkomligt.

Mellan dessa två nivåer finns ett tomrum: data på **anläggnings- eller organisationsenhetsnivå**. Tillräckligt detaljerat för att vara operativt meningsfullt, tillräckligt aggregerat för att vara realistiskt att samla in.

MASSIV+ är konstruerat för det tomrummet.

Det ger måttstocken som hela konstruktionen ska mätas mot: i vilken grad den faktiskt påskyndar omställningen mot netto noll. Varje designval i MASSIV+ - från A/U-separationen till allokeringsreglerna - ska kunna försvaras med hur det stödjer konkreta beslut: inköp, investeringar, regulatorisk infogning.

---

## Idén: värdekedjan som nätverk av noder

MASSIV+ modellerar värdekedjan som ett riktat nätverk av noder.

En **nod** är en organisatorisk enhet - kan vara ett helt bolag, en produktionsanläggning, en produktionslinje, en avdelning eller en fordonsflotta. Standarden är agnostisk till nivån; varje organisation väljer sin egen granularitet så länge täckningen är fullständig och utan överlapp mellan noderna.

Varje nod gör tre saker:

1. **Mäter och rapporterar sina egna Scope 1- och Scope 2-utsläpp**, med ett gemensamt, fastställt set av emissionsfaktorer som alla aktörer är skyldiga att använda.
2. **Tar emot allokerade utsläppsflöden från sina leverantörer.** Det är nodens uppströms Scope 3.
3. **Allokerar sina utsläpp vidare till sina kunder** enligt en deklarerad allokeringsregel - per vikt, per energiinnehåll, per värde eller någon annan dokumenterad proportionell princip.

Konstruktionen bygger på en **bilateral logik**: ett utsläppsflöde mellan två noder bokförs hos båda parter. Det leverantören rapporterar som sin Scope 1+2 blir kundens Scope 3 - direkt, utan branschschabloner i mellanled.

Principen som driver hela systemet är: **ditt Scope 1+2 är mitt Scope 3.**

---

## De tre principerna

Standarden vilar på tre grundprinciper.

**1. Ditt Scope 1+2 är mitt Scope 3.** Varje nod etablerar sina egna faktiska Scope 1- och Scope 2-utsläpp och delar dessa nedströms. Scope 3 byggs upp nedifrån av faktisk data snarare än uppifrån med schabloner. Det är det som gör systemet meningsfullt: varje förbättring i en leverantörs Scope 1+2-rapportering förbättrar direkt kvaliteten på kundens Scope 3-bild.

**2. Faktisk data eller okänt.** Det finns ingen mellannivå av "uppskattning" som får samma status som faktisk data. Antingen finns faktisk primärdata (A för Actual) eller så är utsläppen okända (U för Unknown). U kan behöva kvantifieras med bästa tillgängliga proxy för att Coverage ska kunna beräknas, men proxyvärdet är inte poängen; det är ett underlag för att visa hur mycket av emissionsbilden som ännu saknar faktisk grund. A och U hålls strukturellt åtskilda - de aggregeras aldrig till ett enda värde med ett kvalitetsbetyg vid sidan. Varje nod har ett **Coverage-mått** = A / (A + U) som direkt visar hur stor andel av nodens utsläpp som vilar på faktiska mätvärden.

**3. Standardiserade emissionsfaktorer.** Alla noder använder samma gemensamma set av emissionsfaktorer för Scope 1+2 - per bränsleslag och energibärare. Det eliminerar den godtycklighet i faktorval som annars gör Scope 1+2-data ojämförbara tvärs aktörer och sektorer. Eftersom ditt Scope 1+2 är någons Scope 3 är det avgörande att underlaget är beräknat på samma sätt.

---

## Vad konstruktionen tekniskt garanterar

Tre matematiska egenskaper följer ur principerna.

**Massbalans.** Summan av alla utgående flöden från en nod motsvarar exakt nodens totala utsläppsmassa. Utsläppsmassa varken skapas eller försvinner i propageringen. Det är en konserveringsprincip - en lokal disciplinregel som varje nod upprätthåller utan central samordning.

**Datakvalitet är synlig.** Eftersom A och U hålls åtskilda kan en köpare alltid se hur stor del av en leverantörs rapporterade utsläpp som faktiskt är grundad i mätvärden. U-underlaget behövs för att räkna andelen, men det är inte ett påstående om faktisk precision. En leverantör med Coverage 0,8 är en helt annan datapunkt än en med Coverage 0,2 - även om absoluttalet ser likadant ut.

**Progressiv förbättring.** När en uppströmsleverantör börjar rapportera faktiska värden för utsläpp som tidigare var okända ersätts U-värdet av A-värdet. Det ackumuleras inte ovanpå. Modellen behöver inte byggas om - varje förbättring slår igenom mekaniskt i nästa rapporteringsperiod, hela vägen nedströms. Förbättring sker längs två axlar. Replacement rule höjer andelen faktisk data: okänt blir faktiskt. Finare nodgranularitet höjer relevansen: ett bolagssnitt ersätts av linje- eller produktfamiljsdata för den faktiska leveransen, under nodpartitionens versionskontroll. Den första gör bilden mer faktisk, den andra mer relevant.

---

## Funktionsförskjutningen: från rapport till signal

Dagens dominerande klimatredovisning är retrospektiv. GHG Protocol-rapporter och EPD:er sammanställs en gång om året eller mer sällan, oftast med flera månaders eftersläpning, för att svara på frågan *"vilka utsläpp hade vi förra perioden?"*. Funktionen är primärt compliance: att visa rapporteringspliktig data för en avgränsad period.

MASSIV+ är konstruerat så att utsläppsdata kan fungera som **operativ signal** - något som faktiskt påverkar beslut i den period då data uppstår. MASSIV+-data kan användas för compliance-rapportering precis som GHG Protocol-data, men *konstruktionsändamålet* skiljer sig. Standarden är designad för att stödja beslut i värdekedjan - inköpsbeslut, investeringsbeslut, leverantörsdialog - inte primärt för att fylla rapporteringskrav.

Skillnaden syns i sex dimensioner:

| Dimension | Etablerad rapportering | MASSIV+ |
|---|---|---|
| Primär funktion | Compliance | Beslutsstöd |
| Tidsperspektiv | Retrospektiv | Periodaktuell |
| Beslutsstöd | Begränsat | Strukturellt inbyggt |
| Förbättringar syns | I nästa rapport | I nästa period |
| Datariktning | Uppåt mot rapportmottagare | Mellan affärsparter |
| Datakvalitet | Inbakad i ett samlat värde | Strukturellt åtskild (A/U) |

---

## Adoption: värde från dag ett, utan att vänta på andra

En vanlig invändning mot värdekedjestandarder är att de förutsätter att hela kedjan följer med. "Det är värdelöst tills alla andra också gör det."

MASSIV+ är konstruerat så att den invändningen inte biter. Ett enskilt bolag kan börja rapportera idag, ensamt, och nyttan kommer omedelbart.

- **Intern kunskapsbas.** Att börja mäta sina egna Scope 1+2 enligt en konsekvent metod ger för första gången en bild av var i den egna verksamheten utsläppen ligger - och därmed grunden för att prioritera åtgärder. Det här värdet uppstår utan att en enda leverantör eller kund deltar.
- **Bättre datapost mot kunder.** En leverantör som rapporterar enligt MASSIV+ erbjuder sina kunder en kvalitativt bättre datapost än branschschabloner. Det stärker positionen i upphandlingar oavsett om kunden själv är på standarden.
- **Möjlighet att ställa krav.** En kund som rapporterar enligt MASSIV+ kan börja kräva data från sina leverantörer i samma format. Varje leverantör som ansluter förbättrar Coverage i kundens uppströms Scope 3 - utan att modellen behöver räknas om.

Nyttan av flerstegspropagering - att en investering i utsläppsminskning hos en uppströmsaktör syns flera led nedströms utan att varje mellanled gör egen utredning - växer med antalet noder i en given kedja som har anslutit. Men det är ett bonusvärde ovanpå det grundläggande, inte ett krav.

En specifik möjlighet bör nämnas: en aktör som redan rapporterar verifierade utsläpp under EU ETS kan använda dessa direkt som Scope 1 i MASSIV+, vilket gör tröskeln särskilt låg för cirka 10 000 europeiska anläggningar.

Sett som helhet är detta en **stege i tre steg**: standardiserad Scope 1+2 per nod (värde direkt, ensam), bilateralt utbyte med en motpart (värde så fort en part rapporterar), och flerstegspropagering genom kedjan (nätverksvärde som växer per kedja). Poängen: den vanligaste invändningen - att propagering är osäker i tidig adoption - biter bara på det tredje steget. De två första står ändå.

---

## Förhållande till andra ramverk

MASSIV+ kompletterar de etablerade ramverken. Det adderar ett operativt flödeslager på organisationsnivå som översätter beprövade principer från finansiell redovisning - bilateral bokföring, identifierad motpart, strikt separation av faktisk och okänd data - till klimatdomänen. Data flödar i båda riktningar med flera av de existerande ramverken. Att en sådan bilateral standard kan etableras snabbt har ett modernt prejudikat: mervärdesskatten gick från idé till global norm på ett par decennier och bär idag statsfinanserna i över 170 länder.

Livscykelanalysen (LCA) förtjänar en egen avgränsning. LCA är ett *bedömningsverktyg* vars syfte enligt ISO 14040/14044 är att analysera en produkts miljöpåverkan över dess livscykel. Baumann och Tillman sammanfattar det som att vi behöver bedömningsverktyg såväl som strukturerade sätt att tänka kring miljön, och att "LCA is one such assessment tool, useful for the environmental assessment of products". Nyare översikter beskriver LCA på samma sätt - som beslutsstöd och som ett verktyg för att peka ut miljömässiga hotspots i komplexa värdekedjor (Hellweg & Milà i Canals, *Science*, 2014). För en ad hoc-analys av en enskild produkts avtryck är LCA fortsatt rätt verktyg. MASSIV+ kompletterar den funktionen: standarden svarar på en annan fråga - vad en organisatorisk nod släppte ut och hur det fördelades på dess kunder - och är ett operativt flödeslager på organisationsnivå snarare än ett bedömningsverktyg för enskilda produkter. Fördjupningen [koordinatbytet](fordjupningar/koordinatbytet.md) utvecklar varför de två svarar på olika frågor.

- **GHG Protocol** är grunden för Scope 1+2-värden. MASSIV+ gör samma data jämförbar mellan aktörer genom att kräva standardiserade emissionsfaktorer, och adderar det operativa flödeslager som GHG Protocol Scope 3 saknar. GHG Protocols egen datakvalitetshierarki rangordnar leverantörsspecifik primärdata högst, över branschsnitt och proxy, men i praktiken stannar de flesta Scope 3-rapporter på de lägre stegen. MASSIV+ gör det översta steget till strukturellt förval: eftersom din Scope 3 är leverantörens faktiska Scope 1+2 bär underlaget per konstruktion den specifika motpartens data.
- **ISO 14064-1** är ISO-familjens organisationsnivåstandard. MASSIV+ verkar på samma nivå och kan reduceras till en 14064-1-rapport för noder som tar rollen som rapporteringsentitet.
- **Produktnivåstandarderna** (ISO 14067, EPD, PACT, Catena-X) opererar per produkt snarare än per organisation. Data flödar i båda riktningar: produktdeklarationer kan matas in som primärdata i MASSIV+-noder, och MASSIV+-data kan användas som leverantörsspecifik indata i PCF-beräkningar.
- **DPP (Digital Product Passport)** är en databärare, inte ett beräkningssystem: passdatan är decentraliserad hos aktörerna och ett centralt EU-register håller identifierarna. Bärarstandarderna (EN 1821x, publicerade maj 2026) styr hur passet identifieras och utbyts; vilka fält som krävs bestäms per produktgrupp. MASSIV+-beräknad data kan utgöra underlaget till passets koldioxidfält.
- **PCAF** är finanssektorns standard för financed emissions. PCAF tillhandahåller portföljallokeringen; MASSIV+ tillhandahåller den primärdata på kundnivå som PCAF idag har svårt att få fram.
- **CSRD/ESRS och Voluntary Standard ("VSME").** Reviderade ESRS E1 (gäller från räkenskapsår 2027) tillåter både primärdata och estimat för värdekedjedata, men prioriterar verifierad primärdata. Voluntary Standard Basic (B3) är dataminimum för leverantörer under 1000 anställda. MASSIV+ är det operativa skiktet som gör B3:s Scope 1+2-data användbar - standardiserade EFs, kundallokering, Coverage - och flödar in som högkvalitativ primärinput i det rapporterande bolagets significant Scope 3 categories.

Mer detaljer i [Jämförelse med andra ramverk](positionering/jamforelse-med-andra-ramverk.md).

---

## Var du läser vidare

Om du vill gå djupare finns en handfull fördjupningstexter, var och en med en bärande poäng som kan läsas fristående:

- **[Specifikation](standard/specifikation.md)** - den fullständiga tekniska beskrivningen: noddefinition, allokering, massbalans, replacement rule, Coverage, cirkulära flöden. Cirka 45 minuters läsning.
- **[Bokföringsanalogin](fordjupningar/bokforingsanalogin.md)** - den strukturella parallellen till dubbel bokföring som positioneringsverktyg, och vad den säger om vad MASSIV+ kan bli på sikt.
- **[Exempel: grönt stål i fordonsvärdekedjan](fordjupningar/exempel-gront-stal.md)** - hur principerna ser ut konkret i en faktisk värdekedja.
- **[Koordinatbytet](fordjupningar/koordinatbytet.md)** - varför MASSIV+ följer affären och inte flödet, och hur det förhåller sig till LCA-traditionen.
- **[Produktnivå-invändningen](fordjupningar/produktniva-invandningen.md)** - varför produktupplösning uppstår emergent vid sänkan i stället för som en andra koordinat.
- **[Incitament och konsumtionsled](fordjupningar/incitament-och-konsumtionsled.md)** - var incitamentet att välja lägre uppströmspåverkan bor, och hur gate-talet förhåller sig till konsumtionsledsmekanismer.
- **[Jämförelse med andra ramverk](positionering/jamforelse-med-andra-ramverk.md)** - hur MASSIV+ förhåller sig till GHG Protocol, ISO 14064-1, EPD, PACT, Catena-X, DPP och PCAF.
- **[Positionering och affärsvärde](positionering/positionering-och-affarsvarde.md)** - vad standarden konkret betyder för inköpare, leverantör, storbolag och mindre aktörer.
- **[Metodologiska risker](fordjupningar/metodologiska-risker.md)** - var standarden är strukturellt svag och hur det hanteras.
- **[Uppstartsfriktion](fordjupningar/uppstartsfriktion.md)** - vad som blir svårt i början och varför det är priset för ärlighet.
- **[MASSIV+ vs ecoinvent](positionering/massiv-vs-ecoinvent.md)** - är en MASSIV+-nod "bara" ett cradle-to-gate-dataset?
