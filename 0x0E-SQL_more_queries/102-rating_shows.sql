-- To List all shows from hbtn_0d_tvshows_rate by their rating.
-- The Records are ordered by descending rating.
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS ti
       INNER JOIN `tv_show_ratings` AS ar
       ON ti.`id` = ar.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
