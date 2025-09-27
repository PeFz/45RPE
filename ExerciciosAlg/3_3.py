def concatenador(L, M):

    FinalDeL = L._trailer.prev
    ComecoDeM = M._header.next


    FinalDeL.next = ComecoDeM
    ComecoDeM.prev = FinalDeL

    L._trailer = M._trailer

    return L
