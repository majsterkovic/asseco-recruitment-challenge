# Przekształcenie listy kroków na strukturę hierarchiczną
## Cel

Celem zadania jest weryfikacja umiejętności rozwiązywania problemów korzystając z języka python.

##  Opis zadania

Dany jest plik messages.proto:

```
syntax = 'proto3';

package messages;

message Request {
    message Step {
        int32 id = 1;
        optional int32 parent_id = 2;
        int32 duration = 3;
        string name = 4;
    }

    repeated Step steps = 1;
    optional int32 step_id = 2;
}

message Response {
    message HierarchicalStep {
        string name = 1;
        int32 duration = 2;
        repeated HierarchicalStep children = 3;
    }

    HierarchicalStep hierarchical_step = 1;
    string max_duration_step_name = 2;
    int32 max_duration_step_duration = 3;
}
```

Należy wczytać komunikat wejściowy opisany definicją Request i przekształcić go na komunikat wyjściowy Response, w taki sposób aby listę kroków "Step" zamienić na krok hierarchiczny "HierarchicalStep".

W polu "step_id" znajduje się identyfikator kroku od którego należy rozpocząć budowanie struktury.
Jeśli wartość nie jest ustawiona, to należy rozpocząć od kroku który nie ma ustawionej wartości w polu "parent_id".
Lista kroków "children" ma być posortowana malejąco względem pola "duration".
W polu "max_duration_step_name" ma się znaleźć nazwa kroku który trwał najdłużej (czas trwania danego kroku to "duration" danego kroku minus suma "duration" jego bezpośrednich potomków), a w "max_duration_step_duration" czas trwania tego kroku.


## Wynik

Wynikiem jest plik .py z kodem spełniającym powyższe wymagania. W kodzie ma się znaleźć funkcja która przyjmuje zserializowaną wiadomość Request i zwraca zserializowaną wiadomość Response. Mogą też być inne funkcje i klasy, z których główna funkcja będzie korzystać.

Przykładowe wejście: b'\n\x08\x08\x01\x18\x96\x01"\x01A\n\t\x08\x02\x10\x01\x18-"\x01B\n\t\x08\x03\x10\x01\x182"\x01C\n\t\x08\x04\x10\x02\x18\x14"\x01D\n\t\x08\x05\x10\x02\x18\x14"\x01E\x10\x01'

Przykładowe wyjście: b'\n"\n\x01A\x10\x96\x01\x1a\x05\n\x01C\x102\x1a\x13\n\x01B\x10-\x1a\x05\n\x01D\x10\x14\x1a\x05\n\x01E\x10\x14\x12\x01A\x187'

## Przydatne linki

- https://developers.google.com/protocol-buffers
- https://pypi.org/project/protobuf/
