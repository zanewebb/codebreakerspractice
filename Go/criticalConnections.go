func criticalConnections(n int, connections [][]int) [][]int {
	// Ans slice
	var ans [][]int
	
	// Levels slice
	levels := make([]int, n)
	for i, _ := range levels {
		 levels[i] = -1
	}
	
	// Need to make a node adjacency slice
	// map with keys of ints that goes to slices of ints
	nodes := make(map[int][]int) 
	
	for _, c := range connections {
		 nodes[c[0]] = append(nodes[c[0]], c[1])
		 nodes[c[1]] = append(nodes[c[1]], c[0])
	}    
	
	DFS(connections[0][0], -1, 0, levels, &ans, nodes)
	return ans
}

func DFS(current , parent, level int, levels []int, ans *[][]int, nodes map[int][]int) {    
	levels[current] = level
	
	for _, n := range nodes[current] {
		 if n != parent {
			  if levels[n] == -1 {
					// If we havent visited, continue diving
					DFS(n, current, level + 1, levels, ans, nodes)
					levels[current] = min(levels[n], levels[current])
			  } else {
					
					// Otherwise see if the node we found has a smaller value than ours
					levels[current] = min(levels[n], levels[current])
			  }
		 }
	}
	
	if levels[current] == level && parent != -1{
		 *ans = append(*ans, []int {current, parent})
	}    
}

func min(a int, b int) (int) {
	if a < b {
		 return a
	} else{
		 return b
	}
}