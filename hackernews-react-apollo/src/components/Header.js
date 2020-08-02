import React from 'react'
import { Link } from 'react-router-dom'
import { withRouter } from 'react-router'

function Header(props) {
  return (
    <div>
      <Link to="/">
        List
      </Link>
      <Link to="/create">
        Create
      </Link>
      <Link to="/auth">
        Login
      </Link>
    </div>
  )
}

export default withRouter(Header)