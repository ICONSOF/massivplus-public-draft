---
layout: default
title: "DPP"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 12
---

# MASSIV+ vs. DPP (Digital Product Passport)

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. DPP och [BEAst](beast.md) är bärare och kanaler snarare än beräkningsstandarder - ett register respektive en affärstransaktionsstandard som MASSIV+-data kan flöda i. Ny här? Läs [introduktionen](../../introduktion.md) först.

DPP är ett EU-reglerat krav under ESPR (EU 2024/1781) - ett digitalt identitetskort för produkten som samlar information om material, kemikalier, reparerbarhet, återvinningsbarhet och koldioxidavtryck. Batterier regleras separat (EU 2023/1542) och är först ut med obligatoriskt pass från 18 februari 2027; arbetsplanen 2025-2030 pekar därefter ut järn/stål (den första egentliga delegerade akten), textil, aluminium och däck som prioriterade sektorer, med indikativa datum som rimligen förskjuts. Den tekniska infrastrukturen har tagit ett stort steg: CEN/CENELEC JTC 24 publicerade i slutet av maj 2026 den första uppsättningen EN 1821x-standarder som definierar hur passet identifieras, bärs, överförs, lagras och görs interoperabelt (bland andra EN 18219 unika identifierare, EN 18220 databärare, EN 18216 dataöverföring, EN 18222 API:er); ytterligare standarder i serien väntas senare 2026.

En avgränsning följer direkt av detta och är central för relationen till MASSIV+: EN 1821x styr *hur* passet bärs och utbyts, medan *vilka* datafält som krävs bestäms per produktgrupp av delegerade akter (och identitet och semantik av GS1/ECLASS). DPP är alltså självt tvålagrat - en bärarstandard som är metodneutral för de flesta fält, med innehållskraven i ett separat lager. Det speglar MASSIV+:s egen uppdelning i ett semantiskt lager (vad ett tal betyder) och ett utbyteslager (hur det flyttas), och det gör bärardelen till något MASSIV+ kan använda snarare än konkurrera med.

DPP:s dataarkitektur är dessutom decentraliserad snarare än en central databas. EU:s DPP-register håller de unika identifierarna och en hänvisning till var det fullständiga passet ligger; själva passdatan stannar hos den ansvariga aktören eller en godkänd tjänsteleverantör och nås via databäraren. Det är samma datasuveränitet - datan delas, den samlas inte in centralt - som MASSIV+:s utbyte förutsätter. Det gör också "register" till en oprecis etikett: passet är ett decentraliserat dataobjekt med ett centralt id-register ovanpå.

DPP och MASSIV+ opererar i grunden på olika logiska nivåer. DPP är ett dataobjekt som svarar på *"vad vet vi om den här produkten och var lagras det?"*; MASSIV+ är en beräknings- och propageringsstandard. För merparten av passets fält - material, kemikalier, reparerbarhet, återvinningsbarhet - är passet metodneutralt och bär det datakällan levererar. Koldioxidfältet är undantaget, och där blir relationen mer än en nivåskillnad.

ESPR fastställer att ett avtryck ska bäras men överlåter metoden till sektorspecifika delegerade akter. Där ett avtryck krävs är metoden föreskriven: EU:s referens är PEF (kommissionens rekommendation (EU) 2021/2279) och ISO 14067 - produktnivå-LCA uttryckt som kg CO₂e per funktionell enhet. Batteripasset (EU 2023/1542), det första DPP:t i drift, visar det konkret: obligatorisk avtrycksdeklaration enligt PEF-metoden, funktionell enhet en kWh levererad energi över batteriets livslängd, systemgräns cradle-to-grave (vaggan till graven, dvs. hela livscykeln) men med användningsfasen undantagen enligt batteriregelns egen avgränsning, och företagsspecifik data obligatorisk för samtliga tillverkningssteg. Koldioxidfältet ärver alltså en föreskriven metod.

Två konsekvenser är värda att hålla isär. Den första gäller jämförbarhet. Eftersom koldioxidfältet ärver en metod med betydande frihetsgrader (val av systemgräns, allokering och bakgrundsdata) är fältets värden inte utan vidare jämförbara mellan aktörer, och passets uttalade ändamål är transparens, spårbarhet och cirkularitet snarare än jämförbarhet på klimatfältet. Det är precis den luckan MASSIV+ adresserar i Scope 1+2-ledet: gemensamma emissionsfaktorer och Coverage gör underlaget jämförbart och kvalitetsmärkt. Den andra gäller åtkomst. DPP:s åtkomst är skiktad - konsumentvyn är öppen baskunskap, medan full materialsammansättning och Scope 3-underlag ligger i den behörighetsstyrda B2B-vyn. Ett MASSIV+-nodvärde hör hemma i den behörighetsstyrda vyn, mot en identifierad motpart, inte i det öppna konsumentledet.

Därför går DPP:ns relation till MASSIV+ på koldioxidsidan genom MASSIV+:s relation till [produktstandarderna](produktstandarder.md), snarare än vid sidan av den. Ett MASSIV+-nodvärde är en annan storhet än en PEF-PCF: det gäller en nod och inte en produkt, det täcker det uppströms ledet snarare än cradle-to-grave, och det allokerar och kvalitetsmärker enligt egen logik (massa, energi eller värde; Coverage = A/(A+U)) i stället för PEF:s allokerings- och DQR-regler. DPP är förankrat i produktartefakten - en ny produkt får ett nytt pass som refererar uppströms pass - medan MASSIV+ är förankrat i organisationen och affärsrelationen (se [koordinatbytet](../../fordjupningar/koordinatbytet.md)). Det är därför ett MASSIV+-nodvärde är *underlag* till passets koldioxidfält, inte fältet självt: för en reglerad produktgrupp som batterier utgör MASSIV+-data underlaget som den föreskrivna avtrycksberäkningen förbrukar.

Komplementariteten ligger ett steg in. PEF- och batteriberäkningen kräver företagsspecifik data för de egna processerna men vilar uppströms på sekundär databasdata, utan krav på leverantörsspecifika underlag eller kvalitetsmärkning av det ledet. Det är precis det ledet MASSIV+ förstärker: propagerad primärdata med ett täckningsmått i stället för branschsnitt. MASSIV+ matar alltså den uppströms primärdata som den föreskrivna PCF-beräkningen förbrukar - samma roll som mot EPD, PACT och ISO 14067 - och om värdet kan föras direkt in i avtrycksfältet avgörs av produktgruppens delegerade akt.

| Dimension | DPP | MASSIV+ |
|---|---|---|
| Rättslig grund | Obligatorisk (ESPR 2024/1781) | Frivilligt ramverk |
| Systemtyp | Dataobjekt (bärarstandard EN 1821x) | Propageringssystem |
| Central enhet | Produkt (artefakt) | Nod (organisatorisk enhet) |
| Datalagring | Decentraliserad hos aktören; centralt id-register | Decentraliserad; självrapportering per nod |
| Koldioxidfältets metod | PEF / ISO 14067 per delegerad akt | Nodnivå-allokering; Coverage = A/(A+U) |
| Jämförbarhet på klimatfältet | Inte garanterad (öppen metod, frihetsgrader) | Gemensamma EF + Coverage gör underlaget jämförbart |
| Relation | Bärare; koldioxidfältet ärver produktstandardernas metod | Uppströms primärdatakälla till den föreskrivna PCF-beräkningen |
