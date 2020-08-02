import React, { useState } from 'react'
import { gql } from 'apollo-boost'
import { Mutation } from 'react-apollo'

const POST_MUTATION = gql`
  mutation PostMutation($url: String!, $description: String!) {
    post(url: $url, description: $description) {
      id
      url
      description
    }
  }
`

export default function CreateLink(props) {
  const [url, setUrl] = useState('')
  const [description, setDescription] = useState('')

  const handleSubmit = (event, postMutation) => {
    event.preventDefault()
    console.log(url, description)
    postMutation()
    props.history.push('/')
  }

  return (
    <Mutation mutation={ POST_MUTATION } variables={{ url, description }}>
      { postMutation => (
        <form onSubmit={(event) => handleSubmit(event, postMutation)}>
          <div>
            <label>url: </label>
            <input 
              type="text" 
              placeholder="url"
              value={url}
              onChange={event => setUrl(event.target.value)}
            />
          </div>
          <div>
            <label>description: </label>
            <input 
              type="text" 
              placeholder="description"
              value={description}
              onChange={event => setDescription(event.target.value)}
            />
          </div>
          <button>Submit</button>
        </form>
      ) } 
    </Mutation>
  )
}