function info() {
  return 'Welcome to our GraphQL API'
}

async function feed(parent, args, context, info) {
  const where = args.filter ? {
    OR: [
      { description: { contains: args.filter} },
      { url: { contains: args.filter } }
    ]
  } : {}
  return await context.prisma.link.findMany({ where })
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