import snakeParser as sp

g = sp.SnakeGame()

g.parse_state("0 S;0 A 11 11;3 M 0;5 M 2;6 M 0;9 M 2;10 M 1;12 M 2;13 M 1;14 M 2;15 M 1;16 A 4 6;16 M 2;17 M 1;21 M "
              "2;23 M 0;25 M 2;26 M 0;27 M 2;28 M 0;32 M 3;34 M 0;35 M 2;39 M 0;40 A 11 10;40 M 3;44 M 1;45 M 2;46 M "
              "1;48 M 3;52 M 1;53 A 13 12;53 M 2;57 M 1;59 M 3;65 A 12 1;65 M 1;68 M 2;70 M 0;84 M 3;85 A 4 8;92 M "
              "1;108 M 2;117 M 0;121 M 2;127 M 0;132 A 14 12;134 M 3;141 M 1;144 M 3;146 M 1;154 M 3;155 M 0;160 A 5 "
              "12;164 M 2;173 M 1;177 A 15 10;180 M 3;192 M 0;197 M 2;199 A 11 4;203 M 0;209 A 9 5;210 M 2;213 M "
              "1;219 M 3;221 M 0;225 M 3;230 M 0;231 M 2;237 M 1;238 A 8 0;243 M 2;244 M 0;254 A 9 14;254 M 3;259 M "
              "1;261 M 2;263 M 1;263 M 2;265 M 1;266 M 2;267 M 1;267 M 2;273 M 1;274 M 2;275 M 1;277 M 3;282 M 1;283 "
              "M 2;284 M 1;285 M 3;288 M 1;290 M 2;291 M 1;293 A 9 0;297 M 2;299 M 0;303 M 2;304 M 0;306 M 3;307 M "
              "0;312 M 2;315 M 0;316 M 3;322 M 0;323 M 2;327 M 0;328 M 3;332 M 0;336 M 2;337 A 5 10;343 M 1;353 M "
              "3;355 A 7 12;362 M 1;363 M 2;369 M 1;377 M 3;378 M 0;385 A 5 3;385 M 3;389 M 0;390 M 2;396 M 0;404 A "
              "15 7;404 M 3;415 M 1;417 M 2;419 M 1;421 M 3;422 A 1 10;426 M 1;427 M 2;429 M 1;433 M 2;437 M 0;439 M "
              "2;451 A 6 12;452 M 1;461 M 3;463 M 0;470 M 3;474 A 14 9;482 M 0;485 A 7 0;493 M 2;498 M 0;499 M 2;501 "
              "A 6 14;503 M 1;517 M 3;518 A 6 1;527 M 0;540 M 2;549 A 11 7;549 M 1;556 M 3;560 M 0;562 M 3;571 M "
              "1;572 M 2;580 A 5 0;580 M 1;585 M 2;588 M 0;599 M 2;605 M 0;606 M 3;609 A 15 0;619 A 14 5;620 M 1;623 "
              "M 2;625 M 1;627 A 5 0;629 M 2;637 M 0;643 M 2;647 M 0;648 M 3;651 A 11 5;659 M 1;662 M 2;665 M 1;668 M "
              "3;675 M 0;675 M 2;682 A 10 12;682 M 0;683 M 3;691 M 1;694 M 2;696 M 1;697 M 2;699 M 1;699 M 2;701 M "
              "1;701 M 2;702 M 1;703 M 2;704 M 1;704 M 2;706 M 1;706 M 2;707 M 1;707 M 2;709 M 1;709 M 2;710 M 1;710 "
              "M 2;712 M 1;712 M 2;715 M 0;733 M 3;736 M 1;746 M 3;753 M 1;754 M 2;760 A 12 2;761 M 1;765 M 3;775 M "
              "0;783 M 2;789 M 0;795 M 2;796 A 1 13;800 M 1;802 M 2;808 M 1;812 M 2;813 M 1;818 A 3 1;819 M 3;828 M "
              "0;830 M 3;832 M 0;836 M 2;839 M 0;842 M 3;845 M 0;847 M 2;856 M 0;858 A 4 11;858 M 3;872 M 1;877 M "
              "2;890 M 1;895 A 0 2;900 M 2;904 M 0;918 A 12 3;918 M 3;930 M 1;931 A 7 10;937 M 2;942 M 1;943 A 0 "
              "11;949 M 2;956 M 0;961 A 13 4;967 M 3;978 M 0;979 M 3;981 A 15 11;984 M 1;991 M 2;991 M 1;992 A 4 "
              "4;998 M 2;1001 M 0;1003 M 2;1005 M 0;1005 M 2;1008 M 0;1009 M 2;1013 M 0;1022 A 4 0;1022 M 3;1031 M "
              "0;1032 M 2;1042 M 0;1044 M 3;1053 M 0;1053 M 2;1062 A 10 2;1065 M 1;1075 M 3;1076 M 0;1083 M 3;")
