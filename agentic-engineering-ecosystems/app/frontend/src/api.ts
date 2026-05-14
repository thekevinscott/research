const BASE = ''

export async function fetchJSON<T>(path: string): Promise<T> {
  const res = await fetch(BASE + path, { credentials: 'include' })
  if (res.status === 401) throw new Error('unauthorized')
  if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`)
  return res.json()
}

export interface GitHubUser {
  login: string
  avatar_url: string
  name: string
}

export interface Repo {
  full_name: string
  description: string
  language: string
  updated_at: string
  private: boolean
  html_url: string
}

export function getMe(): Promise<GitHubUser> {
  return fetchJSON('/auth/me')
}

export function getRepos(): Promise<Repo[]> {
  return fetchJSON('/api/repos')
}
