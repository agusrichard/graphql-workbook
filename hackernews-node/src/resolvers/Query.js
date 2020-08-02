function info() {
  return 'Welcome to our GraphQL API'
}

async function feed(parent, args, context, info) {
  return await context.prisma.link.findMany()
}

async function link(parent, args, context, info) {
  return await context.prisma.link.findOne({
    where: { id: args.id }
  })
}

module.exports = {
  info,
  feed,
  link
}