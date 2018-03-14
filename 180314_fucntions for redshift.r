list_packages = c('RPostgreSQL', 'data.table', 'stringr', 'bit64')
for(i in list_packages) {
    if(!length(which(installed.packages()[,1] == i))) {
        install.packages(i)
    }
    eval(parse(text=paste0("library(", i, ")")))
}

# create a connection
# save the password that we can "hide" it as best as we can by collapsing it

# loads the  driver
drv = dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con = dbConnect(drv, dbname = "spwkdw", host = "spwk-dw.cyruu3sfzf7h.ap-northeast-2.redshift.amazonaws.com", port = 5439, user = "root", password = Sys.getenv('AWS_RDS_PW'))

db_help = function() {
    cat('# SQL문 실행법 예시
dbGetQuery(con, "Qeury 문")
dbGetQuery(con, "SELECT * FROM building_pyojebu WHERE sgg_cd LIKE \"11%\"")

# 전체 table 확인하기 ; 2가지 방법
dbGetQuery(con, "select * from pg_catalog.pg_tables")
dbGetQuery(con, "select * from information_schema.tables")

# 특정 table 확인하기
dbExistsTable(con, "building_floor") # TRUE : 있음 / FALSE : 없음

# table 추가하기 _ table 수정이 가능하니 사용에 주의할 것
dbWriteTable(con, "table이름", value = table_data, append = TRUE, row.names = FALSE) # overwrite = TRUE\n')
}

cat('db 관련 도움말이 필요하시면 "db_help()"" 를 입력하세요.\n')
