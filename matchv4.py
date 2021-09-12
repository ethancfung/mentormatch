import pandas as pd

dfmentee = pd.read_excel(
    "Updated AMP First Year Registration 2021-2022 (Responses).xlsx",
    header=0,
)
dfmentor = pd.read_excel(
    "Updated Mentor Matching 2021-2022 (Responses).xlsx",
    header=0,
)
# print(dfmentee.loc[:, "First & Last Name"])
# print(dfmentor.loc[:, "First & Last Name"])
for col in range(len(dfmentee.index)):
    for aCol in range(len(dfmentor.index)):
        test = len(dfmentor.index) - 1
        if (
            dfmentee.values[col][17] == dfmentor.values[aCol][17]
        ):  # both mentor and mentee first choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor first choice: " + dfmentee.values[col][17])
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][17] == dfmentor.values[aCol][18]
        ):  # mentee first choice and mentor second choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee first choice and mentor second choice: "
                + dfmentee.values[col][17]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][18] == dfmentor.values[aCol][17]
        ):  # mentee second choice and mentor first choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor first choice: "
                + dfmentee.values[col][17]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][18] == dfmentor.values[aCol][18]
        ):  # both mentor and mentee second choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print("mentee and mentor second choice: " + dfmentee.values[col][17])
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
        elif (
            dfmentee.values[col][18] == dfmentor.values[aCol][19]
        ):  # mentee 2nd choice and mentor 3rd choice
            print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
            print(
                "mentee second choice and mentor third choice: "
                + dfmentee.values[col][18]
            )
            dfmentor = dfmentor.drop(aCol)
            dfmentor = dfmentor.reset_index()
            dfmentor = dfmentor.drop(columns="index")
            break
print(
    dfmentee.loc[
        :, "What are you interested in? Select all options that apply. [Rank 4]"
    ]
)
