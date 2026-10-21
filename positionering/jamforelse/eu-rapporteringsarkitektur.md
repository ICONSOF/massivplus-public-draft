---
layout: default_banner
title: "EU:s rapporteringsarkitektur"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 15
---

# MASSIV+ och EU:s rapporteringsarkitektur (CSRD/ESRS, Voluntary Standard)

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

CSRD/ESRS, Voluntary Standard ("VSME") och CSDDD är rapporterings- och tillsynsregimer som vilar på beräkningsstandarderna i de övriga jämförelserna - inte beräkningsstandarder i sig. Omnibus I-paketet våren 2026 (direktiv (EU) 2026/470) reviderar denna arkitektur väsentligt och berör MASSIV+ på två sätt: dels genom att skapa en explicit *legal* roll för en frivillig värdekedjekonvention, dels genom att lämna ett operativt utrymme öppet som MASSIV+ är konstruerat att fylla.

## Tre lager, tre olika roller

- **Voluntary Standard, Basic Module (B3)** är kärnan i den frivilliga standarden för bolag med högst 1 000 anställda (kommissionens utkast till delegerad förordning, Ares(2026)4624010, maj 2026, ännu inte antaget). B3 omfattar total energianvändning och "estimated absolute gross GHG emissions" - Scope 1 + location-based (elnätets genomsnittsmix, inte inköpsavtal) Scope 2 - med GHG Protocol Corporate Standard som referens men utan föreskriven EF-källa, utan datakvalitetsdeklaration och utan kundallokering (bilaga I, punkt 32-33). För bolag med högst tio anställda är uppgifterna frivilliga. Det är ett golv för vad som ska rapporteras, inte ett fullt operativt rapportsystem.
- **MASSIV+** ligger som operativt skikt ovanpå B3: samma underliggande Scope 1+2-data, gjord användbar genom (a) ett gemensamt EF-set som gör data jämförbara mellan noder, (b) kundallokering som propageringssteg och (c) A/U-separation med Coverage som datakvalitetsmått. MASSIV+ uppfinner inte rapporteringsplikt - det specificerar hur B3:s dataminimum blir användbart i en värdekedja.
- **ESRS E1** är ramverket för det rapporterande bolaget (det stora bolaget i CSRD-scope). ESRS anger GHG Protocol Corporate Standard som metodbas men låter ESRS egna krav gå före (ESRS E1, AR 39 i 2023 års lydelse; AR 20 i utkastet 2026). Kommissionens utkast till förenklade ESRS (Ares(2026)4623964, maj 2026, ännu inte antaget) låter bolaget använda antingen data från motparter i värdekedjan eller skattningar, beroende på vad som är praktiskt möjligt och tillförlitligt (ESRS 1, punkt 65), och anger att Scope 3-underlag ska prioriteras efter datans egenskaper: aktivitetsspecifik, tidsaktuell och verifierad data (ESRS E1, AR 24 d). I 2023 års lydelse fick skattningar användas först när bolaget efter rimliga ansträngningar inte kunnat samla in uppgifterna (ESRS 1, punkt 69), och bolaget skulle redovisa hur stor andel av Scope 3 som beräknats med primärdata från leverantörer (ESRS E1, AR 46 g). Det kravet finns inte kvar i utkastet. MASSIV+-data flödar in som högkvalitativ primärinput i det rapporterande bolagets significant Scope 3 categories.

## Value chain cap - vad MASSIV+ ligger inom och utom

Omnibus I-direktivet inför en *value chain cap*: bolag som rapporterar enligt CSRD får inte kräva mer hållbarhetsinformation av bolag i värdekedjan med högst 1 000 anställda än vad den frivilliga standarden anger, *när syftet är CSRD-rapportering*. Enligt kommissionens utkast består capen av de uppgifter som är markerade som "necessary" i både basmodulen och den utökade modulen (utkast Ares(2026)4624010, artikel 3 och bilaga II; jfr utkastet till ESRS 1, punkt 66). På klimatsidan är det total energianvändning samt Scope 1 och location-based Scope 2 (B3), och för bolag med högst tio anställda ingår inte ens de. Scope 3 ligger utanför capen eftersom det i standarden är en sektorsspecifik övervägning (bilaga I, punkt 49-52). Det rapporterande bolaget får fråga efter mer, men leverantören har då rätt att avböja och ska informeras om det (utkast Ares(2026)4624010, motivering avsnitt 1).

Det här bromsar den direkta regulatoriska efterfrågan på detaljerad värdekedjedata, men MASSIV+ ligger utanför capen i fyra led:

- **Frivilligt sektorgemensamt protokoll.** Recital 12 i Omnibus I-direktivet undantar uttryckligen "information som vanligen delas mellan aktörer i en sektor" och "tillämpning av hållbarhetskriterier i upphandling". Kommissionens motivering till utkastet om den frivilliga standarden upprepar att capen inte hindrar frivilligt delande av information som vanligen delas mellan bolag i en sektor (Ares(2026)4624010, motivering avsnitt 1). En sektorsgemensam tillämpning av MASSIV+ kan därför falla utanför capen, i den mån den blir sådan etablerad praxis i sektorn.
- **GHG management snarare än rapportering.** Capen täcker rapporteringsfrågor; data som samlas in för operativ utsläppsminskning ligger utanför (utkast Ares(2026)4624010, skäl 4).
- **Parallella regimer.** CSDDD-impact assessments har egna proportionalitetskrav (informationsförfrågningar mot partners <5000 anställda får endast göras när information inte rimligen kan inhämtas på annat sätt) men ingen value chain cap som motsvarar CSRD:s. Frivillig riskhantering är formellt separat med egen logik.
- **Banker och försäkringsbolag.** CRD VI / CRR III / EBA/GL/2024/01 ger finansinstitut en *standalone* skyldighet att samla in klimatdata från låntagare för prudential risk (banktillsynens krav på riskhantering, formellt skilt från hållbarhetsrapporteringen) - helt fri från CSRD-capen, som inte påverkar informationskrav enligt annan unionsrätt (utkast Ares(2026)4624010, skäl 4). Det är samma kanal som PCAF, och MASSIV+:s primärdata är direkt användbar där (se [jämförelsen med PCAF](pcaf.md)).

MASSIV+ är därför en frivillig, sektorgemensam konvention för datadelning som löser det operativa hål ESRS och Voluntary Standard medvetet lämnar öppet. Att ett stort CSRD-bolag *krävde* den av sina leverantörer skulle bryta mot capen.

| Dimension | Voluntary Standard B3 | MASSIV+ | ESRS E1 |
|---|---|---|---|
| Roll | Datafloor för SME i CSRD-värdekedja | Operativt skikt ovanpå B3 | Rapporteringsram för CSRD-bolag |
| Scope 1+2 | "Estimated", location-based S2 | Standardiserade EF:er, fördelade per kund | GHG Protocol-baserad, location + market-based S2 |
| Scope 3 | Ej i Basic | Byggs nedifrån via propagering | Per significant category; primärdata prioriteras, estimat tillåtna |
| Datakvalitet | Ingen formell deklaration | Coverage = (S1+S2+A)/T per nod | "Significant uncertainties" ska redovisas |
| Allokering till kunder | Saknas | Standardiserad propageringsregel | Endast på mottagarsidan; avsändarens fördelning är inte standardiserad |
| Legalt utrymme | Frivilligt komplement, gränsat av cap | Frivilligt sektorgemensamt protokoll (Recital 12) | Obligatoriskt för bolag i CSRD-scope; förenklade ESRS föreslås gälla från räkenskapsår 2027 |

**Ett modernt prejudikat: momsen.** Den bilaterala konsistenslogiken i MASSIV+ - säljarens utgående post är köparens ingående, kedjan terminerar hos slutkonsumenten - är samma som mervärdesskattens. Momsen visar att en sådan standard kan etableras på decennier: den togs från idé till global standard på ett par decennier och bär idag statsfinanserna i över 170 länder. Parallellen utvecklas i [bokföringsanalogin](../../fordjupningar/bokforingsanalogin.md).

---

## Källor

- [Consumption Tax Trends - OECD](https://www.oecd.org/en/topics/consumption-tax-trends.html) - antalet länder med mervärdesskatt.
- Kommissionens delegerade förordning (EU) 2023/2772 om hållbarhetsrapporteringsstandarder (ESRS), ESRS 1 punkt 69 samt ESRS E1 AR 39 och AR 46. [EUR-Lex](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj)
- Direktiv (EU) 2026/470 (Omnibus I). [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2026/470/oj)
- Europeiska kommissionen, utkast till delegerad förordning om ändring av delegerad förordning (EU) 2023/2772 (förenklade ESRS), Ares(2026)4623964, 6 maj 2026, ännu inte antaget: ESRS 1 punkt 65-66 och ESRS E1 AR 20 och AR 24.
- Europeiska kommissionen, utkast till delegerad förordning om en frivillig standard för hållbarhetsrapportering (Voluntary Standard), Ares(2026)4624010, 6 maj 2026, ännu inte antaget: motivering, skäl 4, artikel 3 och bilagorna I-II.
