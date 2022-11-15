{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import GHC.Float (Floating(expm1))
data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval1 :: Expr -> Int
eval1 (Val ex) = ex
eval1 (Add ex1 ex2) = eval1 ex1 + eval1 ex2
eval1 (Sub ex1 ex2) = eval1 ex1 - eval1 ex2
eval1 (Mul ex1 ex2) = eval1 ex1 * eval1 ex2
eval1 (Div ex1 ex2) = div (eval1 ex1) (eval1 ex2)

eval2 :: Expr -> Maybe Int
eval2 (Val ex) = Just ex
eval2 (Add ex1 ex2) =
    eval2 ex1 >>= \a ->
    eval2 ex2 >>= \b ->
    return (a + b)
eval2 (Sub ex1 ex2) =
    eval2 ex1 >>= \a ->
    eval2 ex2 >>= \b ->
    return (a - b)
eval2 (Mul ex1 ex2) =
    eval2 ex1 >>= \a ->
    eval2 ex2 >>= \b ->
    return (a * b)
eval2 (Div ex1 ex2) =
    eval2 ex1 >>= \a ->
    eval2 ex2 >>= \b ->
    if b == 0 then Nothing
    else return (div a b)

eval3 :: Expr -> Either String Int
eval3 (Val ex) = Right ex
eval3 (Add ex1 ex2) =
    eval3 ex1 >>= \a ->
    eval3 ex2 >>= \b ->
    return (a + b)
eval3 (Sub ex1 ex2) =
    eval3 ex1 >>= \a ->
    eval3 ex2 >>= \b ->
    return (a - b)
eval3 (Mul ex1 ex2) =
    eval3 ex1 >>= \a ->
    eval3 ex2 >>= \b ->
    return (a * b)
eval3 (Div ex1 ex2) =
    eval3 ex1 >>= \a ->
    eval3 ex2 >>= \b ->
    if b == 0 then Left "div0"
    else return (div a b)