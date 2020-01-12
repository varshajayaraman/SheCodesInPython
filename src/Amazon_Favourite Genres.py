def findfavGenre(userSongs, songGenres):
    songToGenre = {}
    favGenre = {}
    genres = {}
    for k,v  in songGenres:
        genres[k]=0
        for s in v:
            songToGenre[s]=k

    for u,v in userSongs:
        genres[u]=[]
        maxVal = 0
        for s in v:
            genres[songToGenre[s]] += 1
            maxVal = max(maxVal, genres[songToGenre[s]])
        for g,v in genres:
            if v==maxVal:
                favGenre[u].append(g)
    print(favGenre)
