CREATE TABLE emp (
  empno INT,
  ename VARCHAR(30),
  job VARCHAR(30),
  sal INT
)

INSERT INTO emp
VALUES
(7902,'FORD','ANALYST',3000),
(7788,'SCOTT','ANALYST',3000),
(7369,'SMITH','CLERK',800),
(7900,'JAMES','CLERK',950),
(7876,'ADAMS','CLERK',1100),
(7934,'MILLER','CLERK',1300),
(7782,'CLARK','MANAGER',2450),
(7698,'BLAKE','MANAGER',2850),
(7566,'JONES','MANAGER',2975),
(7839,'KING','PRESIDENT',5000),
(7654,'MARTIN','SALESMAN',1250),
(7521,'WARD','SALESMAN',1250),
(7844,'TURNER','SALESMAN',1500),
(7499,'ALLEN','SALESMAN',1600);

SELECT *
      , sal
      , CASE WHEN job = 'ANALYST' THEN '분석가'
             WHEN job = 'MANAGER' THEN '매니저'
             WHEN job = 'PRESIDENT' THEN '대통령'
             WHEN job = 'SALESMAN' THEN '영업'
             WHEN job = 'CLERK' THEN '사무원'
        END AS [직업_이름]
      ,
        CASE WHEN sal >= 5000 THEN '1등급'
             WHEN sal >= 4000 THEN '2등급'
             WHEN sal >= 3000 THEN '3등급'
             WHEN sal >= 2000 THEN '4등급'
             ELSE '5등급'
        END AS [급여_등급]

    FROM emp;

