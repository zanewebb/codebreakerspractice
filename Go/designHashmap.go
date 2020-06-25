type MyHashMap struct {
	Values []int
	R int
}


/** Initialize your data structure here. */
func Constructor() MyHashMap {
	NewHM := MyHashMap{make([]int, 1000000), 1000001} 
	for i := range NewHM.Values {
		 NewHM.Values[i] = -1
	}
	
	return NewHM
}


/** value will always be non-negative. */
func (this *MyHashMap) Put(key int, value int) {
	this.Values[this.GetHash(key)] = value
}


/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
func (this *MyHashMap) Get(key int) int {
	return this.Values[this.GetHash(key)]
}


/** Removes the mapping of the specified value key if this map contains a mapping for the key */
func (this *MyHashMap) Remove(key int) {
	this.Values[this.GetHash(key)] = -1
}

func (this *MyHashMap) GetHash(key int) int {
	return key % this.R
}