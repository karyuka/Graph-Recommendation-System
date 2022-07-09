from GraphVertex import Graph, Vertex, games_string, games, graphs
from time import sleep
import re 



class Bot:

    def __init__(self):
     self.stop_words = ["no", "stop", "quit", "hate", "bye", "see you"]
    
    def exiting(self, message):
        if message in self.stop_words:
            print("Good bye!")
            return False
        for word in self.stop_words:
          for i in range(len(message)):
            matches = 0
            for j in range(len(word)):
                if (i+j) < len(message):
                  if word[j] == message[i+j]:
                    matches += 1
                  else:
                     break
                else:
                  break
            if matches == len(word):
                self.stop_words.append(message)
                print("OK then, have a nice day!")
                return False
        return True


    def talk(self):
        message = input("Hello! I LOVE VideoGames! Do you have the same interest?\n")
        while self.exiting(message):
            message = self.respond()


    def respond(self):
        reply = input(f"Which of These Games have You played?\n {games_string}")
        while reply.title() not in games:
            print("I Hava No Idea About That Game.. You Can Choose One Of These Instead!\n")
            sleep(2)
            print(games_string)
            reply = input()
        return self.intent_class(reply)


   

    def intent_class(self, game):
        print("That is a nice game!".title())
        price_diff = self.recommend()
        cur_game = None
        similar_games = {}
        for graph in graphs:
            if graph.graph_dict.get(game.title()):
                cur_game = graph.graph_dict[game.title()]
                for game, weight in cur_game.edges.items():
                    if weight <= price_diff:
                        similar_games[game] = graph.graph_dict[game.title()].price
        if similar_games:
          print("A list of Similar games based on the given price difference:\n")
          for game, price in similar_games.items():
             print(f"{game}: {price}$\n")
             print("----------------------")
          return self.respond()
        
                    
        
    def recommend(self):
        ans = input("Want any recommendations about similar games?\n")
        while self.exiting(ans):
            ans = input("What is the maximun price difference you allow Between Game And Suggestions in dollar?\n".title())
            matched = re.match(r".*?\d+.*?", ans.lower())
            if matched:
                ans = matched.group()
                break
        return int(ans)
    
            

bot = Bot()
bot.talk()
