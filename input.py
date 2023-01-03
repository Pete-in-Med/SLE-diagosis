def input_process_A(list_domain,list_result_A,list_result_1):
    i = 0
    while i < len(list_domain):
      print(list_domain[i],"?","(y/n/ni/b)")
      r = input()
      #ensure that the system wouldn't break owing to uppercase and lowercase problems
      up_r = r.upper()
      if up_r == "N":
        # adding the element as Y,N,NI
        list_result_A.append(up_r)
        up_r = 0
        # adding the element as 1,0,0
        # "no information" has been viewed as 0, when calculating the sum
        list_result_1.append(up_r)
        i += 1
      elif up_r =="Y" :
        list_result_A.append(up_r)
        up_r = 1
        list_result_1.append(up_r)
        i += 1
      elif up_r =="NI" :
        list_result_A.append(up_r)
        up_r = 0
        list_result_1.append(up_r)
        i += 1
      elif up_r =="B" :
        #incase that someone press the back button on the first input
        if i == 0:
            print("You have accidentally pressed the back button on the first input, please try to fill in the data again.")
            continue
        else:
            #clear the former answer
            list_result_A.pop()
            list_result_1.pop()
            i -= 1
      elif up_r =="" :
        print("You have accidentally pressed the enter button, please try to fill in the data again.")
      else :
        print('Please check to ensure that the input is "y" / "n" / "ni" / "b", and input the data again')
