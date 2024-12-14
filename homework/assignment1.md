# Podsumowanie

Nasze zastosowanie jest przykładem klasyfikacji z dwoma klasami.

Najwyższą dokładnością wykazał się model oparty o **maszynę wektorów nośnych**.
Ma to dużo sensu gdy weźmiemy pod uwagę jego działanie i nasze dane.
Działa on przez dzielenie przestrzeni wielowymiarowej na dwie części (podział na większą ilość części wymaga kolejnych iteracji).
Jest to dokładnie to czego potrzebujemy do naszego zadania.

Model **kNN** również miał dobre wyniki. Jest on jednak nieprzystosowany do użyć wielowymiarowych.
Warto wspomnieć o tym, że parametr `k=4` dla modelu **kNN** jest nieoptymalny.
Dobór odpowiedniego `k` jest bardzo ważny do odpowiedniego działania modelu.

Odnośnie modelu drzewa decyzyjnego z moich obserwacji wynika iż dochodzi do przetrenowania.
Wiele z liści drzewa ma tylko jeden pasujący element. Jest to jedna z głównych wad tego modelu.
Bardzo łatwo dochodzi do przetrenowania.
