import pandas as pd
import numpy as np

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
        if (
            dfmentee.values[col][17] == dfmentor.values[aCol][17]
        ):  # both mentor and mentee first choice first intrest
            if (
                dfmentee.values[col][11] == dfmentor.values[aCol][11]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][11] != np.nan
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][17])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][12]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][12] != np.nan
            ):
                # mentee 1st intrest mentor 2nd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][17])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][13]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][13] != np.nan
            ):
                # mentee 1st intrest mentor 3rd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][17])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][14]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][14] != np.nan
            ):
                # mentee 1st intrest mentor 4th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][17])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][15]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][15] != np.nan
            ):
                # mentee 1st intrest mentor 5th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][17])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (  # faculty
                dfmentee.values[col][6] == dfmentor.values[aCol][6]
                and dfmentee.values[aCol][17] == "Faculty"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][17])
                print(dfmentee.values[col][6])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (  # rest of the options
                dfmentee.values[aCol][17] == "Gender"
                or dfmentee.values[aCol][17] == "BIPOC Community"
                or dfmentee.values[aCol][17] == "LGBTQ2A+ Community"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor first choice: " + dfmentee.values[col][17])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break

        elif (
            dfmentee.values[col][17] == dfmentor.values[aCol][18]
        ):  # mentee first choice and mentor second choice
            if (
                dfmentee.values[col][11] == dfmentor.values[aCol][11]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][11] != np.nan
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee first choice and mentor second choice: "
                    + dfmentee.values[col][17]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][12]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][12] != np.nan
            ):
                # mentee 1st intrest mentor 2nd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee first choice and mentor second choice: "
                    + dfmentee.values[col][17]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][13]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][13] != np.nan
            ):
                # mentee 1st intrest mentor 3rd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee first choice and mentor second choice: "
                    + dfmentee.values[col][17]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][14]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][14] != np.nan
            ):
                # mentee 1st intrest mentor 4th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee first choice and mentor second choice: "
                    + dfmentee.values[col][17]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][15]
                and dfmentee.values[aCol][17] == "Interests"
                and dfmentee.values[col][15] != np.nan
            ):
                # mentee 1st intrest mentor 5th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee first choice and mentor second choice: "
                    + dfmentee.values[col][17]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (  # faculty
                dfmentee.values[col][6] == dfmentor.values[aCol][6]
                and dfmentee.values[aCol][17] == "Faculty"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee first choice and mentor second choice: "
                    + dfmentee.values[col][17]
                )
                print(dfmentee.values[col][6])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (  # rest of the options
                dfmentee.values[aCol][17] == "Gender"
                or dfmentee.values[aCol][17] == "BIPOC Community"
                or dfmentee.values[aCol][17] == "LGBTQ2A+ Community"
            ):
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
            if (
                dfmentee.values[col][11] == dfmentor.values[aCol][11]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][11] != np.nan
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor first choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][12]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][12] != np.nan
            ):
                # mentee 1st intrest mentor 2nd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor first choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][13]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][13] != np.nan
            ):
                # mentee 1st intrest mentor 3rd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor first choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][1])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][14]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][14] != np.nan
            ):
                # mentee 1st intrest mentor 4th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor first choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][15]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][15] != np.nan
            ):
                # mentee 1st intrest mentor 5th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor first choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (  # faculty
                dfmentee.values[col][6] == dfmentor.values[aCol][6]
                and dfmentee.values[aCol][18] == "Faculty"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor first choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][6])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (  # rest of the options
                dfmentee.values[aCol][18] == "Gender"
                or dfmentee.values[aCol][18] == "BIPOC Community"
                or dfmentee.values[aCol][18] == "LGBTQ2A+ Community"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor first choice: "
                    + dfmentee.values[col][18]
                )
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break

        elif (
            dfmentee.values[col][18] == dfmentor.values[aCol][18]
        ):  # both mentor and mentee second choice
            if (
                dfmentee.values[col][11] == dfmentor.values[aCol][11]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][11] != np.nan
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor second choice: " + dfmentee.values[col][18])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][12]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][12] != np.nan
            ):
                # mentee 1st intrest mentor 2nd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor second choice: " + dfmentee.values[col][18])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][13]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][13] != np.nan
            ):
                # mentee 1st intrest mentor 3rd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor second choice: " + dfmentee.values[col][18])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][14]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][14] != np.nan
            ):
                # mentee 1st intrest mentor 4th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor second choice: " + dfmentee.values[col][18])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][15]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][15] != np.nan
            ):
                # mentee 1st intrest mentor 5th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor second choice: " + dfmentee.values[col][18])
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (  # faculty
                dfmentee.values[col][6] == dfmentor.values[aCol][6]
                and dfmentee.values[aCol][18] == "Faculty"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor second choice: " + dfmentee.values[col][18])
                print(dfmentee.values[col][6])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (  # rest of the options
                dfmentee.values[aCol][18] == "Gender"
                or dfmentee.values[aCol][18] == "BIPOC Community"
                or dfmentee.values[aCol][18] == "LGBTQ2A+ Community"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print("mentee and mentor second choice: " + dfmentee.values[col][18])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break

        elif (
            dfmentee.values[col][18] == dfmentor.values[aCol][19]
        ):  # mentee 2nd choice and mentor 3rd choice
            if (
                dfmentee.values[col][11] == dfmentor.values[aCol][11]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][11] != np.nan
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor third choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][12]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][12] != np.nan
            ):
                # mentee 1st intrest mentor 2nd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor third choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][13]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][13] != np.nan
            ):
                # mentee 1st intrest mentor 3rd intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor third choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][14]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][14] != np.nan
            ):
                # mentee 1st intrest mentor 4th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor third choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (
                dfmentee.values[col][11] == dfmentor.values[aCol][15]
                and dfmentee.values[aCol][18] == "Interests"
                and dfmentee.values[col][15] != np.nan
            ):
                # mentee 1st intrest mentor 5th intrest
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor third choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][11])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
            elif (  # faculty
                dfmentee.values[col][6] == dfmentor.values[aCol][6]
                and dfmentee.values[aCol][18] == "Faculty"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor third choice: "
                    + dfmentee.values[col][18]
                )
                print(dfmentee.values[col][6])
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
            elif (  # rest of the options
                dfmentee.values[aCol][18] == "Gender"
                or dfmentee.values[aCol][18] == "BIPOC Community"
                or dfmentee.values[aCol][18] == "LGBTQ2A+ Community"
            ):
                print(dfmentee.values[col][2] + " and " + dfmentor.values[aCol][2])
                print(
                    "mentee second choice and mentor third choice: "
                    + dfmentee.values[col][18]
                )
                dfmentor = dfmentor.drop(aCol)
                dfmentor = dfmentor.reset_index()
                dfmentor = dfmentor.drop(columns="index")
                break
