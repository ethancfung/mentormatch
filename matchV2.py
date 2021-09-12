import pandas as pd  # I added more choice responses

dfmentee = pd.read_excel(
    "AMP First Year Registration 2021-2022 (Responses).xlsx",
    header=0,
)
dfmentor = pd.read_excel(
    "Mentor Matching 2021-2022 (Responses).xlsx",
    header=0,
)
for col in range(len(dfmentee.index)):
    for aCol in range(len(dfmentor.index)):
        if dfmentee.values[col][12] == dfmentor.values[aCol][12]:
            if (
                dfmentee.values[col][11] == dfmentor.values[aCol][11]
                and dfmentee.values[aCol][12] == "Interests"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][12])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (
                dfmentee.values[col][7] == dfmentor.values[aCol][7]
                and dfmentee.values[aCol][12] == "Major / Minor / Medial"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][12])
                print(dfmentee.values[col][7])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (
                dfmentee.values[aCol][12] == "Gender"
                or dfmentee.values[aCol][12] == "BIPOC Community"
                or dfmentee.values[aCol][12] == "LGBTQ2A+ Community"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][12])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            else:
                pass
        elif dfmentee.values[col][12] == dfmentor.values[aCol][13]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee first choice and mentor second choice: "
                + dfmentee.values[col][12]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif dfmentee.values[col][13] == dfmentor.values[aCol][12]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor first choice: "
                + dfmentee.values[col][12]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif dfmentee.values[col][13] == dfmentor.values[aCol][13]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor second choice: " + dfmentee.values[col][12])
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif dfmentee.values[col][13] == dfmentor.values[aCol][14]:
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor third choice: "
                + dfmentee.values[col][12]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
