# BankersAlgorithm

The banker’s algorithm is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation for predetermined maximum possible amounts of all resources, then makes an “s-state” check to test for possible activities, before deciding whether allocation should be allowed to continue.

# How to use

 - clone the repo
 - run this command from the terminal or simply install numpy => "pip install -r requirements.txt"
 - run this command from the terminal "python app.py"
 - ![image](https://user-images.githubusercontent.com/54520113/118970698-cc4be880-b96e-11eb-973a-2a6f48ba4077.png) : ex : "0 0 1 2,1 0 0 0,1 3 5 4,0 6 3 2,0 0 1 4"
 - ![image](https://user-images.githubusercontent.com/54520113/118970747-dec62200-b96e-11eb-9deb-b8f91e6a87c9.png) : ex : "0 0 1 2,1 7 5 0,2 3 5 6,0 6 5 2,0 6 5 6"
 - ![image](https://user-images.githubusercontent.com/54520113/118970793-ebe31100-b96e-11eb-80bc-8fb8301e5f14.png) : ex : "3 4 3 2"
 - Then the need matrix will be printed and you will be asked if you want to know if the state is safe or not
 - ![image](https://user-images.githubusercontent.com/54520113/118971130-53995c00-b96f-11eb-9a80-42b67d74e4ea.png)
 - if you clicked 1 : ![image](https://user-images.githubusercontent.com/54520113/118971162-601db480-b96f-11eb-95da-1a7d76ea6ec5.png)
 - Then you can click 1 again if you want to know if an immediate request could be granted
 - first enter the process number : ![image](https://user-images.githubusercontent.com/54520113/118971239-7592de80-b96f-11eb-9960-c063241e4670.png)
 - Then the request : ![image](https://user-images.githubusercontent.com/54520113/118971376-a1ae5f80-b96f-11eb-9b7f-55c197ef52f2.png)





