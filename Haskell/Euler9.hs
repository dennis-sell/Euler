import Data.List

-- The python implementation is much quicker.
pythagoreanTriple1000 :: Maybe Integer
pythagoreanTriple1000 = fmap product_tuple . find adds_to_1000 $ possible_triples
  where
    product_tuple (a,b,c) = a * b * c
    adds_to_1000 (a, b, c) = (a^2 + b^2 == c^2) 
    possible_triples = [(x,y,z) | x <- [1..1000], y <- [1..1000], z <- [1..1000], x + y + z == 1000, x <= y, y <= z]
