import datetime as _dt
import hashlib as _hashlib
import json as _json

class Blockchain:

    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block(
            data="Start Genesis Block", proof=1, previous_hash="0", index=1
        )
        self.chain.append(genesis_block)

    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        proof = self.proof_of_work(previous_proof, index, data)
        new_block = self._create_block(data, proof, previous_block["hash"], index)

    # add the new block to the chain
        self.chain.append(new_block)

        return new_block  # return the new block

    def _to_digest(elf, new_proof: int, previous_proof: int, index: str, data: str) -> bytes:
        to_digest = str(new_proof ** 2 - previous_proof ** 2 + index) + data
        return to_digest.encode()

    def proof_of_work(self, previous_proof: str, index: int, data: str) -> int: 
        new_proof = 1
        check_proof = False

        while not check_proof:
            print(new_proof)
            to_digest = self._to_digest(
                new_proof=new_proof, 
                previous_proof=previous_proof, 
                index=index, 
                data=data
            )
        
            hash_value = _hashlib.sha256(to_digest).hexdigest()

            if hash_value[:6] == "000000":
                check_proof = True
            else: 
                new_proof += 1
        return new_proof

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _create_block(
        self, data: str, proof: int, previous_hash: str, index: int
        ) -> dict:
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "proof": proof,
            "previous_hash": previous_hash,
            "data": data,  # add the missing data key-value pair
        }
        return block  # return the block dictionary