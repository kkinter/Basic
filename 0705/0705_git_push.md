# 📌Git Push

## or create a new repository on the command line

```
echo "# MC" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/kkinter/MC.git
git push -u origin main
```

## or push an existing repository from the command line

```
git remote add origin https://github.com/kkinter/MC.git
git branch -M main
git push -u origin main
```



`git remote remove origin` | remote 제거

```bash
$ git remote -v
origin  https://github.com/kkinter (fetch)
origin  https://github.com/kkinter (push)

$ git remote remove origin

$ git remote -v
```



`git remote -v` | remote 확인

```bash
$ git remote -v
origin  https://github.com/kkinter (fetch)
origin  https://github.com/kkinter (push)

$ git remote -v
```



`git branch -M main` | ?

```bash
$ git branch -M main
```



`git remote add origin repository` | 경로 추가

```bash
$ git remote add origin https://github.com/kkinter/MC.git
```



`git push -u origin main` | push

```bash
$ git push -u origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 5.46 KiB | 2.73 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/kkinter/MC.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```



## 수정되거나, 삭제되었을 때

> 추가하기 전

`git status`

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   0705_markdown.md
        deleted:    "\353\247\210\355\201\254\353\213\244\354\232\264 \354\236\205\353\213\210\353\213\244.assets/image-20220705112533329.png"
        deleted:    "\353\247\210\355\201\254\353\213\244\354\232\264 \354\236\205\353\213\210\353\213\244.assets/image-20220705113052820.png"

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        0705_markdown.assets/

no changes added to commit (use "git add" and/or "git commit -a")
```



`git log`

```bash
$ git log
commit 9a6920fd79265924c7ec8dd9de0e9c2efa34dee3 (HEAD -> main, origin/main)
Author: wook <ifol1129@gmail.com>
Date:   Tue Jul 5 17:11:02 2022 +0900

    추가

commit 0dc7e2af9438ee197458aeecc9146cc3dbae84f5
Author: wook <ifol1129@gmail.com>
Date:   Tue Jul 5 16:29:52 2022 +0900

    0705_정리

```

> 추가한 후

```bash
$ git add .

$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   0705_git_push.md
        renamed:    "\353\247\210\355\201\254\353\213\244\354\232\264 \354\236\205\353\213\210\353\213\244.assets/image-20220705112533329.png" -> 0705_markdown.assets/image-20220705112533329.png
        renamed:    "\353\247\210\355\201\254\353\213\244\354\232\264 \354\236\205\353\213\210\353\213\244.assets/image-20220705113052820.png" -> 0705_markdown.assets/image-20220705113052820-16570088335791.png
        new file:   0705_markdown.assets/image-20220705113052820.png
        modified:   0705_markdown.md

$ git log
commit 9a6920fd79265924c7ec8dd9de0e9c2efa34dee3 (HEAD -> main, origin/main)
Author: wook <ifol1129@gmail.com>
Date:   Tue Jul 5 17:11:02 2022 +0900

    추가

commit 0dc7e2af9438ee197458aeecc9146cc3dbae84f5
Author: wook <ifol1129@gmail.com>
Date:   Tue Jul 5 16:29:52 2022 +0900

    0705_정리
        
```



```bash
$ git commit -m '추가2'
[main faaad76] 추가2
 5 files changed, 109 insertions(+), 5 deletions(-)
 rename "\353\247\210\355\201\254\353\213\244\354\232\264 \354\236\205\353\213\210\353\213\244.assets/image-20220705112533329.png" => 0705_markdown.assets/image-20220705112533329.png (100%)
 rename "\353\247\210\355\201\254\353\213\244\354\232\264 \354\236\205\353\213\210\353\213\244.assets/image-20220705113052820.png" => 0705_markdown.assets/image-20220705113052820-16570088335791.png (100%)
 create mode 100644 0705_markdown.assets/image-20220705113052820.png
```



```bash
$ git push -u origin main
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 12 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 60.48 KiB | 20.16 MiB/s, done.
Total 7 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/kkinter/MC.git
   9a6920f..faaad76  main -> main
branch 'main' set up to track 'origin/main'.

$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

$ git log
commit faaad76d3b2d467b3252b0338106b3e0083f00bf (HEAD -> main, origin/main)
Author: wook <ifol1129@gmail.com>
Date:   Tue Jul 5 17:25:44 2022 +0900

    추가2

commit 9a6920fd79265924c7ec8dd9de0e9c2efa34dee3
Author: wook <ifol1129@gmail.com>
Date:   Tue Jul 5 17:11:02 2022 +0900

    추가

commit 0dc7e2af9438ee197458aeecc9146cc3dbae84f5
Author: wook <ifol1129@gmail.com>
Date:   Tue Jul 5 16:29:52 2022 +0900

    0705_정리

```



## 삭제

`rm -rf .git`





 