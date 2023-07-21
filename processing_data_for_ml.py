import pandas as pd
import json
import xlsxwriter
import os
import csv
from difflib import SequenceMatcher
import datetime


#
df_ubuntu_parsed_results= pd.read_csv('ubuntu_parsed_results.csv')
df_redhat_parsed_results= pd.read_csv('redhat_parsed_results.csv')
df_nvd_parsed_results = pd.read_csv('nvd_parsed_results.csv')
df_final_list_of_severities = pd.read_csv('final_cve_list_with_severities.csv')
list_of_cves_1 = []
list_of_severity_rating_1 = []
list_of_cves_2 = []
list_of_severity_rating_2 = []
list_of_cves_3 = []
list_of_severity_rating_3 = []
list_of_cves_4 = []
list_of_severity_rating_4 = []
list_of_cves_5 = []
list_of_severity_rating_5 = []


listOfCveIdentifier = []
listOfPublishedDate = []
listOfLastModified = []
listOfAttackVector = []
listOfAttackComplexity = []
listOfPrivilegesRequired = []
listOfUserInteraction = []
listOfScope = []
listOfConfidentialityImpact = []
listOfIntegrityImpact = []
listOfAvailabilityImpact = []
listOfExploitabilityScore = []
listOfImpactScore = []
listOfToolSeverity = []
listOfVerifiedCve = []
listOfVerifiedSeverity = []
listOfBaseScore = []
listOfBaseSeverity = []

#listOfScope = []

listOfFinalCveIdentifier = []
listOfFinalSeverityRating = []
count=0
df = df_final_list_of_severities

for ind in df.index:
     count = count + 1

     if str(df['cve_identifier'][ind]) != 'nan':
         cveIdentifier = str(df['cve_identifier'][ind])
     else:
         cveIdentifier = None
     listOfFinalCveIdentifier.append(cveIdentifier)

     if str(df['severity_rating'][ind]) != 'nan':
         severityRating = str(df['severity_rating'][ind]).upper()
         if severityRating == 'NONE':
             listOfFinalSeverityRating.append(0)
         elif severityRating == 'LOW':
             listOfFinalSeverityRating.append(1)
         elif severityRating == 'MEDIUM':
             listOfFinalSeverityRating.append(2)
         elif severityRating == 'HIGH':
             listOfFinalSeverityRating.append(3)
         elif severityRating == 'CRITICAL':
             listOfFinalSeverityRating.append(4)
     else:
         severityRating = None
     listOfFinalSeverityRating.append(severityRating)

count=0
df = df_nvd_parsed_results
for ind in df.index:
     count = count + 1

     if str(df['cveIdentifier'][ind]) != 'nan':
         cveIdentifier = str(df['cveIdentifier'][ind])
     else:
         cveIdentifier = None
     listOfCveIdentifier.append(cveIdentifier)

     if str(df['publishedDate'][ind]) != 'nan':
         publishedDate = str(df['publishedDate'][ind])
     else:
         publishedDate = 0
     listOfPublishedDate.append(publishedDate)

     
     if str(df['lastModified'][ind]) != 'nan':
         lastModified = str(df['lastModified'][ind])
     else:
         lastModified = 0
     listOfLastModified.append(lastModified)
    
     if str(df['attackVector'][ind]) != 'nan':
         attackVector = str(df['attackVector'][ind])
         if attackVector =='NETWORK':
             listOfAttackVector.append(4)
         elif attackVector =='ADJACENT' or attackVector =='ADJACENT_NETWORK':
             listOfAttackVector.append(3)
         elif attackVector =='LOCAL':
             listOfAttackVector.append(2)
         elif attackVector =='PHYSICAL':
             listOfAttackVector.append(1)
         else:

             listOfAttackVector.append(0)
     else:
         attackVector = None
         listOfAttackVector.append(0)

     if str(df['attackComplexity'][ind]) != 'nan':
         attackComplexity = str(df['attackComplexity'][ind])

         if attackComplexity == 'LOW':
             listOfAttackComplexity.append(3)
         elif attackComplexity == 'MEDIUM':
             listOfAttackComplexity.append(2)
         elif attackComplexity == 'HIGH':
             listOfAttackComplexity.append(1)
         else:
             #print(attackComplexity)
             #exit()
             listOfAttackComplexity.append(0)
     else:
         attackComplexity = None
         listOfAttackComplexity.append(0)

     if str(df['privilegesRequired'][ind]) != 'nan':
         privilegesRequired = str(df['privilegesRequired'][ind])

         if privilegesRequired == 'NONE':
             listOfPrivilegesRequired.append(3)
         elif privilegesRequired == 'LOW':
             listOfPrivilegesRequired.append(2)
         elif privilegesRequired == 'HIGH':
             listOfPrivilegesRequired.append(1)
     else:
         privilegesRequired = None
         listOfPrivilegesRequired.append(0)

     
     if str(df['userInteraction'][ind]) != 'nan':
         userInteraction = str(df['userInteraction'][ind])

         if userInteraction == 'NONE':
             listOfUserInteraction.append(2)
         elif userInteraction == 'REQUIRED':
             listOfUserInteraction.append(1)
     else:
         cveIdeuserInteractionntifier = None
         listOfUserInteraction.append(0)

     if str(df['scope'][ind]) != 'nan':
         scope = str(df['scope'][ind])

         if scope == 'CHANGED':
             listOfScope.append(2)
         elif scope == 'UNCHANGED':
             listOfScope.append(1)
     else:
         scope = None
         listOfScope.append(0)

     
     if str(df['confidentialityImpact'][ind]) != 'nan':
         confidentialityImpact = str(df['confidentialityImpact'][ind])

         if confidentialityImpact == 'HIGH' or confidentialityImpact == 'COMPLETE':
             listOfConfidentialityImpact.append(3)
         elif confidentialityImpact == 'LOW' or confidentialityImpact == 'PARTIAL':
             listOfConfidentialityImpact.append(2)
         elif confidentialityImpact == 'NONE':
             listOfConfidentialityImpact.append(1)

     else:
         confidentialityImpact = None
         listOfConfidentialityImpact.append(0)
    
     if str(df['integrityImpact'][ind]) != 'nan':
         integrityImpact = str(df['integrityImpact'][ind])

         if integrityImpact == 'HIGH' or integrityImpact == 'COMPLETE' :
             listOfIntegrityImpact.append(3)
         elif integrityImpact == 'LOW' or integrityImpact == 'PARTIAL' :
             listOfIntegrityImpact.append(2)
         elif integrityImpact == 'NONE':
             listOfIntegrityImpact.append(1)

     else:
         integrityImpact = None
         listOfIntegrityImpact.append(0)

     if str(df['availabilityImpact'][ind]) != 'nan':
         availabilityImpact = str(df['availabilityImpact'][ind])

         if availabilityImpact == 'HIGH' or availabilityImpact == 'COMPLETE':
             listOfAvailabilityImpact.append(3)
         elif availabilityImpact == 'LOW' or availabilityImpact == 'PARTIAL':
             listOfAvailabilityImpact.append(2)
         elif availabilityImpact == 'NONE':
             listOfAvailabilityImpact.append(1)

     else:
         availabilityImpact = None
         listOfAvailabilityImpact.append(0)



     #CHECK FROM HERE

     


     if str(df['exploitabilityScore'][ind]) != 'nan':
         exploitabilityScore = float(str(df['exploitabilityScore'][ind]))
         if exploitabilityScore == 0.0:
             listOfExploitabilityScore.append(0)
         elif exploitabilityScore >=0.1 and exploitabilityScore <= 3.9:
             listOfExploitabilityScore.append(1)
         elif exploitabilityScore >=4.0 and exploitabilityScore <= 6.9:
             listOfExploitabilityScore.append(2)
         elif exploitabilityScore >=7.0 and exploitabilityScore <= 8.9:
             listOfExploitabilityScore.append(3)
         elif exploitabilityScore >=9.0 and exploitabilityScore <= 10.0:
             listOfExploitabilityScore.append(5)
     else:
         exploitabilityScore = None
         listOfExploitabilityScore.append(0)

     if str(df['impactScore'][ind]) != 'nan':
         impactScore = float(str(df['impactScore'][ind]))
         if impactScore == 0.0:
             listOfImpactScore.append(0)
         elif impactScore >=0.1 and impactScore <= 3.9:
             listOfImpactScore.append(impactScore)
         elif impactScore >=4.0 and impactScore <= 6.9:
             listOfImpactScore.append(impactScore)
         elif impactScore >=7.0 and impactScore <= 8.9:
             listOfImpactScore.append(impactScore)
         elif impactScore >=9.0 and impactScore <= 10.0:
             listOfImpactScore.append(impactScore)
     else:
         impactScore = None
         listOfImpactScore.append(0)


     try:

        if str(df['redhatSeverity'][ind]) != 'nan':
            redhatSeverity = str(df['redhatSeverity'][ind])

        else:
            redhatSeverity=0

     except KeyError:
        listOfToolSeverity.append(0)

     if str(df['baseScore'][ind]) != 'nan':
         baseScore = float(str(df['baseScore'][ind]))
         if baseScore == 0.0:
             listOfBaseScore.append(0)
         elif baseScore >=0.1 and baseScore <= 3.9:
             listOfBaseScore.append(baseScore)
         elif baseScore >=4.0 and baseScore <= 6.9:
             listOfBaseScore.append(baseScore)
         elif baseScore >=7.0 and baseScore <= 8.9:
             listOfBaseScore.append(baseScore)
         elif baseScore >=9.0 and baseScore <= 10.0:
             listOfBaseScore.append(baseScore)
     else:
         baseScore = None
         listOfBaseScore.append(0)

     if str(df['baseSeverity'][ind]) != 'nan':
         baseSeverity = str(df['baseSeverity'][ind])
         if baseSeverity == 'NONE':
             listOfBaseSeverity.append(0)
         elif baseSeverity == 'LOW':
             listOfBaseSeverity.append(1)
         elif baseSeverity == 'MEDIUM':
             listOfBaseSeverity.append(2)
         elif baseSeverity == 'HIGH':
             listOfBaseSeverity.append(3)
         elif baseSeverity == 'CRITICAL':
             listOfBaseSeverity.append(4)
     else:
         baseSeverity = None
         listOfBaseSeverity.append(0)



     #list_of_cves_1.append(cve_identifier)
     #list_of_severity_rating_1.append(severity_rating)

count = 0
df = df_ubuntu_parsed_results
for ind in df.index:
    count = count + 1

    if str(df['cveIdentifier'][ind]) != 'nan':
        cveIdentifier = str(df['cveIdentifier'][ind])
    else:
        cveIdentifier = None
    listOfCveIdentifier.append(cveIdentifier)

    if str(df['publishedDate'][ind]) != 'nan':
        publishedDate = str(df['publishedDate'][ind])
    else:
        publishedDate = 0
    listOfPublishedDate.append(publishedDate)


    try:
        if str(df['lastModified'][ind]) != 'nan':
            lastModified = str(df['lastModified'][ind])
        else:
            lastModified = 0
        listOfLastModified.append(lastModified)

    except KeyError:
        listOfLastModified.append(0)

    if str(df['attackVector'][ind]) != 'nan':
        attackVector = str(df['attackVector'][ind])
        if attackVector == 'NETWORK':
            listOfAttackVector.append(4)
        elif attackVector == 'ADJACENT':
            listOfAttackVector.append(3)
        elif attackVector == 'LOCAL':
            listOfAttackVector.append(2)
        elif attackVector == 'PHYSICAL':
            listOfAttackVector.append(1)
        else:

            listOfAttackVector.append(0)
    else:
        attackVector = None
        listOfAttackVector.append(0)

    if str(df['attackComplexity'][ind]) != 'nan':
        attackComplexity = str(df['attackComplexity'][ind])

        if attackComplexity == 'LOW':
            listOfAttackComplexity.append(3)
        elif attackComplexity == 'MEDIUM':
            listOfAttackComplexity.append(2)
        elif attackComplexity == 'HIGH':
            listOfAttackComplexity.append(1)
        else:

            listOfAttackComplexity.append(0)
    else:
        attackComplexity = None
        listOfAttackComplexity.append(0)

    if str(df['privilegesRequired'][ind]) != 'nan':
        privilegesRequired = str(df['privilegesRequired'][ind])

        if privilegesRequired == 'NONE':
            listOfPrivilegesRequired.append(3)
        elif privilegesRequired == 'LOW':
            listOfPrivilegesRequired.append(2)
        elif privilegesRequired == 'HIGH':
            listOfPrivilegesRequired.append(1)
    else:
        privilegesRequired = None
        listOfPrivilegesRequired.append(0)

    if str(df['userInteraction'][ind]) != 'nan':
        userInteraction = str(df['userInteraction'][ind])

        if userInteraction == 'NONE':
            listOfUserInteraction.append(2)
        elif userInteraction == 'REQUIRED':
            listOfUserInteraction.append(1)
    else:
        cveIdeuserInteractionntifier = None
        listOfUserInteraction.append(0)

    if str(df['scope'][ind]) != 'nan':
        scope = str(df['scope'][ind])

        if scope == 'CHANGED':
            listOfScope.append(2)
        elif scope == 'UNCHANGED':
            listOfScope.append(1)
    else:
        scope = None
        listOfScope.append(0)

    if str(df['confidentialityImpact'][ind]) != 'nan':
        confidentialityImpact = str(df['confidentialityImpact'][ind])

        if confidentialityImpact == 'HIGH' or confidentialityImpact == 'COMPLETE':
            listOfConfidentialityImpact.append(3)
        elif confidentialityImpact == 'LOW' or confidentialityImpact == 'PARTIAL':
            listOfConfidentialityImpact.append(2)
        elif confidentialityImpact == 'NONE':
            listOfConfidentialityImpact.append(1)

    else:
        confidentialityImpact = None
        listOfConfidentialityImpact.append(0)

    if str(df['integrityImpact'][ind]) != 'nan':
        integrityImpact = str(df['integrityImpact'][ind])

        if integrityImpact == 'HIGH' or integrityImpact == 'COMPLETE':
            listOfIntegrityImpact.append(3)
        elif integrityImpact == 'LOW' or integrityImpact == 'PARTIAL':
            listOfIntegrityImpact.append(2)
        elif integrityImpact == 'NONE':
            listOfIntegrityImpact.append(1)

    else:
        integrityImpact = None
        listOfIntegrityImpact.append(0)

    if str(df['availabilityImpact'][ind]) != 'nan':
        availabilityImpact = str(df['availabilityImpact'][ind])

        if availabilityImpact == 'HIGH' or availabilityImpact == 'COMPLETE':
            listOfAvailabilityImpact.append(3)
        elif availabilityImpact == 'LOW' or availabilityImpact == 'PARTIAL':
            listOfAvailabilityImpact.append(2)
        elif availabilityImpact == 'NONE':
            listOfAvailabilityImpact.append(1)

    else:
        availabilityImpact = None
        listOfAvailabilityImpact.append(0)

    # CHECK FROM HERE

    if str(df['exploitabilityScore'][ind]) != 'nan':
        exploitabilityScore = float(str(df['exploitabilityScore'][ind]))
        if exploitabilityScore == 0.0:
            listOfExploitabilityScore.append(0)
        elif exploitabilityScore >= 0.1 and exploitabilityScore <= 3.9:
            listOfExploitabilityScore.append(1)
        elif exploitabilityScore >= 4.0 and exploitabilityScore <= 6.9:
            listOfExploitabilityScore.append(2)
        elif exploitabilityScore >= 7.0 and exploitabilityScore <= 8.9:
            listOfExploitabilityScore.append(3)
        elif exploitabilityScore >= 9.0 and exploitabilityScore <= 10.0:
            listOfExploitabilityScore.append(4)
    else:
        exploitabilityScore = None
        listOfExploitabilityScore.append(0)

    if str(df['impactScore'][ind]) != 'nan':
        impactScore = float(str(df['impactScore'][ind]))
        if impactScore == 0.0:
            listOfImpactScore.append(0)
        elif impactScore >= 0.1 and impactScore <= 3.9:
            listOfImpactScore.append(impactScore)
        elif impactScore >= 4.0 and impactScore <= 6.9:
            listOfImpactScore.append(impactScore)
        elif impactScore >= 7.0 and impactScore <= 8.9:
            listOfImpactScore.append(impactScore)
        elif impactScore >= 9.0 and impactScore <= 10.0:
            listOfImpactScore.append(impactScore)
    else:
        impactScore = None
        listOfImpactScore.append(0)

    try:

        if str(df['redhatSeverity'][ind]) != 'nan':
            redhatSeverity = str(df['redhatSeverity'][ind])

        else:
            redhatSeverity = 0

    except KeyError:
        listOfToolSeverity.append(0)

    if str(df['baseScore'][ind]) != 'nan':
        baseScore = float(str(df['baseScore'][ind]))
        if baseScore == 0.0:
            listOfBaseScore.append(0)
        elif baseScore >= 0.1 and baseScore <= 3.9:
            listOfBaseScore.append(baseScore)
        elif baseScore >= 4.0 and baseScore <= 6.9:
            listOfBaseScore.append(baseScore)
        elif baseScore >= 7.0 and baseScore <= 8.9:
            listOfBaseScore.append(baseScore)
        elif baseScore >= 9.0 and baseScore <= 10.0:
            listOfBaseScore.append(baseScore)
    else:
        baseScore = None
        listOfBaseScore.append(0)

    if str(df['baseSeverity'][ind]) != 'nan':
        baseSeverity = str(df['baseSeverity'][ind])
        if baseSeverity == 'NONE':
            listOfBaseSeverity.append(0)
        elif baseSeverity == 'LOW':
            listOfBaseSeverity.append(1)
        elif baseSeverity == 'MEDIUM':
            listOfBaseSeverity.append(2)
        elif baseSeverity == 'HIGH':
            listOfBaseSeverity.append(3)
        elif baseSeverity == 'CRITICAL':
            listOfBaseSeverity.append(4)
    else:
        baseSeverity = None
        listOfBaseSeverity.append(0)

    # list_of_cves_1.append(cve_identifier)
    # list_of_severity_rating_1.append(severity_rating)

count = 0
df = df_redhat_parsed_results
for ind in df.index:
    count = count + 1

    if str(df['cveIdentifier'][ind]) != 'nan':
        cveIdentifier = str(df['cveIdentifier'][ind])
    else:
        cveIdentifier = None
    listOfCveIdentifier.append(cveIdentifier)

    if str(df['publishedDate'][ind]) != 'nan':
        publishedDate = str(df['publishedDate'][ind])
    else:
        publishedDate = 0
    listOfPublishedDate.append(publishedDate)

    try:
        if str(df['lastModified'][ind]) != 'nan':
            lastModified = str(df['lastModified'][ind])
        else:
            lastModified = 0
        listOfLastModified.append(lastModified)

    except KeyError:
        listOfLastModified.append(0)

    if str(df['attackVector'][ind]) != 'nan':
        attackVector = str(df['attackVector'][ind]).upper()
        #print(attackVector)
        #exit()
        if attackVector == 'NETWORK':
            listOfAttackVector.append(4)
        elif attackVector == 'ADJACENT' or attackVector == 'ADJACENT_NETWORK':
            listOfAttackVector.append(3)
        elif attackVector == 'LOCAL':
            listOfAttackVector.append(2)
        elif attackVector == 'PHYSICAL':
            listOfAttackVector.append(1)
        else:

            listOfAttackVector.append(0)
    else:
        attackVector = None
        listOfAttackVector.append(0)

    if str(df['attackComplexity'][ind]) != 'nan':
        attackComplexity = str(df['attackComplexity'][ind]).upper()

        if attackComplexity == 'LOW':
            listOfAttackComplexity.append(3)
        elif attackComplexity == 'MEDIUM':
            listOfAttackComplexity.append(2)
        elif attackComplexity == 'HIGH':
            listOfAttackComplexity.append(1)
        else:
            listOfAttackComplexity.append(0)

    else:
        attackComplexity = None
        listOfAttackComplexity.append(0)

    if str(df['privilegesRequired'][ind]) != 'nan':
        privilegesRequired = str(df['privilegesRequired'][ind]).upper()

        if privilegesRequired == 'NONE':
            listOfPrivilegesRequired.append(3)
        elif privilegesRequired == 'LOW':
            listOfPrivilegesRequired.append(2)
        elif privilegesRequired == 'HIGH':
            listOfPrivilegesRequired.append(1)
    else:
        privilegesRequired = None
        listOfPrivilegesRequired.append(0)

    if str(df['userInteraction'][ind]) != 'nan':
        userInteraction = str(df['userInteraction'][ind]).upper()

        if userInteraction == 'NONE':
            listOfUserInteraction.append(2)
        elif userInteraction == 'REQUIRED':
            listOfUserInteraction.append(1)
    else:
        cveIdeuserInteractionntifier = None
        listOfUserInteraction.append(0)

    if str(df['scope'][ind]) != 'nan':
        scope = str(df['scope'][ind]).upper()

        if scope == 'CHANGED':
            listOfScope.append(2)
        elif scope == 'UNCHANGED':
            listOfScope.append(1)
    else:
        scope = None
        listOfScope.append(0)

    if str(df['confidentialityImpact'][ind]) != 'nan':
        confidentialityImpact = str(df['confidentialityImpact'][ind]).upper()

        if confidentialityImpact == 'HIGH' or confidentialityImpact == 'COMPLETE':
            listOfConfidentialityImpact.append(3)
        elif confidentialityImpact == 'LOW' or confidentialityImpact == 'PARTIAL':
            listOfConfidentialityImpact.append(2)
        elif confidentialityImpact == 'NONE':
            listOfConfidentialityImpact.append(1)

    else:
        confidentialityImpact = None
        listOfConfidentialityImpact.append(0)

    if str(df['integrityImpact'][ind]) != 'nan':
        integrityImpact = str(df['integrityImpact'][ind]).upper()

        if integrityImpact == 'HIGH' or integrityImpact == 'COMPLETE':
            listOfIntegrityImpact.append(3)
        elif integrityImpact == 'LOW' or integrityImpact == 'PARTIAL':
            listOfIntegrityImpact.append(2)
        elif integrityImpact == 'NONE':
            listOfIntegrityImpact.append(1)

    else:
        integrityImpact = None
        listOfIntegrityImpact.append(0)

    if str(df['availabilityImpact'][ind]) != 'nan':
        availabilityImpact = str(df['availabilityImpact'][ind]).upper()

        if availabilityImpact == 'HIGH' or availabilityImpact == 'COMPLETE':
            listOfAvailabilityImpact.append(3)
        elif availabilityImpact == 'LOW' or availabilityImpact == 'PARTIAL':
            listOfAvailabilityImpact.append(2)
        elif availabilityImpact == 'NONE':
            listOfAvailabilityImpact.append(1)

    else:
        availabilityImpact = None
        listOfAvailabilityImpact.append(0)

    # CHECK FROM HERE


    try:
        if str(df['exploitabilityScore'][ind]) != 'nan':
            exploitabilityScore = float(str(df['exploitabilityScore'][ind]))
            if exploitabilityScore == 0.0:
                listOfExploitabilityScore.append(0)
            elif exploitabilityScore >= 0.1 and exploitabilityScore <= 3.9:
                listOfExploitabilityScore.append(1)
            elif exploitabilityScore >= 4.0 and exploitabilityScore <= 6.9:
                listOfExploitabilityScore.append(2)
            elif exploitabilityScore >= 7.0 and exploitabilityScore <= 8.9:
                listOfExploitabilityScore.append(3)
            elif exploitabilityScore >= 9.0 and exploitabilityScore <= 10.0:
                listOfExploitabilityScore.append(4)
        else:
            exploitabilityScore = None
            listOfExploitabilityScore.append(0)

    except KeyError:
        listOfExploitabilityScore.append(0)


    try:
        if str(df['impactScore'][ind]) != 'nan':
            impactScore = float(str(df['impactScore'][ind]))
            if impactScore == 0.0:
                listOfImpactScore.append(0)
            elif impactScore >= 0.1 and impactScore <= 3.9:
                listOfImpactScore.append(impactScore)
            elif impactScore >= 4.0 and impactScore <= 6.9:
                listOfImpactScore.append(impactScore)
            elif impactScore >= 7.0 and impactScore <= 8.9:
                listOfImpactScore.append(impactScore)
            elif impactScore >= 9.0 and impactScore <= 10.0:
                listOfImpactScore.append(impactScore)
        else:
            impactScore = None
            listOfImpactScore.append(0)
    except KeyError:
        listOfImpactScore.append(0)

    try:

        if str(df['redhatSeverity'][ind]) != 'nan':
            redhatSeverity = str(df['redhatSeverity'][ind]).upper()
            if redhatSeverity == 'LOW':
                listOfToolSeverity.append(1)
            elif redhatSeverity == 'MODERATE':
                listOfToolSeverity.append(2)
            elif redhatSeverity == 'IMPORTANT':
                listOfToolSeverity.append(3)
            elif redhatSeverity == 'CRITICAL':
                listOfToolSeverity.append(4)

        else:
            redhatSeverity = 0

    except KeyError:
        listOfToolSeverity.append(0)

    if str(df['baseScore'][ind]) != 'nan':
        baseScore = float(str(df['baseScore'][ind]))
        if baseScore == 0.0:
            listOfBaseScore.append(0)
        elif baseScore >= 0.1 and baseScore <= 3.9:
            listOfBaseScore.append(baseScore)
        elif baseScore >= 4.0 and baseScore <= 6.9:
            listOfBaseScore.append(baseScore)
        elif baseScore >= 7.0 and baseScore <= 8.9:
            listOfBaseScore.append(baseScore)
        elif baseScore >= 9.0 and baseScore <= 10.0:
            listOfBaseScore.append(baseScore)
    else:
        baseScore = None
        listOfBaseScore.append(0)

    if str(df['baseSeverity'][ind]) != 'nan':
        baseSeverity = str(df['baseSeverity'][ind]).upper()
        if baseSeverity == 'NONE':
            listOfBaseSeverity.append(0)
        elif baseSeverity == 'LOW':
            listOfBaseSeverity.append(1)
        elif baseSeverity == 'MEDIUM':
            listOfBaseSeverity.append(2)
        elif baseSeverity == 'HIGH':
            listOfBaseSeverity.append(3)
        elif baseSeverity == 'CRITICAL':
            listOfBaseSeverity.append(4)
    else:
        baseSeverity = None
        listOfBaseSeverity.append(0)

    # list_of_cves_1.append(cve_identifier)
    # list_of_severity_rating_1.append(severity_rating)

# unique_list_of_cves = list(set(final_list_of_cves))
# print(len(unique_list_of_cves))

#exit()

#check existing cves
# listOfVerifiedCve = []
# listOfVerifiedSeverity = []
c=0
d=0
print("FinalFixed", len(listOfFinalCveIdentifier))
print("OverallSources", len(listOfCveIdentifier))



for i in range(len(listOfCveIdentifier)):
    if listOfCveIdentifier[i] in listOfFinalCveIdentifier:
        #d +=1
        indexHolder = listOfFinalCveIdentifier.index(listOfCveIdentifier[i])
        #print(indexHolder)
        if listOfBaseSeverity[i] == listOfFinalSeverityRating[indexHolder]:
            #print(listOfCveIdentifier[i], listOfBaseSeverity[indexHolder])
            listOfVerifiedCve.append(listOfCveIdentifier[i])
            listOfVerifiedSeverity.append(listOfFinalSeverityRating[indexHolder])
        c +=1


print(c)
print(len(listOfVerifiedCve))
uniqueList = list(set(listOfVerifiedCve))
listOfMismatches =[]
print(len(uniqueList))
#print(listOfCveIdentifier)

for w in range(len(listOfCveIdentifier)):
    cveIdentifierHolder = listOfCveIdentifier[w]
    for x in range(len(uniqueList)):
        if cveIdentifierHolder == uniqueList[x]:
            verifiedCveHolder = listOfVerifiedCve.index(cveIdentifierHolder)
            verifiedSeverityHolder = listOfVerifiedSeverity[verifiedCveHolder]

            if verifiedSeverityHolder != listOfBaseSeverity[w]:
                listOfMismatches.append(w)


print(listOfMismatches)
#exit()

print(len(listOfCveIdentifier))
print(len(listOfAttackVector))
print(len(listOfAttackComplexity))
print(len(listOfPrivilegesRequired))
#exit()
w=0
with open('final_dataset.csv', 'w') as result_file:
        writer = csv.writer(result_file, dialect='excel')

        for x in range(len(listOfCveIdentifier)):
            if x not in listOfMismatches:
                writer.writerow([listOfCveIdentifier[w]
                                 ,listOfPublishedDate[w]
                                 ,listOfLastModified[w]
                                 ,listOfAttackVector[w]
                                 ,listOfAttackComplexity[w]
                                 ,listOfPrivilegesRequired[w]
                                 ,listOfUserInteraction[w]
                                 ,listOfScope[w]
                                 ,listOfConfidentialityImpact[w]
                                 ,listOfIntegrityImpact[w]
                                 ,listOfAvailabilityImpact[w]
                                 ,listOfExploitabilityScore[w]
                                 ,listOfImpactScore[w]
                                 ,listOfToolSeverity[w]
                                 ,listOfBaseScore[w]
                                 ,listOfBaseSeverity[w]])
                w +=1
result_file.close()