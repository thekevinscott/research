import { useState } from 'react'
import { Repo, GitHubUser } from '../api'

interface Props {
  repos: Repo[]
  selected: Repo | null
  onSelect: (repo: Repo) => void
  user: GitHubUser
  width: number
}

export default function RepoPanel({ repos, selected, onSelect, user, width }: Props) {
  const [filter, setFilter] = useState('')

  const filtered = repos.filter(r =>
    r.full_name.toLowerCase().includes(filter.toLowerCase())
  )

  return (
    <aside className="panel panel-repos" style={{ width }}>
      <div className="panel-header">
        <img src={user.avatar_url} alt="" width={20} height={20} />
        <span>{user.login}</span>
      </div>
      <input
        className="panel-search"
        type="text"
        placeholder="Search repos..."
        value={filter}
        onChange={e => setFilter(e.target.value)}
      />
      <div className="panel-list">
        {filtered.map(repo => (
          <div
            key={repo.full_name}
            className={`panel-item ${selected?.full_name === repo.full_name ? 'active' : ''}`}
            onClick={() => onSelect(repo)}
          >
            <span className="panel-item-name">
              {repo.full_name.split('/').pop()}
            </span>
            {repo.language && (
              <span className="panel-item-meta">{repo.language}</span>
            )}
          </div>
        ))}
      </div>
    </aside>
  )
}
