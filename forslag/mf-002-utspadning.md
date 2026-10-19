---
layout: default_banner
title: "MF-002 Utspädning i genomströmningsnoder"
parent: "Förslag"
nav_order: 2
forslag_id: MF-002
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§1, §8"
forslag_forfattare: Birger Löfgren
forslag_diskussion: https://github.com/ICONSOF/massivplus-public-draft/discussions/49
---

# MF-002 Utspädning i genomströmningsnoder

> **Status:** Utkast. Inte beslutat och ingår inte i standarden. Diskuteras i [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> Berör §1 och §8. Författare: Birger Löfgren.

## Problem

En genomströmningsnod köper in, bearbetar lite och säljer vidare. Nästan alla dess utsläpp kommer uppströms ifrån.

En grossist köper 100 ton av en vara från en leverantör med låga utsläpp och 100 ton av samma vara från en annan leverantör. Den första leveransen bär 40 ton CO2e i uppströmsutsläpp, den andra 200 ton. Grossistens egen Scope 1+2 är 5 ton. Kund X köper varan från den första leverantören och kund Y resten.

Är grossisten en nod som fördelar efter massa får båda kunderna 122,5 ton. X har köpt varan med låga utsläpp men får samma tal som Y. Delas grossisten i en nod per leverantör får X 42,5 ton och Y 202,5 ton. Båda sätten följer specifikationen, och summan är densamma.

Skillnaden ligger i avgränsningen. En nod tillämpar samma andel Shareᵢⱼ på hela sin utsläppsmassa (§3, §4), så alla mottagare av en nod får samma sammansättning per enhet av nyckeln. Utspädning går bara att undvika genom hur noderna avgränsas.

Coverage späds ut på samma sätt. Anta att leverantören med låga utsläpp rapporterar enligt MASSIV+, så att dess 40 ton är faktisk data (A), medan den andra leverantörens 200 ton är okända (U). Som en nod får båda kunderna Coverage 0,18, alltså (5 + 40) / 245. Med en nod per leverantör får X Coverage 1 och Y 0,01. X:s vara har helt faktisk grund, men i en gemensam nod syns det inte.

## Förslag

Fyra tillägg. Textändringen i specifikationen är inte skriven än.

1. **Rekommenderad avgränsning (§1).** Vet noden vilket inflöde som gick till vilken mottagare bör den avgränsas så att inflöden från olika leverantörer inte fördelas tillsammans. Hur fint noden delas är fortfarande användarens val.
2. **Vad som avgränsar en nod (§1).** En nod avgränsas av en motpart eller av en fysisk enhet vars utsläpp går att mäta för sig, aldrig av godset. En nod per vara skulle ge ett tal som följer varan, och det är enligt §5 en produktallokering.
3. **Måttet Dilution, D (§8).** D är den andel av nodens uppströmsutsläpp Aᵢ + Uᵢ som hamnar hos fel mottagare:

   ```
   Dᵢ = ½ · Σⱼ |Shareᵢⱼ − ρᵢⱼ|
   ```

   Shareᵢⱼ är mottagare j:s andel enligt nodens allokeringsregel (§4). ρᵢⱼ är mottagarens andel av uppströmsutsläppen om varje leverantörs utsläpp följer leverantörens gods, fördelat efter fysisk mängd. Båda är andelar, så D går att räkna med alla allokeringsmetoder i §3. D ligger mellan 0 och 1. D är det egna mått som §8 efterlyser för relevansaxeln, för den del som gäller uppströmsutsläppen.
4. **Redovisning (§8).** Noden redovisar D tillsammans med Coverage och anger vad som satte gränsen för avgränsningen: data eller eget val. Vet noden inte vilket inflöde som gick till vilken mottagare går ρ inte att räkna. Noden redovisar då en övre uppskattning räknad på inflödena och anger data som orsak.

## Räkneexempel

Grossisten som en nod, med massa som nyckel: Share = (0,50 ; 0,50) och ρ = (40/240 ; 200/240) = (0,17 ; 0,83).

```
D = ½ · (|0,50 − 0,17| + |0,50 − 0,83|) = 0,33
```

En tredjedel av uppströmsutsläppen hamnar hos fel kund.

Anta nu att grossisten har två siter: ett lager med 4 ton egen Scope 1+2 och en kapverkstad med 1 ton. Allt gods går genom lagret, och bara Y:s gods kapas. I de två sista raderna är lagret och kapverkstaden egna noder för delade resurser (§1), som fördelar sina utsläpp till de noder som använder dem.

| Avgränsning | D | X får | Y får |
|---|---|---|---|
| En nod | 0,33 | 122,5 | 122,5 |
| En nod per site | 0,33 i lagret, 0 i kapverkstaden | 122 | 123 |
| En nod per leverantör | 0 | 42 | 203 |
| En nod per kund | 0 | 42 | 203 |

En nod per site gör den egna Scope 1+2 mer rätt men sänker inte D, eftersom båda leverantörernas gods går genom lagret. En nod per kund har alltid D = 0, eftersom det inte finns någon annan mottagare att flytta utsläpp till.

D beror också på nyckeln. Med intäkt som nyckel, där X står för 60 procent av intäkten, blir D = 0,43 för grossisten som en nod. Även en nod med en enda leverantör får D över 0 med intäkt som nyckel om två kunder betalar olika pris för samma vara. Den som betalar mer får då mer av utsläppen, fast godset är detsamma.

## Konsekvenser

Hur långt D går att få ned avgörs av om noden vet vilket inflöde som gick till vilken mottagare. Var energin mäts påverkar bara den egna Scope 1+2.

Rekommendationen kostar bara när noden har den kopplingen och ändå väljer en grövre avgränsning. D gör det valet synligt för mottagaren.

En nod per leverantör eller per kund har ingen egen energianvändning. Den får sin del av lokalens utsläpp från en nod för den delade resursen. §1 tillåter "vilken annan konsekvent definierad enhet som helst", men beskriver också en nod som en enhet som mäter sina egna Scope 1 och 2. §1 behöver förtydligas så att en nod kan ha noll egna utsläpp.

D ger ett skäl att byta noduppdelning som går att redovisa: D sjunker. Bytet görs under versionskontrollen i §1. Se [#39](https://github.com/ICONSOF/massivplus-public-draft/discussions/39).

## Alternativ som övervägts

- Ett krav på den finaste avgränsning datan medger. Det tar bort användarens avvägning mot insamlingsbördan i §1.
- En beskrivning i ord av hur fint noden är avgränsad. Den går inte att jämföra mellan noder.
- Att låta uppströmsutsläppen följa godset inom en nod. Det strider mot §4, där en andel gäller hela utsläppsmassan, och mot individuationskriteriet i §5.
- En separat spårningsmekanism vid sidan av noderna. En finare avgränsning gör samma arbete.

## Öppna frågor

- Ojämna mängder. D mäter noden som helhet, inte hur hårt en enskild kund drabbas. Med 20 ton från leverantören med låga utsläpp (8 ton CO2e) och 180 ton från den andra (360 ton CO2e) blir D 0,08, men X får 36,8 ton i stället för 8. Behövs ett mått per mottagare?
- Utspädd Coverage. D räknas på A + U tillsammans. Två leverantörer med lika stora utsläpp, där den ena är A och den andra U, ger D = 0, men en gemensam nod ger ändå båda kunderna Coverage 0,5. Ska D också räknas för A och U var för sig?
- Fysisk blandning. I ett el- eller fjärrvärmenät går godset inte att följa, och ρ är inte definierat.
- Den övre uppskattningen. Den jämför varje leverantörs andel av uppströmsutsläppen med samma leverantörs andel av nyckeln. För massa och energiinnehåll följer den andelen av inköpen. Intäkt uppstår först vid försäljningen och kräver ett närmevärde, till exempel andelen av inköpsvärdet. Är påslaget olika på olika varor kan uppskattningen hamna under det verkliga D.
- Verktygsstöd. Ett verktyg skulle kunna föreslå en noduppdelning genom att pröva delningar och visa hur D faller med antalet noder. Om det är praktiskt behöver utforskas: vilken data affärssystemen har, och hur en föreslagen uppdelning hålls stabil över flera perioder.

## Beslut

Inte behandlat.
