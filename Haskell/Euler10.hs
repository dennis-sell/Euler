import Euler41

{- Given n, finds all the odd primes up to 2n + 2 -}
sieveSundaram :: Integer -> [Integer]
sieveSundaram n = map (\ x -> 2 * x + 1) (filter (\x -> not (elem x nums)) [1..n])
    where
        nums = map (\ (i,j) -> i + j + 2*i*j) . 
                filter (\ (x,y) -> x <= y) $ [(x,y) | x <- [1..n], y <- [1..n]]
-- Inefficient with memory.

-- Solution : Sum of primes below 2 million
sumOfPrimes :: Integer
sumOfPrimes = sum . sieveSundaram $ 999999

sumOfPrimes2 = sum . filter isPrime . reverse $ [1..2000000]

