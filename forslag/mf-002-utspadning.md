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

> **Status:** Utkast, omarbetat 2026-10-30, omskrivet 2026-11-22. Ingår inte i standarden. Berör §8. Författare: Birger Löfgren. Diskussion: [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> Vad som får vara en nod behandlas i [MF-004](mf-004-nodindelning.md), och vad som lämnas till nästa organisation i [MF-005](mf-005-allokeringsposter.md).

En grossist köper från en leverantör med låga utsläpp och en med höga. Ger grossisten alla kunder samma snitt får en kund som köpt det gröna inte se det i sina tal. Grossisten kan ändå ha Coverage (faktisk andel, om [MF-008](mf-008-namnbyte.md) antas) 1, eftersom Coverage bara visar hur stor del som har faktisk grund.

Förslaget inför måttet D. D visar hur väl grönare inköp når de kunder som inköpen gjordes för. Grönare betyder här poster med mindre utsläpp per inköpt kvantitet eller med mer faktisk data. D gäller ingen produktegenskap: det mäter om skillnaderna mellan inkommande poster bevaras, oavsett varför de skiljer sig.

D gäller skillnader mellan leverantörer. Skillnader i nodens egna utsläpp, till exempel mellan en linje med fossilfri el och en utan, mäts inte av D.

## Förslag till standardtext

Ett nytt delavsnitt i §8. Definitionerna av Coverage och uppströms-Coverage står kvar.

### D: hur väl skillnader mellan inköp bevaras

1. **Vad D mäter.** D visar hur ett mätområdes fördelning av inkommande A och U till mottagarna avviker från en referens som följer kopplingen mellan inköp och försäljning. Områdets egna Scope 1+2 ingår inte. Det gäller också egna utsläpp som en nod i området fördelar till en annan nod i området, där de bokförs som Actual (§4). Underlaget ska därför visa vilken del av A som kommer från externa leverantörer.

2. **Mätområdet.** Organisationen deklarerar ett eller flera mätområden inom rapporteringsentiteten. Ett område kan vara en nod, en anläggning, ett affärsområde eller hela entiteten. Varje område ska
   1. vara stabilt och inte ändras när noderna inom det ritas om
   2. omfatta steget där inkommande poster fördelas på områdets noder.

   Flöden mellan två mätområden behandlas som poster: inflöde i det mottagande området, mottagare i det avsändande.

3. **Referensen.** Referensen visar hur mottagarna hade fått det om varje leverantörspost följde de inköp som gjordes för dem. Den väljs i denna ordning:
   1. registrerad koppling mellan inköp och försäljning, till exempel order, stycklistor och lagrets artiklar, inklusive avtal som syns i order och leveranser
   2. en drivare eller modell som speglar orsaken, till exempel för ett elnät
   3. en volym- eller värdenyckel.

   En lägre nivå används bara när en högre saknas, och valet motiveras. En avtalad fördelning utan stöd i inköpen är ingen referens. Går ingen referens att ta fram redovisas D som ej beräknat. Referensen bestäms före jämförelsen, dokumenteras och versionshanteras.

4. **Mängderna.** För varje mottagare r används:

   | Beteckning | Betydelse |
   |---|---|
   | a_r, u_r | Inkommande faktiska respektive okända mängder som området fördelar till mottagaren |
   | a_ref,r, u_ref,r | Samma mängder enligt referensen |
   | E | Den inkommande A + U som området fördelar under perioden. Med lagerkonto enligt [MF-001](mf-001-lagerhantering.md) är det inkommande A + U minus lagerförändringen |

   Fördelningen och referensen ska var för sig summera till E, för A och U var för sig. En obalans ska utredas och får inte döljas genom normalisering. En rättelse som enligt [MF-006](mf-006-periodregel.md) bokförs i nästa period kan ge negativa mängder. Den räknas inte in i D utan redovisas bredvid.

5. **Formlerna.**

   ```
   L_r = |a_r - a_ref,r| + |u_r - u_ref,r|
   D_B = sum_r L_r / (2E)
   D_B,r = L_r / (a_r + u_r + a_ref,r + u_ref,r)
   ```

   D_B gäller hela området och D_B,r mottagaren r. Båda ligger mellan 0 och 1. D_B är odefinierat när E är noll, och D_B,r när nämnaren är noll.

6. **Redovisning.** Varje mottagare får sitt D_B,r, sina mängder, referensmängderna och skillnaden, med riktning och med A och U var för sig. Mottagaren får också veta vilket område och vilken referens jämförelsen gäller, och hur stor del av mottagarens mängder som bygger på registrerade kopplingar. Områdets D_B kan lämnas till andra, till exempel i en upphandling.

7. **Tolkning.** D mäter avvikelse från referensen. Ett högt värde betyder inte att en allokeringsnyckel som §3 tillåter är fel. D med olika områden, referenser eller mottagarnivåer jämförs inte med varandra. D gäller området och säger inget om vad som hänt längre upp i kedjan.

## Exempel

En grossist köper 100 ton material från en grön leverantör, med 40 ton CO2e, och 100 ton från en brun, med 200 ton CO2e. Båda deklarerar, så allt är A. Inköpen från den gröna görs för kund X och inköpen från den bruna för kund Y. Referensen blir X 40 och Y 200 ton, och E = 240. Grossistens egna utsläpp ingår inte i D. Talen är påhittade.

Grossisten är en nod och fördelar efter massa, så båda kunderna får 120 ton.

1. Avvikelsen per kund: L_X = |120 − 40| = 80 och L_Y = |120 − 200| = 80.
2. För området: D_B = (80 + 80) / (2 × 240) = 0,33.
3. För kunderna: D_B,X = 80 / (120 + 40) = 0,50 och D_B,Y = 80 / (120 + 200) = 0,25.

D_B går att läsa direkt. Summan av L delat med två är antalet ton som hamnat hos fel kund, här 80 av 240.

Köper X i stället 80 ton av det gröna och Y 20 ton grönt och allt brunt, blir referensen X 32 och Y 208. En nod med massnyckel ger X 96 och Y 144, och D_B = 0,27. En grön och en brun nod ger D_B = 0.

## Varför området omfattar fördelningen på noder

Om D räknades inne i varje nod skulle det inte se utjämning som görs när inkommande poster fördelas på organisationens noder. Det är skälet till krav 2 b.

| Grossistens indelning | X får | Y får | D inne i varje nod | D för området |
|---|---:|---:|---:|---:|
| En nod, massnyckel | 120 | 120 | 0,33 | 0,33 |
| En nod per kund, posterna följer inköpen | 40 | 200 | 0 | 0 |
| En nod per kund, varje post delad hälften var | 120 | 120 | 0 | 0,33 |
| En grön och en brun nod | 40 | 200 | 0 | 0 |

I den tredje raden har varje nod bara en kund, så inne i noden finns ingen fördelning som kan avvika. Kunderna får ändå samma snitt som med en nod. Samma lucka finns med varje indelning: läggs halva den bruna posten i den gröna noden blir D inne i noderna också 0.

Mätområdet ändrar inte hur något räknas. Fördelningen sker nod för nod, och posterna går nod till nod. Bara mätningen görs över området, och aldrig utanför organisationen. Krav 2 a hindrar att områden väljs för att dölja, och gör att olika indelningar kan jämföras mot samma område.

## Referensen följer affären

Referensen bygger på kopplingen mellan inköp och försäljning, inte på materialet.

- Köper ett stålverk grönt skrot för en viss kunds order, följer referensen det inköpet även om skrotet smälts tillsammans med annat ([produktnivåinvändningen](../fordjupningar/produktniva-invandningen.md#3-det-fall-där-invändningen-har-en-reell-poäng)).
- Köps varor till lager går kopplingen genom lagrets artiklar. En nod per artikelgrupp med eget lagerkonto enligt MF-001 håller skillnaden genom lagret.
- Köps råvara till gemensam drift utan koppling till någon försäljning blir referensen snittet, och D = 0 är rätt.
- I ett elnät saknas ofta kopplingen mellan producent och kund. Då kan en modell användas, nivå 2 i rangordningen.

En grossist som redan har uppgifter om leverantör, artikelgrupp och leverans ska använda dem. Ingen behöver kartlägga varje inköps väg genom kedjan för att börja.

Rangordningen följer kostnadsredovisningen, som knyter kostnader först direkt, sedan efter en drivare och sist med en volymnyckel. Aktivitetsbaserad kalkylering jämför på samma sätt en grov fördelning med en fördelning efter orsak, och skillnaden per kund motsvarar D_B,r.

## A och U jämförs var för sig

Referensen ger X 100 ton A och Y 100 ton U. En gemensam nod ger båda 50 A och 50 U. Båda får 100 ton, så en jämförelse av totalerna ger D = 0. Jämförs A och U var för sig blir D_B = 0,5. Områdets Coverage är 0,5 i båda fallen, men kundernas går från 1 och 0 till 0,5. D visar alltså också om skillnaden mellan en leverantör som deklarerar och en som inte gör det bevaras.

## Ett lågt D_B kan dölja en kunds avvikelse

Referensen ger X 8 ton och Y 360. En massnyckel på 10/90 ger X 36,8 och Y 331,2. D_B är 0,078, men X får 28,8 ton mer än referensen, med D_B,X = 0,64. Därför får varje mottagare sitt eget värde, och mängd och riktning.

D_B är ett viktat medelvärde av relationsvärdena, med vikten w_r = (a_r + u_r + a_ref,r + u_ref,r) / (2E). Vikterna summerar till 1.

## Mottagarnivån påverkar D

Är X och Y i föregående exempel två leveransgrupper till samma kund är D_B 0,5 när grupperna jämförs separat, men noll om de slås ihop till en kundtotal. Mottagarnivån anges därför för mottagaren och ska passa syftet.

## Stora organisationer och många interna noder

I en koncern späds D_B ut om hela koncernen är ett område. Jämnar en anläggning ut 5 000 ton i en koncern med E = 2 miljoner ton blir D_B 0,0025. Koncernen kan därför dela in sig i flera stabila områden, till exempel anläggningar eller affärsområden, där flöden mellan områdena behandlas som poster. Utjämning syns då i det område där den görs.

Med många interna steg mellan inköp och kund, till exempel smältverk, valsning och lager, byggs referensen steg för steg utifrån kopplingen mellan inköp och försäljning. Området behöver bara sträcka sig så långt som den kopplingen finns. Egna utsläpp i ett internt steg bokförs som Actual i nästa, så varje internt flöde delas i externt inflöde och egna utsläpp.

## Begränsningar

D gäller fördelningen inom området. Skillnader kan redan ha jämnats ut hos leverantören, och ett lokalt D = 0 visar inte att hela kedjan har bevarat dem. Byte av referens, område, mottagarnivå eller U-underlag kan ändra D utan att utsläppen har ändrats, så versionskontroll behövs när D följs över tid.

## Alternativ som övervägts

- D inne i varje nod. Avvisat, eftersom det inte ser utjämning när poster fördelas på noderna.
- Att förbjuda noder per kund. Avvisat, eftersom utjämningen kan göras med vilken indelning som helst och eftersom MF-004 tillåter gränser efter kunder.
- Bara ett D för hela organisationen. Avvisat, eftersom det späds ut i stora organisationer och en liten kund kan påverkas mycket utan att det syns.
- Ett mått på bara A + U. Avvisat, eftersom det missar utjämning mellan faktisk och okänd del.
- En avtalad fördelning som referens. Avvisat, eftersom en referens lika med fördelningen ger D = 0 per definition.
- En generell övre uppskattning av D när ingen referens finns. Avvisad, eftersom en grov uppskattning inte är visad vara en övre gräns för alla tillåtna nycklar.

## Öppna frågor

- Hur ska skillnader i nodens egna utsläpp mätas? Ett förslag är andelen av nodens egna utsläpp som mäts i noden, i stället för att fördelas från en gemensam resurs med en nyckel.
- Räcker andelen registrerade kopplingar, punkt 6, som ett enklare mått i små organisationer, utan D?

## Beräkningskontroll

Formlernas egenskaper kan kontrolleras med [d-fast-avgransning.py](../assets/berakningar/d-fast-avgransning.py), som räknar med exakta bråk. Programmet kontrollerar balans, gränsvärden, viktningen av relationsvärden, att egna utsläpp hålls utanför och att D inte ändras vid omindelning, med 100 varierade fördelningar.

## Beslut

Inte behandlat. Förslaget avser ett nytt mått i §8 och kräver separat beslut.
