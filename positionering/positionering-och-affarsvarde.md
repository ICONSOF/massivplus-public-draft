# Positionering och affärsvärde

> **Poäng:** Varför detta är värt att göra - för inköpare, leverantör, stor och liten - och var i landskapet av befintliga ramverk MASSIV+ faktiskt sitter.

Den här texten kan läsas fristående. Den förutsätter en grundläggande bild av vad MASSIV+ är - läs [introduktionen](../introduktion.md) först om du inte är bekant med ramverket.

---

## Vad MASSIV+ är - kort sagt

MASSIV+ är en **öppen standard för beräkning och propagering av utsläppsdata på organisationsnivå** - utformad för det utrymme där produktnivådata är otillgänglig men bolagsnivådata är för grov. Standarden definierar hur Scope 1+2 beräknas, hur utsläpp allokeras och propageras mellan noder, och hur faktisk och okänd data hålls isär - med matematisk konsistens garanterad av massbalansen.

## Var informationsarbetet utförs

Den djupare designprincipen i MASSIV+ är att flytta informationsarbetet dit data faktiskt finns. Under GHG Protocol gissar köparen sin Scope 3 uppifrån trots att hen inte har leverantörens data; leverantören har data men har negativt incitament att dela den, eftersom detaljerade volyms- och energidata kan användas i prisförhandlingar. Fel part gör beräkningen, med fel verktyg.

På produktnivå gör EPD, ISO 14067, PACT och Catena-X redan exakt detta - leverantören räknar sin produkts livscykel, publicerar en deklaration, och kunder konsumerar resultatet utan att se underliggande affärsdata. MASSIV+:s bidrag är att tillämpa samma informationsekonomi på *organisationsnivå*, där data är mer åtkomlig, tröskeln dramatiskt lägre, och propageringen kan ske kontinuerligt - inte som ögonblicksbilder var tredje till femte år.

Många större bolag gör redan en informell variant av detta på organisationsnivå för att kunna rapportera Scope 3 kategori 1 (purchased goods and services). Olika metoder används: rådata begärs in från First-tier-leverantörer (total energiförbrukning, total producerad volym) följt av egen volymbaserad allokering, LCAer från Tier 1-leverantörer används som indata, eller egna interna beräkningar baserat på inköpt material (SEK, kg eller annat). Alla är approximationer av nodprincipen. Konsekvenserna av att improvisera är välkända: leverantörens affärskritiska data exponeras med risk för missbruk i prisförhandlingar, allokeringen blir grov när volymen har annan energiintensitet än övrig produktion, andra och tredje tier blir en svart låda som måste fyllas med branschschabloner, och auditörer ställer berättigade frågor om hur luckorna är hanterade. MASSIV+ adresserar detta genom att flytta allokeringsansvaret till parten som har informationen, standardisera vilken information som faktiskt utbyts, och garantera systemkonsistens utan central samordning.

## Komplementär till etablerade ramverk

Relationerna till omgivande standarder och ramverk är komplementära snarare än konkurrerande. GHG Protocol är grunden som MASSIV+-noder bygger på för sina Scope 1+2-värden. Produktstandarderna (ISO 14067, EPD, PACT, Catena-X) och MASSIV+ utbyter data i båda riktningar: PCF-data kan flöda in i MASSIV+-noder som primärdata, och MASSIV+-noddata kan användas som leverantörsspecifik indata i PCF-beräkningar. DPP kan bära MASSIV+-beräknad emissionsdata som ett av sina datafält.

GHG Protocol-kategorier med annan ontologi adresseras av andra metodiker. Användarfasen (kat 11) och end-of-life (kat 12) genererar utsläpp hos brukare eller avfallshanterare *efter* värdekedjan, och adresseras av LCA use-phase-modellering. Investeringar (kat 15) adresseras av PCAF:s portföljbaserade attribution; MASSIV+ kompletterar PCAF genom att tillhandahålla den primärdata på kundnivå som PCAF idag har svårt att få fram.

Se [jämförelse med andra ramverk](jamforelse-med-andra-ramverk.md) för detaljer.

## Standarden som en stege

MASSIV+ kan antas stegvis: det är en stege där varje steg har eget värde och egen tröskel, så adoption blir gradvis snarare än binär.

- **Lager 1 - standardiserad Scope 1+2 per nod.** Gemensamma emissionsfaktorer, identifierad rapporterande enhet, deklarerad metodik. Kräver ingen kunskap om uppströmsutsläpp och inget deltagande från leverantörer eller kunder. Värdet stannar hos den rapporterande aktören: internt beslutsstöd, en konsistent grund över tid, jämförbarhet med andra på samma nivå, och en metodik som tål CSRD-granskning. Lägst tröskel - där flest kan börja. (ETS-anläggningar kan använda verifierad ETS-data direkt som Scope 1.)
- **Lager 2 - bilateralt utbyte med allokering.** Avsändaren allokerar sin Scope 1+2 till mottagarna och deklarerar det bilateralt; mottagaren bygger faktiskt Scope 3 (A) eller markerar okänt (U). Det är här den bilaterala bokföringen faktiskt realiseras, och här MASSIV+ skiljer sig metodologiskt från GHG Protocol, PACT och Catena-X. Värde uppstår även om bara ena parten är på standarden - en leverantörs MASSIV+-deklaration slår branschschabloner oavsett om kunden rapporterar.
- **Lager 3 - flerstegspropagering.** Förändringar i en nods Scope 1+2 propagerar nedströms i nästa period, flera led, utan att varje mellanled gör egen utredning. Det är här nätverkseffekten biter, och den växer med antalet anslutna noder *i en given kedja* snarare än globalt.

Att lagren har olika värde och olika tröskel har en konkret konsekvens: den vanligaste invändningen - att flerstegspropagering är komplicerad och osäker i tidig adoption - biter bara på Lager 3. Lager 1 och 2 bär en stor del av nyttan och står oberoende av den. Se [bokföringsanalogin](../fordjupningar/bokforingsanalogin.md) för den fullständiga genomgången.

## Affärsnytta

MASSIV+ förvandlar klimatdata från en årlig rapporteringsbörda till ett operativt styrinstrument. Coverage gör datakvalitet handlingsbar, replacement rule låter förbättringar slå igenom omedelbart, och massbalansen säkerställer att utsläppsmassa varken skapas eller försvinner i propageringen. Konkret innebär det att utsläppsminskning kan följas upp kvartalsvis - både internt och som krav eller incitament mot leverantörer.

**För inköparen** blir Coverage ett upphandlingsverktyg och inköp för första gången ett aktivt klimatstyrinstrument - inte bara redovisat. När per-enhet-allokeringar är jämförbara mellan leverantörer oavsett vertikal integration kan pris-vs-koldioxid bli en faktisk beslutsdimension, och krav kan riktas exakt mot leverantörer där datakvaliteten är låg.

**För leverantören** räcker en MASSIV+-deklaration mot samtliga kunder utan att energi- och produktionsdata exponeras. Effekten är att klimatdataarbete går från kostnadspost till prissättbar tillgång - hög Coverage får ett marknadsvärde när nedströms kunder kan motivera att betala för datakvalitet som förbättrar deras egen rapport. Vertikalt integrerade producenter får dessutom för första gången synliggöra faktisk effektivitet.

**Storleken på bolaget** påverkar främst drivkraften, inte nyttan. Storbolag drivs av sin egen CSRD-rapportering (ESRS E1) och av SBTi-åtaganden, och vinner framför allt på att auditkostnaden flyttar från "försvara metodval" till "verifiera standardefterlevnad" - tid och konsultkostnader som idag går åt till att försvara godtyckliga val (vilken EF-databas, vilken allokeringsregel, vilken spend-faktor) blir mekaniskt verifieringsarbete. För mindre bolag (<1000 anställda) gäller CSRD:s value chain cap - stora kunder kan inte längre lagligt begära mer än Voluntary Standard Basic i ren rapporteringsfråga - så drivkraften ligger utanför capen: frivilliga sektoröverenskommelser, upphandlingskriterier, operativ utsläppsminskning (GHG management snarare än rapportering), och banksidan (prudential climate risk är inte begränsad av capen). Nyttan förblir densamma - låg ingångströskel, en deklaration som duger mot alla kunder, samma data som indata i PCF/EPD - men positioneringen är frivillig värdedelning snarare än compliance-leverans. Se [EU:s rapporteringsarkitektur](jamforelse/eu-rapporteringsarkitektur.md) för detaljer om de fyra kanalerna utanför capen.

---

*Källa: Utdrag ur MASSIV+ teknisk specifikation, 2026-05-06.*
