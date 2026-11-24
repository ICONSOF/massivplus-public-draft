---
layout: default_banner
title: "MF-002 Utspädning och fördelningsmåttet D"
parent: "Förslag"
nav_order: 2
forslag_id: MF-002
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§8"
forslag_forfattare: Birger Löfgren
forslag_diskussion: https://github.com/ICONSOF/massivplus-public-draft/discussions/49
---

# MF-002 Utspädning och fördelningsmåttet D

> **Status:** Utkast, omarbetat 2026-10-30, omskrivet 2026-11-22, reviderat 2026-11-24. Ingår inte i standarden. Berör §8. Författare: Birger Löfgren. Diskussion: [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> Fler exempel och bakgrund finns i fördjupningen [Fördelningsmåttet D](../fordjupningar/fordelningsmattet-d.md).

## I korthet

- En grossist som köper från en leverantör med låga utsläpp och en med höga kan ge alla kunder samma snitt. Då ser en kund som köpt det gröna inte det i sina tal.
- D visar hur stor andel av utsläppen från leverantörerna som har hamnat hos andra kunder än dem inköpen gjordes för. D = 0 betyder att leverantörernas utsläpp har hamnat hos rätt kund. D = 1 betyder att allt har hamnat hos fel kund.
- Vilken kund ett inköp gjordes för avgörs av kopplingen mellan inköp och försäljning, till exempel en order eller ett artikelnummer. Fördelningen efter kopplingen kallas referensen, och D jämför den faktiska fördelningen med den.
- D räknas för ett mätområde, normalt en anläggning. Då syns utjämning också när posterna fördelas mellan flera noder.
- Varje kund får sitt eget värde.

D gäller skillnader i utsläpp mellan de poster som mätområdet tar emot från sina leverantörer, oavsett orsak. Två leveranser från samma leverantör är olika poster bara om leverantören deklarerar dem var för sig. Skillnader i mätområdets egna utsläpp mäts inte av D. Coverage (faktisk andel, om [MF-008](mf-008-namnbyte.md) antas) visar hur stor del som har faktisk grund, och D visar om den hamnar hos rätt kund.

## Förslag till standardtext

Ett nytt delavsnitt i §8. Definitionerna av Coverage och uppströms-Coverage står kvar.

### D: andelen utsläpp som hamnat hos fel kund

1. **Vad D visar.** D visar hur stor andel av de utsläpp som ett mätområde har fått från sina leverantörer som mätområdet har fördelat till andra mottagare än dem inköpen gjordes för. D gäller skillnader mellan de inkommande posterna, åt båda hållen och oavsett orsak, till exempel grönt stål, fossilfri el hos leverantören eller kortare transporter. Egenskaper som inte ändrar utsläppen, till exempel ursprung, andel återvunnet material eller certifiering, syns inte i D. A och U räknas var för sig. Mätområdets egna Scope 1+2 räknas inte in, inte heller när en nod i mätområdet fördelar dem till en annan nod i mätområdet och de där bokförs som Actual (§4).

2. **Mätområdet.** Utjämning kan göras redan när inkommande poster fördelas på organisationens noder, och det steget syns inte inne i någon nod. D räknas därför för ett mätområde som omfattar det steget. Om inget annat väljs är mätområdet en anläggning, alltså en plats där organisationen bedriver verksamhet, till exempel en fabrik, ett lager eller en terminal, med alla noder där. Görs inköpen gemensamt för flera anläggningar omfattar mätområdet alla dem. Organisationen får välja andra mätområden inom rapporteringsentiteten, till exempel ett affärsområde eller hela bolaget, och motiverar då valet. Ett mätområde ska (a) vara detsamma även om noderna inom det delas in på nytt, och (b) omfatta steget där inkommande poster fördelas på mätområdets noder. Ett flöde mellan två mätområden räknas som en post.

3. **Referensen.** Referensen är hur leverantörernas utsläpp skulle ha fördelats om varje inkommande post följde kopplingen mellan inköp och försäljning, alltså till de mottagare inköpet gjordes för. Kopplingen hämtas i denna ordning:
   - (a) en registrerad koppling, till exempel order, stycklista eller artikelnummer
   - (b) en drivare eller modell, till exempel för ett elnät
   - (c) en volym- eller värdenyckel

   Den finaste kopplingen som finns används. Det räcker att kopplingen visar hur varje post fördelades på mottagarna, eftersom posten har ett A och ett U för hela sin mängd. En koppling per order ger alltså samma referens som en koppling per post. Finns kopplingen bara på en grövre nivå, till exempel en artikel som köps från flera leverantörer, blandas posterna inom den nivån, och skillnaden mellan dem syns inte i D. En avtalad fördelning utan stöd i inköpen räcker inte. Finns ingen koppling redovisas D som ej beräknat. Referensen bestäms i förväg, dokumenteras och versionshanteras.

4. **Uträkningen.** För varje mottagare jämförs det mottagaren fick från leverantörernas utsläpp med det referensen ger, för A och U var för sig:
   - Mottagarens avvikelse är skillnaden i A plus skillnaden i U, räknat utan tecken.
   - Mätområdets D är summan av alla mottagares avvikelser delad med två gånger E. Varje ton som hamnat fel räknas två gånger, som överskott hos en mottagare och som underskott hos en annan.
   - Mottagarens D är mottagarens avvikelse delad med summan av det mottagaren fick och det referensen ger.

   E är det som mätområdet fördelar av leverantörernas A och U under perioden, med avdrag för lagerförändring om mätområdet har lagerkonto enligt [MF-001](mf-001-lagerhantering.md). Fördelningen och referensen ska summera till E. Båda värdena ligger mellan 0 och 1.

   En rättelse som enligt [MF-006](mf-006-periodregel.md) bokförs i nästa period kan ge negativa mängder. Den räknas inte in utan redovisas bredvid.

5. **Redovisning.** Varje mottagare får sitt D, vad den fick och vad den skulle ha fått enligt referensen, för A och U var för sig, och vilket mätområde, vilken referens och vilken mottagarnivå jämförelsen gäller, till exempel kund eller leveransgrupp. Mottagaren får också veta hur stor del av dess mängder som bygger på registrerade kopplingar. Mätområdets D kan lämnas till andra, till exempel i en upphandling. Då lämnas också det högsta mottagar-D och antalet mottagare, utan att mottagarna namnges. Den som efterfrågar D anger vilken grund som gäller: mätområde, referensens rang och mottagarnivå.

6. **Tolkning.** Ett högt D betyder inte att en allokeringsnyckel som §3 tillåter är fel. D jämförs bara när mätområde, referensens rang och mottagarnivå är av samma slag och redovisas, till exempel mellan anbudsgivare som räknat D för den anläggning som levererar. D säger inget om vad som hänt längre upp i kedjan.

## Exempel

En grossist köper 100 ton material från en grön leverantör, som bär 40 ton CO2e, och 100 ton från en brun, som bär 200 ton. Inköpen från den gröna görs för kund X och inköpen från den bruna för kund Y. Referensen är alltså X 40 och Y 200 ton, och E = 240. Talen är påhittade.

Grossisten är en nod och fördelar efter massa, så X och Y får 120 ton var.

| | X | Y |
|---|---:|---:|
| Fick | 120 | 120 |
| Referensen | 40 | 200 |
| Avvikelse | 80 | 80 |
| Mottagarens D | 80 / (120 + 40) = 0,50 | 80 / (120 + 200) = 0,25 |

Mätområdets D är (80 + 80) / (2 × 240) = 0,33. Det betyder att 80 av 240 ton har hamnat hos fel kund. X påverkas mest, eftersom X köpte grönt och fick tre gånger mer än referensen.

Har grossisten i stället en nod för grönt och en för brunt får X 40 och Y 200 ton, och mätområdets D blir 0.

## Varför D räknas för ett mätområde

Om D räknades inne i varje nod skulle det inte se utjämning som görs när posterna fördelas på organisationens noder. Därför ska mätområdet omfatta det steget, krav (b) i punkt 2.

| Grossistens indelning | X får | Y får | D inne i varje nod | D för mätområdet |
|---|---:|---:|---:|---:|
| En nod | 120 | 120 | 0,33 | 0,33 |
| En nod per kund, posterna följer inköpen | 40 | 200 | 0 | 0 |
| En nod per kund, varje post delad hälften var | 120 | 120 | 0 | 0,33 |
| En grön och en brun nod | 40 | 200 | 0 | 0 |

I den tredje raden har varje nod bara en kund, så inne i noden finns inget att avvika från. Kunderna får ändå samma snitt som med en nod.

Mätområdet ändrar inte hur något räknas. Fördelningen sker nod för nod. Bara mätningen görs för mätområdet, och aldrig utanför organisationen. Krav (a) i punkt 2 gör att olika indelningar mäts mot samma mätområde och kan jämföras.

## Mer om referensen

Kopplingen kan gälla flera inköp åt gången. Har grossisten ett artikelnummer för gröna varor, som köps från två leverantörer, följs båda inköpen åt till dem som köper artikeln. Inom artikeln blandas de två leverantörerna, eftersom kopplingen bara finns på artikelnivå. Vet grossisten vilken leverantör varje leverans kom från ska den uppgiften användas, eftersom referensen då följer varje post.

Kopplingen gäller affären, inte materialet. Köper ett stålverk grönt skrot för en viss kunds order gäller kopplingen även om skrotet smälts tillsammans med annat ([produktnivåinvändningen](../fordjupningar/produktniva-invandningen.md#3-det-fall-där-invändningen-har-en-reell-poäng)). Varor i lager kopplas via lagrets artiklar. Köps råvaran till gemensam drift utan koppling till någon försäljning blir referensen snittet, och D = 0 är rätt.

## Begränsningar

D gäller mätområdet. Skillnader kan redan ha jämnats ut hos leverantören. D räknas per period och säger inget om skillnader mellan perioder. Byte av referens, mätområde eller mottagarnivå kan ändra D utan att utsläppen har ändrats, så versionskontroll behövs när D följs över tid.

## Alternativ som övervägts

- D inne i varje nod. Avvisat, se tabellen ovan och [fördjupningen, avsnitt 6](../fordjupningar/fordelningsmattet-d.md#6-varför-d-räknas-för-ett-mätområde-och-inte-inne-i-varje-nod).
- Att förbjuda noder per kund. Avvisat, eftersom utjämningen kan göras med vilken indelning som helst, och eftersom det skulle träffa legitima noder med en enda kund.
- Ett enda D för hela organisationen. Avvisat, eftersom små utjämningar försvinner i en stor organisation ([fördjupningen, avsnitt 4](../fordjupningar/fordelningsmattet-d.md#4-vanliga-situationer)).
- En avtalad fördelning som referens. Avvisat, eftersom en referens lika med fördelningen ger D = 0.
- Ett mått på bara A + U. Avvisat, eftersom det missar utjämning mellan faktisk och okänd del.
- En övre uppskattning av D när ingen referens finns. Avvisad, eftersom en grov uppskattning inte är visad vara en övre gräns för alla tillåtna nycklar.

## Öppna frågor

- Hur ska skillnader i nodens egna utsläpp mätas? Exempel: ett stålverk har två linjer, en som drivs med fossilfri el och en med naturgas. Är stålverket en nod får kunderna på båda linjerna samma snitt. D visar inte det, eftersom linjernas utsläpp är stålverkets egna. Ett förslag är andelen av nodens egna utsläpp som mäts i noden, i stället för att fördelas från en gemensam resurs med en nyckel.
- Behövs en storleksgräns för det högsta mottagar-D som lämnas vidare, punkt 5? En mycket liten mottagare kan få ett högt D av en liten avvikelse.
- Räcker andelen registrerade kopplingar, punkt 5, som ett enklare mått i små organisationer?

## Beräkningskontroll

Formlernas egenskaper kan kontrolleras med [d-fast-avgransning.py](../assets/berakningar/d-fast-avgransning.py), som räknar med exakta bråk.

## Beslut

Inte behandlat. Förslaget avser ett nytt mått i §8 och kräver separat beslut.
