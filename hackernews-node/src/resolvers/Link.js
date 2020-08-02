async function postedBy(parent, args, contex) {
  return context.prisma.link.findOne({
		where: { id: parent.Id }
	}).postedBy()
}

module.exports = { postedBy }