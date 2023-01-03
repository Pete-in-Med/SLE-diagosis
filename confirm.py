#the definition of the confirm process
def confirm_process():
    #help to get out of the whole system
    import os,sys
    while True :
      confirm = input("Please confirm whether the result is correct or not(y/n):")
      up_confirm = confirm.upper()
      if up_confirm == "Y":
        break
      elif up_confirm == "N":
        #quit the system and ask the doctor to input the data again
        print("If you enter the wrong input, please stop the system and restart the system again")
        sys.exit()
      elif up_confirm =="" :
        print("You have accidentally pressed the enter button, please try to fill in the data again.")
      else :
        print('Please check to ensure that the input is "y" or "n", and input the data again')
