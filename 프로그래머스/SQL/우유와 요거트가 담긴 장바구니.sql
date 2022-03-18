/*
CART_PRODUCTS 테이블은 장바구니에 담긴 상품 정보를 담은 테이블입니다. CART_PRODUCTS 테이블의 구조는 다음과 같으며,
ID, CART_ID, NAME, PRICE는 각각 테이블의 아이디, 장바구니의 아이디, 상품 종류, 가격을 나타냅니다.

데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 
우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.
*/

-- 코드를 입력하세요
SELECT A.CART_ID
-- 우유를 산 장바구니 아이디 Unique 값 추출된 테이블 생성
FROM (SELECT DISTINCT CART_ID
     FROM CART_PRODUCTS
     WHERE NAME = "Milk"
     ) AS A
-- 요거트를 산 장바구니 아이디 Unique 값 추출된 테이블 생성 후, inner join으로 교집합만 추출
INNER JOIN (SELECT DISTINCT CART_ID
          FROM CART_PRODUCTS
          WHERE NAME = "Yogurt") AS B 
          ON A.CART_ID = B.CART_ID
ORDER BY A.CART_ID;