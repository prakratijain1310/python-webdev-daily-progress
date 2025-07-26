#Enter no of line you want to read 
with open("myfile.txt", "w") as file:
    file.write("Hello\nHellooooooo\nHello\nHello\nHello\nHello\n")
'''n=int(input("enter"))
with open("myfile.txt", "r") as file:
    lines=file.readlines()
    for i in range(n):
        print(lines[i])'''

#readline(),read()
'''with open("myfile.txt", "r") as file:
    content1= file.readlines()
    content2= file.read()
    print(content1)
    print(content2)'''

#largest word
with open("myfile.txt", "r") as file:
    lines=file.readlines()
    print(lines)
    print(max(lines))

    