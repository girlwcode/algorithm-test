/*
ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 
각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
*/
-- 코드를 입력하세요
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC LIMIT 1;
# 근데 이건 ORDER BY 절로 푼 풀이라 좋지 않음.


-- 코드를 입력하세요
SELECT MAX(DATETIME)
FROM ANIMAL_INS;
# MAX 사용한 이 풀이가 나을 듯 -> 연산이 더 적음

