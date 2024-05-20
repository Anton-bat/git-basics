
def rec_reverse(w):
    if len(w) == 0:
        return ""
    else:
        return w[-1] + rec_reverse(w[:-1])

res = rec_reverse("hello")
print(res)
