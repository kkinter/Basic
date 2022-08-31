## FLEX BOX

### flex-direction

`row` | 초기값

`row-reverse`

`column`

`column-reverse`

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-15-57-39-image.png)



### flex-wrap

`nowrap`  | 초기값

```css
.container {
  display: flex;
  flex-wrap: wrap;
}
```

- flex-wrap 을 wrap 으로 해주면, 오버플로우가 발생하지 않고, 플렉스 라인이 생성.



### flex-flow

```css
.container {
  display: flex;
  flex-flow: column wrap;
}
```

- `flex-grow: 0`: 아이템이 확대되지 않습니다.
- `flex-shrink: 1`: 항목이 `flex-basis`보다 작게 축소될 수 있습니다.
- `flex-basis: auto`: 항목의 기본 크기는 `auto`입니다.



### justify-content

```css
.container {
  display: flex;
  justify-content: flex-end;
}
```

| 값               | 정렬                                                                               |
| --------------- | -------------------------------------------------------------------------------- |
| `flex-start`    | ![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-16-10-56-image.png) |
| `flex-end`      | ![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-16-11-28-image.png) |
| `center`        | ![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-16-11-58-image.png) |
| `space-around`  | ![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-16-12-08-image.png) |
| `space-between` | ![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-31-16-12-31-image.png) |

- 컨테이너에 여유 공간이 없으면, 아무런 변화가 없음.

#### `flex-direction` 을 column으로 설정하면, 동일하게 작동




