import { useState, useEffect } from 'react'
import { getRepos, Repo } from '../api'

export default function RepoList() {
  const [repos, setRepos] = useState<Repo[]>([])
  const [error, setError] = useState('')

  useEffect(() => {
    getRepos()
      .then(setRepos)
      .catch(e => setError(e.message))
  }, [])

  if (error) return <div className="error">{error}</div>
  if (!repos.length) return <div>Loading repos...</div>

  return (
    <div className="repo-list">
      {repos.map(repo => (
        <div key={repo.full_name} className="repo-card">
          <div className="repo-name">
            {repo.private && <span className="badge">private</span>}
            {repo.full_name}
          </div>
          {repo.description && <div className="repo-desc">{repo.description}</div>}
          <div className="repo-meta">
            {repo.language && <span>{repo.language}</span>}
            <span>{new Date(repo.updated_at).toLocaleDateString()}</span>
          </div>
        </div>
      ))}
    </div>
  )
}
