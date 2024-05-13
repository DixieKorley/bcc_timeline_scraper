```
NewSequence = 
VAR Sequences =
    SELECTCOLUMNS(
        GENERATESERIES(
            MIN('Timeline'[ConvertedYear]), 
            MAX('Timeline'[ConvertedYear]), 
            1
        ),
        "Sequence", [Value]
    )
RETURN
UNION(
    ADDCOLUMNS(
        FILTER('Timeline', 'Timeline'[ConvertedYear] <> EARLIER('Timeline'[ConvertedYear])),
        "ConvertedYear", 'Timeline'[ConvertedYear]
    ),
    SELECTCOLUMNS(
        EXCEPT(Sequences, 'Timeline'),
        "ConvertedYear", [Sequence]
    )
)
```



```
NewSequence = 
VAR Sequences =
    SELECTCOLUMNS(
        GENERATESERIES(
            MIN('Timeline'[ConvertedYear]), 
            MAX('Timeline'[ConvertedYear]), 
            1
        ),
        "Sequence", [Value]
    )

VAR OriginalNumbers =
    SELECTCOLUMNS('Timeline', 
"ConvertedYear,
'Timeline'[ConvertedYear])

RETURN
UNION(
    ADDCOLUMNS(
        FILTER(OriginalNumbers, 'Timeline'[ConvertedYear] <> EARLIER('Timeline'[ConvertedYear])),
        "ConvertedYear", 'Timeline'[ConvertedYear]
    ),
    SELECTCOLUMNS(
        EXCEPT(Sequences, OriginalNumbers),
        "ConvertedYear", [Sequence]
    )
)
```