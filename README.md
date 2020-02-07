
### Recommendation algorithm.
Based on fetching data from accounting system exported report with rows: DateTime, Art.
The example below is from 1C accounting software - most popular soft for business management in Russia (and most likely in all post-soviet countries).

| Дата                | Номенклатура                                                         |
|---------------------|----------------------------------------------------------------------|
| 31.01.2020 15:10:28 | а 0135 замок для стола L=35мм                                        |
| 31.01.2020 11:53:21 | а Фрог-N45 мех-м с автоматическим подъемом вставки                   |
| 31.01.2020 11:53:21 | а 1280(D+H)FrZшкант металлический d=8мм                              |
| 31.01.2020 11:53:21 | а CY-83N -Замок кнопочный                                            |
| 31.01.2020 11:42:08 | а  K 0401 (Лизард)механизм (R+L) подъема вставки                     |
| 31.01.2020 11:42:08 | а IN 35/750/540  SL м-зм внут. креп.д/стол 750 мм,                   |
| 31.01.2020 11:42:08 | а EX 47/1200/960/9 М SL м-зм ВНЕШ.креп.д/стола 1200                  |
| 31.01.2020 11:42:08 | аЕХ 35/700/485 SL м-зм ВНЕШН. креп.д/стола 700 мм,                   |
| 31.01.2020 11:42:08 | аЕХ 35/750/530 SL м-зм ВНЕШН. креп.д/стола 750 мм,                   |
| 31.01.2020 10:29:31 | а Альф 47/980/1550 SL м-зм д/столов, трос, нагр.90кг                 |
| 31.01.2020 10:29:31 | а SLH-45 Петля подпружиненная с фиксацией для крыльев вставок столов |
| 31.01.2020 10:29:31 | а 0135 замок для стола L=35мм                                        |
| 31.01.2020 10:29:31 | а 0650N замок-крючок для стола L=50мм                                |
| 31.01.2020 10:29:31 | а D EX 47/1100/908 SL м-зм ВНЕШ.крепл.д/стола 1100                   |

The script gets the multiple xlsx files (don't ask why it is so, i wonder myself) and glues them together.
Then it compiles the dictionary with all the unique goods as keys with collections of similar goods as values.
The higher number of item in collection - the higher similarity with key item.
For example you buy eggs and this thing says you to buy flour and milk also.

It's also suitable for calculating recommendation for particular client (buyer), but needs for some small changes.
Will init separate repo later with this stuff.