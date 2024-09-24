import requests
url='https://random-word-api.herokuapp.com/word'

params={'number':1}

response = requests.get(url, params=params)
if response.status_code == 200: 
    data = response.json()
else:
    print(f"Failed to retrieve words. Status code: {response.status_code}")
    print(f"Response content: {response.text}")
    
    
 

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word=data[0]
str_word=""
for i in word:
    str_word+="_"

correct_letters=[]
gameover=False
hangManCounter=0

print(HANGMANPICS[0])
print(str_word)
while not gameover:
    display=""
    choice= input("choose a letter: ").lower()
    for i in word:
        if i==choice:
            display+=choice
            correct_letters.append(choice)
        elif i in correct_letters:
            display+=i
        else:
            display+="_"
    if choice not in word:
        hangManCounter+=1  
    print(HANGMANPICS[hangManCounter])
    print(display)   
    if "_" not in display:
        gameover=True
        print("GameOver You WIN!")
    if hangManCounter== 5:
        gameover=True
        print(HANGMANPICS[6])
        print("GameOver You Lose!")
        
        
