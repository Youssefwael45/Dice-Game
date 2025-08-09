import random

def roll():
    return random.randint(1, 6)

def get_players():
    while True:
        try:
            players = int(input("🎲 Number of players (2-4) => "))
            if 2 <= players <= 4:
                return players
            else:
                print("❌ Number should be between 2 and 4.")
        except ValueError:
            print("❌ Please enter a valid number.")

def get_player_names(num_players):
    names = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1} => ").strip()
        if not name:  # If empty, assign a default name
            name = f"Player{i+1}"
        names.append(name)
    return names

def show_instructions():
    print("\n📜 GAME INSTRUCTIONS 📜")
    print("1. Each player takes turns rolling a dice.")
    print("2. You can roll as many times as you want in your turn.")
    print("3. If you roll a 1, your turn ends immediately and you score 0 for that round.")
    print("4. You can choose to stop rolling at any time to keep your points.")
    print("5. First player to reach 50 points wins!")
    print("🎯 Strategy: Know when to stop rolling to keep your points safe!\n")

def play_game():
    num_players = get_players()
    player_names = get_player_names(num_players)

    show_instructions()
    
    max_score = 50
    player_scores = [0 for _ in range(num_players)]

    while max(player_scores) < max_score:
        for player_index in range(num_players):
            print(f"\n--- {player_names[player_index]}'s turn ---")
            current_score = 0
            
            while True:
                should_roll = input("Roll the dice? (y to roll, any other key to stop) => ").lower()
                if should_roll != "y":
                    break

                value = roll()
                print(f"🎲 You rolled a: {value}")
                
                if value == 1:
                    print("🎯 You rolled a 1! Turn over, no points this round.")
                    current_score = 0
                    break  # Ends the turn immediately
                else:
                    current_score += value
                    print(f"🔹 Current turn score: {current_score}")

            player_scores[player_index] += current_score
            print(f"🏆 Total score for {player_names[player_index]}: {player_scores[player_index]}")

            if player_scores[player_index] >= max_score:
                break  # Stop if someone wins

    winner_score = max(player_scores)
    winner_index = player_scores.index(winner_score)

    print("\n🎉 GAME OVER 🎉")
    print(f"🏆 {player_names[winner_index]} wins with {winner_score} points! 🏆")
    print("\n📊 Final Scores:")
    for name, score in zip(player_names, player_scores):
        print(f"{name} => {score}")

while True:
    play_game()
    replay = input("\n🔄 Do you want to play again? (y/n) => ").lower()
    if replay != "y":
        print("👋 Thanks for playing! Goodbye.")
        break
