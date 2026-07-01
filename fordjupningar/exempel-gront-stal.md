---
layout: default_banner
title: "Exempel: grönt stål"
parent: "Fördjupningar"
nav_order: 3
---

# Illustrativt exempel: grönt stål i fordonsvärdekedjan

> **Syfte:** Att konkret illustrera hur MASSIV+ tillämpar sina grundprinciper i en verklig värdekedja, och hur detta skiljer sig metodologiskt från EPD-baserad redovisning.

---

## Värdekedjan

Exemplet följer en enkel tre-nodskedja inom fordonssektorn:

```
Ståltillverkaren  →  Rörproducenten  →  Komponenttillverkaren  →  Fordonstillverkaren
```

- **Ståltillverkaren** producerar stål - konventionellt och fossilfritt
- **Rörproducenten** köper stålämnen från Ståltillverkaren och tillverkar rör
- **Komponenttillverkaren** köper rör från Rörproducenten och tillverkar fotsteg till lastbilar
- **Fordonstillverkaren** monterar fotstegen i sina fordon

---

## Redovisning enligt EPD-baserat arbetssätt

Komponenttillverkaren behöver redovisa klimatpåverkan från inköpt stål. Ett vanligt tillvägagångssätt ser ut så här:

1. Ståltillverkaren publicerar en EPD - ett dokument med deklarerat CO₂-värde per kg stål, beräknat för en given produkttyp och produktionsmix vid en given tidpunkt
2. Rörproducenten vidarebefordrar EPD-värdet till Komponenttillverkaren, eventuellt med ett påslag för den egna rörproduktionen
3. Komponenttillverkaren använder värdet i sin klimatredovisning

EPD:er uppdateras normalt vart tredje år, vilket innebär att förändringar i produktionsmix - exempelvis ökad andel fossilfri produktion - inte nödvändigtvis återspeglas i löpande redovisning. Rörproducentens egna processutsläpp framgår inte alltid separat. I book-and-claim-system, där attributcertifikat för fossilfritt stål kan säljas frikopplat från den fysiska leveransen, uppstår risk för dubbelräkning om residualen - den konventionella volym som återstår efter att certifikat utfärdats - inte redovisas explicit av alla parter.

---

## Redovisning enligt MASSIV+

I MASSIV+ rapporterar varje aktör sina egna Scope 1- och Scope 2-utsläpp. Dessa propageras nedströms och utgör Scope 3 hos mottagande nod.

### Steg 1 - Ståltillverkaren rapporterar sina Scope 1+2

Ståltillverkaren beräknar sina utsläpp från stålproduktionen - energianvändning, processgaser, bränslen - med standardens gemensamma emissionsfaktorer. Andelen fossilfri produktion påverkar det totala Scope 1+2-värdet. Ståltillverkaren allokerar utsläppsmassan till sina kunder i proportion till levererad volym.

Rörproducenten tillgodoräknar sin andel av Ståltillverkarens Scope 1+2 som uppströms Scope 3.

### Steg 2 - Rörproducenten rapporterar sina Scope 1+2

Rörproducenten beräknar sina egna utsläpp från rörproduktionen - el, värme, bränslen. Till detta adderas uppströms Scope 3 från steg 1. Rörproducenten allokerar den sammanlagda utsläppsmassan till sina kunder i proportion till levererad volym.

Komponenttillverkaren tillgodoräknar sin andel som uppströms Scope 3.

### Steg 3 - Komponenttillverkaren rapporterar sina Scope 1+2

Komponenttillverkaren beräknar sina egna utsläpp och adderar uppströms Scope 3 från steg 2. Komponenttillverkaren allokerar vidare till Fordonstillverkaren.

### Fordonstillverkarens Scope 3

Fordonstillverkaren tar emot ett Scope 3-värde som härleds från primärdata i samtliga tre uppströmsnoder, och som uppdateras varje rapporteringsperiod i takt med att nodernas Scope 1+2 förändras.

---

## Vad förändras - och för vem

MASSIV+ innebär ett perspektivskifte: från produktens deklarerade CO₂-avtryck till organisationsenhetens faktiska utsläpp, propagerade löpande längs värdekedjan. Konsekvenserna är olika för olika aktörer.

**Ståltillverkaren** redovisar sina faktiska Scope 1+2 med standardens gemensamma emissionsfaktorer. Varje utsläppsminskning - oavsett om den drivs av ETS-kostnadstrycket, investeringar i fossilfri produktion eller energieffektivisering - propageras automatiskt till alla kunder i nästa rapporteringsperiod. Effekten av att minska utsläppen är bredare och mer direkt synlig i värdekedjan än i ett EPD-baserat system.

**Rörproducenten** blir synlig som en egen nod med egna Scope 1+2. I EPD-baserad redovisning är mellanledsaktörers processutsläpp ofta osynliga eller inbakade i ett vidarebefordrat värde. I MASSIV+ redovisas de separat och skapar ett eget incitament att minska.

**Komponenttillverkaren** får löpande uppdaterad primärdata uppströms, men tappar möjligheten att peka på en specifik produkttyp - exempelvis fossilfritt stål - om inte Ståltillverkaren definierar separata noder per produktionsprocess. Valet av nodgranularitet hos Ståltillverkaren avgör vilken upplösning som är möjlig nedströms.

**Fordonstillverkaren** får ett Scope 3-värde för stålkedjan som baseras på faktisk primärdata och uppdateras varje rapporteringsperiod. Det är inte direkt jämförbart med PCF-baserade värden från andra delar av leverantörsbasen - men EPD-värden är i praktiken inte heller direkt jämförbara sinsemellan, givet skillnader i systemgränser, allokeringsmetoder och tidpunkt för beräkning. Jämförbarhet mellan olika redovisningsansatser är ett generellt problem i fältet som föregår MASSIV+.

---

## Konsekvenser av förändrad produktionsmix hos Ståltillverkaren

Om Ståltillverkaren ökar sin andel fossilfri produktion sjunker deras totala Scope 1+2 per producerat ton. Enligt MASSIV+:s propageringslogik påverkas Rörproducentens uppströms Scope 3 i nästkommande rapporteringsperiod, och förändringen fortplantar sig vidare till Komponenttillverkaren och Fordonstillverkaren.

Uppdateringsfrekvensen är kopplad till rapporteringsperioden snarare än till revisionscykeln för produktdeklarationer.

---

## Nodgranularitet: ett designval med metodologiska konsekvenser

Om Ståltillverkaren definierar en enda nod för hela sin stålproduktion allokeras ett viktat genomsnitt av konventionella och fossilfria utsläpp till samtliga kunder i proportion till volymandelar. Distinktionen mellan produkttyper går förlorad i aggregeringen.

Om Ståltillverkaren istället definierar separata noder - en för konventionell produktion, en för fossilfri produktion - allokeras varje nods Scope 1+2 enbart till de kunder som köper från respektive nod. Kunder till den fossilfria noden får den nodens utsläppsvärden; kunder till den konventionella noden får den nodens. Noderna är oberoende av varandra i allokeringsberäkningen.

Valet av nodgranularitet är Ståltillverkarens och måste vara konsekvent över tid samt metodologiskt motiverat enligt standarden. Det påverkar direkt vilken upplösning som är möjlig i nedströmsnodernas Scope 3-redovisning.

---

## Partiell täckning: när leverantörer inte rapporterar enligt MASSIV+

Om en leverantör inte rapporterar Scope 1+2 enligt MASSIV+ klassificeras utsläppen från den relationen som okända (U). Mottagande nod kan använda bästa tillgängliga externa data - leverantörens EPD, PCF, PACT/Catena-X-utbyte eller annan källa - som grund för sitt U-underlag. Detta underlag används för Coverage och prioritering, men räknas inte som A även om det bygger på primärdata, eftersom A förutsätter att leverantören själv har utfärdat en MASSIV+-deklaration. Distinktionen handlar inte om värdets numeriska kvalitet utan om vem som står bakom det som ansvarig avsändare.

Rapporteringen blockeras aldrig - noden kan fullt ut redovisa sina egna Scope 1+2 och den faktiska andelen av Scope 3 där MASSIV+-rapporterad primärdata finns. Coverage-måttet (A/(A+U)) reflekterar ofullständigheten transparent. När en leverantör väl utfärdar en MASSIV+-deklaration ersätter denna det okända värdet via replacement rule, och Coverage förbättras.

Om en kund nedströms inte rapporterar enligt MASSIV+ påverkas inte leverantörens redovisning. Noden är självständig oavsett nedströmsparters val av ramverk.

---

## Dubbelräkning och massbalansens roll

I book-and-claim-system uppstår risk för dubbelräkning när attributcertifikat för fossilfri produktion säljs till en kund medan övriga kunder fortsätter räkna med ett genomsnitt som inkluderar den fossilfria volymen - det vill säga när residualen inte redovisas explicit. Huruvida detta sker i praktiken beror på hur certifikatsystemet är utformat och följs upp.

I exemplet ovan allokerar Ståltillverkaren volymsbaserat - en av de proportionella allokeringsmetoder MASSIV+ tillåter. Antag att Ståltillverkaren har 100 tCO₂ totalt och tre kunder som köper 50%, 30% och 20% av volymen. De får då 50, 30 respektive 20 tCO₂ - summan är alltid exakt 100. Det finns inget utrymme att ge en kund ett lägre värde utan att de övriga automatiskt får ett högre. Dubbelräkning är matematiskt utesluten, inte beroende av att något certifikatsystem följs upp korrekt. MASSIV+ stödjer inte book-and-claim som allokeringsmetod - allokeringen sker uteslutande på basis av massflöde.

---

## Jämförelse av metodologiska egenskaper

| Egenskap | EPD/book-and-claim | MASSIV+ |
|---|---|---|
| Uppdateringsfrekvens | Normalt vart 2-3 år | Varje rapporteringsperiod |
| Mellanledsaktörers utsläpp synliga | Inte nödvändigtvis | Alltid - som separata noder |
| Risk för dubbelräkning via certifikat | Ja, om residual saknas | Strukturellt utesluten via massbalans |
| Produktnivåupplösning | Ja, via produktspecifik EPD | Beroende av nodgranularitet |
| Kräver produktspårning per SKU | Ja | Nej |
| Hanterar saknad uppströmsdata | Nej | Ja - klassificeras som U |
| Påverkas av nedströmsparters val av ramverk | Inte tillämpligt | Nej |

MASSIV+ producerar inte ett CO₂-värde per kilogram produkt i den mening som EPD-standarden avser. Systemgränsdragningen är annorlunda: MASSIV+ redovisar utsläpp på organisationsenhetsnivå och propagerar dessa längs värdekedjan, medan en EPD beräknar utsläpp allokerade till en specifik produkt längs dess livscykel. De två ansatserna är metodologiskt komplementära snarare än direkt jämförbara.
