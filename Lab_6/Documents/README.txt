Ćwiczenie 6 - Exploratory Data Analysis

Oryginalny plik 1_KUJAWSKO-POMORSKIE.csv jest dostępny w folderze OriginalData. Ze względu na importowalny format pliku nie wykonywałem żadnych działań w tym kierunku. Aby wczytać go w języku Python wykorzystałem bibliotekę pandas, a dokładniej funkcję read_csv. 

Początkowym krokiem, który wykonałem była zmiana w kolumnie "Płeć kupującego". Komórki, w których występował napis "bd.", a więc nie zawierały informacji na temat płci zastąpiłem wartością NaN. To działanie miało na celu łatwiejsze przetwarzanie oraz odczytywanie danych z tej kolumny.

Następnym etapem prac była zmiana pierwszej kolumny. Nic nie mówiącą nazwę "Unnamed: 0" zastąpiłem nagłówkiem "ID", co jasno wskazuje na to, że pierwsza kolumna odpowiada za numer identyfikacyjny danego klienta. 

Przetworzone dane zapisałem do nowego pliku, który, tak jak plik oryginalny, jest w formacie .csv.

W celu uzyskania wykresów oraz szczegółowych danych dotyczących przetworzonego DataFrame'u napisałem skrypt pod nazwą DataAppendix.ipynb. Otrzymane informacje trafiły do pliku o takiej samej nazwie, tylko z innym rozszerzeniem, w folderze Documents.

Struktura katalogów:
laboratorium-6-Juninho25 - folder główny
AnalysisData - folder zawierający przetworzone dane
CommandFiles - folder zawierający skrypty: Preprocessing.ipynb do przetwarzania danych oraz DataAppendix.ipynb do analizy tych danych
Documents - folder zawierający plik README.md oraz DataAppendix.txt, a także obrazy przedstawiające wykresy
OriginalData - folder zawierający oryginalny plik tb.csv oraz folder Metadata, w którym z kolei znajduje się plik z opisem oryginalnego pliku.