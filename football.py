#ALIAKBAR_POORAHMADI
class Footbalist:
   
    def __init__(self, first_name, last_name, number, height, weight, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.height = height
        self.weight = weight
        self.age = age 
    
    def player_first_number(self):
        return('The player first name: '+ self.first_name)
    
   
    def player_last_number(self):
        return('The playerlast name: '+ self.last_name)
    
    
    def player_number(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' number is ' +str(self.number))
  
    def player_height(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' height is ' +str(self.height))
    
     
    def player_weight(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' weight is ' +str(self.weight) + 'kg')
    
     
    def player_age(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' age is ' +str(self.age))
    

class Goalkeeper(Footbalist):
    pass

class Defenders(Footbalist):
    pass

class Midfielders(Footbalist):
    pass

class Forwards(Footbalist):
    pass


player_1 = Footbalist('amir' , 'amiry' , 8 , 186 , 91, 21)
player_2 = Goalkeeper('ali' , 'akbary' , 5 , 189 , 24)
player_3 = Forwards('esmail' , 'najmei' , 6 , 181 , 25)
player_4 = Forwards('Ehsan' , 'sobhani' , 9 , 184 , 27)
player_5 = Midfielders('mohammad' , 'emadi' , 10 , 176 , 23)
player_6 = Midfielders('Mahmood' , 'taheri' , 2 , 180 , 25)
player_6 = Defenders('aliakbar' , 'poorahmadi' , 1 , 177 , 26)



print(player_1.player_first_number())
print(player_1.player_last_number())
print(player_1.player_number())
print(player_1.player_height())
print(player_1.player_weight())
print(player_1.player_age())