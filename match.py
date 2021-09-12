import pandas as pd

dfmentee = pd.read_excel(
    "AMP First Year Registration 2021-2022 (Responses).xlsx",
    header=0,
)
dfmentor = pd.read_excel(
    "Mentor Matching 2021-2022 (Responses).xlsx",
    header=0,
)
i = 0
# print(dfmentee.values[0][12])
# dfmentee = dfmentee.drop(index=0)
# print(dfmentee.values[0][12])
for col in range(len(dfmentee.index)):
    for aCol in range(len(dfmentor.index)):
        if (
            dfmentee.values[col][12] == dfmentor.values[aCol][12]
        ):  # both mentor and mentee first choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor first choice: " + dfmentee.values[col][12])
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][12] == dfmentor.values[aCol][13]
        ):  # mentee first choice and mentor second choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee first choice and mentor second choice: "
                + dfmentee.values[col][12]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][13] == dfmentor.values[aCol][12]
        ):  # mentee second choice and mentor first choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor first choice: "
                + dfmentee.values[col][12]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][13] == dfmentor.values[aCol][13]
        ):  # both mentor and mentee second choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor second choice: " + dfmentee.values[col][12])
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][13] == dfmentor.values[aCol][14]
        ):  # mentee first choice and mentor second choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor third choice: "
                + dfmentee.values[col][12]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
    i += 1
# for aCol in range(len(dfmentor.index)):
#    print(dfmentor.values[aCol][2])
print(dfmentor.index)
print(i)
