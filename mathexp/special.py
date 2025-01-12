from mpmath import mp

special_alias={
    "pi":"pi",
    "π":"pi",
}

def pi(mod:str="3"):
    precision=int(mod)
    mp.dps=precision
    return mp.pi