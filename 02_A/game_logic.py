import random

class HangmanGame:
    def __init__(self, word_list=None, common_clue=None):
        self.common_clue = common_clue
        
        # word_list from user is now just a list of strings
        if word_list:
             # Validate and filter
            self.word_list = []
            for item in word_list:
                # Handle if it was passed as dict (legacy support) or string
                val = ""
                if isinstance(item, dict):
                     val = item.get("word", "")
                elif isinstance(item, str):
                     val = item
                
                if val.strip():
                    # For user words, we use the common_clue
                    self.word_list.append({
                        "word": val.strip().upper(),
                        "clue": self.common_clue if self.common_clue else ""
                    })
            self.word_list = self.word_list[:7]
        else:
            self.word_list = []
            
        # Fallback
        if not self.word_list:
            # If falling back to default, we ignore the user's common_clue (likely empty anyway)
            # and use our specific clues.
            self.word_list = [
                {"word": "PYTHON", "clue": "A popular snake-named language"},
                {"word": "DEVELOPER", "clue": "Someone who writes code"},
                {"word": "HANGMAN", "clue": "The name of this game"},
                {"word": "AGENTS", "clue": "AI helpers"},
                {"word": "INTERFACE", "clue": "Where user meets system"},
                {"word": "VARIABLE", "clue": "A storage for data"},
                {"word": "FUNCTION", "clue": "A block of reusable code"}
            ]
            
        self.reset_game()

    def reset_game(self):
        selection = random.choice(self.word_list)
        self.word = selection["word"]
        self.clue = selection["clue"]
        self.guesses = set()
        self.max_errors = 6
        self.errors = 0
        self.won = False
        self.lost = False

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.guesses or self.finished:
            return False
        
        self.guesses.add(letter)
        
        if letter not in self.word:
            self.errors += 1
            if self.errors >= self.max_errors:
                self.lost = True
        else:
            if all(char in self.guesses for char in self.word):
                self.won = True
        return True

    @property
    def current_state(self):
        # We define what characters are "guessable" (same as in GUI keyboard)
        # Anything else (like tabs, or weird symbols) should be auto-revealed
        guessable = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !?,.-'\"@#()&*+/[]"
        return "".join([char if char in self.guesses or char not in guessable else "_" for char in self.word])

    @property
    def finished(self):
        return self.won or self.lost
