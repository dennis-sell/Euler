module Euler41 where

import Data.Digits
import Data.Maybe
import Data.List

permutation [] = [[]]
permutation xs = [y| x <- xs, y <- map (x:) $ permutation $ delete x xs]

allPandigitalNumbers :: Integer -> [Integer]
allPandigitalNumbers n = reverse . sort . map (unDigits 10) . permutation $ [1..n]

isPrime :: Integer -> Bool
isPrime n = loop n 2 (floor . sqrt . fromIntegral $ n)
  where
    loop n check limit  | check > limit        =  True
                        | mod n check == 0      =  False
                        | otherwise             =  loop n (check + 1) limit

largestPandigitalPrime :: Integer
largestPandigitalPrime = loop 9
  where
    loop 1 = 1
    loop n = case find isPrime (allPandigitalNumbers n) of
                Just x -> x
                Nothing -> loop (n - 1)
