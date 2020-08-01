const { GraphQLServer } = require('graphql-yoga')
require('dotenv').config()

let links = [{
  id: 'link-0',
  url: 'www.howtographql.com',
  description: 'Fullstack tutorial for GraphQL'
}]

let idCount = links.length
const resolvers = {
  Query: {
    info: () => `This is the API of a Hackernews Clone`,
    feed: () => links,
    link: (parent, args) => {
      let found = links.filter(link => link.id === args.id)
      console.log('found', found)
      return found[0]
    }
  },
  Mutation: {
    post: (parent, args) => {
      const link = {
        url: args.url,
        description: args.description,
        id: `link-${idCount++}`
      }
      links.push(link)
      return link
    },
    updateLink: (parent, args) => {
      let found = links.filter(link => link.id === args.id)[0]
      found.url = args.url || found.url
      found.description = args.description || found.description
      return found
    },
    deleteLink: (parent, args) => {
      let others = links.filter(link => link.id !== args.id)
      return links.filter(link => link.id === args.id)[0]
    }
  }
}

const server = new GraphQLServer({
  typeDefs: './src/schema.graphql',
  resolvers
})
const port = process.env.PORT
server.start({ port }, () => console.log('Server is running on port 8000'))
