library(RSQLite)
library(Hmisc)

con <- dbConnect(SQLite(), "/home/ana/dev/talks/2013/distill/mysite_com/mysite.sqlite3")
png("plot.png", width=640, height=400)

### "query"
v <- fetch(dbSendQuery(con, "select * from polls_choice"))
dotchart(v$votes, labels=v$choice_text, pch=19, cex=1.5)
         

### "off"
dev.off()
