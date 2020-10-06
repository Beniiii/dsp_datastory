# Andere Sterne, Andere Jahre



## Ziel

Die beiden am Projekt beteiligten Studierenden verfolgen mit ihrer jeweiligen Datastory individuelle Ziele, bedienen sich hierfür aber an demselben Rohdatensatz. Deswegen wurde die Sammlung der Daten gemeinsam vorgenommen.

### Ziel Benjamin Huber

Diese Datastory soll zur generellen Analyse von Sternendaten dienen, um bestimmte Abhängigkeiten von Attributen herauszufinden. Sternen werden in einem bestimmten Spektralen Typen klassifiziert. In dieser Datastory soll herausgefunden werden, was typische Eigenschaften von spezifischen Typen sind und wie diese stochastisch Verteilt sind und ob es gegebenenfalls gewisse Exoten gibt.

### Ziel Philip Colombo

Mit der Datenstory soll der Frage nachgegangen werden, wie lange ein typisches Jahr im Universum dauert. Auf der Erde ist ein Jahr bestimmt durch den Umlauf des Planeten um die Sonne, welcher rund 365 Tage dauert. Wenn der Umlauf um den Heimatstern als Definition für ein Jahr dient, haben aber bereits die anderen Planeten in unserem Sonnensystem ein dementsprechend längeres oder kürzeres Jahr. Die Untersuchung der Daten von zur Zeit rund 4000 Exoplaneten soll aufzeigen, ob das Erdenjahr der Norm im Universum entspricht oder eher als Ausnahme gewertet werden muss. Ferner soll untersucht werden, welche Eigenschaften von Planeten und deren Heimatsternen, in welcher Konstellation, die typische Länge eines Jahres im Universum bestimmen und wie lang diese eigentlich ist..



## Datengrundlage

Die Daten für die Datastory stammen vom NASA Exoplanet Archive, welches laufend die aktuellen Daten zu bekannten und vermuteten Exoplaneten sowie Daten von verschiedenen Missionen zur Untersuchung von Exoplaneten zur Einsicht und zum Download öffentlich zur Verfügung stellt. Neben einem Web-Interface bietet das Exoplanet Archive auch einen API-Zugriff auf die Daten des Archivs, welcher für diese Datastory verwendet wurde. Mit der API können verschiedene Datensammlungen bezogen werden. Für diese Datastory wird die sogenannte "Composite Planet Data" Datensammlung verwendet, welche Daten von verschiedenen Datensammlungen zusammenträgt um einen möglichst vollständigen, statistisch auswertbaren Datensatz aller bestätigter Exoplaneten bereitzustellen.

Mit der API des Exoplanet Archive wäre es möglich, die Daten bereits vor dem Download einzugrenzen. Für diese Datastory wird jedoch zuerst der gesamte Datensatz bezogen und anschliessend mit Python auf die tatsächlich verwendeten Daten reduziert. Da zum Zeitpunkt der Erstellung dieser Datastory erst rund 4000 Exoplaneten bestätigt sind, wird der Überschuss an heruntergeladenen Daten als vernachlässigbar betrachtet. Da die Zahl an bestätigten Exoplaneten jedoch stetig steigt und mit den Daten neuer Missionen stark ansteigen dürfte, sollte zukünftig die Reduktion der Daten bereits beim Download in Betracht gezogen werden.

Um die aktuellen Daten aus dem Exoplanet Archive zu beziehen, kann das Skript "DataStory.py" ausgeführt werden. Für die korrekte Ausführung des Skripts ist Python 3.7 notwendig, sowie die Libraries "urllib" und "pandas". Wenn das Skript korrekt ausgeführt werden kann, werden die Daten im CSV-Format im Verzeichnis data in der Datei "Data.csv" gespeichert. Damit das Skript korrekt funktioniert, muss das Verzeichnis data existieren und schreibbar sein sowie eine Internetverbindung aufgebaut werden können.

Für diese Datastory wurde der Rohdatensatz zuletzt am 17. Oktober 2019 von der URL <https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=compositepars> bezogen.

Quellen:
- NASA Exoplanet Archive: <https://exoplanetarchive.ipac.caltech.edu/index.html>)
- Aktueller Rohdatensatz: <https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=compositepars>
- Dokumentation des Rohdatensatzes: <https://exoplanetarchive.ipac.caltech.edu/docs/API_compositepars_columns.html>
- Dokumentation der API des Exoplanet Archive: <https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html>



### Beschreibung der Attribute

Im folgenden sind die Attribute im Datensatz beschrieben. Die Einheiten der Attribute sind in der Beschreibung vermerkt und zu jedem Attribut wird der Datentyp und der Wertebereich aufgelistet.



#### planet_name

Name des Planeten.

- Typ: String
- Wertebereich: String



#### controversial_flag

Anzweiflung des Status als Planet.

- Typ: Int
- Wertebereich: 0 oder 1 (0 = nicht angezweifelt, 1 = angezweifelt



#### planet_letter

Dem Planeten zugeordneter Buchstabe im Planetensystem.

- Typ: Char
- Wertebereich: 'b', 'c', ... 'i']



#### planet_mass

Masse des Planeten in Erdmassen.

- Typ: Float
- Wertebereich: 0.02 ... 239000.0



#### planet_radius

Radius des Planeten in Erdradien.

- Typ: Float
- Wertebereich: 0.336 ... 77.342



#### orbital_period

Umlaufzeit des Planeten um den Heimatstern in Tagen.

- Typ: Float
- Wertebereich: 0.09070629 ... 7300000.0



#### orbital_radius

Längster Radius der Umlaufbahn des Planeten um den Heimatstern in astronomischen Einheiten (AE).

- Typ: Float
- Wertebereich: 0.0044 ... 2500.0



#### eccentricity

Exzentrizität bzw. Abweichung der Umlaufbahn des Planeten um seinen Heimatstern von einem perfekten Kreis.

- Typ: Float
- Wertebereich: 0.0 ... 0.95



#### host_name

Name des Heimatsterns.

- Typ: String
- Wertebereich: String



#### binary_flag

Hinweis: Dieses Attribut wird in der Dokumentation des Exoplanet Archive erwähnt, scheint aber nicht Teil der heruntergeladenen Daten zu sein.

Umlauf des Planeten um ein binäres Sternensystem.

- Typ: Int
- Wertebereich: 0 oder 1 (0 = kein binäres System, 1 = binäres System



#### stellar_mass

Masse des Heimatsterns in Sonnenmassen.

- Typ: Float
- Wertebereich: 0.01 ... 23.56



#### stellar_radius

Radius des Heimatsterns in Sonnenradien.

- Typ: Float
- Wertebereich: 0.01 ... 71.23



#### stellar_temperature

Temperatur des Heimatsterns in Kelvin.

- Typ: Float
- Wertebereich: 575.0 ... 57000.0



#### stellar_age

Alter des Heimatsterns in Jahrmilliarden (Mrd. J.).

- Typ: Float
- Wertebereich: 0.001 ... 14.9



#### optical_magnitude

Brightness of the host star as measured using the V (Johnson) or the Kepler-band in units of magnitudes.

- Type: Float
- Range: 0.85 ... 20.5



#### near_ir_magnitude

Brightness of the host star as measured using the Ks (2MASS) or the J (2MASS) in units of magnitudes.

- Type: Float
- Range: -3.00 ... 17.00



#### spectral_type

Classification of the star based on their spectral characteristics following the Morgan-Keenan system.

- Type: String
- Range: see https://space.fandom.com/wiki/Stellar_classification



#### stellar_surface_gravity

Gravitational acceleration experienced at the stellar surface, measured in cm/s**2.

- Type: Float
- Range: 1.2 ... 5.6
- Unit: log10(cm/s**2)



#### stellar_luminosity

Amount of energy emitted by a star per unit time, measured in units of solar luminosities.

- Type: Float
- Range: -6.00 ... 3.6
- Unit: log10(Solar luminosity)



#### stellar_metallicity

Measurement of the metal content of the photosphere of the star as compared to the hydrogen content.

- Type: Float
- Range: -0.90 ... 0.8
- Unit: dex, see https://joe-antognini.github.io/astronomy/what-is-a-dex



