# SO2 Projekt II Etap

Projekt to symulacja wyścigu gdzie każdy bolid to pojedyńczy wątek. Każdy z tych wątków walczy o następujące zasoby:
* tor na którym możejechać
* stacje do tankowania
* dostępny pitstop
* stacje do zmiany opon

Działanie programu polega na dodaniu losowej wartości miezy 1 a 3 do pokonanego dystansu gdy auto porusza się po torze i jednocześnie odjęciu losowych wartości od innych statystyk bolidu. Są to paliwo, ogólny stan auta oraz stan opon. <br>

Zasady przydziału zasobów:
* jeżeli wszystkie wymienione wcześniej statystyki są większe od zera bolid może próbować wjechać na tor o ile będzie dostepny.
* jeżeli pawio spadnie do zera bolid stara się dostać do stacji paliw
* jeżeli stan samochodu spadnie do wartości poniżej 30% już stara się dostać do piststopu 
* jeżeli stan opon spadnie do wartości poniżej 30% bolid już stara się dostać do stacji zmiany opon

Użytkownik sam definiuje ilość samochodów, torów, stacji paliw, pitstopów oraz stacji zmiany opon. Zarządzanie zasobami jednak najlepiej widać gdy liczba torów i aut jest podobna a stacji i pitstopów znacząco mniejsza.
