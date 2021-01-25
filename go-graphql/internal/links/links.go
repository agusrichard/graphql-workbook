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
		INSERT INTO Links(Title, Address) VALUES ($1, $2) RETURNING id;
	`, link.Title, link.Address).Scan(&id)

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
		SELECT id, title, address FROM Links;
	`)

	if err != nil {
		fmt.Println("Error", err)
	} else {
		var link Link
		defer rows.Close()
		for rows.Next() {
			err = rows.Scan(&(link.ID), &(link.Title), &(link.Address))
			if err != nil {
				fmt.Println("Error", err)
			} else {
				links = append(links, Link{
					ID:      link.ID,
					Title:   link.Title,
					Address: link.Address,
				})
			}
		}
	}

	return links
}
