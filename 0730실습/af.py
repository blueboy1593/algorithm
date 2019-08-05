test_num = int(input())
for t in range(test_num):
   K, N, M = map(int, input().split())
   m_list = list(map(int, input().split()))
   cnt = -1
   difference_list= []
   difference_list.append(m_list[0])
   for i in range(M-1):
       difference_list.append(abs(m_list[i] - m_list[i+1]))
   difference_list.append(0)
   difference_list.append(0)
   # print(m_list)
   # print('K =' + str(K))
   # print(difference_list)            # 테스트용
   for difference in difference_list:
      if difference > K:
          cnt = 0
   result_list = []
   su = 0
   bus = 0
   if cnt == -1:
       cnt = 0
       while bus < N:
           for i in range(cnt, len(difference_list)):
               su += difference_list[i]
               if N - bus <= K :
                   bus = N
                   break
               elif su + difference_list[i+1] > K:
                   break
           # print('su는' + str(su))
           if bus == N:
               break
           else:
               cnt += 1
               bus += su
               su = 0
           # print('cnt=' + str(cnt))
           # print('bus=' + str(bus))
   print('#' + str(t + 1) + ' ', end='')
   print(str(cnt))