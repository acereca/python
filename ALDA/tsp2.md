# Programmierübung TSP2

## Laufzeitberechnung
Die Laufzeit für meine Implementierung der Nächster-Nachbar-Heuristik lässt sich mit

> N*log(N)^2

abschätzen, dabei beruht diese Abschätzung auf folgenden Schleifendurchläufen:

1. Es müssen für N Nodes Die jeweils nächsten Nachbarn gesucht werden (N)
2. Für jede Node n müssen (N-n) Distanzen berechnet werden (log(N))
3. Und diese N-n Distanzen mit (N-n-1) anderen Distanzen verglichen werden,
    um den nächsten Nachbarn zu finden (log(N))
