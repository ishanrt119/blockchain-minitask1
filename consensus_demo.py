import random

# Simulate Proof-of-Work (PoW)
def simulate_pow():
    miners = {
        "MinerA": random.randint(100, 1000),
        "MinerB": random.randint(100, 1000),
        "MinerC": random.randint(100, 1000)
    }
    winner = max(miners, key=miners.get)
    print("\nPoW Simulation:")
    print(f"Miner power: {miners}")
    print(f"Selected Validator: {winner} (Highest Computational Power: {miners[winner]})")
    print("PoW selects the miner with the most computing power.\n")
    return winner

# Simulate Proof-of-Stake (PoS)
def simulate_pos():
    stakers = {
        "StakerA": random.randint(100, 1000),
        "StakerB": random.randint(100, 1000),
        "StakerC": random.randint(100, 1000)
    }
    winner = max(stakers, key=stakers.get)
    print("\nPoS Simulation:")
    print(f"Staker stakes: {stakers}")
    print(f"Selected Validator: {winner} (Highest Stake: {stakers[winner]})")
    print("PoS selects the staker with the highest stake in the network.\n")
    return winner

# Simulate Delegated Proof-of-Stake (DPoS)
def simulate_dpos():
    delegates = ["DelegateA", "DelegateB", "DelegateC"]
    votes = {
        "User1": random.choice(delegates),
        "User2": random.choice(delegates),
        "User3": random.choice(delegates)
    }

    # Tally votes
    vote_count = {d: 0 for d in delegates}
    for vote in votes.values():
        vote_count[vote] += 1

    max_votes = max(vote_count.values())
    top_candidates = [d for d, v in vote_count.items() if v == max_votes]
    winner = random.choice(top_candidates)  # Break tie randomly if needed

    print("\nDPoS Simulation:")
    print(f"Voter decisions: {votes}")
    print(f"Vote tally: {vote_count}")
    print(f"Selected Delegate: {winner} (Most Votes)")
    print("DPoS selects delegates based on community voting.\n")
    return winner

# Run all simulations
if __name__ == "__main__":
    print("=== Consensus Algorithm Comparison ===")
    pow_validator = simulate_pow()
    pos_validator = simulate_pos()
    dpos_delegate = simulate_dpos()
    print("Simulation Complete: Validators Selected via PoW, PoS, and DPoS.")
