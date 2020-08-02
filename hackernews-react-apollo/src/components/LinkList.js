import React from 'react'
import Link from './Link'
import { gql } from 'apollo-boost'
import { Query } from 'react-apollo'

const FEED_QUERY = gql`
  {
    feed {
      links {
        id
        url
        description
      }
    }
  }
`

export default function LinkList(props) {

  return (
    <Query query={ FEED_QUERY }>
      {({ loading, error, data }) => {
        if (loading) return <div>Fetching...</div>
        if (error) return <div>Error...</div>

        console.log('data in LinkList', data)
        const linksToRender = data.feed.links

        return (
        <div>
          { linksToRender.map(link => <Link key={link.id} link={link}/>) }
        </div>)
      }}
    </Query>
  )
}