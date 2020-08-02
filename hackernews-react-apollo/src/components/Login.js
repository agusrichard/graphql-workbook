import React, { useState } from 'react'

export default function Login(props) {
  const [isLogin, setIsLogin] = useState(true)
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')


  return (
    <form>
      <h3>{ isLogin ? 'Login' : 'Sign Up' }</h3>
      { isLogin && (
        <div>
          <label>Name</label>
          <input 
            type="text"
            placeholder="Name"
            value={name}
            onChange={event => setName(event.target.value)}
          />
        </div>
      ) }
      <div>
        <label>Email</label>
        <input 
          type="email"
          placeholder="Email"
          value={email}
          onChange={event => setEmail(event.target.value)}
        />
      </div>
      <div>
        <label>Password</label>
        <input 
          type="password"
          placeholder="Password"
          value={password}
          onChange={event => setPassword(event.target.value)}
        />
      </div>
      <button>{ isLogin ? 'Login' : 'Sign Up' }</button>
      <div>
        {
          isLogin ?
          <p onClick={() => setIsLogin(!isLogin)}>Need an account?</p>
          :
          <p onClick={() => setIsLogin(!isLogin)}>Already have an account?</p>
        }
      </div>
    </form>
  )
}