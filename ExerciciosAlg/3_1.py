def size(self):
    count = -1
    walk = self._header

    while walk != self._trailer:
        count += 1
        walk = walk._next

    return count

#vai de o(1), para o(n), de constante para linear