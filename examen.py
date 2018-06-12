# Ome Henk is sinds mei op pensioen, maar weet niet echt goed wat gedaan met zijn vrije tijd.
# Op raad van zijn kleinkinderen leert hij programmeren in Python als nieuwe hobby!
# Henk zou graag een tool maken om activiteiten te plannen voor/met zijn kleinkinderen.
# De 9 kleinkinderen van Henk zijn gebundeld in een lijst (family) waar Henk enkele functies voor wil maken.
# Help jij Henk om zijn droom waar te maken?

########################
## DEEL 1 (in de les) ##
########################

# Geeft het aantal gasten voor een familiefeest terug. Wanneer partners_included op True staat zijn
# de liefjes van de groepsgenoten ook uitgenodigd (Relationship). Hou hier rekening mee! (2pt)
def number_of_guests(group, partners_included=False):
    return NotImplementedError

# Geeft het gemiddelde budget van de volledige groep terug (1pt)
def average_budget(group):
    return NotImplementedError

# Geeft een lijst terug van alle personen uit de groep die aan alle voorwaarden voldoen. (2pt)
def activity_participants(group, min_age, max_age, cost):
    return NotImplementedError



########################
## DEEL 2 (na de les) ##
########################

# Print de leden van de volledige groep volgens volgende structuur: "The members of this group are: Alice, Bob,
# Charlie, David, Edward, Fabian, Gerald, Harvey and Ike." (1pt)
def print_group(group):
    return NotImplementedError

# Deze functie zal de grootste uitdaging zijn. Henk heeft op het internet iets gelezen over de 'time-bibliotheek'.
# Henk wil dat de leeftijden van zijn kinderen niet hardcoded in het systeem zitten, maar dat hun geboortedatum
# opgeslagen wordt. De structuur van de elementen uit de dictionary zullen dus verandere naar:
# Alice = {'Name': 'Alice', 'Birthday': <geboortedag>, 'Relationship': True, 'Budget': 100}
# Dit moet het mogelijk maken om met de functie next_birthday(group) het kleinkind te vinden met de eerstvolgende
# verjaardag. Wanneer je de gegevens van de andere kleinkinderen aanpast mag je hun verjaardagen vrij kiezen,
# maar op zo een manier dat hun leeftijd nog steeds klopt. Bijvoorbeeld voor Alice mag je 19 juni 1999 als fictieve
# geboortedatum kiezen, want in dat geval is ze nog steeds 18 jaar (zodat de gegevens acuraat blijven) (4pt)
def next_birthday(group):
    return NotImplementedError

def main():
    Alice = {'Name': 'Alice', 'Age': 18, 'Relationship': True, 'Budget': 100}
    Bob = {'Name': 'Bob', 'Age': 17, 'Relationship': False, 'Budget': 100}
    Charlie = {'Name': 'Charlie', 'Age': 13, 'Relationship': False, 'Budget': 20}
    David = {'Name': 'David', 'Age': 12, 'Relationship': False, 'Budget': 50}
    Edward = {'Name': 'Edward', 'Age': 6, 'Relationship': False, 'Budget': 9999}
    Fabian = {'Name': 'Fabian', 'Age': 25, 'Relationship': True, 'Budget': 9999}
    Gerald = {'Name': 'Gerald', 'Age': 15, 'Relationship': False, 'Budget': 250}
    Harvey = {'Name': 'Harvey', 'Age': 15, 'Relationship': True, 'Budget': 40}
    Ike = {'Name': 'Ike', 'Age': 2, 'Relationship': False, 'Budget': 120}

    family = [Alice, Bob, Charlie, David, Edward, Fabian, Gerald, Harvey, Ike]

    ### YOUR TEST CODE STARTS HERE ###


    ### YOUR TEST CODE ENDS HERE ###
    return

if __name__ == "__main__":
    main()
