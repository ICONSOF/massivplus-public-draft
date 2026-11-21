---
layout: default_banner
title: "MF-008 Nya namn för Coverage och massbalans"
parent: "Förslag"
nav_order: 8
forslag_id: MF-008
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§5, §8"
forslag_forfattare: Birger Löfgren
forslag_diskussion: https://github.com/ICONSOF/massivplus-public-draft/discussions/56
---

# MF-008 Nya namn för Coverage och massbalans

> **Status:** Utkast, 2026-11-21. Ingår inte i standarden. Berör §5 och §8 och alla texter som använder orden. Författare: Birger Löfgren. Diskussion: [#56](https://github.com/ICONSOF/massivplus-public-draft/discussions/56).

Två av standardens viktigaste ord betyder redan något annat i de ramverk MASSIV+ jämförs med. Betydelserna ligger så nära att läsaren lätt missförstår. Förslaget byter Coverage mot *faktisk andel* och massbalans mot *bevarandeprincipen*, båda i samma release.

## Vad orden betyder i dag

**Coverage** är i MASSIV+ andelen av en nods utsläpp som vilar på faktisk data, deklarerad av den ansvariga avsändaren ([§8](../standard/specifikation.md#8-coverage---mått-på-datakvalitet)). På andra håll betyder ordet något annat:

| Ramverk | Vad coverage betyder där |
|---|---|
| ISO 14044, 4.2.3.6.2 | Hur väl data representerar studiens tid, plats och teknik |
| Catena-X PCF Rulebook v3, 4.2.1 | Att bortkapade processer tillsammans är högst 3 % av avtrycket, "97% coverage" |
| PACT 2.3 | Andelen av avtrycket som ingår i bedömningen av datakvalitet (borttaget i 3.0) |
| SBTi och CDP | Hur stor del av utsläppen ett mål omfattar |

En LCA-praktiker som läser "Coverage 0,8" tror att data är 80 % representativa, eller att 80 % av avtrycket är med efter bortkapning. MASSIV+ menar att 80 % av utsläppen kommer från avsändare som själva har deklarerat dem.

GHG Protocols Scope 3-standard och ESRS använder inte ordet, men har det mått som ligger närmast: andelen utsläpp som räknats med data från leverantörer och andra parter i värdekedjan. Ingen av dem ger måttet ett kort namn.

**Massbalans** betyder i MASSIV+ att en nod för vidare alla sina utsläpp, varken mer eller mindre ([§5](../standard/specifikation.md#5-massbalansprincipen---systemets-invarians)). På andra håll:

| Ramverk | Vad massbalans betyder där |
|---|---|
| ISO 14064-1, bilaga C, och utsläppshandeln | Ett sätt att räkna utsläpp från kolet som går in i och ut ur en process |
| ISO 14044 | En kontroll av att en process in- och utflöden går ihop |
| ISO 22095 | En spårbarhetsmodell där certifierat och ocertifierat material blandas och den certifierade andelen fördelas på papper |

MASSIV+ ligger närmare bokföringen än någon av dessa. Det som går ihop är ansvaret för utsläppen, inte material ([massbalansen i MASSIV+](../fordjupningar/massbalansen-i-massiv.md), [ISO 22095](../positionering/jamforelse/iso-22095.md)).

## Förslag till standardtext

1. **Coverage blir faktisk andel.** Ordet Coverage ersätts med *faktisk andel* och uppströms-Coverage med *uppströms faktisk andel*, i specifikationen och i alla texter som använder orden. Formlerna i §8 ändras inte.
2. **Massbalans blir bevarandeprincipen.** Massbalans och massbalansprincipen ersätts med *bevarandeprincipen*. Formeln i §5 ändras inte.
3. **Rubrikerna.** §5 får rubriken "Bevarandeprincipen - systemets invarians" och §8 rubriken "Faktisk andel - mått på datakvalitet".
4. **En not i §8.** "Måttet hette tidigare Coverage. Ordet har andra betydelser i ISO 14044, Catena-X, PACT, SBTi och CDP."
5. **En not i §5.** "Principen hette tidigare massbalans, och teknisk litteratur kallar den ofta så. Ordet har andra betydelser i ISO 14064-1, ISO 14044 och ISO 22095. När de betydelserna nämns anges alltid källan."
6. **Engelska.** *Actual share*, *upstream actual share* och *conservation principle*.

## Varför de här namnen

*Faktisk andel* följer bokstaven A, för Actual, och standardens andra princip, faktisk data eller okänt. Samma ord går då från principen till måttet, och namnet säger vad måttet visar.

*Bevarandeprincipen* säger vad regeln gör: utsläpp skapas inte och försvinner inte när de förs vidare. Det ligger nära bokföringsekvationen, och det är också vad ICC-panelens princip *Conservation across entities* heter ([bokföringsanalogin](../fordjupningar/bokforingsanalogin.md#4-den-framväxande-tanken-om-bokföring-av-utsläpp)).

Båda byts samtidigt, så att orden bara ändras en gång.

## Konsekvenser

- Specifikationen, introduktionen, fördjupningarna, positioneringen, förslagen och de engelska versionerna ändras i samma release. Coverage förekommer i dag 18 gånger i specifikationen och massbalans 10 gånger.
- Rubrikerna i §5 och §8 får nya ankare, så länkar till dem uppdateras i samma release.
- Fördjupningen *Massbalansen i MASSIV+* får en ny titel, och etiketterna `§5 mass balance` och `§8 coverage` i Discussions byter namn.
- Verktyg som visar måttet behöver byta etikett.
- Förslagen MF-001, MF-002, MF-004, MF-005, MF-006 och MF-007 anger det nya namnet inom parentes vid första förekomsten. Antas MF-008 byts orden ut helt.

## Alternativ som övervägts

- *Deklarerad andel.* Fångar att A gäller ansvarig avsändare och inte hur exakt talet är (§2), men förväxlas lätt med deklarerad enhet i ISO 14067 och EPD.
- *Balansprincipen.* Pekar mot bokföringen, men ordet är vagt för sig.
- *Coverage med ett tillägg*, till exempel coverage av faktisk data. Minsta ändringen, men krocken med ISO 14044 står kvar.
- Att behålla orden och förklara dem. Avvisat, eftersom de andra betydelserna finns i just de ramverk som MASSIV+-läsare kommer från.

## Öppna frågor

- Ordalydelsen i ISO 14044, 4.2.3.6.2, är hittills läst via sekundärkällor och ska kontrolleras mot originalet.
- Ska Coverage stå kvar som sökord eller alias i engelska texter under en övergångstid?

## Beslut

Inte behandlat. Förslaget avser nya namn i §5 och §8 och i alla texter som använder orden.
