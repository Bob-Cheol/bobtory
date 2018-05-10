list_packages = c('RPostgreSQL', 'data.table', 'foreign', 'stringr', 'bit64', 'lubridate', 'foreach', 'doParallel', 'dplyr')	# 사용할 packages list
for(i in list_packages) {
  if(!length(which(installed.packages()[,1] == i))) {
    install.packages(i)
  }
  eval(parse(text=paste0("library(", i, ")")))
}
options(scipen=999)	# 숫자표기 길이 제한 해제

# create a connection
# save the password that we can "hide" it as best as we can by collapsing it

# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
dbCon = dbConnect(dbDriver("PostgreSQL"), dbname = "spwkdw", host = "spwk-dw.cicvuwhjlhxo.ap-northeast-2.rds.amazonaws.com", port = 5432, user = "root", password = Sys.getenv('AWS_PGS_PW'))

dbGetTable = function(text) {
  data = dbGetQuery(dbCon, text)
  for(i in 1:ncol(data)) { data[,i] = iconv(data[,i], 'UTF-8', 'EUC-KR') }
  return(data)
}

dbChange = function(text) {
  dbDisconnect(dbCon)
  for(i in 1:10) {
    tryCatch({
      dbCon = dbConnect(dbDriver("PostgreSQL"), dbname = text, host = "spwk-dw.cicvuwhjlhxo.ap-northeast-2.rds.amazonaws.com", port = 5432, user = "root", password = Sys.getenv('AWS_PGS_PW'))
      cat(text, '연결\n')
      return(dbCon)
      },
      error = function(e) cat('error(', i, ')'),
      warning = function(w) cat('warning(', i, ')')
    )
  }
  cat('\n연결실패\n')
  return(dbCon)
}

dbCurrent = function() {
  currentDB = dbGetQuery(dbCon, "select current_database()")[1,1]
  cat(paste0('current-DB : ', currentDB, '\n'))
}

dbList = function() {
  dbGetQuery(dbCon, "SELECT datname FROM pg_database WHERE datistemplate = false")
}

dbTableList = function() {
  dbGetQuery(dbCon, "SELECT table_catalog, table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
}

dbDescription = function() {
  browseURL('https://docs.google.com/spreadsheets/d/1uztusrcpc8_5nf6icbvERVhkkZNjEkk-LXV49vM3eto/edit#gid=0', browser = getOption('browser'))
}

db_help = function() {
  cat('# 접속중인 DB 확인하기
dbCurrent()

# DB List 확인하기
dbList()

# 활성 DB 바꾸기 _ 불편...
dbCon = dbChange("[DB name]")

# Table List 확인하기
dbTableList()

# EUC-KR로 인코딩해서 받기
dbGetTable("[Qeury 문]")

# SQL문 실행법 예시
dbGetQuery(dbCon, "[Qeury 문]")

# table 추가하기 _ table 수정이 가능하니 사용에 주의할 것
dbWriteTable(dbCon, "table이름", value = table_data, append = FALSE, row.names = FALSE) # overwrite = TRUE

# 서버의 DB 및 컬럼구성을 알고 싶으시면 "dbDescription()"을 입력하세요.\n')
}

cat('db 관련 도움말이 필요하시면 "db_help()" 를 입력하세요.\n')
