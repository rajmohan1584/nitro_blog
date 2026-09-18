import { useEffect, useState } from 'react'
import './App.css'

interface Post {
  id: number
  author: string
  title: string
  content: string
  date_posted: string
}

function App() {
  const [posts, setPosts] = useState<Post[]>([])
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch('/posts')
      .then((res) => res.json())
      .then((data) => setPosts(data.data))
      .catch(() => setError('Failed to load posts'))
  }, [])

  return (
    <>
      <h1>Nitro Blog</h1>
      {error && <p>{error}</p>}
      {posts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
          <p>
            <em>
              {post.author} &middot; {post.date_posted}
            </em>
          </p>
        </article>
      ))}
    </>
  )
}

export default App
