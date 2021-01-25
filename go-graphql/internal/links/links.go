package links

import (
	"go-graphql/config"
	"go-graphql/internal/users"
)

type Link struct {
	ID      string
	Title   string
	Address string
	User    *users.User
}

func (link Link) Save() (int, error) {
	var id int
	tx, err := config.DB.Begin()

	err = tx.QueryRow(`
		INSERT INTO Links(Title, Address) VALUES ($1, $2) RETURNING id;
	`, link.Title, link.Address).Scan(&id)

	if err != nil {
		tx.Rollback()
	} else {
		tx.Commit()
	}

	return id, err
}
