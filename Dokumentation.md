# PeerPost-LA0120

# LA-0120

### Beschreibung

Gruppe: Luca Jeaneret, Justus Meister

Wir entwickeln einen Peer to Peer Applikation, in dem kann man anderen Geräten Dateien senden durch die Applikation. 

## 1. Informieren 

### 1.1 Anforderungen
| An-№ | Typ            | Beschreibung                                                                     |
| ---- | -------------- | --------------------------------------------------------------------------------- |
| 1    | Funktional     | Die Applikation soll es Nutzern ermöglichen, Dateien zwischen verschiedenen Geräten zu senden. |
| 2    | Funktional     | Die Applikation soll sicherstellen, dass nur autorisierte Geräte auf die gesendeten Dateien zugreifen können. |
| 3    | Funktional     | Die Applikation soll es Nutzern ermöglichen, mehrere Dateien gleichzeitig zu senden. |
| 4    | Funktional     | Die Applikation soll verschiedene Dateitypen (Bilder, Dokumente) unterstützen. |
| 5    | Qualitativ     | Die Applikation soll eine benutzerfreundliche Oberfläche zur Auswahl und zum Senden von Dateien bieten. |
| 6    | Funktional     | Die Applikation soll es ermöglichen, Dateien nur an bestimmte Geräte zu senden. |
| 7    | Funktional     | Die Applikation soll eine Möglichkeit bieten, gesendete Dateien zu empfangen und zu speichern. |
| 8    | Qualitativ     | Die Applikation soll eine geringe Latenz und schnelle Übertragungsraten bieten, auch bei grösseren Dateien. |
| 9    | Qualitativ     | Die Applikation soll eine hohe Zuverlässigkeit aufweisen und nur bei Netzwerkausfällen oder Verbindungsabbrüchen abbrechen. |
| 10   | Qualitativ     | Die Applikation soll eine benutzerfreundliche und intuitive Oberfläche haben, die eine einfache Bedienung für alle Altersgruppen ermöglicht. |
| 11   | Randbedingung | Die Applikation muss eine funktionierende Internetverbindung erfordern, um Dateien zu übertragen. |
| 12   | Randbedingung | Die Applikation muss eine sichere Verbindung für die Kommunikation zwischen den Geräten gewährleisten. |
| 13   | Randbedingung | Die Applikation muss sicherstellen, dass die Dateiübertragung auch bei grossen Dateien ohne Datenverlust oder Fehler erfolgt. |


### 1.1 User Stories

### User Stories

| US-№  | An-№ | Verbindlichkeit | Beschreibung                                                                 |
| ----- | ---- | ---------------- | ---------------------------------------------------------------------------- |
| 1.1   | 1    | muss             | Als User möchte ich Dateien zwischen verschiedenen Geräten senden können, damit ich Daten problemlos austauschen kann. |
| 2.1   | 2    | muss             | Als User möchte ich sicherstellen, dass nur autorisierte Geräte auf die gesendeten Dateien zugreifen können, damit meine Daten geschützt sind. |
| 3.1   | 3    | muss             | Als User möchte ich mehrere Dateien gleichzeitig senden können, damit ich meine Aufgaben effizienter erledigen kann. |
| 4.1   | 4    | muss             | Als User möchte ich verschiedene Dateitypen (z. B. Bilder, Dokumente) senden können, um flexibel in der Dateiübertragung zu sein. |
| 5.1   | 5    | muss             | Als User möchte ich eine benutzerfreundliche Oberfläche haben, damit ich Dateien einfach auswählen und senden kann. |
| 6.1   | 6    | muss             | Als User möchte ich die Möglichkeit haben, Dateien nur an bestimmte Geräte zu senden, damit ich die Kontrolle über den Empfänger behalte. |
| 7.1   | 7    | muss             | Als User möchte ich gesendete Dateien empfangen und speichern können, um sie später wieder zu verwenden oder zu bearbeiten. |
| 8.1   | 8    | muss             | Als User möchte ich, dass die Applikation eine geringe Latenz und schnelle Übertragungsraten bietet, damit der Dateiübertragungsprozess schnell und effizient ist. |
| 9.1   | 9    | muss             | Als User möchte ich, dass die Applikation zuverlässig funktioniert, auch bei Verbindungsabbrüchen oder Netzwerkproblemen, damit die Dateiübertragung nicht unnötig unterbrochen wird. |
| 10.1  | 10   | muss             | Als User möchte ich eine benutzerfreundliche und intuitive Oberfläche haben, die es mir ermöglicht, die Applikation ohne Vorkenntnisse zu nutzen. |
| 11.1  | 11   | muss             | Als User möchte ich sicherstellen, dass die Applikation eine funktionierende Internetverbindung erfordert, damit die Dateiübertragung ohne Probleme erfolgt. |
| 12.1  | 13   | muss             | Als User möchte ich, dass die Applikation eine sichere Verbindung für die Kommunikation zwischen den Geräten verwendet, damit meine Daten nicht abgehört werden können. |
| 13.1  | 14   | muss             | Als User möchte ich, dass auch grosse Dateien sicher und ohne Fehler übertragen werden, damit ich keine Daten verliere. |


## 2. Planen

### 2.1 Arbeitspakete

| AP-№  | Zuständig  | Frist       | Beschreibung                                                                | Geplante Zeit |
| ----- | ---------- | ----------- | --------------------------------------------------------------------------- | ------------- |
| 1     | Jeanneret  | 8.11.24     | Erstellung des Projektantrag und Festlegung der Meilensteine/Ziele.         | 90 min        |
| 2     | Jeanneret  | 8.11.24     | Anforderungen und User-storeis schreiben.                                   | 60 min        |
| 3     | Jeanneret  | 8.11.24     | Arbeitspakete und Testfälle schreiben.                                      | 60 min        |
| 4     | Meister    | 8.11.24     | Herausfinden wie man Pythonscripts in eine C# Applikation implementieren kann.| 180 min     |
| 5     | alle       | 15.11.24    | Host Script schreiben.                                                      | 180 min       |
| 6     | alle       | 22.11.24    | Client Script schreiben.                                                    | 180 min       |
| 7     | alle       | 29.11/6.12.24| Intergration der Scripts in C#                                             | 360 min       |
| 8     | alle       | 13.12.24    | Frontend machen                                                             | 180 min       |
| 9     | alle       | 20.12.24    | Programm Testen                                                             | 60 min        |
| 10    | Individuel | 20.12.24    | Portfolio schreiben.                                                        | 120 min       |


### 2.2 Testfälle

| TC-№ | Ausgangslage                      | Eingabe                                               | Erwartete Ausgabe                                               |
| ---- | --------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------- |
| 1.1  | PC ist gestartet                  | Applikation öffnen                                    | Applikation öffnet sich.                                         |
| 2.1  | Applikation gestartet             | Host auswählen                                        | Host ausgewählt und läuft.                                       |
| 3.1  | Applikation anders gestartet      | Client auswählen                                      | Client ausgewählt und läuft.                                     |
| 4.1  | Client gestartet und läuft        | Nachricht senden auswählen                            | Nachricht kann gesendet werden.                                  |
| 4.2  | Nachricht senden ausgewählt       | Nachricht schreiben und senden                        | Host erhält die Nachricht.                                       |
| 5.1  | Client gestartet und läuft        | Datei senden auswählen                                | Datei kann gesendet werden.                                      |
| 5.2  | Datei senden ausgewählt           | Datei auswählen und senden                            | Host erhält Datei.                                                |


## 3. Entscheiden

### 3.1 Entscheiden

Wir haben uns entschieden das man nur einfache Dateien und Nachrichten senden kann, weil wir nicht so viel Zeit haben.

## 4. Realisieren

### 4.1 Realisieren

| AP-№ | Datum     | Zuständig        | geplante Zeit | tatsächliche Zeit |
| ---- | --------- | ---------------- | ------------- | ----------------- |
| 1    | 8.11.24   | Jeanneret        | 90 min        |      90 min       |
| 2    | 8.11.24   | Jeanneret        | 60 min        |      60 min       |
| 3    | 8.11.24   | Jeanneret        | 60 min        |      60 min       |
| 4    | 8.11.24   | Meister          | 180 min       |      180 min      |
| 5    | 15.11.24  | alle             | 180 min       |      180 min      |
| 6    | 22.11.24  | alle             | 180 min       |      180 min      |
| 7    | 29.11/ 6/13.12.24  | alle             | 360 min       |      440 min      |
| 8    | 13.12.24   | alle             | 180 min       |        0 min      |
| 9    | 20.12.24  | alle             | 60 min        |       90 min      |
| 10   | 20.12.24  | Individuel       | 120 min       |      120 min      |


## 5 Testen

### 5.1 Testprotokoll

| TC-№   | Datum      | Resultat | Tester        | Bemerkung |
| ------ | ---------- | -------- | ------------- | --------- |
| 1.1    | 20.12.2024 | OK       | Jeanneret     |           |
| 2.1    | 20.12.2024 | NOK      | Jeanneret     | Applikation kann nicht auf dem Python Script zugreifen. Aber man kann das Script selber starten. |
| 3.1    | 20.12.2024 | NOK      | Jeanneret     | Applikation kann nicht auf dem Python Script zugreifen. Aber man kann das Script selber starten. |
| 4.1    | 20.12.2024 | OK       | Jeanneret     |           |
| 4.2    | 20.12.2024 | OK       | Jeanneret     |           |
| 5.1    | 20.12.2024 | OK       | Jeanneret     |           |
| 5.2    | 20.12.2024 | OK       | Jeanneret     |           |




### 5.2 Testbericht

Das Programm läuft nicht wie erwünscht. Irgendetwas ging bei der Integration des C#-Codes schief.
Die Skripte funktionieren wie geplant und wurden erfolgreich getestet.
Der nächste Schritt ist, die Anwendung zu reparieren, damit sie veröffentlicht werden kann.
