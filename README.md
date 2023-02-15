# DigSecTest 

## Instructions
1) Read the CSV file financials
2) Import Python Regex
3) 3.1. Run the function 'credit_card_occurrences'
   3.2. Save 'credit_card_occurrences' output in CC_List 
4) 4.1. Run the function 'MBIs_occurrences'
   4.2. Save 'MBIs_occurrences' output in MBIs_List
5) 5.1. create output file
   5.2. write the output
   
## Answers to questions
1) I found 2 problems:
- There where many values under the 'cc_num' column with invalid format, I assumed that all of these valuse are not represnt credit cards, and I've tried to search just valid credit cards according to the formats I found in the internet.
- Not all of the MBIs under 'medicare_id' column are valid, so again I tried to find in the internet the MBI format and searched it.
2) In order to indetify this data, I would check phrases that starts with numbers or contian number in thier first section before a comma. another way to indentify it is to connect to external DB who has the streets information.
