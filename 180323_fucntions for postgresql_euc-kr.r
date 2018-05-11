list_packages = c('RPostgreSQL', 'data.table', 'rlist', 'stringr', 'bit64', 'lubridate', 'foreach', 'dplyr')	# ����� packages list
for(i in list_packages) {
  if(!length(which(installed.packages()[,1] == i))) {
    install.packages(i)
  }
  eval(parse(text=paste0("library(", i, ")")))
}
options(scipen=999)	# ����ǥ�� ���� ���� ����

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
      cat(text, '����\n')
      return(dbCon)
      },
      error = function(e) cat('error(', i, ')'),
      warning = function(w) cat('warning(', i, ')')
    )
  }
  cat('\n�������\n')
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
  cat('# �������� DB Ȯ���ϱ�
dbCurrent()

# DB List Ȯ���ϱ�
dbList()

# Ȱ�� DB �ٲٱ� _ ����...
dbCon = dbChange("[DB name]")

# Table List Ȯ���ϱ�
dbTableList()

# EUC-KR�� ���ڵ��ؼ� �ޱ�
dbGetTable("[Qeury ��]")

# SQL�� ����� ����
dbGetQuery(dbCon, "[Qeury ��]")

# table �߰��ϱ� _ table ������ �����ϴ� ��뿡 ������ ��
dbWriteTable(dbCon, "table�̸�", value = table_data, append = FALSE, row.names = FALSE) # overwrite = TRUE

# ������ DB �� �÷������� �˰� �����ø� "dbDescription()"�� �Է��ϼ���.\n')
}

cat('db ���� ������ �ʿ��Ͻø� "db_help()" �� �Է��ϼ���.\n')
