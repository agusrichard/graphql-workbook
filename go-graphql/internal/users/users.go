package users

import (
	"go-graphql/config"
	"log"

	"golang.org/x/crypto/bcrypt"
)

type User struct {
	ID       string `json:"id"`
	Username string `json:"username"`
	Password string `json:"password"`
}

func (user *User) Create() error {
	tx, err := config.DB.Begin()

	hashedPassword, err := HashPassword(user.Password)

	_, err = tx.Exec(`
		INSERT INTO Users(Username, Password) VALUES($1, $2);
	`, user.Username, hashedPassword)

	if err != nil {
		tx.Rollback()
	} else {
		tx.Commit()
	}

	return err
}

func HashPassword(password string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), 14)
	return string(bytes), err
}

func CheckPasswordHash(password, hash string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
	return err == nil
}

func GetUserIdByUsername(username string) (int, error) {
	var id int
	err := config.DB.QueryRow(`
		SELECT ID from Users WHERE username=$1
	`, username).Scan(&id)

	if err != nil {
		log.Fatal("Error get user id by username")
	}

	return id, nil
}

func (user *User) Authenticate() bool {
	var hashedPassword string
	err := config.DB.QueryRow(`
		SELECT Password from Users WHERE username=$1
	`, user.Username).Scan(&hashedPassword)

	if err != nil {
		log.Fatal("Error to authenticate user")
	}

	return CheckPasswordHash(user.Password, hashedPassword)
}
