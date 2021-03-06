const { GraphQLServer, PubSub } = require('graphql-yoga')
const { PrismaClient } = require('@prisma/client')
const Query = require('./resolvers/Query')
const Mutation = require('./resolvers/Mutation')
const Subscription = require('./resolvers/Subscription')
const User = require('./resolvers/User')
const Link = require('./resolvers/Link')
const Vote = require('./resolvers/Vote')

require('dotenv').config()


const resolvers = {
  Query,
  Mutation,
  Subscription,
  User,
  Link,
  Vote
}

const prisma = new PrismaClient()
const pubsub = new PubSub()

const server = new GraphQLServer({
  typeDefs: './src/schema.graphql',
  resolvers,
  context: request => {
    return {
      ...request,
      prisma,
      pubsub
    }
  }
})
const port = process.env.PORT
server.start({ port }, () => console.log('Server is running on port 8000'))
