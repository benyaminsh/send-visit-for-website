from termcolor import colored
from requests import get
from os import system

system("cls")

Link = str(input("Enter Link web Site : "))


def Send(url):

    check = url[0:5]
    
    if check != "https":
        print("Error : Site address must be https !")
        exit()
        
    else: pass

    print("\nStart . . . \n")
    
    try:
        ProxyFileHTTPS = open("Https.txt","r+")
    except:
        print("Error : The Https.txt file does not exist!")
        exit()


  

    NumberSent = 0
    NumberNotSent = 0
     
    for proxyHTTPS in ProxyFileHTTPS.readlines():
        
        if len(proxyHTTPS) >= 0:
            print(f"-----\n\nSending ... \n\n{colored('<!>','yellow')} {colored('Proxy','blue')} > {proxyHTTPS} \n\n{colored('<!>','yellow')}  {colored('Number Sent','green')} > {NumberSent} \n\n{colored('<!>','yellow')} {colored('Number Not Sent','red')} > {NumberNotSent}\n\n----\n")
            try:
                proxyDict = {
                    "https": f"http://{proxyHTTPS}",               
                    }



                result = get(url,timeout=(100000),proxies=proxyDict).status_code

              

                if result == 200:
                    NumberSent += 1
                else: 
                    NumberNotSent += 1


            except:
                NumberNotSent += 1
        
        else: pass
    
    return f"--------\n\nNumber Sent : {NumberSent}\n\nNumber Not Sent : {NumberNotSent}\n\n--------\n\nEnd :)"


        
        
        
        



print(Send(Link))