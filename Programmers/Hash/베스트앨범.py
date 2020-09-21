from collections import defaultdict

def solution(genres, plays):
    answer = []
    cnt_dict = defaultdict(int)
    songs_dict = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        cnt_dict[genre] += plays[i]
        songs_dict[genre].append((i, plays[i]))
    cnt_items = cnt_dict.items()
    cnt_items = sorted(cnt_items, key=lambda x: -x[1])
    
    for cn in cnt_items:
        songs = songs_dict[cn[0]]
        if len(songs) == 1:
            answer.append(songs[0][0])
        else:
            songs.sort(key=lambda x: (-x[1], x[0]))
            answer.append(songs[0][0])
            answer.append(songs[1][0])
    return answer

solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500])