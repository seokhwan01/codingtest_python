sensor_num = int(input())
station_num = int(input())
sensor_list = list(map(int,input().split()))
sensor_list.sort()
#print(f"정렬된 센서 리스트 : {sensor_list}")
##해결 방법
## 센서를 정렬 시키고 옆 좌표와 차이를 distance_list에 저장
#거리 차이가 가장 큰 차이 station_num-1개 만큼 삭제
#나머지 거리 차이를 더 해줌
#1 3 6 6 7 9의 차이 리스트 : [2,3,0,1,2] -> 정렬: [3,2,2,1,0] 
#최대 값 부터 k-1개 0으로 변경 [0,2,2,1,0] 

if station_num>=sensor_num: #기지국 갯수가 센서 갯수보다 많으면 인덱스에서 에러 발생
    print(0)

else:
    distance_list=[]
    
    for  i in range(len(sensor_list)-1):
        distance_list.append(sensor_list[i+1]-sensor_list[i])
    distance_list.sort(reverse=True)

    #print(f"정렬된 거리 차이 리스트 : {distance_list}")
    for i in range(station_num-1):
        distance_list[i]=0
    #print(f"기지국 거리 합 리스트 : {distance_list}")
    print(sum(distance_list))