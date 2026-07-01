---
layout: default
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
- **[PACT / Pathfinder](pact-pathfinder.md)** - beräkning och utbyte av PCF längs värdekedjan.
- **[Catena-X](catena-x.md)** - fordonsindustrins PCF-regelbok och dataplattform.

---

## Den generella relationen

ISO 14040/14044, ISO 14067, EPD/ISO 14025, PACT och Catena-X delar ett gemensamt perspektiv: produkten är den centrala analysenheten. Utsläpp beräknas per deklarerad enhet (kg CO₂e per kg stål, per bil, per kWh) längs en definierad livscykel. MASSIV+ spårar också flöden i värdekedjan men på *organisationsnivå* snarare än produktnivå. Allokeringen är till kunder snarare än till deklarerade enheter, och beräkningen är per nod snarare än per produkt.

MASSIV+ bygger på etablerad allokeringsmetodik. ISO 14044:s allokeringshierarki - undvik via subdivision eller systemexpansion, annars fysiska samband (massa, energi, kvantitet), annars ekonomiskt värde - är ärvd av ISO 14067, EPD och GHG Protocol Product Standard och utgör en sedan länge etablerad standard för *vilken princip* allokeringen ska följa. MASSIV+ importerar denna hierarki rakt av i sitt val av allokeringsregel per nod (se [specifikationen §3](../../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Det nya är tillämpningsnivån, inte principen: allokeringen sker på organisation/nod → kund som propageringssteg, snarare än mellan biprodukter inom en process per deklarerad produktenhet. Det är denna logiska nivå - leverantörens fördelning av sina totala Scope 1+2 mellan sina kunder - som varken ISO, GHG Protocol eller EU:s rapporteringsstandarder hittills har standardiserat.

Det innebär att systemen mäter olika saker och inte konvergerar mot samma svar. De är komplementära snarare än konkurrerande. Relationen är konkret och praktisk i två riktningar:

**Produktdata in i MASSIV+.** En leverantör med en verifierad PCF (ISO 14067, PACT, Catena-X, EPD) besitter faktisk primärdata som kan matas in i en MASSIV+-nod och ger Coverage nära 1 - förutsatt att PDS (Primary Data Share) är hög. PDS och Coverage är konceptuellt identiska mått: båda anger andelen faktisk primärdata i det rapporterade värdet.

**MASSIV+-data in i produktberäkningar.** En nod med hög Coverage och faktiska Scope 1+2-data producerar leverantörsspecifik organisationsdata som kan användas som indata i PCF-beräkningar enligt alla produktstandarderna - som ett bättre alternativ till sekundärdatabaser när leverantörsspecifik PCF saknas. Data är allokerad efter en konsistent regel snarare än kopplad till en specifik deklarerad enhet, vilket ska dokumenteras i mottagarens PDS-beräkning.

En komplikation kvarstår: MASSIV+ kräver standardiserade emissionsfaktorer för Scope 1+2; produktstandarderna tillåter aktören att välja egna. Data från de två systemen är därmed inte direkt jämförbara utan en notering om vilka EF:er som använts.
