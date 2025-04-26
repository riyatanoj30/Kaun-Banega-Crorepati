# Kaun Banega Crorepati Game

import Questions as q
        
def main(naam):
    print("Namaskar Deviyon Aur Sajaano Aap Sabhi Ka Swagat Hai Kaun Banega Crorepati Me!")
    print(f"Toh Aaj Humare Sath Hai {naam} Ji, Chaliye Shuru Karte hai Bina Kisi Deri Ke...")
    money = 0
    print("\n\nPehla Padav Shuru Hota Hai")
    for question, answer in q.Level_1().items():
        print(f"Question: {question}")
        for idx, option in enumerate(answer["options"], 1):
            print(f"{idx}. {option}")
        
        
        user_answer = int(input("Choose the correct answer (1-4): "))
        
        
        if answer["options"][user_answer - 1] == answer["correct_answer"]:
            print("Correct! ")
            money += 10000  
        else:
            print(f"Afsos Galat Jawab! Sahi Jawab hai: {answer['correct_answer']}")
            print(f"Bohot hi acha Khele aap! Par aapka Khel Yahi Samapt Hota Hai Aur Aaj Aap Sirf {money} rupee Hi Le Ja Payenge! \n\t\tDhanyawad Aapka Radhe Radhe")
            break  
    
    if money == 50000:
        print("\n\n Badhai Ho! Aapne Badi Hi Safalta Se Pehla Padav Paar Kar Liya.")
        print(f"Aapki Kul Dhan Rashi Ho Chuki Hai {money} rupee!")
        print("\n\n Agle Padav Ke Sawal Ye Rahe Aapke Screen Par")
        for question, answer in q.Level_2().items():
            print(f"Question: {question}")
            for idx, option in enumerate(answer["options"], 1):
                print(f"{idx}. {option}")
        
            
            user_answer = int(input("Choose the correct answer (1-4): "))
        
           
            if answer["options"][user_answer - 1] == answer["correct_answer"]:
                print("Correct! ")
                money += 500000  
            else:
                print(f"Afsos Galat Jawab! Sahi Jawab hai: {answer['correct_answer']}")
                print(f"Bohot hi acha Khele aap! Par aapka Khel Yahi Samapt Hota Hai Aur Aaj Aap Sirf {money} rupee Hi Le Ja Payenge! \n\t\tDhanyawad Aapka Radhe Radhe")
                break  
    else:
        print("Khel Samapt Ho Gaya")

    if money == 2550000:
        print("\n\n Badhai Ho! Aapne Badi Hi Safalta Se Dusra Padav Paar Kar Liya.")
        print(f"Aapki Kul Dhan Rashi Ho Chuki Hai {money} rupee!")
        print("\n\n Agle Padav Ke Sawal Ye Rahe Aapke Screen Par")
        for question, answer in q.Level_3().items():
            print(f"Question: {question}")
            for idx, option in enumerate(answer["options"], 1):
                print(f"{idx}. {option}")
        
           
            user_answer = int(input("Choose the correct answer (1-4): "))
        
            
            if answer["options"][user_answer - 1] == answer["correct_answer"]:
                print("Correct! ")
                money += 2000000  
            else:
                print(f"Afsos Galat Jawab! Sahi Jawab hai: {answer['correct_answer']}")
                print(f"Bohot hi acha Khele aap! Par aapka Khel Yahi Samapt Hota Hai Aur Aaj Aap Sirf {money} rupee Hi Le Ja Payenge! \n\t\tDhanyawad Aapka Radhe Radhe")
                break     

        print("Dher Sari Badhai Ho Aap Bante Hai Crorepati")
        print(f"Aapki Kul Jeeti Hui Rashi Hui {money} Rupee")
        print("\n\n\n\t\tAfsos Itni Mehnat Ke Baad Bhi Ye Sirf Ek Game Tha I mean Paise Jeete Par Mil Nai Paye Koi Nai Ese Hi Mehnat Karte Rahe Radhe Radhe")
    else:
        print("Khel Samapt Ho Gaya")
    
Choice = int(input("Press 1 To Start Game / Press 2 To Exit Game: "))
if Choice == 1:
    name = input("Enter Players Name: ")
    main(name)
else:
    print("Aapka Khub Khub Abhar Fir Aayega Game Khelne...Radhe Radhe")
