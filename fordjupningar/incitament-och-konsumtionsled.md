---
layout: default
title: "Incitament och konsumtionsled"
nav_order: 10
---

# Var incitamentet att välja lägre uppströmspåverkan bor

> **Poäng:** MASSIV+ skapar incitamentet att välja lägre uppströmspåverkan *endogent* så länge det finns en nedströms nod - propageringen är själv incitamentet. Mot en sänka (en privatkonsument) tar propageringen slut, och där blir MASSIV+ i stället en infrastruktur för incitament: den producerar ett verifierbart, specifikationsupplöst tal vid grinden som en extern policymekanism kan haka i. A/U-separationen - faktisk, deklarerad data (A) respektive ännu okänd (U) - är motorn som avgör hur skarp den signalen kan bli.

Den här texten bygger vidare på [produktnivå-invändningen](produktniva-invandningen.md) - särskilt randvillkoret att propageringen fortsätter så länge mottagaren är en nod och avslutas vid en sänka. Läs [introduktionen](../introduktion.md) först om du inte är bekant med ramverket.

---

## 1. Frågan: hur långt uppströms räcker incitamentet?

En produkt är en konfiguration. Ett fordon kan ha stålkaross eller aluminium, ett visst batteri, ett visst material i inredningen, en viss fälg. Varje specifikation motsvarar en annan uppsättning inkommande affärsrelationer till den tillverkande noden, med olika allokerad börda.

Den operativa frågan är: när skillnaden i specifikation motsvarar en skillnad i uppströmspåverkan, når den skillnaden fram till den som faktiskt väljer specifikationen, och får valet en konsekvens? Svaret beror helt på var sänkan ligger.

---

## 2. Det endogena fallet: incitament genom propagering

När mottagaren är en nod propagerar specifikationsskillnaden vidare som en organisationsallokering. En köpare som väljer den mer utsläppsintensiva konfigurationen får en högre inkommande börda än en köpare som väljer den mindre intensiva, och den bördan propagerar vidare till köparens egna kunder.

Incitamentet är då inbyggt i propageringen. Varje nod vill minska sin inkommande börda för att kunna erbjuda sina kunder ett lägre tal. Specifikationsvalet blir en konkurrensparameter mellan affärsrelationer: det finns en nedströms mottagare som bär skillnaden, och därför finns ett tryck bakåt genom kedjan. I det här fallet skapar MASSIV+ incitamentet själv - propageringen är incitamentet, och ingen extern mekanism behövs för att det ska bita.

---

## 3. Sänkan: från incitament till infrastruktur för incitament

Vid en privatkonsument finns ingen nedströms mottagare. Propageringen tar slut, och frågan blir vad som överhuvudtaget skapar incitamentet. Privatkunden ser ett tal men har utan en extern mekanism ingen anledning att agera på det.

Här är distinktionen som bör hållas ren i positioneringen:

> MASSIV+ skapar incitament endogent så länge det finns en nedströms nod. Mot en sänka blir standarden i stället en infrastruktur för incitament, som behöver en policymekanism för att bita.

MASSIV+ levererar talet per specifikation vid den sista noden (se [produktnivå-invändningen, avsnitt 6](produktniva-invandningen.md)), men själva incitamentet mot en privatkonsument måste komma utifrån. Rätt formulering är därför att standarden gör privatkonsumtion *styrbar* genom att producera ett verifierbart, specifikationsupplöst tal vid grinden - den styr inte privatkonsumtion i sig.

---

## 4. A/U-separationen är motorn

För att ett specifikationsval ska kunna differentieras korrekt måste den inkommande bördan vara faktisk (A) och inte schablon (U) för just de komponenter som skiljer sig åt. Om både den utsläppsintensiva och den mindre intensiva vägen kommer in som U-schabloner kan systemet bara skilja dem åt genom en generisk faktorskillnad, och då är incitamentet bara så skarpt som schablonens upplösning.

Det ger ett argument för A som går utöver korrekthet: A-data är inte bara mer korrekt, det är en *förutsättning* för att specifikationsval ska kunna belönas. Ju högre andel A i de differentierande komponenterna, desto skarpare prissignal kan en specifikation bära. A/U-separationen (se [introduktionen](../introduktion.md)) är därmed inte bara ett mått på datakvalitet utan själva motorn i specifikationsincitamentet.

---

## 5. Policymekanismen: konsumtionsledet

Ett gate-tal vid sänkan är den storhet en konsumtionsledsmekanism behöver. Två exempel, ett etablerat och ett framväxande, visar formen:

- **CBAM** (EU:s gränsjusteringsmekanism för koldioxid) är redan en konsumtionsledsmekanism för en delmängd av varor. Den prissätter inbäddade utsläpp i importerade produkter vid EU:s gräns och förutsätter att ett tal per vara kan fastställas.
- **"Laghum-ekonomin"** (Stefan Krook, *The Laghum Economy: A New Brief for a Healthy Planet*, Volante, 2025) är ett framväxande förslag om att flytta skattebasen från arbete till resurskonsumtion och lägga beskattningen i konsumtionsledet snarare än hos producenten. Förslaget vilar uttryckligen på spårbarhet: känner man produktens resurs- och utsläppsinnehåll beskattas den därefter, annars faller den på en schablonskatt som sätts något högre. Den logiken - exakt tal vid spårbart, schablon vid okänt - är konceptuellt parallell med MASSIV+:s A/U-separation: båda ger ett incitament att deklarera faktiskt snarare än att luta sig mot sekundärdata.

Skillnaden i koordinat kvarstår och bör noteras: dessa mekanismer tänker i produkt- och flödestermer (närmare produktkoldioxidberäkning och E-liability), medan MASSIV+ arbetar i affärsrelationskoordinat på organisationsnivå och löser upp till produkt först vid sänkan. MASSIV+ är alltså den infrastruktur som kan producera det verifierbara gate-talet; policymekanismen är det som gör talet till ett incitament för den som inte längre har någon nedströms affär att propagera till.

---

## 6. Öppen fråga: per komponent eller aggregerat tal

En designfråga avgör hur skarpt incitamentet kan bli, och den gränsar mot koordinatens integritet. Ska den differentierande bördan kunna brytas ut *per komponent* i nodens tal till nästa nod, eller bara som ett *aggregerat produkttal*?

- Per komponent ger en mycket skarpare styrning - en köpare kan se att det är just ett enskilt materialval som driver bördan. Men det närmar sig produktupplösning inne i propageringen, den gräns som [produktnivå-invändningen](produktniva-invandningen.md) håller.
- Aggregerat tal håller koordinaten ren men trubbar av signalen.

Detta är en oavgjord designfråga snarare än en löst regel. Den bör lösas i samklang med individuationskriteriet: en per-komponent-uppdelning som förblir en egenskap hos affärsrelationen (varierar med motparten) håller koordinaten; en som blir en egenskap hos godset (följer med oavsett köpare) tippar över i produktkoordinat. Var gränsen dras påverkar den normativa specifikationen och behandlas därför också där.

---

## 7. Sammanfattning

> Uppströms är propageringen incitamentet: varje nod vill sänka sin inkommande börda för att erbjuda kunder ett lägre tal, och specifikationsval blir en konkurrensparameter mellan affärsrelationer. Vid sänkan tar propageringen slut och MASSIV+ blir infrastruktur för incitament - ett verifierbart gate-tal som en konsumtionsledsmekanism kan haka i. A/U-separationen avgör hur skarp signalen kan bli, eftersom bara faktiska data (A) för de differentierande komponenterna gör ett specifikationsval belöningsbart.

---

## Referenser

- Europeiska kommissionen, *Carbon Border Adjustment Mechanism (CBAM)*, förordning (EU) 2023/956.
- S. Krook, *The Laghum Economy: A New Brief for a Healthy Planet* (Volante, 2025).
- R. Kaplan & K. Ramanna m.fl., *A Proto-Standard for Carbon Accounting and Auditing using the E-Liability Method* (2025) - för produkt- och transaktionskoordinaten som jämförelse.
