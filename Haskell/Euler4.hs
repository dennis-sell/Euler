import Data.Digits
import Data.List

products :: [Integer]
products = [x * y | x <- [100..999], y <- [100..999]]

largestPalindrome :: Maybe Integer
largestPalindrome = find isPalindrome orderedProducts
  where
    orderedProducts = reverse. sort $ products

isPalindrome :: Integer -> Bool
isPalindrome n = digitList == (reverse digitList)
  where
    digitList = digits 10 n
