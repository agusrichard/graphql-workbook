import React from 'react'
import { Link } from 'react-router-dom'
import { withRouter } from 'react-router'

function Header(props) {
  return (
    <div>
      <Link to="/">
        list
      </Link>
      <Link to="/create">
        create
      </Link>
    </div>
  )
}

export default withRouter(Header)