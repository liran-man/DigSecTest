# read csv file with a name financials
with open("financials.csv", "r") as file:
    text = file.read()

############################################################################################
##################################### Credit Cards #########################################
############################################################################################
import re

# function that returns list of credit cards founds in the input string
def credit_card_occurrences(string):
    Visa_regex = re.compile(r"^(?:4[0-9]{12}(?:[0-9]{3})?)")
    Master_Card_regex = re.compile(r"( ^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)")
    American_Express_regex = re.compile(r"3[47][0-9]{13}")
    Diners_regex = re.compile(r"3(?:0[0-5]|[68][0-9])[0-9]{11}")
    Discover_regex = re.compile(r"6(?:011|5[0-9]{2})[0-9]{12} ")
    JCB_regex = re.compile(r"(?:2131|1800|35\d{3})\d{11}$")
    regexes = [Visa_regex,Master_Card_regex, American_Express_regex, Diners_regex, Discover_regex, JCB_regex]
    credit_cards = []
    for r in regexes:
        for i in r.r.findall(string):
            credit_cards.append(i)
    return credit_cards

CC_List = credit_card_occurrences(text)
print(CC_List)

########################################################################################################
##################################### Medicare Beneficiary Identifier ##################################
########################################################################################################

# function that returns list of MBIs founds in the input string
def MBIs_occurrences(string):
    # the regex expression tries to keep the MBI format: [Number[1-9], Character[A-Z], Character or Number[0-9], Number[0-9], Character, Character or Number[0-9], Number[0-9], Character, Character, Number[0-9], Number[0-9]]
    MBI_regex = re.compile(r'\b[1-9](?![sloibzSLOIBZ])[a-zA-Z](?![sloibzSLOIBZ)])[a-zA-Z0-9][0-9]-?(?![sloibzSLOIBZ])[a-zA-Z](?![sloibzSLOIBZ])[a-zA-Z0-9][0-9]-?(?![sloibzSLOIBZ])[a-zA-Z]{2}\d{2}\b')
    MBIs = MBI_regex.findall(string)
    return MBIs


MBIs_List = MBIs_occurrences(text)
print(MBIs_List)

#########################################################################################################
# Create new file
file = open("output.txt", "x")
file = open("output.txt", "a")
file.write("The number of credit card occurrences in the file is:" + str(len(CC_List)))
file.write("The number of MBIs occurrences in the file is:" + str(len(MBIs_List)))

file.close()