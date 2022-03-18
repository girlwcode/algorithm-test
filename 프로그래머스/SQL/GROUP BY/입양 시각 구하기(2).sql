/*
ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 
각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지,
각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
*/

-- 코드를 입력하세요
SELECT H.HOUR, IFNULL(C.COUNT, 0) AS COUNT -- COUNT가 NULL 인 경우, 0으로 대체
FROM
-- 우선, 0부터 23까지 있는 테이블 H 생성
(SELECT @N := @N +1 AS HOUR 
    FROM  ANIMAL_OUTS, (SELECT @N := -1 FROM DUAL) NN
    LIMIT 24) AS H
    
LEFT JOIN -- LEFT JOIN 진행
-- 원하는 검색 결과를 담은 테이블 C 생성
(SELECT HOUR(DATETIME) AS HOUR , COUNT(DATETIME) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR) AS C
    ON H.HOUR = C.HOUR
ORDER BY HOUR;