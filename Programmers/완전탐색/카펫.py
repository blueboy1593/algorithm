def solution(brown, yellow):
    answer = []
    area = brown + yellow
    # 연립방정식을 구현할 수 있으면 좋겠지만, 생각이 나지 않으니 yellow 면적을 기준으로 시도해보자.
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i
            if area == (i + 2) * (j + 2):
                answer = [j + 2, i + 2]
                break
    return answer