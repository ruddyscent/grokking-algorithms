# Dynamic programming

### 11.1
With iPhone (\$2,000), Guitar (\$1,500), and MP3 (\$1,000), you can maximize the value of the loot to \$4,500.

### 11.2
Water (3lb, 10), food (2lb, 9), camera (1lb, 6) is the optimal combination with value of 25.
|      |1    |2    |3       |4       |5         |6         |
|------|-----|-----|--------|--------|----------|----------|
|water |0    |0    |10 (w)  |10 (w)  |10 (w)    |10 (w)    |
|book  |3 (b)|3 (b)|10 (w)  |13 (w b)|13 (w b)  |13 (w b)  |
|food  |3 (b)|9 (f)|10 (w)  |13 (w b)|19 (w f)  |22 (w b f)|
|camera|6 (c)|9 (f)|15 (f c)|16 (w c)|20 (f j c)|25 (w f c)|

### 11.3
The length of the  longest  common  substring between "blue" and "clues" is 3.
| |b|l|u|e| |
|-|-|-|-|-|-|
|c|0|0|0|0|0|
|l|0|1|0|0|0|
|u|0|0|2|0|0|
|e|0|0|0|3|0|
|s|0|0|0|0|0|