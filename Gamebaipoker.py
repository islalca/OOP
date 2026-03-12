import random

# --- 1. LỚP CARD (Lá bài) ---
class Card:
    # Định nghĩa thứ tự sức mạnh của các lá bài để dùng cho compareTo
    RANK_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, rank, suit, faceUp=False):
        self.rank = rank     # Hạng bài: 2->10, J, Q, K, A
        self.suit = suit     # Chất: Cơ, Rô, Chuồn, Bích
        self.faceUp = faceUp # Trạng thái lật (True/False)

    def flip(self):
        self.faceUp = not self.faceUp

    def compareTo(self, other_card):
        # Trả về > 0 nếu lớn hơn, < 0 nếu nhỏ hơn, 0 nếu bằng nhau
        return self.RANK_VALUES[self.rank] - self.RANK_VALUES[other_card.rank]

    def __str__(self):
        if self.faceUp:
            return f"[{self.rank} {self.suit}]"
        return "[Úp]"


# --- 2. LỚP DECK (Bộ bài) ---
class Deck:
    def __init__(self):
        self.cards = [] # Tương đương cards[52]
        self.reset()

    def reset(self):
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♥', '♦', '♣', '♠']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit, faceUp=False))

    def shuffle(self):
        random.shuffle(self.cards)

    def topCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

    def dealTo(self, hand):
        card = self.topCard()
        if card:
            hand.addCard(card)


# --- 3. LỚP HAND (Tay bài) ---
class Hand:
    def __init__(self):
        self.cards = [] # Tương đương cards[2] trong Texas Hold'em
        self.value = 0  # Điểm số/Sức mạnh của tay bài

    def addCard(self, card):
        if len(self.cards) < 2:
            self.cards.append(card)

    def compareTo(self, other_hand):
        # Trong thực tế cần hàm đánh giá tay bài phức tạp (Cù lũ, Thùng, Sảnh...)
        # Ở đây làm mẫu so sánh dựa trên value
        return self.value - other_hand.value
        
    def show_hand(self):
        return " - ".join(str(card) for card in self.cards)


# --- 4. LỚP PLAYER (Người chơi & Kế thừa) ---
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def makeMove(self):
        pass # Sẽ được ghi đè ở lớp con

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def makeMove(self):
        print(f"Lượt của {self.name}:")
        action = input("Chọn hành động (Theo/Tố/Bỏ): ")
        return action

class ComputerPlayer(Player):
    def __init__(self, name, difficulty="Normal"):
        super().__init__(name)
        self.difficulty = difficulty

    def makeMove(self):
        # AI logic cơ bản
        actions = ["Theo", "Tố", "Bỏ"]
        action = random.choice(actions)
        print(f"Máy {self.name} (Độ khó: {self.difficulty}) chọn: {action}")
        return action


# --- 5. LỚP POKERGAME (Trò chơi chính) ---
class PokerGame:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [] # Tương đương players[2..8]
        self.round = 1
        self.currentPlayer = 0
        
        # Khởi tạo người chơi (1 Người, còn lại là Máy)
        self.players.append(HumanPlayer("Người Chơi 1"))
        for i in range(1, max(2, min(8, num_players))):
            self.players.append(ComputerPlayer(f"Bot {i}"))

    def playRound(self):
        print(f"\n=== BẮT ĐẦU VÒNG {self.round} ===")
        self.deck.reset()
        self.deck.shuffle()
        
        # Chia bài cho mỗi người chơi (2 lá)
        for _ in range(2):
            for player in self.players:
                self.deck.dealTo(player.hand)
                
        # Lật bài lên để test hiển thị
        for player in self.players:
            for card in player.hand.cards:
                card.flip()
            print(f"{player.name} đang cầm: {player.hand.show_hand()}")

        # Lượt của người chơi đầu tiên
        self.currentPlayer = 0
        self.players[self.currentPlayer].makeMove()
        
        self.round += 1

# --- TEST CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    print("Khởi tạo Game Poker với 3 người chơi (1 Người, 2 Máy)...")
    game = PokerGame(num_players=3)
    game.playRound()