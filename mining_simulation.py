import hashlib
import time

class Block:
    def __init__(self, index, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = ''
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        print(f"\nMining Block {self.index} with difficulty {difficulty}...")

        start_time = time.time()
        attempts = 0

        while True:
            self.hash = self.compute_hash()
            attempts += 1
            if self.hash.startswith(prefix):
                break
            self.nonce += 1

        end_time = time.time()
        print(f"Block {self.index} mined!")
        print(f"Nonce Attempts: {attempts}")
        print(f"Time Taken: {end_time - start_time:.4f} seconds")
        print(f"Final Hash: {self.hash}")


if __name__ == "__main__":
    difficulty = 1  
    block = Block(1, "This is a proof-of-work demo block.")
    block.mine_block(difficulty)

