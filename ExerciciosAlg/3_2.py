def middle(self):
    if(self.isEmpty()):
        return 0
    mid = self._header.next # Pegando o header + 1
    pathern = self._trailer.prev # Pegando o trailer -1

    while(mid != pathern and mid.next != pathern):
        mid = mid.next
        pathern = pathern.prev
        # Enquanto o primeiro for diferente do ultimo e o proximo do primeiro nao for o ultimo, o primeiro
        # vai receber o proximo e o ultimo vai receber um a menos logo, o mid vai i++ e o pathern vai i--

    return mid


# O(N)