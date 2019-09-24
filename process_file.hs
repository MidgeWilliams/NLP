import Data.List
import System.IO

punct = ".,;?!"

placeToSplit :: [Char] -> [Int]
placeToSplit ls = [y | x <- punct, y <- x `elemIndices` ls]

pwords :: [Char] -> [[Char]]
pwords ls = checkPunct (words ls)

pwords :: [Char] -> [[Char]]
checkPunct ls = [x | y <- ls, x <- splitPunct y]

splitPunct :: [Char] -> [[Char]]
splitPunct y | null (placeToSplit y) = [y]
             | otherwise = fst (splitAt (head placeToSplit y) y) : [head (snd (splitAt (head placeToSplit y) y)) : tail (snd (splitAt (head placeToSplit y) y))]

main = do
  fileAsk <- putStrLn "File name please"
  fileName <- getLine
  contents <- readFile fileName
  pwords contents
