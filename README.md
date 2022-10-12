# Corsi

| Sigla | Anno | Semestre | Corso | Versione | Note |
| --- | --- | --- | --- | --- | --- |
| APAL | 3 | 1 | Analisi e Progettazione di Algoritmi | 1.0.5 |  |
| BIOINF | 3 | 1 | Elementi di Bioinformatica | 1.0.3 |  |
| ROPR | 3 | 1 | Ricerca Operativa e Pianificazione delle Risorse | 1.0.4 |  |
| APS | 3 | 1 | Ingegneria del Software | N/A | Sigla da discutere |
|  |  |  |  |  |

# Dipendenze

## Linux

### Debian-based

 - texlive
 - texlive-latex-extra
 - texlive-science
 - texlive-pictures

### Arch-based

 - texlive-most

## Patologia

Sei libero di sperimentare sulle varie distribuzioni gia' descritte o assenti quali siano le dipendenze specifiche minime richieste.

Al 10/10/2022 Debian sembra essere ottimale.

# Istruzioni

Lancia `make` (con pdflatex e dipendenze installate) per generare i file pdf `appunti.pdf` per ogni sotto cartella.

# Discussioni in corso

## Sigla per Ingegneria del Corso

E' necessario trovare una sigla accettabile per quel corso. Io ricorrerei ad APS fino a che non sara' individuata una migliore.

proposte attuali:

 - IS
 - INOS
 - INGSOF
 - APS (provvisoria)

## Presenza dei PDF nel repository github

E' opportuno non caricare i pdf sul repo e permettere a ciascuno di generarli, pena il fatto di dover usare un PC con texlive per sincronizzare i progressi.