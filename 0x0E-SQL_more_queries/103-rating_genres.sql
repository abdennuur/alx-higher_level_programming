-- To List all genres in the database hbtn_0d_tvshows_rate by their rating.
-- The Records are ordered by descending rating.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS gi
       INNER JOIN `tv_show_genres` AS sa
       ON sa.`genre_id` = gi.`id`

       INNER JOIN `tv_show_ratings` AS ar
       ON ar.`show_id` = sa.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
