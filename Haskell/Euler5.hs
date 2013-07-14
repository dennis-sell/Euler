import Data.Digits

largest_5_digit_product :: Integer -> Integer
largest_5_digit_product n = take_max_5 . digits 10 $ n
  where 
    take_max_5 (a:b:c:d:e:tl) = max (a * b * c * d * e) (take_max_5 (b:c:d:e:tl))
    take_max_5 _ = 0
