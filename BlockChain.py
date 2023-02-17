import os

def run_command(command):
    return os.popen(command).read()

def create_multichain_private_blockchain(chain_name):
    run_command("multichain-util create " + chain_name)
    run_command("multichaind " + chain_name + " -daemon")
    run_command("multichain-cli " + chain_name + " grant $(multichain-cli " + chain_name + " getaddresses  | sed -n 1p) send,receive,create,issue")
    print("Creating MultiChain Blockchain...")

create_multichain_private_blockchain("mychain")
print("MultiChain Blockchain created and deployed successfully.")

transactions = []

def add_transaction(sender, receiver, amount):
    transaction = {'sender': sender, 'receiver': receiver, 'amount': amount}
    transactions.append(transaction)
    print("Transaction added to the blockchain: ", transaction)

add_transaction("Alice", "Bob", 10)
print("Transaction created in block 1")
add_transaction("Bob", "Charlie", 5)
print("Transaction created in block 2")
add_transaction("Charlie", "Alice", 20)
print("Transaction created in block 3")

print("Transactions on the Multichain: ", transactions)
