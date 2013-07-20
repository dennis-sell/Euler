import Euler41

answer = loop 10001 2
  where
    loop count current  | count == 0        = current - 1
                        | isPrime current   = loop (count - 1) (current + 1)
                        | otherwise         = loop count (current + 1)
