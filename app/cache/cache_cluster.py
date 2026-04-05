from app.cache.cache_node import CacheNode
import hashlib

class CacheCluster:
    def __init__(self,num_nodes=3,replicas=3):
        self.ring={}
        self.sorted_keys=[]
        self.replicas=replicas

        for i in range(num_nodes):
            node=CacheNode()
            for j in range(replicas):
                virtual_node_key= f"node-{i}-replica-{j}"
                hash_key=self._hash(virtual_node_key)
                self.ring[hash_key]=node
                self.sorted_rings.append(hash_key)
        
        self.sorted_keys.sort()

    def _hash(self,key):
        return int(hashlib.md5(key.encode()).hexdigest(),16)

    def _get_node(self,key):
        hash_key=self._hash(key)
        
        for node_hash in self.sorted_keys:
            if hash_key<=node_hash:
                return self.ring[node_hash]
        
        return self.ring[self.sorted_keys[0]]
    
    def set(self,key,value,ttl=None):
        node= self._get_node(key)
        node.set(key,value,ttl)
    
    def get(self,key):
        node=self._get_node(key)
        return node.get(key)
    
    def delete(self,key):
        node=self._get_node(key)
        node.delete(key)