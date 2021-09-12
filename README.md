# ASUS Mentorship Program's Automatic Matching

The is program was commissioned by the ASUS Mentorship Program. The goal of this project is to mitigate the manual matching of first years to upper years by having a program do it instead. First years and upper years sign up through a Google Forms and then automatically being paired through the program. 

This code was based on the Virtual Water Cooler created by Dennis Huynh. The code can be found here: [https://github.com/DennisH3/Virtual-Water-Cooler](https://github.com/DennisH3/Virtual-Water-Cooler)

## How to Use the Program
1. Download the responses from the Google Forms as CSV files
2. Download the asus_mentorship_match.py program from this GitHub
3. Move the asus_mentorship_match.py and the CSV responses files into the same folder
4. Open the asus_mentorship_match.py file in a Python IDE of your choice
5. Ensure that all file names, column names, and values match within the program with the CSV files
6. Run the program
7. Open "email_asus_matches.csv" to confirm the results

## Data
The data used for the matching Python program can be found in Test Data. There are two files, one for mentee sign ups and one for mentor sign ups. Both are synthetically generated.

## Output
The output of the matches can be found in email_asus_matches.csv