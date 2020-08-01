const { GraphQLServer } = require('graphql-yoga')
require('dotenv').config()

const typeDefs = `
type Query {
  info: String!
}
`

const resolvers = {
  Query: {
    info: () => `This is the API of a Hackernews Clone`
  }
}

const server = new GraphQLServer({
  typeDefs,
  resolvers
})
const port = process.env.PORT
server.start({ port }, () => console.log('Server is running on port 8000'))
