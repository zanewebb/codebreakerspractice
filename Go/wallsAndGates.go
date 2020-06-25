func wallsAndGates(rooms [][]int)  {
	var gates [][]int
	
	for r := 0; r< len(rooms); r++{
		 for c := 0; c < len(rooms[0]); c++{
			  if rooms[r][c] == 0{
					gates = append(gates, []int {r,c})
			  }
		 }
	}
	
	// printSlice(gates)
	
	
	// step outwards from the gates
	var dirs = [...][2]int {{0,1}, {0,-1}, {1,0}, {-1,0}}

	for len(gates) > 0 {
		 
		 // Pop the front of the slice
		 popped := gates[0]
		 gates = gates[1:]
		 
		 // fmt.Printf("Popped: [%v,%v]\n", popped[0], popped[1])

		 for _, dir := range dirs {
			  newr := popped[0] + dir[0]
			  newc := popped[1] + dir[1]
			  // fmt.Printf("checking pos: [%v,%v]\n", newr, newc)
			  
			  if newr < len(rooms) && newr >= 0 && newc < len(rooms[0]) && newc >= 0 && rooms[newr][newc] == 2147483647{
					// fmt.Printf("confirmed pos: [%v,%v]\n", newr, newc)
					rooms[newr][newc] = rooms[popped[0]][popped[1]] + 1
					gates = append(gates, []int {newr, newc})
			  }
		 }
		 
		 // printSlice(gates)
		 // fmt.Printf("-----------------\n")
	}
	
}

func printSlice(gates [][]int){
	// Double checking the vals added
	for _, g := range gates {
		 fmt.Printf("%v, %v \n", g[0], g[1])
	}
}