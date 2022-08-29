## HTML 시작하기

`<P>` | 문단

`<em>` | 이탤릭체

```html
<p>My cat is very grumpy</p>
```

1. `<p>` 여는 태그

2. `</p>` 닫는 태그

3. `My cat is ` 내용(Content)

4. (1, 2, 3) 통틀어 요소(Element)

#### 포함(내포:內包)된 요소(Nesting elements)

```html
<p>My cat is <strong>very</strong> grumpy.</p>
```

#### 블럭 레벨 요소 vs 인라인 요소(Block versus inline elements)`

```html
<em>first</em><em>second</em><em>third</em>

<p>fourth</p><p>fifth</p><p>sixth</p>
```

```
firstsecondthird < em은 인라인 요소

fourth < p는 블록 레벨 요소 

fifth

sixth
```

1. 인라인 요소는 항상 블록 레벨 요소 안에 포함

#### 빈 요소(Empty elements)

```html
<img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png">
```

1. 모든 요소가 여는 태그, 내용, 닫는 태그 패턴을 따르진 않음

2. img 태그가 그런 경우

#### 속성(Attributes)

```html
<p class="editor-note">My cat is very grumpy</p>
```

1. 요소에 실제론 나타나진 않지만, 추가적인 내용을 담고 싶을 때 사용

2. 위의 코드는 나중에 스타일에 관련된 내용을 위해 class 속성을 부여

##### 실습: 요소에 속성 추가하기

```html
<p>A link to my <a href="https://www.naver.com/" title="Naver" target="_blank"> favorite website.</a></p>
```

1.  a 태그로 favorite website.  를 감싼 후

2.  a 태그에 href 속성, title 속성, target 속성을 추가

`<a href="" title="" target="">`

#### 참과 거짓 속성(Boolean attributes)

```html
<input type="text" disabled>

<input type="text">
```

1. 불 속성, 일반적으로 이름과 동일한 하나의 값만을 가질 수 있음.

2. disabled 속성을 양식 입력 요소에 할당하면, 비활성화가 됨.

#### HTML 문서의 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```

#### Entity references: HTML에 특수 문자 포함

| Literal character | Character reference equivalent |
| ----------------- |:------------------------------:|
| <                 | <                              |
| >                 | >                              |
| "                 | "                              |
| '                 | '                              |
| &                 | &                              |

```html
<p>In HTML, you define a paragraph using the <p> element.</p>

<p>In HTML, you define a paragraph using the &lt;p&gt; element.</p>
```

#### HTML 주석

```html
<p>I'm not inside a comment</p>

<!-- <p>I am!</p> -->
```

1. `<!-- Content -->`


