---
layout: default_banner
title: "MF-002 Utspädning i genomströmningsnoder"
parent: "Förslag"
nav_order: 2
forslag_id: MF-002
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§1, §3, §8"
forslag_forfattare: Birger Löfgren
---

# MF-002 Utspädning i genomströmningsnoder

> **Status:** Utkast. Inte beslutat och ingår inte i standarden. Diskuteras i [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> Berör §1, §3 och §8. Författare: Birger Löfgren.

## Problem

En grossist köper 100 ton av en vara från en leverantör med låga utsläpp, med en ärvd börda på 40 ton CO2e, och 100 ton av samma vara från en annan leverantör, med 200 ton CO2e. Den egna Scope 1+2 är 5 ton. Kund X köper varan från den första leverantören och kund Y resten.

Räknas hela grossisten som en nod och fördelas bördan efter massa får båda kunderna 122,5 ton. X har köpt varan med låga utsläpp men får samma tal som Y. Delas noden efter inflöde får X 42,5 ton och Y 202,5 ton. Båda uppfyller specifikationens krav på allokering, och summan är densamma. Skillnaden ligger i hur noden är avgränsad.

Coverage ser inte den här skillnaden. En nod kan ha bara faktisk data och ändå radera den differentiering som kom in uppströms.

## Förslag

Utkast till tillägg:

- **Rekommenderad avgränsning.** Där det går att följa vilket inflöde som gick till vilken kund bör noden avgränsas så att inflöden från olika leverantörer inte förs samman i en gemensam fördelning. Hur fint noden delas är fortfarande användarens val, och avvägningen mot insamlingsbördan i §1 står kvar.
- **Individuation.** En nod avgränsas av en motpart eller av en fysisk enhet vars utsläpp går att mäta för sig. Gods som passerar noden används som allokeringsinformation inom den, inte som grund för avgränsningen.
- **Måttet Dilution (D).** D är den andel av nodens ärvda börda som fördelningen flyttar bort från de kunder vars köp den följer:

  ```
  D = ½ · Σⱼ |κⱼ − ρⱼ|
  ```

  där κⱼ är kund j:s andel av nodens fördelningsnyckel och ρⱼ är kund j:s andel av den ärvda bördan när den följer godset. Båda är andelar, så D är detsamma oavsett om noden fördelar efter massa, energi, värde eller något annat. D ligger mellan 0 och 1. Den egna Scope 1+2 ingår inte, eftersom den fördelas med nyckel hur noden än är avgränsad.
- **Redovisning.** Noden redovisar D vid sidan av Coverage, och om det var data eller ett eget val som satte gränsen för avgränsningen. Saknas kopplingen mellan inflöde och kund går ρ inte att räkna. Noden redovisar då en övre uppskattning räknad på inflödena, och anger data som orsak.

Textändringen i specifikationen är inte skriven än.

## Räkneexempel

Exemplet ovan, med massa som nyckel. Hela grossisten som en nod ger κ = (0,50 ; 0,50) och ρ = (40/240 ; 200/240) = (0,17 ; 0,83):

D = ½ · (|0,50 − 0,17| + |0,50 − 0,83|) = **0,33**

En tredjedel av den ärvda bördan hamnar hos fel kund. Med värde som nyckel, där X står för 60 procent av intäkten, blir κ = (0,60 ; 0,40) och D = 0,43.

Antag att grossisten har två siter, ett lager med 4 ton egen Scope 1+2 och en kapverkstad med 1 ton, att allt gods går genom lagret och att bara Y:s gods kapas. Med massa som nyckel ger de fyra avgränsningarna:

| Avgränsning | D | X | Y |
|---|---|---|---|
| Hela grossisten | 0,33 | 122,5 | 122,5 |
| Per site | 0,33 i lagret, 0 i kapverkstaden | 122 | 123 |
| Per leverantör | 0 i båda | 42,5 | 202,5 |
| Per kund | 0 i båda | 42,5 | 202,5 |

## Konsekvenser

Uppdelning efter var energin används gör den egna bördan mer korrekt, men påverkar inte utspädningen så länge båda leverantörernas gods passerar samma site. Det som avgör hur långt utspädningen går att få ned är kopplingen mellan inflöde och kund. En nod per kund kan inte flytta börda till någon annan kund och har därför alltid D = 0, också när energin inte mäts per kund. Den egna bördan fördelas då in i noderna enligt mönstret för delade resurser i §1.

Rekommendationen kostar bara där kopplingen finns och noden ändå väljer en grövre avgränsning. D gör det valet synligt, och kunden kan skilja en nod som saknar data från en som avstått från att använda den.

D ger också ett sakligt skäl att byta noduppdelning, nämligen att D sjunker, och det skälet kan redovisas. Bytet går genom versionshanteringen av nodpartitionen i §1. Se [#39](https://github.com/ICONSOF/massivplus-public-draft/discussions/39).

## Alternativ som övervägts

- **En separat spårningsmekanism vid sidan av noderna.** Den behövs inte, eftersom en finare avgränsning gör samma arbete.
- **Ett krav på den finaste nivå där datan finns.** Det tar bort användarens avvägning i §1, också där en finare uppdelning är dyr och skillnaden liten.
- **En kvalitativ beskrivning av hur fint noden är avgränsad.** Den går inte att jämföra mellan noder. Två noder som båda anger "per affärsenhet" kan ha helt olika mycket utspädning.

## Öppna frågor

- **Ojämna mängder.** D mäter vad noden som helhet blandar ihop, inte hur hårt en enskild kund drabbas. Köper grossisten 20 ton från leverantören med låga utsläpp (8 ton CO2e) och 180 ton från den andra (360 ton CO2e) blir D bara 0,08, men X får 36,8 ton i stället för 8. Behövs ett mått per kundflöde vid sidan av D?
- **Fysisk blandning.** Där flöden blandas fysiskt, som i ett el- eller fjärrvärmenät, finns ingen spårning att jämföra mot och ρ är inte definierat.
- **Den övre uppskattningen.** Utan koppling mellan inflöde och kund jämförs varje leverantörs andel av den ärvda bördan med samma leverantörs andel av nyckeln. För fysiska nycklar som massa och energiinnehåll följer den andelen av inköpen. Ett värde uppstår först vid försäljningen, och då behövs ett närmevärde, till exempel andelen av inköpsvärdet. Det förutsätter samma påslag på alla varor. Gör det inte det kan uppskattningen hamna under det verkliga D, och då är den inte längre en övre gräns.
- **Verktygsstöd.** Eftersom D går att räkna ur data noden redan har, skulle ett verktyg kunna föreslå en noduppdelning genom att pröva delningar och visa hur D faller med antalet noder. Om det är praktiskt behöver utforskas: vilken data som finns tillgänglig i affärssystemen, och hur en föreslagen uppdelning hålls stabil över flera perioder.

## Beslut

Inte behandlat.
