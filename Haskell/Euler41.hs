import Data.Digits
import Data.List

permutation [] = [[]]
permutation xs = [y| x <- xs, y <- map (x:) $ permutation $ delete x xs]

all_pandigital_numbers = reverse . sort . map (unDigits 10) . permutation . digits 10 $ 123456789
