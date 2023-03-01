# Bicocca Appunti

Repository con appunti dei corsi universitari che frequento. NON ESAUSTIVI.

I pdf sono caricati sulle Github Pages. Per accedere: https://frefolli.github.io/bicocca-appunti/

## Corsi

| Sigla | Anno | Semestre | Corso | Versione | Note |
| --- | --- | --- | --- | --- | --- |
| APAL | 3 | 1 | Analisi e Progettazione di Algoritmi | 1.0.7 |  |
| BIOINF | 3 | 1 | Elementi di Bioinformatica | 1.0.7 |  |
| ROPR | 3 | 1 | Ricerca Operativa e Pianificazione delle Risorse | 1.0.7 |  |
| APS | 3 | 1 | Ingegneria del Software | 1.0.2 |  |
| SAF | 3 | 2 | Sicurezza e Affidabilita' | 1.0.0 |  |
|  |  |  |  |  |

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
