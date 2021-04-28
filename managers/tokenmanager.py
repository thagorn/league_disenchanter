class TokenManager:
    def __init__(self):
        self.six = [[], []]
        self.seven = [[], [], []]

    def process(self, token):
        if token["lootName"] == "CHAMPION_TOKEN_6":
            self.six[token["count"] -1].append(token)
        if token["lootName"] == "CHAMPION_TOKEN_7":
            self.seven[token["count"] -1].append(token)

    def _names(self, tokens):
        return [token["itemDesc"] for token in sorted(tokens, key=lambda x: x["itemDesc"])]

    def _print_row(self, tokens, mastery):
        if len(tokens) == 0:
            return
        count = tokens[0]["count"]
        print(f"You have {count} Champion Mastery {mastery} token{'s' if count > 1 else ''} for: {self._names(tokens)} ")

    def summarize(self):
        self._print_row(self.six[0], 6)
        self._print_row(self.six[1], 6)
        self._print_row(self.seven[0], 7)
        self._print_row(self.seven[1], 7)
        self._print_row(self.seven[2], 7)
