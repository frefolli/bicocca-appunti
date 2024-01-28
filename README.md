# Bicocca Appunti

Repository con appunti dei corsi universitari che frequento. NON ESAUSTIVI.

I pdf sono caricati sulle Github Pages. Per accedere: https://frefolli.github.io/bicocca-appunti/

__Attenzione__: non tutti i pdf sono caricati, se si vuole visionare gli appunti di materie non piu' attuali si deve scaricare il repository e compilare "manualmente" (eseguire `make -C cartella`) gli appunti a cui si e' interessati.

## Corsi

| Sigla | Anno | Semestre | Corso | Versione | Note | Esito |
| --- | --- | --- | --- | --- | --- | --- |
| APAL | 3 | 1 | Analisi e Progettazione di Algoritmi | 1.0.7 |  | 30 |
| BIOINF | 3 | 1 | Elementi di Bioinformatica | 1.0.7 |  | 30 |
| ROPR | 3 | 1 | Ricerca Operativa e Pianificazione delle Risorse | 1.0.7 |  | 22 |
| APS | 3 | 1 | Ingegneria del Software | 1.0.2 |  | 29 |
| SAF | 3 | 2 | Sicurezza e Affidabilita' | 1.0.0 |  | 30 |
| ML | 4 | 1 | Machine Learning | 1.0.0 | NaN |
| TCOM | 4 | 1 | Teoria della Computazione | 1.0.0 | NaN |
| MCOR | 4 | 1 | Modelli della Concorrenza | 1.0.0 | 25 |
|  |  |  |  |  |

Nota bene: spesso spostero' questa tabella in un glossario degli acronimi dei corsi.

## Dipendenze

### Linux

#### Debian-based

 - texlive
 - texlive-latex-extra
 - texlive-science
 - texlive-pictures

#### Arch-based

 - texlive-most

### Patologia

Sei libero di sperimentare sulle varie distribuzioni gia' descritte o assenti quali siano le dipendenze specifiche minime richieste.

Al 10/10/2022 Debian sembra essere ottimale.

## Istruzioni

Per compilare i pdf, lancia `make` (con pdflatex e dipendenze installate), il quale generera' i file pdf `appunti.pdf` per ogni sotto cartella.

Per far gestire l'hosting locale con npm:static-server, usare `make start-host` e `make stop-host`.
