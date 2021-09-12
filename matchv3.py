import pandas as pd# I tried to use functions

dfmentee = pd.read_excel(
    "AMP First Year Registration 2021-2022 (Responses).xlsx",
    header=0,
)
dfmentor = pd.read_excel(
    "Mentor Matching 2021-2022 (Responses).xlsx",
    header=0,
)
i = 0
for col in range(len(dfmentee.index)):
    for aCol in range(len(dfmentor.index)):
        if dfmentee.values[col][12] == dfmentor.values[aCol][12]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor first choice: " + dfmentee.values[col][12])
        elif dfmentee.values[col][12] == dfmentor.values[aCol][13]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee first choice and mentor second choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][12] == dfmentor.values[aCol][14]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee first choice and mentor third choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][13] == dfmentor.values[aCol][12]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor first choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][13] == dfmentor.values[aCol][13]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor second choice: " + dfmentee.values[col][12])
        elif dfmentee.values[col][13] == dfmentor.values[aCol][14]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor third choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][14] == dfmentor.values[aCol][12]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee third choice and mentor first choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][14] == dfmentor.values[aCol][13]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee third choice and mentor second choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][14] == dfmentor.values[aCol][14]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor third choice:" + dfmentee.values[col][12])
        elif dfmentee.values[col][12] == dfmentor.values[aCol][15]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee first choice and mentor fourth choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][12] == dfmentor.values[aCol][16]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee first choice and mentor fifth choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][13] == dfmentor.values[aCol][15]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor fourth choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][13] == dfmentor.values[aCol][16]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor fifth choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][14] == dfmentor.values[aCol][15]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee third choice and mentor fourth choice: "
                + dfmentee.values[col][12]
            )
        elif dfmentee.values[col][14] == dfmentor.values[aCol][16]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee thid choice and mentor fifth choice: "
                + dfmentee.values[col][12]
            )
        dfmentor = dfmentor.drop(aCol)
        dfmentor = dfmentor.reset_index()
        dfmentor = dfmentor.drop(columns="index")
        break
    i += 1
print(dfmentor.index)
print(i)
