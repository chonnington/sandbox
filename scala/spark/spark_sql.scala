matchSummaryT.createOrReplaceTempView("match_desc")
missSummaryT.createOrReplaceTempView("miss_desc")
spark.sql("""SELECT a.field, a.count + b.count total, a.mean - b.mean delta
             FROM match_desc a INNER JOIN miss_desc b ON a.field = b.field
             WHERE a.field NOT IN ("id_1", "id_2")
             ORDER BY delta DESC, total DESC""").show()