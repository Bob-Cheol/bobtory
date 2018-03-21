list_packages = c('RPostgreSQL', 'data.table', 'stringr', 'bit64', 'aws.s3')
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

dbGetTable = function(text) {
    data = dbGetQuery(con, text)
    for(i in 1:ncol(data)) { data[,i] = iconv(data[,i], 'UTF-8', 'EUC-KR') }
    return(data)
}

dbDescription = function() {
    browseURL('https://docs.google.com/spreadsheets/d/1uztusrcpc8_5nf6icbvERVhkkZNjEkk-LXV49vM3eto/edit#gid=0', browser = getOption('browser'))
}

db_help = function() {
    cat('# SQL�� ����� ����
dbGetQuery(con, "Qeury ��")
dbGetQuery(con, "SELECT * FROM building_pyojebu WHERE sgg_cd LIKE \"11%\"")

# EUC-KR�� ���ڵ��ؼ� �ޱ�
dbGetTable("Qeury ��")

# ��ü table Ȯ���ϱ� ; 2���� ���
dbGetQuery(con, "select * from pg_catalog.pg_tables")
dbGetQuery(con, "select * from information_schema.tables")

# Ư�� table Ȯ���ϱ�
dbExistsTable(con, "building_floor") # TRUE : ���� / FALSE : ����

# table �߰��ϱ� _ table ������ �����ϴ� ��뿡 ������ ��
dbWriteTable(con, "table�̸�", value = table_data, append = TRUE, row.names = FALSE) # overwrite = TRUE

# ������ DB �� �÷������� �˰� �����ø� "dbDescription()"�� �Է��ϼ���.\n')
}

cat('db ���� ������ �ʿ��Ͻø� "db_help()"" �� �Է��ϼ���.\n')
