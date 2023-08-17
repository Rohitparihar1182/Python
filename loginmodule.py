def enter_ph_no():
    ph_no=int(input("enter your mobile number:"))
    return ph_no
def enterdata():
    Name=input("enter your name: ")
    User_name=input("enter username: ")
    Pass=input("enter a strong password atlest 8 character(must contain a Character and an integer): ")
    E_mail=input("enter your e-mail: ")
    D_O_B=input("enter your date of birth: ").split(" ")
    return(Name,User_name,E_mail,D_O_B)
