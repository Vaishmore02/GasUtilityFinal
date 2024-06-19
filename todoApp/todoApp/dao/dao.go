package dao

var (
	insertScript = `INSERT INTO my_keyspace.users (id,user_id, title, description, status, createdAt, updatedAt)
  VALUES ();`
)

func