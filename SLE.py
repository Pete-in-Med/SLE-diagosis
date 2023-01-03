import Prework.input

#the definition of the whole SLE diagnose
def SLE_diagnosis():
    #SLE diagnosis
    #the SLE diagnosis is consisted of five steps
    #the factors used in the project(doctors could easily change these factors to renew the system)
      #test name
        #list_clinical_domain, list_immunology_domain
      #test weight
        #all in the forth step
      #test value
        #upANA_r, ANA_value, list_clinical_result_A, list_immunology_result_B, dic_clinical, dic_immunology, dic_all

    #Welcome
    print(f"Please read the following descriptions before entering the criteria:\n1. Do not count a criterion if there is a more likely explanation than SLE\n2. Criteria need not occur simultaneously.\n3. If the symptom has an obvious cause, that specific symptom could not be taken into account.")

    #First step : classify by ANA
    #help to get out of the whole system
    import os,sys
    while True :
      #input ANA(antinuclear antibodies) at a titer of ≥1:80 on HEp-2 cells or an equivalent positive test (ever)
      ANA_r = input("Do the patient has his or her ANA value?(y/n)")
      upANA_r = ANA_r.upper()
      if upANA_r == "N":
        # ANA_value is an important element in "2019 European League Against Rheumatism/American College of Rheumatology Classification Criteria for Systemic Lupus Erythematosus"
        # the system couldn't start lacking of ANA_value
        print("In this case, the patient didn't have enough figures to proof that he or she is a SLE patient")
        sys.exit()
      elif upANA_r =="Y" :
        #start to input data
        ANA_value = input("Please enter the value of ANA at a titer of ≥1:80 on HEp-2 cells:")
        break
      elif upANA_r =="" :
        print("You have accidentally pressed the enter button, please try to fill in the data again.")
      else :
        print('Please check to ensure that the input is "y" or "n", and input the data again')


    #Second step : ask for the condition of the patient
    #input data
    #clinical domains and criteria
    list_clinical_domain = ["Fever","Autoimmune hemolysis","Thrombocytopenia","Leukopenia","Seizure","Psychosis","Delirium","Acute cutaneous lupus","Subacute cutaneous OR discoid lupus",
    "Oral ulcers","Non-scarring alopecia","Acute pericarditis","Pleural or pericardial effusion","Joint involvement"]
    list_immunology_domain = ["Anti-cardiolipin antibodies OR Anti-β2GP1 antibodies OR  Lupus anticoagulant","Low C3 AND low C4","Low C3 OR low C4 ","Anti-dsDNA antibody* OR Anti-Smith antibody"]
    list_clinical_result_A = []
    list_clinical_result_1 = []
    list_immunology_result_B = []
    list_immunology_result_2 = []

    #clinical domain
    print(f"\nThe following is the input process of the clinical data!\nPlease use y/n/ni/b to respectively represent yes/no/no information/back")
    Prework.input.input_process_A(list_clinical_domain,list_clinical_result_A,list_clinical_result_1)

    #Renal biopsy class distinguishment
    while True :
        Renal_biopsy_class = input("What is the Renal biopsy class of the patient?(1,2,3,4,5,6)")
        if Renal_biopsy_class =="":
            print("You have accidentally pressed the enter button, please try to fill in the data again.")
            continue
        #if the user doesn't input integer, than the user would need to input the data again
        try:
            Renal_biopsy_class = int(Renal_biopsy_class)
        except ValueError:
            print('Please check to ensure that the input is an integer, the class of renal biopsy class, and input the data again.')
            continue
        if Renal_biopsy_class == 3 or Renal_biopsy_class == 4:
            #use extend to append a list instead of an object into a list
            list_clinical_domain.extend(["Renal biopsy Class III or IV lupus nephritis","Renal biopsy Class II or V lupus nephritis"])
            list_clinical_result_A.extend(["Y","N"])
            list_clinical_result_1.extend([1,0])
            break
        elif Renal_biopsy_class == 2 or Renal_biopsy_class == 5:
            list_clinical_domain.extend(["Renal biopsy Class III or IV lupus nephritis","Renal biopsy Class II or V lupus nephritis"])
            list_clinical_result_A.extend(["N","Y"])
            list_clinical_result_1.extend([0,1])
            break
        elif Renal_biopsy_class == 1:
            list_clinical_domain.extend(["Renal biopsy Class III or IV lupus nephritis","Renal biopsy Class II or V lupus nephritis"])
            list_clinical_result_A.extend(["N","N"])
            list_clinical_result_1.extend([0,0])
            break
        else:
            print("Please check to ensure that you have entered the correct renal biopsy class of the patient, and input the data again.")

    #proteinuria_value distinguishment
    while True :
        proteinuria_value = input("What is the proteinuria value of the patient(mg/24h)?")
        if proteinuria_value =="":
            print("You have accidentally pressed the enter button, please try to fill in the data again.")
            continue
        try:
            proteinuria_value = float(proteinuria_value)
        except ValueError:
            print('Please check to ensure that the input is an integer or float, and input the data again')
            continue

        if proteinuria_value > 500:
            list_clinical_result_A.append("Y")
            list_clinical_result_1.append(1)
            list_clinical_domain.append("Proteinuria >0.5g/24h")
            break
        else:
            list_clinical_result_A.append("N")
            list_clinical_result_1.append(0)
            list_clinical_domain.append("Proteinuria >0.5g/24h")
            break

    #immunology domain
    #print an empty space to let the system be easier to read
    print(f"\nThe following is the input process of the immunology data!\nPlease use y/n/ni/b to respectively represent yes/no/no information/back")
    Prework.input.input_process_A(list_immunology_domain,list_immunology_result_B,list_immunology_result_2)


    #Third step : confirm the data
    #print readable dictionary
    dic_clinical = dict(zip(list_clinical_domain, list_clinical_result_A))
    dic_immunology = dict(zip(list_immunology_domain, list_immunology_result_B))
    import pprint
    print(f"\nThe following part is about clinical data")
    # doesn't use the function of sorting the dicts to print readable dictionary
    pprint.pprint(dic_clinical,sort_dicts=False)
    print(f"Renal biopsy class: {Renal_biopsy_class}")
    print(f"Proteinuria value: {proteinuria_value}\n\nThe following part is about immunology data")
    pprint.pprint(dic_immunology)
    Prework.confirm.confirm_process()


    #Forth step : dealing with data
    #patient result
    #use numpy to arrange the data
    import numpy as np
    arr_clinical_result = np.zeros((7, 4))
    arr_immunology_result = np.zeros((3,4))

    #result
    #clinical part
    arr_clinical_result[0,0:1] = list_clinical_result_1[0:1]
    arr_clinical_result[1,0:3] = list_clinical_result_1[1:4]
    arr_clinical_result[2,0:3] = list_clinical_result_1[4:7]
    arr_clinical_result[3,0:4] = list_clinical_result_1[7:11]
    arr_clinical_result[4,0:2] = list_clinical_result_1[11:13]
    arr_clinical_result[5,0:1] = list_clinical_result_1[13:14]
    arr_clinical_result[6,0:3] = list_clinical_result_1[14:17]

    #immunology part
    arr_immunology_result[0,0:1] = list_immunology_result_2[0:1]
    arr_immunology_result[1,0:2] = list_immunology_result_2[1:3]
    arr_immunology_result[2,0:1] = list_immunology_result_2[3:4]

    #weight
    #clinical weight
    arr_clinical_weight = np.array([[2,0,0,0], [4,4,3,0],[5,3,2,0],[6,4,2,2],[6,5,0,0],[6,0,0,0],[10,8,4,0]])
    #immunology weight
    arr_immunology_weight = np.array([[2,0,0,0],[4,3,0,0],[6,0,0,0]])

    #value
    #multiply
    #to calculate the value of specific categories
    arr_clinical_value = np.multiply(arr_clinical_result, arr_clinical_weight)
    arr_immunology_value = np.multiply(arr_immunology_result,arr_immunology_weight)
    arr_all_value = np.vstack((arr_clinical_value,arr_immunology_value))
    #max
    max_clinical_value = np.amax(arr_clinical_value, axis=1)
    max_immunology_value = np.amax(arr_immunology_value,axis=1)
    #sum
    total_clinical_value = np.sum(max_clinical_value)
    total_immunology_value = np.sum(max_immunology_value)
    sum_up = 0
    sum_up = total_clinical_value + total_immunology_value


    #Fifth step : output
    #classification
    if sum_up >= 10 :
      upSLE_r = "Y"
      print(f"\nThe patient is diagnosed as SLE")
    else :
      upSLE_r = "N"
      print(f"\nThe current test project does not provide sufficient evidence to determine a positive result")

    #all No Information columns in the list
    print(f"If you need more precise results, you need to complete the patient's data by doing the following tests\nHere are the missing data of the patient in the clinical domain")
    for key,value in dic_clinical.items():
      if value == "NI":
          print(key)
    print("Here are the missing data of the patient in the immunology domain")
    for key,value in dic_immunology.items():
      if value == "NI":
          print(key)
    print(f"\n")

    arr_all_domain = np.array([["Fever",0,0,0],["Autoimmune hemolysis","Thrombocytopenia","Leukopenia",0],["Seizure","Psychosis","Delirium",0],["Acute cutaneous lupus","Subacute cutaneous OR discoid lupus","Oral ulcers","Non-scarring alopecia"],
    ["Acute pericarditis","Pleural or pericardial effusion",0,0],["Joint involvement",0,0,0],["Renal biopsy Class III or IV lupus nephritis","Renal biopsy Class II or V lupus nephritis","Proteinuria >0.5g/24h",0],
    ["Anti-cardiolipin antibodies OR Anti-β2GP1 antibodies OR  Lupus anticoagulant",0,0,0],["Low C3 AND low C4","Low C3 OR low C4 ",0,0],["Anti-dsDNA antibody* OR Anti-Smith antibody",0,0,0]])
    # Find index of maximum value from 2D numpy array
    result = np.where(arr_all_value == np.amax(arr_all_value))
    listofcordinates = list(zip(result[0],result[1]))
    for cord in listofcordinates:
      (index_a,index_b) = cord

    print(f"Total score:{sum_up}\nClinical score:{total_clinical_value}\nImmunology score:{total_immunology_value}\n")

    max_key = arr_all_domain[int(index_a),int(index_b)]
    max_value = arr_all_value[int(index_a),int(index_b)]
    if sum_up == 0:
        print(f"\nReference:This system is based on the 2019 European League Against Rheumatism/American College of Rheumatology Classification Criteria for Systemic Lupus Erythematosus\n")
        pass
    else:
        print(f"\nHere is the symptom which accounts for the highest proportion of the score:{max_key}\nThe score of the this symptom accounts for{(max_value/sum_up)*100:.2f}%of the total points\nReference:This system is based on the 2019 European League Against Rheumatism/American College of Rheumatology Classification Criteria for Systemic Lupus Erythematosus\n")

    if upSLE_r == "N":
        sys.exit()
