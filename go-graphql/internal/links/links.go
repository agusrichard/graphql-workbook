package links

import (
	"fmt"
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
		INSERT INTO Links(title, address, userid) VALUES ($1, $2, $3) RETURNING id;
	`, link.Title, link.Address, link.User.ID).Scan(&id)

	if err != nil {
		tx.Rollback()
	} else {
		tx.Commit()
	}

	return id, err
}

func GetAll() []Link {
	var links []Link
	rows, err := config.DB.Query(`
		SELECT
			l.id,
			l.title,
			l.address,
			l.userid,
			u.username,
			u.password
		FROM Links l
		JOIN Users u
		ON l.userid = u.id;
	`)

	if err != nil {
		fmt.Println("Error", err)
	} else {
		var link Link
		var userId int
		var username, password string
		defer rows.Close()
		for rows.Next() {
			err = rows.Scan(
				&(link.ID),
				&(link.Title),
				&(link.Address),
				&userId,
				&username,
				&password,
			)
			if err != nil {
				fmt.Println("Error", err)
			} else {
				links = append(links, Link{
					ID:      link.ID,
					Title:   link.Title,
					Address: link.Address,
					User: &users.User{
						Username: username,
						Password: password,
					},
				})
			}
		}
	}

	return links
}
