#-*- coding:utf-8 -*-
"""
 ███▄    █  ▄▄▄       ███▄    █  █    ██  ███▄ ▄███▓
 ██ ▀█   █ ▒████▄     ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒
▓██  ▀█ ██▒▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░
▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ 
▒██░   ▓██░ ▓█   ▓██▒▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░
   ░   ░ ░   ░   ▒      ░   ░ ░  ░░░ ░ ░ ░      ░   
         ░       ░  ░         ░    ░            ░   
                                                    
"""
banner="""
███╗   ██╗ █████╗ ███╗   ██╗██╗   ██╗███╗   ███╗
████╗  ██║██╔══██╗████╗  ██║██║   ██║████╗ ████║
██╔██╗ ██║███████║██╔██╗ ██║██║   ██║██╔████╔██║
██║╚██╗██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║    
██║ ╚████║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║        
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝  

      ┌┐ ┬ ┬  ┌─┐┌─┐┌┬┐ │ ┬  ┌─┐┌─┐┌─┐
      ├┴┐└┬┘  │  ├─┤ │  │ │  ├┤ └─┐└─┐
      └─┘ ┴   └─┘┴ ┴ ┴  │ ┴─┘└─┘└─┘└─┘

                                     version 0.1
"""
MainMenu = """  1. Show Framework
  2. New Chain
  3. Modify Chain
  4. Delete Chain
"""
SubMenu2 = """

"""
subMenu3 = """

"""
subMenu4 = """

"""
C_END = "\033[0m"
C_UNDER = "\033[4m"
C_CYAN = "\033[36m"
C_RED = "\033[31m"
C_GREEN  = "\033[32m"
C_PURPLE = "\033[35m"
C_YELLOW = "\033[33m"

#------------------------------------------------------------#
def readFW():
    try :
        f = open("chains",'r')
        fw = f.read()
        f.close()
    except: fw = ""
    return fw[:-2]

#------ Menu Func ------#
def show_fw(fw):
    ret = ""
    if fw == "" : ret = "No Chains"
    else :
        chains = fw.split('\n')
        cnt = 0
        for chain in chains:
            cnt += 1
            ret += "- Chain " + str(cnt) + ':\n' + C_RED
            for module in chain.split(','):
                ret += module + "-"
            ret = ret[:-1]+'\n'+C_END
    return ret.replace('P)-','P)-\n'+C_YELLOW)

#----- Main -----#
if __name__ == "__main__" :
    print banner

    while True:
        print MainMenu
        num = raw_input(C_UNDER+"NANUM"+C_END+" > ")

        if num == 'q' or num == 'Q': 
            print "Good Bye"
            break

        try:num = int(num)
        except :num = 0

        fw = readFW()
        if num ==  1:
            print C_CYAN+"<Show Framwork>"+C_END
            print show_fw(fw)
        elif num == 2:
            print C_CYAN+"<New Chain>"+C_END
        
        elif num == 3:
            print C_CYAN+"<Modify Chain>"+C_END
        
        elif num == 4:
            print C_CYAN+"<Delete Chain>"+C_END
        
        else:
            print C_RED+"Try Again."+C_END
