def findfavGenre(userSongs, songGenres):
    songToGenre = {} #song:genre
    favGenre = {} #user:genre1,genre2
    genres = {} #genre:count
    for k,v  in songGenres.items():
        if not v or len(v)<1:
            continue
        for s in v:
            if s:
                genres[k] = 0
                songToGenre[s]=k

    print(songToGenre, genres)
    for u,v in userSongs.items():
        favGenre[u]=[]
        maxVal = 0
        if not v or len(v)<1:
            continue
        for s in v:
            try:
                genres[songToGenre[s]] += 1
                maxVal = max(maxVal, genres[songToGenre[s]])
            except:
                pass
        print(genres)
        for g,v in genres.items():
            if v==maxVal:
                favGenre[u].append(g)
            genres[g]=0
    print(favGenre)
