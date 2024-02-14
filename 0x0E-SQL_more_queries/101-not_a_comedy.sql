-- To Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- The Records are ordered by ascending show title.
SELECT DISTINCT `title`
  FROM `tv_shows` AS ti
       LEFT JOIN `tv_show_genres` AS sa
       ON sa.`show_id` = ti.`id`

       LEFT JOIN `tv_genres` AS gi
       ON gi.`id` = sa.`genre_id`
       WHERE ti.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS ti
	             INNER JOIN `tv_show_genres` AS sa
		     ON sa.`show_id` = ti.`id`

		     INNER JOIN `tv_genres` AS gi
		     ON gi.`id` = sa.`genre_id`
		     WHERE gi.`name` = "Comedy")
 ORDER BY `title`;
