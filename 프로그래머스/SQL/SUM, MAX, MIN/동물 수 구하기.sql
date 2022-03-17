/*
ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 
각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.
*/

-- 코드를 입력하세요
SELECT COUNT(ANIMAL_ID)
FROM ANIMAL_INS;

SELECT COUNT(*)
FROM ANIMAL_INS;
#이것도 맞는 코드 -> 더 reasonable함 (행의 갯수 구함. null 제외)