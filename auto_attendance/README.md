### check_test.py

개발 만료된 테스트용이다.

### leave_work.py

전체화면일때는 이미지를 잘 찾아내지만, 화면이 하프모드이거나 반응형으로 작아지면 이미지 소싱이 불가능하므로 현재는 전체화면으로 진행을 해야한다.

- 반복문 코드 리팩토링 진행 해야함

### gui_test.py

GUI모드로 진행을 시작.

- 인풋박스 2개를 이미지 파일을 불러오는 용도로 만들어 데이터를 받고, 이미지를 찾는다. 2개중에 이미지가 일치하지 않을경우 콘솔에 에러를 발생하며, 디버그를 중지시킨다.
- 이미지를 넣으면 썸네일용으로 이미지를 보여주게 해준다.
- 언제부터 시작할껀지 타임아웃 가능한 인풋박스 만들기.
- 시작버튼 생성

start {
first_thumbnail: "image1.png",
second_thumbnail: "image2.png",
timer: "00:00",
}

#### installing

```
 pip install opencv-python image pyautogui datetime
```

#### Times

```
60 1m
120 2m
180 3m
240 4m
300 5m
600 10m
1200 20m
1800 30m
2400 40m
2460 41m << Success
3600 1h << Success
```
