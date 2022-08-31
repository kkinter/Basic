# Media embedding

## HTML의 이미지

```html
<img src="test.jpg">

<img src="imgs/test.jpg">

<img src="https://www.example.com/images/dinosaur.jpg">
```

## Alternative text

```html
<img src="test.jpg"
     alt="The head and torso of a dinosaur skeleton;
          it has a large head with long sharp teeth">
```

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-29-14-57-26-image.png)

alt 속성의 유용성

- 사용자가 시각적인 장애를 가지고 있는 경우, 내용을 읽어 줄 수 있음.

- 텍스트만 지원되는 브라우저를 사용하는 경우도 있음.

- 텍스트를 제공하여 검색엔진이 이를 활용할 수 있도록 도와줌.

## Width and height and Img titles

```html
<img src="test.jpg"
     alt="The head and torso of a dinosaur skeleton;
          it has a large head with long sharp teeth"
     width="400"
     height="341"
     title="test">
```

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-08-29-15-00-22-image.png)

**이미지 크기를 변경해야 한다면  CSS를 사용하도록 하자.**


