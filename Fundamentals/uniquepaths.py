def navigate(curX: int, curY: int, finishX: int, finishY: int) -> int:
      print("evaluating: " + str(curX) + ", " + str(curY))
      #found the solution
      if curX == finishX-1 and curY == finishY-1 :
         return 1
      # overshot your bounds
      elif curX == finishX or curY == finishY:
         return 0
      #continue searching
      
      else:
         return navigate(curX + 1, curY, finishX, finishY) + navigate(curX , curY + 1, finishX, finishY)

if __name__ == "__main__":
   print(navigate(0, 0, 23, 12))


   # elif curX + 1 == finishX:
   #       return navigate(curX, curY + 1, finishX, finishY)
   #    elif curY + 1 == finishY:
   #       return navigate(curX + 1, curY, finishX, finishY)
   # elif curX == finishX-1:
   #          return navigate(curX , curY + 1, finishX, finishY)
   #      elif curY == finishY-1:
   #          return navigate(curX + 1, curY, finishX, finishY)


#    def uniquePaths(self, m: int, n: int) -> int:
#         # initial position is 0, 0
#         return navigate(0, 0, m, n)
    
# def navigate(curX: int ,curY: int, finishX: int, finishY: int ) -> int:
#         #found the solution
#         if curX == finishX-1 and curY == finishY-1 :
#             return 1
#         # overshot your bounds
#         elif curX >= finishX or curY >= finishY:
#             return 0
#         #continue searching
#         elif curX == finishX-1:
#             return navigate(curX , curY + 1, finishX, finishY)
#         elif curY == finishY-1:
#             return navigate(curX + 1, curY, finishX, finishY)
#         else:
#             return navigate(curX + 1, curY, finishX, finishY) + navigate(curX , curY + 1, finishX, finishY)
        