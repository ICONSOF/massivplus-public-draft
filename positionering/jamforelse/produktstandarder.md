---
layout: default_banner
title: "Produktstandarder"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 6
---

# MASSIV+ och produktnivåstandarderna

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

De fem produktnivåstandarderna delar ett gemensamt perspektiv på MASSIV+. Den här sidan ger den generella relationen som gäller dem alla; varje standard behandlas sedan på en egen sida:

- **[ISO 14040/14044](iso-14040-14044.md)** - grundstandarderna för livscykelanalys.
- **[ISO 14067](iso-14067.md)** - produktens koldioxidavtryck (PCF).
- **[EPD / ISO 14025](epd.md)** - tredjepartsverifierad miljödeklaration.
- **[PACT](pact-pathfinder.md)** - beräkning och utbyte av PCF längs värdekedjan.
- **[Catena-X](catena-x.md)** - fordonsindustrins PCF-regelbok och dataplattform.

---

## Den generella relationen

ISO 14040/14044, ISO 14067, EPD/ISO 14025, PACT och Catena-X delar ett gemensamt perspektiv: produkten är den centrala analysenheten. Utsläpp beräknas per deklarerad enhet (kg CO₂e per kg stål, per bil, per kWh) längs en definierad livscykel. MASSIV+ spårar också flöden i värdekedjan, men räknar på en annan enhet:

| | Produktstandarderna | MASSIV+ |
|---|---|---|
| Nivå | Produkt | Organisation |
| Allokering går till | Deklarerad enhet | Kund |
| Beräkningsenhet | Per produkt | Per nod |

MASSIV+ bygger på etablerad allokeringsmetodik. ISO 14044:s allokeringshierarki - undvik via subdivision eller systemexpansion, annars fysiska samband (massa, energi, kvantitet), annars ekonomiskt värde - är ärvd av ISO 14067, EPD och GHG Protocol Product Standard (avsnitt 9.2, tabell 9.1-9.2) och är en sedan länge etablerad standard för *vilken princip* allokeringen ska följa. MASSIV+ importerar denna hierarki rakt av i sitt val av allokeringsregel per nod (se [specifikationen §3](../../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Det nya är tillämpningsnivån, inte principen: allokeringen sker på organisation/nod → kund som propageringssteg, snarare än mellan biprodukter inom en process per deklarerad produktenhet. Det är denna logiska nivå - leverantörens fördelning av sina totala Scope 1+2 mellan sina kunder - som varken ISO, GHG Protocol eller EU:s rapporteringsstandarder hittills har standardiserat.

Det innebär att systemen mäter olika saker och inte konvergerar mot samma svar. De är komplementära. Relationen är konkret och praktisk i två riktningar:

**Produktdata in i MASSIV+.** En leverantör med en verifierad PCF (ISO 14067, PACT, Catena-X, EPD) har primärdata som mottagaren kan använda som grund för ett välunderbyggt U-underlag. Det räknas som faktisk data (A) först när leverantören själv utfärdar en MASSIV+-deklaration, som då kan bygga på samma underliggande mätdata (se [specifikationen §2](../../standard/specifikation.md#separation-av-faktisk-och-okänd-data)). PDS (Primary Data Share) och Coverage är analoga mått: båda anger hur stor andel av det rapporterade värdet som vilar på faktisk data. Måtten räknar på olika grund: i PDS är en datapunkt primär när både aktivitetsdata och emissionsfaktor är primära, medan A i MASSIV+ är det som en ansvarig avsändare har deklarerat (PACT Methodology 3.0, avsnitt 4.2.2; Catena-X-regelboken, avsnitt 7.2.4). El som räknats med en gemensam listfaktor är därför faktisk data i MASSIV+ men sekundärdata i PDS.

**MASSIV+-data in i produktberäkningar.** En nod med hög Coverage och faktiska Scope 1+2-data producerar leverantörsspecifik organisationsdata. I ISO 14040/14044, ISO 14067, PACT och Catena-X kan den användas som indata för en inköpt vara i någon annans studie, som ett bättre alternativ till sekundärdatabaser när leverantörsspecifik PCF saknas. Catena-X-regelboken anger själv att anläggnings- eller företagsspecifika data ska användas när produktspecifika saknas, även om de då kan innehålla mer än produktionens utsläpp (avsnitt 6.1). Det förutsätter att mottagaren dokumenterar tre saker: att talet är allokerat med nodens nyckel och inte beräknat per deklarerad enhet, att det innehåller nodens omkostnader som administration och resor, som Catena-X utesluter ur ett PCF (regelboken, avsnitt 4.2) och som PACT utesluter om de inte är väsentliga (PACT Methodology 3.0, avsnitt 3.3.1.1, som nämner tjänsteresor, pendling, kapitalvaror och FoU), och hur stor U-delen är och med vilken metod den är kvantifierad. En PDS beräknas enligt PACT eller Catena-X, och studien gör en känslighetsanalys på nyckel och U.

I en EPD är användningen villkorlig. Talet täcker bara klimatindikatorerna, så övriga indikatorer måste komma från annat underlag, och data som inte uppfyller kraven på representativa sekundärdata räknas som proxydata, som ska motiveras i datakvalitetsbedömningen och redovisas (PCR 2019:14, avsnitt 4.6.1 och 4.6.5). Verifieraren avgör. PEF och batteriförordningen kräver i första hand EF-kompatibla dataset (rekommendation (EU) 2021/2279, bilaga I, avsnitt 4.6.3) och fabriksspecifika modeller, och där kan ett aggregerat MASSIV+-tal med U-del inte användas direkt (se [DPP](dpp.md)).

Som produktens eget resultat duger talet som klimatredovisning i bokföringsmening. Ett klimatavtryck enligt ISO 14067, eller ett delavtryck vagga till grind, blir det först om någon gör en studie enligt standarden, och då är MASSIV+-talet indata i den studien. Det kan inte ersätta en EPD eller en LCA för offentliga jämförande påståenden.

En komplikation kvarstår: MASSIV+ kräver standardiserade emissionsfaktorer för Scope 1+2; produktstandarderna tillåter aktören att välja egna. Data från de två systemen är därmed inte direkt jämförbara utan en notering om vilka EF:er som använts.

## Källor

- GHG Protocol, *Product Life Cycle Accounting and Reporting Standard* (2011), avsnitt 9.2 med tabell 9.1-9.2 (s. 62-63) om att undvika och utföra allokering. [PDF](https://ghgprotocol.org/sites/default/files/standards/Product-Life-Cycle-Accounting-Reporting-Standard_041613.pdf)
- WBCSD, *PACT Methodology*, version 3.0 (2025), avsnitt 3.3.1.1 (s. 31) om aktiviteter utanför PCF och avsnitt 4.2.2 (s. 63-64) om Primary Data Share. [WBCSD](https://www.wbcsd.org/resources/pact-methodology-version-3/)
- Catena-X, *Catena-X Product Carbon Footprint Rulebook (CX-PCF Rules)*, version 3 (augusti 2024), avsnitt 4.2 (s. 16) om utsläpp som utesluts, 6.1 (s. 30) om primärdata och 7.2.4 (s. 33-35) om Primary Data Share.
- EPD International, *PCR 2019:14 Construction products*, version 2.0.1 (2025), avsnitt 4.6.1 (s. 27-28) om datakategorier och 4.6.5 (s. 30) om datakvalitetsbedömning. [PDF](https://api.environdec.com/api/v2/EPDLibrary/Files/7c2cae37-dc0a-4734-9cd6-08dda4d191db/Data)
- Kommissionens rekommendation (EU) 2021/2279 om PEF- och OEF-metoderna, bilaga I, avsnitt 4.6.3 (EUT L 471, 30.12.2021, s. 274) om vilka dataset som ska användas. [EUR-Lex](https://eur-lex.europa.eu/eli/reco/2021/2279/oj)
