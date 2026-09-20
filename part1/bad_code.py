

def chk(l):
    """استخراج أسماء المستخدمين الخاملين لأكثر من 30 يوماً."""
    res = []
    for x in l:
        if(x[2] * 86400) > 2592000:
            res.append(x[0])
    return res

u = [
    ["Ahmed", "ahmed@email.com", 35],
    ["Sara", "sara@email.com", 10],
    ["Mona", "mona@email.com", 40]
]

print(chk(u))


