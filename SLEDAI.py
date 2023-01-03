import Prework.input

#definition of the SLEDAI standard
def SLEDAI_standard():
    #SLEDAI
    #SLEDAI data collect
    list_result_C = []
    list_result_3 = []
    list_SLEDAI = ["Seizure","Psychosis","Organic brain syndrome","Visual disturbance","Cranial nerve disorder","Lupus headache","CVA","Vasculitis","Arthritis","Myositis","Urinary casts","Hematuria","Proteinuria","Pyuria","Rash","Alopecia","Mucosal ulcers","Pleurisy","Pericarditis","Low complement","Increased DNA binding","Fever","Thrombocytopenia","Leukopenia"]
    Prework.input.input_process_A(list_SLEDAI,list_result_C,list_result_3)

    #SLEDAI data confirm
    dic_SLEDAI = dict(zip(list_SLEDAI, list_result_C))
    #print readable dictionary
    import pprint
    print(f"\nThe following part is the data of SLEDAI")
    pprint.pprint(dic_SLEDAI,sort_dicts=False)
    Prework.confirm.confirm_process()

    #SLEDAI data processing
    import numpy as np
    arr_SLEDAI_result = np.array(list_result_3)

    #weight
    arr_SLEDAI_weight = np.array([8,8,8,8,8,8,8,8,4,4,4,4,4,4,2,2,2,2,2,2,2,1,1,1])
    arr_SLEDAI_value = np.multiply(arr_SLEDAI_result,arr_SLEDAI_weight)

    #sum
    total = np.sum(arr_SLEDAI_value)
    float(total)

    #distinguishment
    if total >  19 :
        print("very high activity")
    elif total > 10 :
        print("high activity")
    elif total > 5 :
        print("moderate activity")
    elif total > 1 :
        print("mild activity")
    else:
        print("no activity")
    print(f"Reference:This system is based on SLEDAI-2K(30 Days).2010.")
