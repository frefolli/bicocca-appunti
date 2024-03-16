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
| ML | 4 | 1 | Machine Learning | 1.0.0 | 30 |
| TCOM | 4 | 1 | Teoria della Computazione | 1.0.0 | 25 |
| MCOR | 4 | 1 | Modelli della Concorrenza | 1.0.0 | 25 |
| TELE | 4 | 2 | Sistemi e Servizi di Telecomunicazione | 1.0.0 | NaN |
| ARCH | 4 | 2 | Architetture Dati | 1.0.0 | NaN |
| SCMT | 4 | 2 | Sistemi Complessi: Modelli e Simulazioni | 1.0.0 | NaN |
|  |  |  |  | 1.0.0 | NaN |

Nota bene: presto spostero' questa tabella in un glossario degli acronimi dei corsi, ma non adesso.

## Dipendenze

### Linux

#### Debian-based (LTA)

 - texlive
 - texlive-latex-extra
 - texlive-science
 - texlive-pictures

#### Arch-based (16/03/24)

 - texlive (ex: texlive-most)

### Patologia

Sei libero di sperimentare sulle varie distribuzioni gia' descritte o assenti quali siano le dipendenze specifiche minime richieste.

Al 10/10/2022 Debian sembra essere ottimale.

## Istruzioni

Per compilare i pdf, lancia `make` (con pdflatex e dipendenze installate), il quale generera' i file pdf `appunti.pdf` per ogni sotto cartella.

Per far gestire l'hosting locale con npm:static-server, usare `make start-host` e `make stop-host`.
