## layout

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-15-37-08-image.png)

`인라인`  | 문장의 단어처럼 작동, `<span>` 이 일반적으로 사용되며, 공백이 유지됨.

`블록`      **|** 나란히 배치되지 않음.  



### flex

```css
.my-element {
	display: flex;
}
```

- 자식을 인라인처럼 나란히 정렬하고, 블록 방향으로 높이를 높힘.

- 동일한 축에 유지되며, 공간이 부족할 때, 줄 바꿈 X

- 대신 서로 같은 라인에 스쿼시 시도 > `align-items`, `justify-content`, `flex-wrap`

- 자식 요소를 플렉스 항목으로 변환. 

### Grid

```css
.my-element {
	display: grid;
}
```

- 플렉스와 여러 면에서 유사, 다축 레이아웃을 제어하도록 설계

```css
.my-element {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
}
```

<img src="file:///C:/Users/Wook/AppData/Roaming/marktext/images/2022-08-31-15-48-27-image.png" title="" alt="" width="647">

```css
.my-element :first-child {
  grid-row: 1/3;
  grid-column: 1/4;
}

.my-element {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
  max-width: 500px;
}
```

<img src="file:///C:/Users/Wook/AppData/Roaming/marktext/images/2022-08-31-15-50-29-image.png" title="" alt="" width="663">
