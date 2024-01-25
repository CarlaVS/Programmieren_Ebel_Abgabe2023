# Programmieren_Ebel_Abgabe2023
## Problem
Grafiken werden mit Passepartout gerahmt. Für eine ansprechende Präsentation werden sie dazu in Gruppen (Konvolut) eingeteilt, die in Rahmen derselben Größe präsentiert werden. Die Grafiken werden also in Gruppen eingeteilt, in denen die Abweichung der Dimensionen in Höhe und Breite nicht mehr als einen definierten Abstand haben darf (2 cm in diesem Beispiel). Anschließend werden für jede Grafik in jeder Gruppe individuell die Werte für die Innenmaße des Passepartout berechnet. Die Außenmaße des Passepartout werden für jede Gruppe abhängig von der maximalen Höhe und Breite berechnet.  

  Für das Passepartout wird ein Innenmaß (Maß der Graphik + 2 cm in diesem Fall) und ein Außenmaß berechnet (maximale Dimensionen der Gruppe + 6 bzw 7 cm, abhängig von der Größe der Graphiken).

## Lösung
Zunächst wird der Grenzwert von Graphiken festgelegt um die großen von kleinen Graphiken zu unterscheiden (in diesem Fall 40 cm). Dann wird der maximale Abweichungswert in cm definiert (in diesem Fall 2 cm). Die Tabelle der Grafiken wird eingelesen und für jede Grafik wird ein Python Objekt der Klasse G_object generiert. Den Grafiken wird für das Attribut small ein boolescher Wert zugewiesen, je nachdem ob sie ein Maß von über 40 cm haben.  

  Die Liste der Objekte wird randomisiert neu geordnet. Um alle theoretisch möglichen Permutationen der Liste zu ermitteln wäre zum Beispiel die Funktion permutations aus der Library itertools anzuwenden. Der vorliegende Code beschränkt sich auf 5000 randomisierte Listen. Im Testdurchlauf wurden so sehr gute Ergebnisse erzeilt.
Anschließend werden aus den randomisiert geordneten Listen Gruppen gebildet, die den Grenzabweichungswert von 2 cm einhalten. Wird eine solche Gruppe ermittelt, wird sie in ein Python Set umgewandelt, diese Sets werden in einer Liste gesammelt.  
  In der Funktion clear_result werden danach die Sets entfernt, die Teilmenge einer größeren Liste sind. Danach werden die Gruppen für eine bessere Präsentation des Endergebnisses ihrer Größe nach geordnet.  
  
  Die Passepartouts werden nun für diese vorliegenden Gruppen berechnet. Dabei werden aus jedem Grafikobjekt G_object mehrere Objekte der Klasse G_individual gebildet, da die Außenmaße des jeweiligen Passepartout von der Gruppe abhängig sind.Grafiken mit dem Attribut small = True wird ein Passepartoutmaß von 6 cm zugeordnet, ansonsten sind es 7 cm.
Zur Präsentation der Ergebnisse wird eine Tkinter Benutzeroberfläche erstellt. Für einen guten Überblick über mögliche Gruppen wurde den repräsentierten Python Objekten bei ihrer Erstellung jeweils eine Farbe zugewiesen. Eine Grafik, die in zwei Gruppen vorkommt, hat also in beiden Gruppen die selbe Farbe.
Die Benutzeroberfläche listet jeweils in einer Zeile die zugehörigen Grafiken mit den Maßen des Passepartout innen (*PP Höhe innen* und *PP Breite innen*), die Außenmaße des Passepartout (*PP Höhe außen* und *PP Breite außen*) und die Rahmenmaße (*Rahmenhöhe und -breite innen und außen*) auf.
