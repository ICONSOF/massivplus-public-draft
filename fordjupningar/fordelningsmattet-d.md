---
layout: default_banner
title: "Fördelningsmåttet D"
parent: "Fördjupningar"
nav_order: 15
---

# Fördelningsmåttet D

> **Poäng:** D visar hur stor andel av utsläppen från leverantörerna som har hamnat hos andra kunder än dem inköpen gjordes för. En kund kan se om ett grönare inköp når fram, och en organisation kan se vilken nodindelning som bevarar skillnaderna bäst.

Måttet föreslås i [MF-002](../forslag/mf-002-utspadning.md), som ännu inte är antaget. Den här texten visar hur det räknas och används i praktiken.

---

## 1. Vad D är

En organisation som köper från flera leverantörer kan ge alla kunder samma snitt. Då får en kund som köpt grönt samma tal som en kund som köpt brunt. D visar hur mycket av leverantörernas utsläpp som har hamnat fel på det sättet.

- D = 0: alla kunder har fått utsläppen från de inköp som gjordes för dem.
- D = 1: allt har hamnat hos fel kund.

D gäller skillnader i utsläpp mellan de poster organisationen tar emot från sina leverantörer, åt båda hållen och oavsett orsak. Två leveranser från samma leverantör är olika poster bara om leverantören deklarerar dem var för sig. Det spelar ingen roll om skillnaden beror på grönt stål, fossilfri el hos leverantören eller kortare transporter. Den som köpt grönare och fått för mycket syns, och den som köpt med högre utsläpp och fått för lite syns också. Egenskaper som inte ändrar utsläppen, till exempel ursprung, andel återvunnet material eller certifiering, syns inte i D. Skillnader i organisationens egna utsläpp mäts inte heller av D.

## 2. Varför D behövs

MASSIV+ ska göra det möjligt att minska utsläppen genom att välja grönare inköp. Det fungerar bara om valet syns i talen hela vägen till den som valde. D behövs för två saker.

**Kunden ska kunna se att ett grönare inköp når fram.** En kund som betalar för grönare material, eller ställer krav på det, behöver veta att leverantörens fördelning för vidare skillnaden. Kundens eget D visar det. Är det högt har kundens val jämnats ut, och kunden kan fråga leverantören varför.

**Organisationen ska kunna välja en bra nodindelning.** Hur noderna delas in avgör om skillnaderna mellan leverantörerna bevaras. En enda nod jämnar ut allt. En nod per artikelgrupp kan hålla isär grönt och brunt. D gör det möjligt att jämföra indelningarna:

1. Välj ett mätområde, normalt anläggningen.
2. Räkna D för mätområdet med den nuvarande indelningen.
3. Räkna D för samma mätområde med de indelningar som är tänkbara, till exempel en nod per artikelgrupp eller per leverantör.
4. Välj den indelning som ger lågt D och som går att dokumentera och behålla från period till period, enligt [MF-004](../forslag/mf-004-nodindelning.md).

Lägst möjliga D är inget mål i sig. En finare indelning kräver mer data och arbete. D visar vad den finare indelningen ger, så att organisationen kan avgöra om det är värt det.

## 3. Räkna D steg för steg

En grossist köper två sorters material. Talen är påhittade.

| Inköp | Gjort för | Utsläpp |
|---|---|---:|
| Grön leverantör, 100 ton | Kund X | 40 ton CO2e |
| Brun leverantör, 100 ton | Kund Y | 200 ton CO2e |
| Summa | | 240 ton |

Grossisten är en enda nod och fördelar efter massa. Båda kunderna får därför 120 ton.

**Steg 1. Vad borde varje kund ha fått?** Följ kopplingen mellan inköp och försäljning. Inköpet från den gröna leverantören gjordes för X, så X borde ha fått 40 ton. Y borde ha fått 200. Det kallas referensen.

**Steg 2. Hur mycket skiljer det?** Jämför det kunden fick med referensen, utan tecken. X fick 120 men borde ha fått 40, en skillnad på 80. Y fick 120 men borde ha fått 200, också 80. Har leverantörerna både faktiska (A) och okända (U) utsläpp jämförs de var för sig och läggs ihop.

**Steg 3. Mätområdets D.** Lägg ihop skillnaderna och dela med två gånger allt som kom in:

> (80 + 80) / (2 × 240) = 0,33

Varje ton som hamnat fel räknas två gånger, som överskott hos en kund och som underskott hos en annan. Därför delas med två. Det betyder att 80 av 240 ton, en tredjedel, har hamnat hos fel kund.

**Steg 4. Varje kunds D.** Dela kundens skillnad med det kunden fick plus det kunden borde ha fått:

> X: 80 / (120 + 40) = 0,50
>
> Y: 80 / (120 + 200) = 0,25

X påverkas mest, eftersom X köpte grönt men fick tre gånger mer än referensen.

**Med en nod för grönt och en för brunt** får X 40 och Y 200 ton. Skillnaderna blir noll, och D = 0.

## 4. Vanliga situationer

**Kunderna köper från flera leverantörer.** Har grossisten ett artikelnummer för gröna varor, som köps från två leverantörer, följer kopplingen artikeln. Exempel: den gröna artikeln bär 24 ton, och X har köpt tre fjärdedelar av den. Då borde X ha fått 18 ton. Har grossisten en nod för den gröna artikeln och en för den bruna får X sina 18 ton, och D = 0. Är grossisten en enda nod får X i stället snittet av båda artiklarna. Inom artikeln skiljs leverantörerna inte åt, eftersom kopplingen bara finns på artikelnivå. Vet grossisten vilken leverantör varje leverans kom från ska den uppgiften användas.

**Varor i lager.** Kopplingen går via lagrets artiklar: lagersystemet visar att X:s försäljning kom ur det gröna lagret. Har grossisten en nod för grönt och en för brunt, med var sitt lagerkonto enligt [MF-001](../forslag/mf-001-lagerhantering.md), bevaras skillnaden genom lagret.

**Flera steg inom samma bolag.** Följ kopplingen steg för steg, till exempel från inköp via smältverk och valsning till försäljning. Köptes grönt skrot för en viss kunds order gäller kopplingen även om skrotet smälts tillsammans med annat. Saknas kopplingen i något steg borde alla kunder efter det steget ha fått snittet.

**Ett stort bolag.** Räkna inte D för hela koncernen på en gång. Små utjämningar försvinner då i det stora talet. Dela in bolaget i några stabila mätområden, normalt anläggningarna, och räkna D för vart och ett. Ett flöde mellan två mätområden räknas som en post från en leverantör.

**Leverantörer som deklarerar och leverantörer som inte gör det.** D jämför A och U var för sig. Får en kund som köpt från en leverantör som deklarerar ändå bara snittet av A och U, syns det i D, även om kunden fick rätt mängd totalt.

## 5. Läsa värdena

- **Titta på kundens eget D, inte bara mätområdets.** Ett lågt D för mätområdet kan dölja att en liten kund har fått mycket fel. Exempel: mätområdets D är 0,08, men en liten kund har fått nästan fem gånger så mycket som referensen, och kundens D är 0,64.
- **Jämför bara D på samma grund.** Om två kundgrupper slås ihop till en kan D sjunka utan att något har ändrats. Därför anges alltid vilket mätområde, vilken referens och vilken mottagarnivå D gäller. Anbudsgivare i en upphandling kan jämföras när alla räknat på samma grund, till exempel för den anläggning som levererar.
- **Ett högt D betyder inte att något är fel.** En nyckel som specifikationen tillåter kan ge ett högt D. D visar vad nyckeln gör med skillnaderna mellan leverantörerna.

## 6. Varför D räknas för ett mätområde och inte inne i varje nod

En nod med en enda kund får alltid D = 0 om D räknas inne i noden. En grossist kan då dela in sig i en nod per kund, dela varje leverantörs post hälften var på noderna och ändå ge kunderna samma snitt som förut. Varje nod får D = 0, men utjämningen finns kvar. Den gjordes när posterna fördelades på noderna.

Därför räknar MF-002 D för ett mätområde som omfattar det steget. Fördelningen sker fortfarande nod för nod. Det är bara mätningen som görs för mätområdet, och aldrig utanför organisationen.
