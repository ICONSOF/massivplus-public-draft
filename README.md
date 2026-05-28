# MASSIV+

> Öppen standard för beräkning och propagering av utsläppsdata i värdekedjor - på organisationsnivå.

---

## Vad är MASSIV+?

MASSIV+ modellerar värdekedjan som ett riktat nätverk av noder. Varje nod rapporterar sina egna Scope 1+2 med standardiserade emissionsfaktorer och allokerar dem proportionellt vidare till sina kunder. Mottagaren bygger sin Scope 3 nedifrån från faktisk data, inte uppifrån med branschschabloner.

Standarden vilar på tre principer:

- **Ditt Scope 1+2 är mitt Scope 3.** Bilateral bokföring av utsläppsflöden mellan motparter. Scope 3 byggs nedifrån från verklig data.
- **Faktisk data eller okänt.** Ingen uppskattning får samma status som faktisk data. Faktisk data (A) och okänt (U) hålls strukturellt åtskilda; U kvantifieras bara som täckningsunderlag för Coverage.
- **Standardiserade emissionsfaktorer.** Alla noder använder samma fastställda set. Eftersom ditt Scope 1+2 är någons Scope 3 måste underlaget vara jämförbart.

## Vad finns publicerat här?

Detta är ett publikt utkast. Materialet växer stegvis. Just nu:

- **[Bokföringsanalogin](fordjupningar/bokforingsanalogin.md)** - varför MASSIV+:s bilaterala konstruktion är strukturellt identisk med dubbel bokföring, och vad det säger om vad standarden kan bli på sikt.

Fler texter (introduktion, full specifikation, fler fördjupningar, positioneringstexter) läggs ut allt eftersom.

## Hur du kan bidra

Se [CONTRIBUTING.md](CONTRIBUTING.md) för hur frågor, kommentarer och förslag tas emot. Tröskeln är låg: du behöver bara ett Github-konto.

## Status och kontakt

MASSIV+ är ett pågående utvecklingsarbete. Texterna här är arbetsdokument under granskning och vidareutveckling. Frågor och kommentarer går till `info@massivplus.org` eller via [Discussions](../../discussions).

Källkod för referensimplementationen (en interaktiv simulator) ligger i ett separat repo: [ICONSOF/MASSIV_node_approach](https://github.com/ICONSOF/MASSIV_node_approach).
