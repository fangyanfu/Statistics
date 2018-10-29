# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:26:42 2018

@author: yanfu
"""
"""
Discrete distribution 
- Binomial distribution: To measure probility of X success in N "Binomial events"
    Pn(x) = Cn(x) * P(s) ^ x * (1-P(s)) ^ (n-x)
    probility of X success events in N outcomes
    Cn(x) combination! choose x from n, how many?
    P(s) possibility of success
    E(X) = n*P(s)
    Var(X) = n * P(s) * (1-P(s))
    
    
- Poisson distribution: To measure probability of sth in a period/time
    Pn(x) = [u^x * e^(-u)]/x!
    u represents E(period), average times of happen in a period/time, u is also the variance
    e = 2.71828
    x represents how many times you want to know happen in a period/time
    
- Hypergeometric distribution: 
    like binomial, 2 things different(trials not independent, P(s)diff from trial to trial)
    Pn(x) = [ Cr(x) * CN-r(n-x) ] / CN(n)
    Cr(x), to choose x from total success cases r
    CN-r(n-x), to choose n - x unsuccess from total unsuccess cases N-r
    CN(n) to choose n from total N cases
    E(x) = n * (r/N)
    Var = n * (r/N) * (1 - r/N) * (N-n/N-1)
"""