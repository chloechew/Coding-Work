print("Title of program: Caitlin's Awesome Encourager [Not really a word but meh -_-]")
print()
while True:
  description = input("How do you feel today?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("Awwwwww you will be fineeeee CHEER UP!!!! You can always talk to me if you are feeling very sad!! I will help you to the best of my ability:)))))) Jiayouzzzzz okayyyy I will always be here for you if you need help. Whoopie!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Yayyyyy being happy is always the BEST!!!! Continue to stay positive!!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("You should take a short rest... being tired won't help!! I shall set timers for you!! Jiayouzzzzzz you are much stronger than you think:)))))")
      counter += 1
    if each_word == "awesome":
      feelings_list.append("awesome")
      encouragement_list.append("You are AWESOME in every way")
      counter += 1
    if each_word == "meh":
      feelings_list.append("meh")
      encouragement_list.append("Hehe we will feel meh sometimes toooooo")
      counter += 1
    if each_word == "laughy":
      feelings_list.append("laughy")
      encouragement_list.append("Whoop!!!!! Be like meeeee and laugh a lotttt!!!! Don't listen to friends that tell you to stop laughing!!!!!!! It has been scientifically proven that laughing is good for your health!!! [According to The Caitlin Scientific lab of research]")
      counter += 1

  if counter == 0:
    
      output = "Use words like sad, happy, tired, awesome ,laughy and meh. Alsoooo don't caps the first letter if not it will not work"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
