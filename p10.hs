fibs :: [Int]
fibs = 1 : (1 : zipWith (+) fibs (tail fibs))

nat :: [Int]
nat = 1 : (map (+1) nat)

get :: Int
get = sum [fib |(cnt, fib) <- zip nat fibs, cnt `mod` 3 == 0, fib < 4000000]