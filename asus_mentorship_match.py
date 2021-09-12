"""Documentation"""

# Program Name: ASUS Mentorship Program's Automatic Matching

# Author: Ethan Fung and Dennis Hyunh

# Date: September 11th 2021

# Version: 6

# Python version: Python3

"""Purpose"""

# The is program was commissioned by the ASUS Mentorship Program. The goal of this project was to
# mitigate the manual matching of first years to upper years by having a program do it instead. First years
# and upper years sign up through a Gooogle Forms and then automatically being paired through the program.
# This code was based on the Virtual Water Cooler created by Dennis Hyunh.


"""How to Set Up and Use Program"""
# 1. Put csv files in the same folder as python file
# 2. Change names of dfmentee and dfmentor to the correct names of csv files
# 3. check that the names columns of data being retrieved from the csv files are correct/ the same as in the csv files
# 4. run the program and a csv file will be outputted in the same folder

"""Initializations"""
# Import statements
import pandas as pd
import numpy as np

"""Load the Data"""

# Read part of the first years responses
dfmentee = pd.read_csv(
    "Updated AMP First Year Registration 2021-2022 (Responses) - Form Responses 1.csv",
    usecols=[
        "Queen's Email?",
        "First & Last Name",
        "Pronouns",
        "Faculty",
        "What are you interested in? Select all options that apply. [Rank 1]",
        "What are you interested in? Select all options that apply. [Rank 2]",
        "What are you interested in? Select all options that apply. [Rank 3]",
        "What are you interested in? Select all options that apply. [Rank 4]",
        "What are you interested in? Select all options that apply. [Rank 5]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank #1]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank #2]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank #3]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank #4]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank #5]",
    ],
)

# Read part of the mentors responses
dfmentor = pd.read_csv(
    "Updated Mentor Matching 2021-2022 (Responses) - Form Responses 1.csv",
    usecols=[
        "Queen's Email?",
        "First & Last Name",
        "Faculty",
        "Pronouns",
        "What are you interested in? Select all options that apply. [Rank 1]",
        "What are you interested in? Select all options that apply. [Rank 2]",
        "What are you interested in? Select all options that apply. [Rank 3]",
        "What are you interested in? Select all options that apply. [Rank 4]",
        "What are you interested in? Select all options that apply. [Rank 5]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank 1]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank 2]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank 3]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank 4]",
        "Rank the importance of each column of matching criteria: (NOTE: view above for ranking explanation) [Rank 5]",
    ],
)

# Rename columns
dfmentee.columns = [
    "email",
    "full_name",
    "pronouns",
    "faculty",
    "interest1",
    "interest2",
    "interest3",
    "interest4",
    "interest5",
    "imp1",
    "imp2",
    "imp3",
    "imp4",
    "imp5",
]
dfmentor.columns = [
    "email",
    "full_name",
    "pronouns",
    "faculty",
    "interest1",
    "interest2",
    "interest3",
    "interest4",
    "interest5",
    "imp1",
    "imp2",
    "imp3",
    "imp4",
    "imp5",
]

# Create identifaction column
dfmentee["position"] = "mentee"
dfmentor["position"] = "mentor"

# Create new dataframe that holds all the data
df = dfmentor.append(dfmentee, ignore_index=True)

# Create match confirmation columns
df["status"] = 0
df["matched_interest"] = ""
df["matched_imp"] = ""

# Change empty cells to empty strings
df.fillna("", inplace=True)

"""Matching constraints"""

"""
Desc:
    Function that checks for pair matching, 
    matches the top three importances for first year and upper year, 
    then first year leftover preferences are prioritized (4 and 5), 
    upper year leftover preferences are last prioritized (4 and 5)
    Params: a, b (row in pandas DataFrame)
    Output: boolean
"""


def match(a, b):
    # Check if it is a first year and an upper year
    if a["position"] != b["position"]:
        # Go through the top three importances for first year and upper year
        for i in range(1, 4):
            for j in range(1, 4):
                # Check if importances are the same and not empty
                if (
                    a["imp{}".format(i)] == b["imp{}".format(j)]
                    and a["imp{}".format(i)] != ""
                    and b["imp{}".format(j)] != ""
                ):
                    # Check if importance is interests
                    if a["imp{}".format(i)] == "Interests":
                        # Go through the interests for first year and upper year
                        for x in range(1, 4):
                            for y in range(1, 4):
                                # Check if interests are the same and not empty
                                if (
                                    a["interest{}".format(x)]
                                    == b["interest{}".format(y)]
                                    and a["interest{}".format(x)] != ""
                                    and b["interest{}".format(y)] != ""
                                ):
                                    # Update status column as matched
                                    a["status"] = 1
                                    b["status"] = 1
                                    # Update pair importance column
                                    a["matched_imp"] = (
                                        a["imp{}".format(i)]
                                        + ", "
                                        + b["imp{}".format(j)]
                                    )
                                    b["matched_imp"] = (
                                        a["imp{}".format(i)]
                                        + ", "
                                        + b["imp{}".format(j)]
                                    )
                                    # Update pair interests column
                                    a["matched_interest"] = (
                                        a["interest{}".format(x)]
                                        + ", "
                                        + b["interest{}".format(y)]
                                    )
                                    b["matched_interest"] = (
                                        a["interest{}".format(x)]
                                        + ", "
                                        + b["interest{}".format(y)]
                                    )
                                    # Move to next pair
                                    return True
                    # Check if importance is gender
                    elif a["imp{}".format(i)] == "Gender":
                        # Check if pronouns are the same
                        if a["pronouns"] == b["pronouns"]:
                            # Update status column as matched
                            a["status"] = 1
                            b["status"] = 1
                            # Update pair importance column
                            a["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(j)]
                            )
                            b["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(j)]
                            )
                            # Move to next pair
                            return True
                    # Check if importance is faculty
                    elif a["imp{}".format(i)] == "Faculty":
                        # Check if faculties are the same
                        if a["faculty"] == b["faculty"]:
                            # Update status column as matched
                            a["status"] = 1
                            b["status"] = 1
                            # Update pair importance column
                            a["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(j)]
                            )
                            b["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(j)]
                            )
                            return True
                    else:
                        a["status"] = 1
                        b["status"] = 1
                        a["matched_imp"] = (
                            a["imp{}".format(i)] + ", " + b["imp{}".format(j)]
                        )
                        b["matched_imp"] = (
                            a["imp{}".format(i)] + ", " + b["imp{}".format(j)]
                        )
                        # Move to next pair
                        return True
            # Go through the leftover importances for first year (4 and 5), the code repeats
            for k in range(4, 6):
                if (
                    a["imp{}".format(i)] == b["imp{}".format(k)]
                    and a["imp{}".format(i)] != ""
                    and b["imp{}".format(k)] != ""
                ):
                    if a["imp{}".format(i)] == "Interests":
                        for x in range(1, 4):
                            for y in range(1, 4):
                                if (
                                    a["interest{}".format(x)]
                                    == b["interest{}".format(y)]
                                    and a["interest{}".format(x)] != ""
                                    and b["interest{}".format(y)] != ""
                                ):
                                    a["status"] = 1
                                    b["status"] = 1
                                    a["matched_imp"] = (
                                        a["imp{}".format(i)]
                                        + ", "
                                        + b["imp{}".format(k)]
                                    )
                                    b["matched_imp"] = (
                                        a["imp{}".format(i)]
                                        + ", "
                                        + b["imp{}".format(k)]
                                    )
                                    a["matched_interest"] = (
                                        a["interest{}".format(x)]
                                        + ", "
                                        + b["interest{}".format(y)]
                                    )
                                    b["matched_interest"] = (
                                        a["interest{}".format(x)]
                                        + ", "
                                        + b["interest{}".format(y)]
                                    )
                                    return True
                    elif a["imp{}".format(i)] == "Gender":
                        if a["pronouns"] == b["pronouns"]:
                            a["status"] = 1
                            b["status"] = 1
                            a["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(k)]
                            )
                            b["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(k)]
                            )
                            return True
                    elif a["imp{}".format(i)] == "Faculty":
                        if a["faculty"] == b["faculty"]:
                            a["status"] = 1
                            b["status"] = 1
                            a["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(k)]
                            )
                            b["matched_imp"] = (
                                a["imp{}".format(i)] + ", " + b["imp{}".format(k)]
                            )
                            return True
                    else:
                        a["status"] = 1
                        b["status"] = 1
                        a["matched_imp"] = (
                            a["imp{}".format(i)] + ", " + b["imp{}".format(k)]
                        )
                        b["matched_imp"] = (
                            a["imp{}".format(i)] + ", " + b["imp{}".format(k)]
                        )
                        return True
        # Go through the leftover importances for upper year (4 and 5), the code repeats
        for m in range(4, 6):
            for n in range(1, 6):
                if (
                    a["imp{}".format(m)] == b["imp{}".format(n)]
                    and a["imp{}".format(m)] != ""
                    and b["imp{}".format(n)] != ""
                ):
                    if a["imp{}".format(m)] == "Interests":
                        for x in range(1, 4):
                            for y in range(1, 4):
                                if (
                                    a["interest{}".format(x)]
                                    == b["interest{}".format(y)]
                                    and a["interest{}".format(x)] != ""
                                    and b["interest{}".format(y)] != ""
                                ):
                                    a["status"] = 1
                                    b["status"] = 1
                                    a["matched_imp"] = (
                                        a["imp{}".format(m)]
                                        + ", "
                                        + b["imp{}".format(n)]
                                    )
                                    b["matched_imp"] = (
                                        a["imp{}".format(m)]
                                        + ", "
                                        + b["imp{}".format(n)]
                                    )
                                    a["matched_interest"] = (
                                        a["interest{}".format(x)]
                                        + ", "
                                        + b["interest{}".format(y)]
                                    )
                                    b["matched_interest"] = (
                                        a["interest{}".format(x)]
                                        + ", "
                                        + b["interest{}".format(y)]
                                    )
                                    return True
                    elif a["imp{}".format(m)] == "Gender":
                        if a["pronouns"] == b["pronouns"]:
                            a["status"] = 1
                            b["status"] = 1
                            a["matched_imp"] = (
                                a["imp{}".format(m)] + ", " + b["imp{}".format(n)]
                            )
                            b["matched_imp"] = (
                                a["imp{}".format(m)] + ", " + b["imp{}".format(n)]
                            )
                            return True
                    elif a["imp{}".format(m)] == "Faculty":
                        if a["faculty"] == b["faculty"]:
                            a["status"] = 1
                            b["status"] = 1
                            a["matched_imp"] = (
                                a["imp{}".format(m)] + ", " + b["imp{}".format(n)]
                            )
                            b["matched_imp"] = (
                                a["imp{}".format(m)] + ", " + b["imp{}".format(n)]
                            )
                            return True
                    else:
                        a["status"] = 1
                        b["status"] = 1
                        a["matched_imp"] = (
                            a["imp{}".format(m)] + ", " + b["imp{}".format(n)]
                        )
                        b["matched_imp"] = (
                            a["imp{}".format(m)] + ", " + b["imp{}".format(n)]
                        )
                        return True


"""
Desc:
    Function that makes pairs.
    Params: df (pandas Data Frame)
    Output: match_successes (list of pandas Data Frame), unmatched_df (pandas Data Frame)
"""


def matchMaking(df):

    # Transform the dataframe into a list of dictionaries
    records = df.to_dict("records")
    total_records = len(records)

    # Prepare lists to store matches and non-matches
    match_successes = []
    match_failures = []

    # Main loop
    while len(records) > 1:
        for i, n in enumerate(records):
            if i > 0:
                if match(records[0], n) is True:
                    match_successes.append([records.pop(i), records.pop(0)])
                    print(f"Match! records left: {len(records)}/{total_records}")
                    break
            if i + 1 == len(records):
                match_failures.append(records.pop(0))
                print("Cannot match a record...")

    # Add the last record to the match failures
    if len(records) > 0:
        match_failures.append(records.pop(0))

    print(f"Matching complete!")
    print(f"Number of matched records: {2*len(match_successes)}")
    print(f"Number of unmatched records: {len(match_failures)}")

    # Create a dataframe for non-matches
    unmatched_df = pd.DataFrame(match_failures)

    return match_successes, unmatched_df


# Store the list of matches and no matches
matches = matchMaking(df)[0]
noMatches = matchMaking(df)[1]

print(matches)
print(noMatches)

# Convert each pair into data frame
for i in range(len(matches)):
    matches[i] = pd.DataFrame(matches[i])

# Combine matches and noMatches into one data frame
emailDF = pd.concat(
    [pd.concat(matches, ignore_index=True), noMatches], ignore_index=True
)

# Save to csv
emailDF.to_csv("./email_asus_matches.csv", index=False)
