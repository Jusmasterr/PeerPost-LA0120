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
| 4    | Funktional     | Die Applikation soll verschiedene Dateitypen (z. B. Bilder, Videos, Dokumente) unterstützen. |
| 5    | Qualitativ     | Die Applikation soll eine benutzerfreundliche Oberfläche zur Auswahl und zum Senden von Dateien bieten. |
| 6    | Funktional     | Die Applikation soll es ermöglichen, Dateien nur an bestimmte Geräte zu senden. |
| 7    | Funktional     | Die Applikation soll eine Möglichkeit bieten, gesendete Dateien zu empfangen und zu speichern. |
| 8    | Qualitativ    | Die Applikation soll eine geringe Latenz und schnelle Übertragungsraten bieten, auch bei größeren Dateien. |
| 9    | Qualitativ     | Die Applikation soll eine hohe Zuverlässigkeit aufweisen und nur bei Netzwerkausfällen oder Verbindungsabbrüchen abbrechen. |
| 10   | Qualitativ     | Die Applikation soll eine benutzerfreundliche und intuitive Oberfläche haben, die eine einfache Bedienung für alle Altersgruppen ermöglicht. |
| 11   | Randbedingung | Die Applikation muss eine funktionierende Internetverbindung erfordern, um Dateien zu übertragen. |
| 12   | Randbedingung | Die Applikation muss sicherstellen, dass alle Dateiübertragungen mit einer Ende-zu-Ende-Verschlüsselung geschützt sind. |
| 13   | Randbedingung | Die Applikation muss eine sichere Verbindung für die Kommunikation zwischen den Geräten gewährleisten. |
| 14   | Randbedingung | Die Applikation muss sicherstellen, dass die Dateiübertragung auch bei großen Dateien ohne Datenverlust oder Fehler erfolgt. |


### User Stories

| US-№ | Verbindlichkeit | Typ        | Beschreibung                                                                                                                                                  |
| ---- | --------------- | ---------- | ----------------------------------------------------------------------------- |
| 1.1    | Muss            | Qualität | Als User möchte ich ein selbsterklärendes und übersichtliches GUI, damit ich mich einfach zurecht finden kann.                                                          |
| 1.2    | Muss            | Qualität | Als User möchte ich ein modernes GUI haben, um meine User-Experience ertragbar zu machen.                                                                    |
| 2.1    | Muss            | Funktional | Als User möchte ich die einzelnen Räume meines Smarthomes erfassen können, um meine Geräte zu erfassen.                                                                        |
| 3.1    | Muss            | Funktional | Als User möchte ich Geräte innerhalb eines Raums mit Namen und Typ erfassen können, um diese anzusteuern.                                            |
| 3.2    | Muss            | Funktional | Als User möchte ich die Möglichkeit haben, Lichter, Heizungen und Storen als Geräte erfassen zu können, um diese anzusteuern.                                         |
| 4.1    | Muss            | Funktional | Als User möchte ich die Daten der Geräte und Räume bearbeiten können, um die Daten aktuell zu halten.                                            |
| 4.2    | Muss            | Funktional | Als User möchte ich Geräte und Räume aus dem System entfernen können, um keine überflüssigen Elemente zu haben. |
| 4.3    | Muss            | Funktional | Als User möchte ich, dass die Daten der Geräte und Räume gespeichert werden, um das System wiederverwendbar zu machen.            |
| 5.1    | Muss            | Funktional | Als User möchte ich Lichter an- und ausschalten können, um das Licht an- und ausschalten zu können.                                             |
| 5.2    | Muss            | Funktional | Als User möchte ich die Temperatur der Heizungen anpassen können, um im Winter nicht zu erfrieren.                                             |
| 5.3    | Kann            | Funktional | Als User möchte ich die Storen hoch- und runterlassen können und Sie anwinkeln, um zu kontrolieren wie viel Lich ins Haus kommt.                                        |

### Testfälle

#### TC-№: 2.1.1
Beschreibung: Räume erfassen
Ausgangslage: Programm gestartet
Eingabe: 1. Button(Raumerfassung) gedrückt | 2. Raum benannt | 3. Button(Erfassen) gedrückt
Ausgaabe: 4. Raum mit gewähltem Namen erstellt

#### TC-№: 2.1.2
Beschreibung: Räume erfassen
Ausgangslage: Programm gestartet
Eingabe: 1. Button(Raumerfassung) gedrückt | 2. Raum benannt | 3. Button(Abbrechen) gedrückt
Ausgaabe: 4. Erfassen des Raums abgebrochen

#### TC-№: 3.1.1
Beschreibung: Geräte erfassen
Ausgangslage: Raum ausgewählt
Eingabe: 1. Button(Geräterfassung) gedrückt | 2. Gerätetyp ausgewählt | 3. Gerät benannt | 4. Button(Erfassen) gedrückt
Ausgaabe: 5. Gerät mit gewähltem Typ und Namen erstellt.

#### TC-№: 3.1.2
Beschreibung: Geräte erfassen
Ausgangslage: Raum ausgewählt
Eingabe: 1. Button(Geräterfassung) gedrückt | 2. Gerätetyp ausgewählt | 3. Gerät benannt | 4. Button(Abbrechen) gedrückt
Ausgaabe: 5. Erfassen des geräts abbgebrochen.

#### TC-№: 4.1.1
Beschreibung: Räume bearbeiten
Ausgangslage: Raum ausgewählt
Eingabe: 1. Button(Bearbeiten) gedrückt | 2. Namen geändert | 3. Button(Speichern) gedrückt
Ausgaabe: 4. Name des gewählten Raums aktialisiert

#### TC-№: 4.1.2
Beschreibung: Geräte bearbeiten
Ausgangslage: Gerät ausgewählt
Eingabe: 1. Button(Bearbeiten) gedrückt | 2. Namen geändert | 3. Typ geaändert | 4. Button(Speichern) gedrückt
Ausgaabe: 5. Name und Typ des gewählten Geräts aktialisiert

#### TC-№: 4.2.1
Beschreibung: Räume entfernen
Ausgangslage: Raum ausgewählt
Eingabe: 1. Button(Entfernen) gedrückt | 2. Entfernen bestätigt
Ausgaabe: 4. Raum entfernt

#### TC-№: 4.2.2
Beschreibung: Geräte entfernen
Ausgangslage: Gerät ausgewählt
Eingabe: 1. Button(Entfernen) gedrückt | 2. Entfernen bestätigt
Ausgaabe: 3. Gerät entfernt

#### TC-№: 4.3.1
Beschreibung: Räume und Geräte speichern
Ausgangslage: Programm neugestartet
Eingabe: 2. Raum ausgewählt
Ausgaabe: 1. zuvor erstellte Räume ersichtlich | 3. zuvor erstellte Geräte ersichtlich

#### TC-№: 5.1.1
Beschreibung: Licht an/aus
Ausgangslage: Gerät vom Typ Licht ausgewählt (Licht aus)
Eingabe: 1. Button(Licht an) gedrückt | 3. Button(Licht aus) gedrückt
Ausgaabe: 2. Licht geht an | 4. Licht geht aus

#### TC-№: 5.2.1
Beschreibung: Heizung bedienen
Ausgangslage: Gerät vom Typ heizung ausgewählt (Temperatur: 18°)
Eingabe: 1. Slider(Temperatur) drei Stellen nach oben | 3. Slider(Temperatur) eine Stelle nach unten
Ausgaabe: 2. (Temperatur: 21°) | 4. (Temperatur: 20°)

#### TC-№: 5.2.1
Beschreibung: Storen bedienen
Ausgangslage: Gerät vom Typ Storen ausgewählt (Position: oben)
Eingabe: 1. Button(Runter) gedrückt | 3. Button(Anwinkeln) gedrückt | 5. Button(Hoch) gedrückt
Ausgaabe: 2. (Position: unten) | 4. (Position: angewinkelt) | 6. (Position: oben)


### Planen

| AP-№ | Datum      | Arbeitspaket                                           | Verantwortliche Person                      |
| ---- | ---------- | ------------------------------------------------------ | ------------------------------------------- |
| 1    | 23.08.2024 | Projekt Idee wählen                                    | Fabian Meyer, Justus Meister                |
| 2    | 23.08.2024 | Anforderungen, Userstories, Testfälle schreiben        | Justus Meister                              |
| 3    | 23.08.2024 | Vertrautmachen mit WPF       | Justus Meister, Fabian Meyer                           |
| 4    | 30.08.2024 | Erstellen des MainGrids für das GUI        | Justus Meister                              |
| 5    | 30.08.2024 | Erstellen und designen der Buttons        | Fabian Meyer                              |
| 6    | 06.09.2024 | Erstellen und designen der Navigationsleisten        | Justus Meister        |
| 7    | 13.09.2024 | Erstellen der Funktion fürs Hinzufügen vo Räumen        | Justus Meister        |
| 8    | 13.09.2024 | Erstellen der Funktion fürs Hinzufügen vo Räumen        | Justus Meister        |
| 9    | 20.09.2024 | Erstellen der Funktion fürs bedienen der Geräte       | Justus Meister        |
| 10    | 20.09.2024 | Feinschliff des Codes und Design       | Justus Meister        |


### Realisieren

| AP-№ | Datum      | Durchgeführt von...  in... min                                           |
| ---- | ---------- | ------------------------------------------------------ |
| 1    | 23.08.2024 | Justus Meister, Fabian Meyer (15min)                   |
| 2    | 23.08.2024 | Justus Meister (90min)                   |
| 3    | 23.08.2024 | Justus Meister, Fabian Meyer (90min)                   |
| 4    | 30.08.2024 | Justus Meister (50min)                   |
| 5    | 30.08.2024 | Fabian Meyer (30min)                   |
| 6    | 06.09.2024 | Justus Meister (60min)                   |
| 7    | 13.09.2024 | Justus Meister (80min)                   |
| 8    | 13.09.2024 | Justus Meister (90min)                  |
| 9    | 20.09.2024 | Justus Meister (80min)                  |



### Testprotokoll

| TC-№   | Datum      | Resultat | Tester        |
| ------ | ---------- | -------- | ------------- |
| 2.1.1  | 01.11.2024 | OK       | Justus Meister |
| 2.1.2  | 01.11.2024 | OK       | Justus Meister |
| 3.1.1  | 01.11.2024 | OK       | Justus Meister |
| 3.1.2  | 01.11.2024 | OK       | Justus Meister |
| 4.1.1  | 01.11.2024 | NOK       | Justus Meister |
| 4.1.2  | 01.11.2024 | NOK       | Justus Meister |
| 4.2.1  | 01.11.2024 | NOK       | Justus Meister |
| 4.2.2  | 01.11.2024 | NOK       | Justus Meister |
| 4.3.1  | 01.11.2024 | NOK       | Justus Meister |



### Testbericht

Die Grundfunktionen funktionieren, jedoch funktionieren ein paar Funktionen nicht.
