**Struktura katalogów:**

- Lab_2
    - Analysis Data
        - Earthquake_data_answer.csv
    - Comand Files
        - DataAppendix.ipynb
        - DataProcessing.ibynb
    - Documents
        - DataAppendix.txt
        - README.md
    - Original Data
        - Metadata
            - README.md
        - earthquake_data.csv
    
Oryginalne dane zostały zamieszczone w pliku ***Lab_2\Original Data\earthquake_data.csv***, a opis tych danych znajduje się w pliku ***Lab_2\Original Data\Metadata\README.md***

W celu przetworzenia danych został utworzony *jupyter-notebook* (***Lab_2\Comand Files\DataProcessing.ipynb***), który imoprtuje dane oryginalne, przetwarza je, a następnie rezultat zapisuje w pliku ***Lab_2\Analysis Data\Earthquake_data_answer.csv***

Celem przetwarzania danych było pogrupowanie danych według **wieku** i **płci** badanych oraz obliczenie ilości odpowiedzi **Yes** oraz **No** na pytanie ***Do you think the ""Big One"" will occur in your lifetime?*** dla każdej grupy wiekowej oraz płci.

Za pomocą pliku ***Lab_2\Comand Files\DataApendix.ipynb*** został opracowany dodatek do danych, w którym można znaleźć wykresy utworzone na podstawie przetworzonych danych oraz informację o danych. Na podstawie dodatku został utworzony dokument tekstowy ***Lab_2\Documents\DataAppendix.txt***, w którym zostało umieszczone podsumowanie.