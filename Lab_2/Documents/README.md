Ćwiczenie 1 - TIER protocol i tidy data

Oryginalny plik tb.csv jest dostępny w folderze OriginalData. Ze względu na importowalny format pliku nie wykonywałem żadnych działań w tym kierunku. Aby wczytać go w języku Python wykorzystałem bibliotekę pandas, a dokładniej funkcję read_csv.

Początkowym krokiem, który wykonałem była zmiana nazwy pierwszej kolumny. Nic nie mowiącą nazwę "iso2" zastąpiłem nagłówkiem "country", co jasno wskazuje na to, że pierwsza kolumna odpowiada za nazwy państw. Następnie usunąłem niepotrzebne dane, jak na przykład wiersze w całości wypełnione niezdefiniowanymi danymi. Postanowiłem także usunąć całą kolumnę "new_sp", gdyż w końcowym rozrachunku nie wprowadzała ona niczego nowego do analizy danych.

Następnym etapem prac był tak zwany "melting", czyli doprowadzenie danych do czytelniejszej postaci poprzez zmianę organizacji DataFrame'u. W wyniku tego działania powstały nowe kolumny.

Końcowy etap, nazwany "tidying", co można przetłumaczyć na sprzątanie, polegał na ostatecznym uporządkowaniu danych, aby jak najbardziej poprawić ich czytelność i przejrzystość. Głównymi działaniami w tym etapie przetwarzania danych była ekstrakcja danych z jednej kolumny na dwie oddzielne z informacją o płci oraz przedziale wiekowym. Do tego był mi potrzebny utworzony słownik, natomiast kolumna "column" po uzyskaniu z niej danych stała się bezużyteczna, więc została usunięta.

Przetworzone dane zapisałem do nowego pliku, który, tak jak plik oryginalny, jest w formacie .csv.

W celu uzyskania wykresów oraz szczegółowych danych dotyczących przetworzonego DataFrame'u napisałem skrypt pod nazwą DataAppendix.ipynb. Otrzymane informacje trafiły do pliku o takiej samej nazwie, tylko z innym rozszerzeniem, w folderze Documents.

Struktura katalogów:
Lab_2 - folder główny
AnalysisData - folder zawierający przetworzone dane
CommandFiles - folder zawierający skrypty: lab2.ipynb do przetwarzania danych oraz DataAppendix.ipynb do analizy tych danych
Documents - folder zawierający plik README.md oraz DataAppendix.txt, a także obrazy przedstawiające wykresy
OriginalData - folder zawierający oryginalny plik tb.csv oraz folder Metadata, w którym z kolei znajduje się plik z opisem oryginalnego pliku.