list_packages = c('RPostgreSQL', 'data.table', 'rlist', 'stringr', 'bit64', 'lubridate', 'foreach', 'dplyr')	# 사용할 packages list
for(i in list_packages) {
  if(!length(which(installed.packages()[,1] == i))) {
    install.packages(i)
  }
  eval(parse(text=paste0("suppressMessages(library(", i, "))")))
}
options(scipen=999)	# 숫자표기 길이 제한 해제

# create a connection
# save the password that we can "hide" it as best as we can by collapsing it

# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
dbCon = dbConnect(dbDriver("PostgreSQL"), dbname = "spwkdw", host = "spwk-dw.cicvuwhjlhxo.ap-northeast-2.rds.amazonaws.com", port = 5432, user = "root", password = Sys.getenv('AWS_PGS_PW'))

dbGetTable = function(text, data.table=FALSE) {
  data = dbGetQuery(dbCon, text)
  for(i in 1:ncol(data)) { data[,i] = iconv(data[,i], 'UTF-8', 'EUC-KR') }
  if(data.table) {
    return(data.table(data))
  }
  return(data)
}

dbSetTable = function(database=database_name, table=table_name, data=data, overwrite=FALSE, append=FALSE) {
  dbCon <<- dbChange(database)
  return(dbWriteTable(dbCon, table, data, row.names=FALSE, overwrite=overwrite, append=append))
}

dbChange = function(text) {
  dbDisconnect(dbCon)
  for(i in 1:10) {
    tryCatch({
      dbCon <<- dbConnect(dbDriver("PostgreSQL"), dbname = text, host = "spwk-dw.cicvuwhjlhxo.ap-northeast-2.rds.amazonaws.com", port = 5432, user = "root", password = Sys.getenv('AWS_PGS_PW'))
      cat(text, '연결\n')
      return(dbCon)
      },
      error = function(e) cat('error(', i, ') '),
      warning = function(w) cat('warning(', i, ') ')
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

dbAppendGoogleSheetList = function() {
  return()
}

dbUpdateGoogleSheet = function() {
  # dbChange('workspace')
  # sheet_url = dbGetTable('select * from googlesheet_url')
  sheet_url = data.frame(
    database = 'workspace',
    table = c('category_own', 'category_landuse_zone', 'category_bld_use', 'category_strc', 'category_jimok', 'data_rule'),
    url = c(
       'https://docs.google.com/spreadsheets/d/e/2PACX-1vReYPG62NNOt1O58SxycguyqzoaQf_irgbh6hkfgMphixRzpJJj2COPfKg1jR6UputSUiCstXoZ4f42/pub?gid=0&single=true&output=csv',
       'https://docs.google.com/spreadsheets/d/e/2PACX-1vSG92AzpS9yQNK45mRarjtTl8sSS6537y4MKgwlDu3it6VLw5ZYBhI_8C_p5hIBphveFK8gGVPvnT7d/pub?gid=0&single=true&output=csv',
       'https://docs.google.com/spreadsheets/d/e/2PACX-1vS8i0ebCOtCKa1WjqIllu6quzUfqHaiwbwkfUl5PMJPSjatpRC5TEWWwPQXxTdYOqBz-dPLd3PwFG6B/pub?gid=2012344268&single=true&output=csv',
       "https://docs.google.com/spreadsheets/d/e/2PACX-1vTmiRDkR-Me8d6exSjlgIXdVJ1ZvLBZ57ywuBuQTBen5tn1njB5aeuqeQClw7rrGMXD44SAFpcCiimo/pub?gid=0&single=true&output=csv",
       "https://docs.google.com/spreadsheets/d/e/2PACX-1vTvNbHtfbTm7-jmTFFNtGL1-0QSxFCir23TtyoxW75z1tqyBu9yrNHhljcZLWj4uzYXAVawU_oeVEYT/pub?gid=1693110064&single=true&output=csv",
       "https://docs.google.com/spreadsheets/d/e/2PACX-1vSOAqZJ-7MN1Q2JYI79gb-vribBwoCDjRIn24RtN7_tRgMcTk9Sw8Kq4EJ-syNlVaAl3JANdgXuySJE/pub?gid=0&single=true&output=csv"
    ),
    stringsAsFactors=FALSE
  )
  for(i in 1:nrow(sheet_url)) {
    sheet_data = read.csv(sheet_url$url[i], fileEncoding='UTF-8', colClasses='character')
    if(dbSetTable(sheet_url$database[i], sheet_url$table[i], sheet_data, overwrite=TRUE)) { # update함수이므로 항상 overwrite
      cat(paste0(sheet_url$table[i], ' is updated\n'))
    } else {
      cat(paste0(sheet_url$table[i], ' fails update\n'))
    }
  }
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
