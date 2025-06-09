import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block {self.index}:\n" \
               f"Timestamp: {self.timestamp}\n" \
               f"Data: {self.data}\n" \
               f"Previous Hash: {self.previous_hash}\n" \
               f"Hash: {self.hash}\n"


blockchain = []# Create the genesis block
block0 = Block(0, time.time(), "Genesis Block", "0")
blockchain.append(block0)

# Block 1
block1 = Block(1, time.time(), "Block 1 Data", block0.hash)
blockchain.append(block1)

# Block 2
block2 = Block(2, time.time(), "Block 2 Data", block1.hash)
blockchain.append(block2)

# Print the blockchain
print("Blockchain:")
for block in blockchain:
    print(block)

#alter block1
blockchain[1].data = "New data"
blockchain[1].hash = blockchain[1].compute_hash()

# Print blockchain after alteration
print("Blockchain After Alteration:")
for block in blockchain:
    print(block)

# Check if chain is still valid
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i-1]
        if current.hash != current.compute_hash():
            print(f"Block {i} hash is invalid.")
            return False
        if current.previous_hash != previous.hash:
            print(f"Block {i} has incorrect previous hash.")
            return False
    return True

# Validate blockchain
print("Is Blockchain Valid?", is_chain_valid(blockchain))

#expected output
#block1 data is altered
#block2 prev hash is invalid