import { useState, useEffect, useCallback } from 'react'
import { getMe, getRepos, getIssues, listSessions, createSession, destroySession, GitHubUser, Repo, GitHubIssue, MachineSession } from './api'
import Login from './components/Login'
import RepoPanel from './components/RepoPanel'
import SessionPanel from './components/SessionPanel'
import ChatView from './components/ChatView'
import ResizeHandle from './components/ResizeHandle'

export default function App() {
  const [user, setUser] = useState<GitHubUser | null>(null)
  const [repos, setRepos] = useState<Repo[]>([])
  const [selectedRepo, setSelectedRepo] = useState<Repo | null>(null)
  const [sessions, setSessions] = useState<MachineSession[]>([])
  const [selectedSession, setSelectedSession] = useState<MachineSession | null>(null)
  const [issues, setIssues] = useState<GitHubIssue[]>([])
  const [loading, setLoading] = useState(true)

  const [repoWidth, setRepoWidth] = useState(220)
  const [sessionWidth, setSessionWidth] = useState(200)

  useEffect(() => {
    getMe()
      .then(u => {
        setUser(u)
        return getRepos()
      })
      .then(setRepos)
      .catch(() => setUser(null))
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    if (!user) return
    const fetchSessions = () => {
      listSessions().then(setSessions).catch(() => {})
    }
    fetchSessions()
    const interval = setInterval(fetchSessions, 5000)
    return () => clearInterval(interval)
  }, [user])

  const handleSelectRepo = (repo: Repo) => {
    setSelectedRepo(repo)
    setIssues([])
    const [owner, name] = repo.full_name.split('/')
    getIssues(owner, name).then(setIssues).catch(() => setIssues([]))
  }

  const handleNewSession = async () => {
    if (!selectedRepo) return
    try {
      const session = await createSession(selectedRepo.full_name)
      setSessions(prev => [session, ...prev])
      setSelectedSession(session)
    } catch (e) {
      console.error('Failed to create session:', e)
    }
  }

  const handleCloseSession = async (session: MachineSession) => {
    destroySession(session.id).catch(() => {})
    setSessions(prev => prev.filter(s => s.id !== session.id))
    if (selectedSession?.id === session.id) {
      setSelectedSession(null)
    }
  }

  const clamp = (val: number, min: number, max: number) => Math.max(min, Math.min(max, val))

  const resizeRepo = useCallback((delta: number) => {
    setRepoWidth(w => clamp(w + delta, 120, 400))
  }, [])

  const resizeSession = useCallback((delta: number) => {
    setSessionWidth(w => clamp(w + delta, 120, 400))
  }, [])

  if (loading) return <div className="loading-screen">waking up...</div>
  if (!user) return <div className="login-screen"><Login /></div>

  return (
    <div className="layout">
      <RepoPanel
        repos={repos}
        selected={selectedRepo}
        onSelect={handleSelectRepo}
        user={user}
        width={repoWidth}
      />
      <ResizeHandle onResize={resizeRepo} />
      <SessionPanel
        sessions={sessions}
        selected={selectedSession}
        onSelect={setSelectedSession}
        onNew={handleNewSession}
        onClose={handleCloseSession}
        repoSelected={!!selectedRepo}
        issues={issues}
        width={sessionWidth}
      />
      <ResizeHandle onResize={resizeSession} />
      <main className="main-pane">
        {selectedSession && selectedRepo ? (
          <ChatView repo={selectedRepo} session={selectedSession} />
        ) : (
          <div className="empty-state">
            <div className="empty-state-art">
{`   ___
  / o \\
 | ~~~ |
  \\___/`}
            </div>
            <p>{selectedRepo ? 'pick a session or start one' : 'pick a repo to begin'}</p>
          </div>
        )}
      </main>
    </div>
  )
}
