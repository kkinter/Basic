# 📌Gitignore

## 🏷️버전 관리랑 상관 없는 파일 어떻게 관리해야 할까요?



`touch .gitignore` | .gitignore 파일 생성 

git에서 추적하지 않는 파일들을 기재한다.



VS Code 폴더 트리의 git logo로도 확인할 수 있음.

>  **항상 최상위 Directory에 존재해야 한다.**
>
> ```bash
> ## Ignore File ##
> 
> *.exe #모든 exe 파일 제외  * >> 와일드 카드
> secret/ # secret 폴더 제외
> secret.csv # secret.csv 만 제외
> ```

**`❗이미 커밋된 파일은 반드시 삭제를 해야 적용이 된다.`**

**`❗각 프로젝트마다 미리 gitignore를 설정하는 습관을 기르자. `**



## 🏷️개발환경이 다를 때, 필요한 사이트



[gitignore.io](http://gitignore.io)



## 🏷️와일드 카드

| **`*`**              | 문자 여러 개  |
| -------------------- | ------------- |
| `?**`**              | **문자 하나** |
| **`[abcde]`**        |               |
| **`[a-e]`**          |               |
| **`[!abcde]`**       |               |
| **`[!a-e]`**         |               |
| **`{debian,linux}`** |               |

