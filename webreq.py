import requests
import validators

print("""\

██╗    ██╗███████╗██████╗ ██████╗ ███████╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔═══██╗
██║ █╗ ██║█████╗  ██████╔╝██████╔╝█████╗  ██║   ██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ██║▄▄ ██║
╚███╔███╔╝███████╗██████╔╝██║  ██║███████╗╚██████╔╝
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝ 
                                            
              ┌─┐┬  ┌─┐┬ ┬┌─┐
              ├─┤│  ├─┘├─┤├─┤
              ┴ ┴┴─┘┴  ┴ ┴┴ ┴ (1.3)
               
               
               
                                      
                    """)

ver=False
while not ver:
    input_url = input("Enter the URL: ")

    if not validators.url(input_url):
        print("""
        
        ⚠ WARNING! ⚠ : Invalid URL!
        
        """)
    else:
        ver=True

print("""\
    
1) GET
2) POST
3) HEAD
    """)

choice = int(input("Enter your choice: "))

if choice == 1:
    print("""\
    
1) Simple GET
2) GET + Cookie
3) GET + Payload
4) GET + Custom Header

    """)

    choice2 = int(input("\nEnter your choice: "))
    if choice2 == 1:
        r = requests.get(input_url)
        
    elif choice2 == 2:
        cookiename = input("\nEnter your cookie name: ")
        cookievalue = input("\nEnter your cookie value: ")
        cookies = {cookiename: cookievalue}
        r = requests.get(input_url, cookies=cookies)
        
    elif choice2 == 3:
        PayloadParamName = input("\nEnter your Payload name: ")
        PayloadParamValue = input("\nEnter your Payload value: ")
        cookies = {PayloadParamName: PayloadParamValue}
        r = requests.get(input_url, params=cookies)
        
    elif choice2 == 4:
        HeaderName = input("\nEnter your Header name: ")
        HeaderValue = input("\nEnter your Header value: ")
        headers = {HeaderName: HeaderValue}
        r = requests.get(input_url, headers=headers)
        
    print("\nRESPONSE:\n\n"+r.text)

if choice == 2:
    print("""\
    
1) Simple POST
2) POST + Cookie
    
    """)

    choice2 = int(input("\nEnter your choice: "))
    if choice2 == 1:
        r = requests.post(input_url)
        
    elif choice2 == 2:
        cookiename = input("\nEnter your cookie name: ")
        cookievalue = input("\nEnter your cookie value: ")
        cookies = {cookiename: cookievalue}
        r = requests.post(input_url, cookies=cookies)
    
    print("\nRESPONSE:\n\n"+r.text)

if choice==3:
    x = requests.head(input_url)
    print("\nRESPONSE:\n\n"+x.headers)