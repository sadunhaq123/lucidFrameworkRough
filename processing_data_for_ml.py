import pandas as pd
import json
import xlsxwriter
import os
import csv
from difflib import SequenceMatcher
import datetime



df_ubuntu_parsed_results= pd.read_csv('ubuntu_parsed_results.csv')
df_redhat_parsed_results= pd.read_csv('redhat_parsed_results.csv')
df_nvd_parsed_results = pd.read_csv('nvd_parsed_results.csv')
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
listOfBaseScore = []
listOfBaseSeverity = []
listOfExploitabilityScore = []
listOfImpactScore = []
#listOfScope = []


#Working with different severities, same assigners but different modification time
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
         publishedDate = None
     listOfPublishedDate.append(publishedDate)

     
     if str(df['lastModified'][ind]) != 'nan':
         lastModified = str(df['lastModified'][ind])
     else:
         lastModified = None
     listOfLastModified.append(lastModified)
    
     if str(df['attackVector'][ind]) != 'nan':
         attackVector = str(df['attackVector'][ind])
         if attackVector =='NETWORK':
             listOfAttackVector.append(4)
         elif attackVector =='ADJACENT':
             listOfAttackVector.append(3)
         elif attackVector =='LOCAL':
             listOfAttackVector.append(2)
         elif attackVector =='PHYSICAL':
             listOfAttackVector.append(1)
     else:
         attackVector = None
         listOfAttackVector.append(0)

     if str(df['attackComplexity'][ind]) != 'nan':
         attackComplexity = str(df['attackComplexity'][ind])

         if attackComplexity == 'LOW':
             listOfAttackComplexity.append(2)
         elif attackComplexity == 'HIGH':
             listOfAttackComplexity.append(1)
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

         if confidentialityImpact == 'HIGH':
             listOfConfidentialityImpact.append(3)
         elif confidentialityImpact == 'LOW':
             listOfConfidentialityImpact.append(2)
         elif confidentialityImpact == 'NONE':
             listOfConfidentialityImpact.append(1)

     else:
         confidentialityImpact = None
         listOfConfidentialityImpact.append(0)
    
     if str(df['integrityImpact'][ind]) != 'nan':
         integrityImpact = str(df['integrityImpact'][ind])

         if integrityImpact == 'HIGH':
             listOfIntegrityImpact.append(3)
         elif integrityImpact == 'LOW':
             listOfIntegrityImpact.append(2)
         elif integrityImpact == 'NONE':
             listOfIntegrityImpact.append(1)

     else:
         integrityImpact = None
         listOfIntegrityImpact.append(0)

     if str(df['availabilityImpact'][ind]) != 'nan':
         availabilityImpact = str(df['availabilityImpact'][ind])

         if availabilityImpact == 'HIGH':
             listOfAvailabilityImpact.append(3)
         elif availabilityImpact == 'LOW':
             listOfAvailabilityImpact.append(2)
         elif availabilityImpact == 'NONE':
             listOfAvailabilityImpact.append(1)

     else:
         availabilityImpact = None
         listOfAvailabilityImpact.append(0)



     #CHECK FROM HERE

     if str(df['baseScore'][ind]) != 'nan':
         baseScore = str(df['baseScore'][ind])
     else:
         baseScore = None

     if str(df['baseSeverity'][ind]) != 'nan':
         baseSeverity = str(df['baseSeverity'][ind])
     else:
         baseSeverity = None


     if str(df['exploitabilityScore'][ind]) != 'nan':
         exploitabilityScore = str(df['exploitabilityScore'][ind])
     else:
         exploitabilityScore = None

     if str(df['impactScore'][ind]) != 'nan':
         impactScore = str(df['impactScore'][ind])
     else:
         impactScore = None

     list_of_cves_1.append(cve_identifier)
     list_of_severity_rating_1.append(severity_rating)




# unique_list_of_cves = list(set(final_list_of_cves))
# print(len(unique_list_of_cves))

exit()

with open('final_cve_list_with_severities.xlsx', 'w') as result_file:
        writer = csv.writer(result_file, dialect='excel')

        for w in range(len(final_list_of_cves)):
            writer.writerow([final_list_of_cves[w]
                            ,final_list_of_severity_rating[w]])
result_file.close()