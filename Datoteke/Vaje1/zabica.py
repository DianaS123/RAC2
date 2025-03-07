from functools import lru_cache

def zabica(mocvara):
    n = len(mocvara)
    @lru_cache(maxsize=None)
    def pomozna(i, e):
        """
            Žabica na i-tem lokvanju z trenutno energijo e.
        """
        if i+e >= n:
            # žabica je izven jezera
            return 0
        else:
            # energija se poveča za toliko, kolikor poje muh na novem lokvanju
            nova_energija = e + mocvara[i]
            return 1 + min(pomozna(i+k, nova_energija - k) for k in range(1, nova_energija + 1))
    # žabica začne na prvem lokvanju z energijo 0
    return pomozna(0, 0)


# testni podatki za funkcijo
mocvara1 = []
mocvara2 = [2, 4, 1, 2, 1, 3, 1, 1, 5]
mocvara3 = [4, 1, 8, 2, 11, 1, 1, 1, 1, 1]

print(zabica(mocvara1))  # 0
print(zabica(mocvara2))  # 3
print(zabica(mocvara3))  # 2

