-- To List all genres of the database hbtn_0d_tvshows
-- And not linked to the show Dexter.
-- The Records are sorted by ascending genre name.
SELECT DISTINCT `name`
  FROM `tv_genres` AS gi
       INNER JOIN `tv_show_genres` AS sa
       ON gi.`id` = sa.`genre_id`

       INNER JOIN `tv_shows` AS ti
       ON sa.`show_id` = ti.`id`
       WHERE gi.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS gi
	             INNER JOIN `tv_show_genres` AS sa
		     ON gi.`id` = sa.`genre_id`

		     INNER JOIN `tv_shows` AS ti
		     ON sa.`show_id` = ti.`id`
		     WHERE ti.`title` = "Dexter")
 ORDER BY gi.`name`;
