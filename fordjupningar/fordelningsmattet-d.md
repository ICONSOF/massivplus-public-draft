---
layout: default_banner
title: "Fördelningsmåttet D"
parent: "Fördjupningar"
nav_order: 15
---

# Fördelningsmåttet D

> **Poäng:** D visar hur stor andel av utsläppen från leverantörerna som har hamnat hos andra kunder än dem inköpen gjordes för. Det gör det möjligt för en kund att se om ett grönare inköp når fram, och för en organisation att välja den nodindelning som bevarar skillnaderna mellan leverantörerna bäst.

Måttet föreslås i [MF-002](../forslag/mf-002-utspadning.md), som ännu inte är antaget. Här finns fler exempel och bakgrunden till valen.

---

## 1. Vad D mäter, och vad det inte mäter

D gäller ingen produktegenskap. Grönt stål är bara ett exempel. D mäter om skillnaderna mellan en organisations inkommande poster bevaras när den fördelar till kunderna. Olika poster ger olika mängd utsläpp per inköpt kvantitet, och varför de skiljer sig spelar ingen roll.

D mäter inte skillnader i organisationens egna utsläpp, till exempel mellan en linje med fossilfri el och en utan. Det behöver ett annat mått, som står som öppen fråga i MF-002.

## 2. När kunderna köper från flera leverantörer

| Inköp | Artikel | Material | Utsläpp |
|---|---|---:|---:|
| Leverantör A | Grön | 40 ton | 10 ton CO2e |
| Leverantör B | Grön | 40 ton | 14 ton CO2e |
| Leverantör C | Brun | 100 ton | 200 ton CO2e |

X köper 60 ton grönt. Y köper 20 ton grönt och 100 ton brunt. Kopplingen finns på artikelnivå. Den gröna artikeln bär 24 ton, och X har köpt tre fjärdedelar av den, så referensen ger X 18 ton och Y 6 + 200 = 206 ton.

En nod med massnyckel fördelar 224 ton på 180 ton material: X får 74,7 och Y 149,3. Avvikelsen är 56,7 ton för båda, och D = 113,3 / 448 = 0,25. En nod per artikel ger D = 0.

## 3. A och U jämförs var för sig

Referensen ger X 100 ton A och Y 100 ton U. En gemensam nod ger båda 50 A och 50 U. Båda får 100 ton, så en jämförelse av totalerna ger D = 0. Jämförs A och U var för sig blir D = 0,5.

Områdets Coverage är 0,5 i båda fallen, men kundernas går från 1 och 0 till 0,5. D visar alltså också om skillnaden mellan en leverantör som deklarerar och en som inte gör det når fram.

## 4. Ett lågt D för området kan dölja en kunds avvikelse

Referensen ger X 8 ton och Y 360. En massnyckel på 10/90 ger X 36,8 och Y 331,2. Områdets D är 0,078, men X får 28,8 ton mer än referensen, och X:s eget värde är 0,64. Därför får varje kund sitt eget värde, och mängd och riktning.

Områdets D är ett viktat medelvärde av kundernas värden. Vikten för en kund är (fått + referens) / (2E), och vikterna summerar till 1.

## 5. Mottagarnivån påverkar D

Är X och Y i exemplet i avsnitt 3 två leveransgrupper till samma kund blir D 0,5 när grupperna jämförs separat, men noll om de slås ihop till en kundtotal. Därför anges mottagarnivån tillsammans med värdet.

## 6. Varför inte D inne i varje nod

En nod med en enda kund får alltid D = 0 om D räknas inne i noden. En grossist som jämnar ut inflödena kan därför dela in sig i en nod per kund och dela varje post hälften var på noderna. Kunderna får samma snitt som förut, men varje nod får D = 0. Samma lucka finns med varje indelning: läggs halva den bruna posten i den gröna noden blir D inne i noderna också 0.

Att förbjuda noder per kund löser inte det, eftersom utjämningen går att göra ändå. Det skulle också träffa legitima noder med en enda kund, till exempel en linje som bara tillverkar åt en fordonstillverkare.

Ett sätt att stanna helt i noden vore att redovisa fördelningen av inkommande poster på egna noder som en egen nod och räkna D där. För att jämföra olika indelningar måste nodernas värden ändå läggas ihop för organisationen. MF-002 räknar därför D för ett område. Fördelningen sker fortfarande nod för nod, och bara mätningen görs för området.

## 7. Stora organisationer och många interna noder

I en koncern späds D ut om hela koncernen är ett område. Jämnar en anläggning ut 5 000 ton i en koncern med E = 2 miljoner ton blir koncernens D 0,0025. Koncernen kan därför dela in sig i flera stabila områden, till exempel anläggningar eller affärsområden, där flöden mellan områdena räknas som poster. Utjämning syns då i det område där den görs.

Med många interna steg mellan inköp och kund, till exempel smältverk, valsning och lager, byggs referensen steg för steg utifrån kopplingen mellan inköp och försäljning. Området behöver bara sträcka sig så långt som den kopplingen finns. Egna utsläpp i ett internt steg bokförs som Actual i nästa (§4), så varje internt flöde delas i inflöde från leverantörer och egna utsläpp.

Ett område ligger inom en rapporteringsentitet, på samma sätt som en nod ligger inom en organisation. Är varje bolag i en koncern sin egen entitet är försäljning mellan bolagen poster mellan organisationer, och D mäts i respektive bolag.

## 8. Lager

Ett inköp till lager har ingen kund när det görs, men försäljningen ur lagret registreras per artikel. Har det gröna en egen artikel visar lagersystemet att X:s försäljning kom ur det gröna lagret. Lagerkontot i [MF-001](../forslag/mf-001-lagerhantering.md) gäller per nod. Med en nod per artikelgrupp har varje nod sitt lagerkonto, och skillnaden bevaras genom lagret. Är allt en nod jämnar lagerkontot ut skillnaden, och D visar det.

## 9. Som i kostnadsredovisningen

Kostnadsredovisningen har länge haft samma problem. Omkostnader som fördelas med en grov nyckel gör att vissa produkter och kunder subventionerar andra. Aktivitetsbaserad kalkylering jämför den grova fördelningen med en fördelning efter vad som driver kostnaden, och skillnaden per kund motsvarar kundens D. Rangordningen för referensen i MF-002, registrerad koppling före drivare före volymnyckel, följer kostnadsredovisningens ordning: direkt hänförbart först, sedan efter drivare, sist med volymnyckel.

Kaplan och Ramanna hänvisar till aktivitetsbaserad kalkylering men kräver att fördelningen på produkter granskas med rimlig säkerhet ([bokföringsanalogin](bokforingsanalogin.md#4-den-framväxande-tanken-om-bokföring-av-utsläpp)). MASSIV+ kräver ingen viss fördelning, men mäter hur mycket den avviker.

## 10. Andra alternativ som övervägts

- Bara ett D för hela organisationen. Späds ut i stora organisationer, och en liten kund kan påverkas mycket utan att det syns.
- En generell övre uppskattning av D när ingen referens finns. En grov uppskattning är inte visad vara en övre gräns för alla tillåtna nycklar.
