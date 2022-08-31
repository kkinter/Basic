## Grid

### 정말 일반적인 레이아웃

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-16-17-09-image.png)

### 그리드 용어

### 

| 그리드 라인 | <img title="" src="file:///C:/Users/Wook/AppData/Roaming/marktext/images/2022-08-31-16-19-01-image.png" alt="" width="344"> | 그리드에 네 개의 열이 있는 경우, 마지막 열 다음을 포함하여 5개의 라인 |
| ------ | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| 그리드 트랙 | <img title="" src="file:///C:/Users/Wook/AppData/Roaming/marktext/images/2022-08-31-16-19-15-image.png" alt="" width="331"> |                                           |
| 그리드 셀  | <img title="" src="file:///C:/Users/Wook/AppData/Roaming/marktext/images/2022-08-31-16-19-27-image.png" alt="" width="330"> | 행 트랙과, 열 트랙의 교차점으로, 그리드의 가장 작은 공간         |
| 그리드 영역 | <img src="file:///C:/Users/Wook/AppData/Roaming/marktext/images/2022-08-31-16-19-36-image.png" title="" alt="" width="324"> |                                           |
| 그리드 갭  | <img title="" src="file:///C:/Users/Wook/AppData/Roaming/marktext/images/2022-08-31-16-19-47-image.png" alt="" width="304"> |                                           |

### 그리드 컨테이너

```css
.container {
  display: grid;
}
```

### 그리드 항목

```html
<div class="container">
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
</div>
```

### 행과 열

3개의 열 트랙, 2개의 행 트랙 및 트랙 사이에 10 픽셀 갭으로 구성된 그리드.

```css
.container {
    display: grid;
    grid-template-columns: 5em 100px 30%;
    grid-template-rows: 200px auto;
    gap: 10px;
}
```

### fr 단위

동일한 세 개의 열을 가지려면 아래와 같아야 함.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
```

- `fr` 단위는 flexbox에서 `flex: auto`를 사용하는 것과 유사한 방식으로 작동.

- 항목이 배치된 후에 공간을 분배.


