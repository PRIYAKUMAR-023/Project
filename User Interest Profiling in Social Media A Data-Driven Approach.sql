create database project;
USE PROJECT;
Create table PRIYAPOST
(
POST_ID VARCHAR(50),
KIND_OF_POST VARCHAR(100),
TITLE VARCHAR(100),
POST_DATE DATE,
LIKSES_COUNT INT,
COMMENTS_COUNT INT
);
SELECT * FROM PRIYAPOST;
INSERT INTO PRIYAPOST VALUES('20001','PHOTO','FAMILY','2020/09/26',126,7);
INSERT INTO PRIYAPOST VALUES('20002','PHOTO','FAMILY','2020/09/27',136,1);
INSERT INTO PRIYAPOST VALUES('20003','PHOTO','SOLO','2020/10/30',129,0);
INSERT INTO PRIYAPOST VALUES('20004','PHOTO','FRIENDS','2021/04/02',125,12);
INSERT INTO PRIYAPOST VALUES('20005','PHOTO','FRIENDS','2021/04/02',135,2);
INSERT INTO PRIYAPOST VALUES('20006','PHOTO','SOLO','2021/07/17',153,26);
INSERT INTO PRIYAPOST VALUES('20007','PHOTO','FAMILY','2021/09/10',155,4);
INSERT INTO PRIYAPOST VALUES('21008','REEL','SOLO','2021/11/23',125,17);
INSERT INTO PRIYAPOST VALUES('21009','PHOTO','SOLO','2021/11/24',147,2);
INSERT INTO PRIYAPOST VALUES('21010','REEL','SOLO','2021/12/17',106,15);
INSERT INTO PRIYAPOST VALUES('21011','PHOTO','SOLO','2021/12/23',133,12);
INSERT INTO PRIYAPOST VALUES('22012','PHOTO','FAMILY','2022/01/17',147,2);
INSERT INTO PRIYAPOST VALUES('22013','PHOTO','FRIENDS','2022/03/05',136,11);
INSERT INTO PRIYAPOST VALUES('22014','PHOTO','SOLO','2022/04/07',131,8);
INSERT INTO PRIYAPOST VALUES('22015','REEL','FRIENDS','2022/04/10',115,3);
INSERT INTO PRIYAPOST VALUES('22016','VIDEO','FRIENDS','2022/04/29',116,3);
INSERT INTO PRIYAPOST VALUES('22017','PHOTO','FAMILY','2022/06/19',153,4);
INSERT INTO PRIYAPOST VALUES('22018','PHOTO','SOLO','2022/08/30',172,6);
INSERT INTO PRIYAPOST VALUES('22019','PHOTO','SOLO','2022/09/05',133,13);
INSERT INTO PRIYAPOST VALUES('22020','REEL','SOLO','2022/10/23',147,17);
INSERT INTO PRIYAPOST VALUES('22021','PHOTO','FRIENDS','2022/11/18',146,22);
INSERT INTO PRIYAPOST VALUES('22022','REEL','FRIENDS','2022/11/29',133,12);
INSERT INTO PRIYAPOST VALUES('22023','PHOTO','SOLO','2022/12/04',155,4);
INSERT INTO PRIYAPOST VALUES('23024','VIDEO','SOLO','2023/01/01',136,15);
INSERT INTO PRIYAPOST VALUES('23025','PHOTO','SOLO','2023/01/14',168,19);
INSERT INTO PRIYAPOST VALUES('23026','PHOTO','SOLO','2023/04/02',165,20);
INSERT INTO PRIYAPOST VALUES('23027','PHOTO','FRIENDS','2023/04/10',145,6);
INSERT INTO PRIYAPOST VALUES('23028','PHOTO','SOLO','2023/04/23',150,11);
INSERT INTO PRIYAPOST VALUES('23029','PHOTO','SOLO','2022/11/12',218,35);

-- 1. Post Type Distribution:
-- What is the distribution of post types in the PRIYAPOST table, and which type is most prevalent? 

SELECT KIND_OF_POST,
COUNT(KIND_OF_POST) AS POST_COUNT,
ROUND((COUNT(KIND_OF_POST)*100)/(SELECT COUNT(POST_ID)FROM PRIYAPOST),3)AS PERCENTAGE
FROM PRIYAPOST
GROUP BY KIND_OF_POST


-- 2. Popular Titles:
-- Which titles in the table have received the highest number of likes and comments?

SELECT * FROM PRIYAPOST 
WHERE(LIKES_COUNT,COMMENTS_COUNT)IN
(SELECT MAX(LIKES_COUNT)AS MAX_LIKES,
        MAX(COMMENTS_COUNT)AS MAX_COMMENTS FROM PRIYAPOST);
        
-- 3. Engagement Patterns Over Time:
-- How does the likes count vary over time for the given data? Are there specific dates with higher engagement?

SELECT POST_DATE, SUM(LIKES_COUNT) AS TOTAL_LIKES
FROM PRIYAPOST
GROUP BY POST_DATE
ORDER BY TOTAL_LIKES DESC;

-- 4.Most Engaging Post:
 -- Identify the post with the highest combined likes and comments. What type of post is it, and what is the title?

SELECT * FROM PRIYAPOST
ORDER BY (LIKES_COUNT + COMMENTS_COUNT) DESC
LIMIT 1;


-- 5.Post Type vs. Likes
-- Is there a correlation between the type of post and the number of likes it receives?

SELECT KIND_OF_POST, ROUND(AVG(LIKES_COUNT),2) AS AVERAGE_LIKES
FROM PRIYAPOST
GROUP BY KIND_OF_POST;

-- 6.Title Analysis for Likes:
-- Are there specific titles that consistently result in higher likes, and if so, what are they?

SELECT TITLE, ROUND(AVG(LIKES_COUNT)) AS AVERAGE_LIKES
FROM PRIYAPOST
GROUP BY TITLE
ORDER BY AVERAGE_LIKES DESC;

-- 7. Engagement Over Time by Post Type:
-- How does the engagement (likes and comments) evolve over time for each post type?

SELECT POST_DATE, KIND_OF_POST, 
SUM(LIKES_COUNT) AS TOTAL_LIKES, 
SUM(COMMENTS_COUNT) AS TOTAL_COMMENTS
FROM PRIYAPOST
GROUP BY POST_DATE, KIND_OF_POST
ORDER BY POST_DATE, KIND_OF_POST;

-- 8. Average Likes and Comments:
-- What are the average likes and comments counts for the posts in the table?

SELECT 
AVG(LIKES_COUNT) AS AVG_LIKES,
AVG(COMMENTS_COUNT)AS AVG_COMMENTS 
FROM PRIYAPOST;

-- 9.Most Commented Post:
-- Identify the post with the highest number of comments. What type of post is it, and what is the title?


SELECT  POST_ID, KIND_OF_POST, TITLE, COMMENTS_COUNT
FROM PRIYAPOST
ORDER BY COMMENTS_COUNT DESC
LIMIT 1;

-- 10. Post Type Preferences:
-- Based on the given data, is there a noticeable preference for a specific post type?

SELECT KIND_OF_POST, COUNT(*) AS POST_COUNT
FROM PRIYAPOST
GROUP BY KIND_OF_POST
ORDER BY POST_COUNT DESC;


-- 11.Engagement Trends by Title:
-- Are there specific titles that consistently lead to higher engagement trends over time?

SELECT TITLE, AVG(LIKES_COUNT) AS AVERAGE_LIKES, AVG(COMMENTS_COUNT) AS AVERAGE_COMMENTS
FROM PRIYAPOST
GROUP BY TITLE
ORDER BY AVERAGE_LIKES DESC, AVERAGE_COMMENTS DESC;





