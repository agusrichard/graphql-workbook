import React from 'react'

export default function Link(props) {
	console.log('Link props', props)
  return (
		<div>
			{ props.link.url } { props.link.description }
		</div>
	)
}