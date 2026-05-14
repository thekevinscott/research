import { useState, useEffect } from 'react'
import { getMe, GitHubUser } from './api'
import Login from './components/Login'
import RepoList from './components/RepoList'

export default function App() {
  const [user, setUser] = useState<GitHubUser | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getMe()
      .then(setUser)
      .catch(() => setUser(null))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <div className="container">Loading...</div>

  return (
    <div className="container">
      <header>
        <h1>Agent Sandbox</h1>
        {user && (
          <span className="user">
            <img src={user.avatar_url} alt="" width={24} height={24} />
            {user.login}
          </span>
        )}
      </header>
      {user ? <RepoList /> : <Login />}
    </div>
  )
}
