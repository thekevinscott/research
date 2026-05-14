import Select, { StylesConfig } from 'react-select'
import { Repo } from '../api'

interface RepoOption {
  value: string
  label: string
  repo: Repo
}

const darkStyles: StylesConfig<RepoOption> = {
  control: (base) => ({
    ...base,
    background: '#161b22',
    borderColor: '#30363d',
    '&:hover': { borderColor: '#58a6ff' },
    boxShadow: 'none',
  }),
  menu: (base) => ({
    ...base,
    background: '#161b22',
    border: '1px solid #30363d',
  }),
  option: (base, state) => ({
    ...base,
    background: state.isFocused ? '#1f2937' : 'transparent',
    color: '#e6edf3',
    '&:active': { background: '#253040' },
  }),
  singleValue: (base) => ({ ...base, color: '#e6edf3' }),
  input: (base) => ({ ...base, color: '#e6edf3' }),
  placeholder: (base) => ({ ...base, color: '#8b949e' }),
  indicatorSeparator: (base) => ({ ...base, background: '#30363d' }),
  dropdownIndicator: (base) => ({ ...base, color: '#8b949e' }),
}

interface Props {
  repos: Repo[]
  selected: Repo | null
  onSelect: (repo: Repo | null) => void
}

export default function RepoSelector({ repos, selected, onSelect }: Props) {
  const options: RepoOption[] = repos.map(r => ({
    value: r.full_name,
    label: r.full_name.split('/').pop()!,
    repo: r,
  }))

  const current = selected
    ? options.find(o => o.value === selected.full_name) ?? null
    : null

  return (
    <Select<RepoOption>
      styles={darkStyles}
      options={options}
      value={current}
      onChange={(opt) => onSelect(opt?.repo ?? null)}
      placeholder="Search repos..."
      isClearable
      formatOptionLabel={(opt) => (
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          {opt.repo.private && <span className="badge">private</span>}
          <span>{opt.label}</span>
          {opt.repo.language && (
            <span style={{ color: '#8b949e', fontSize: '0.8rem', marginLeft: 'auto' }}>
              {opt.repo.language}
            </span>
          )}
        </div>
      )}
    />
  )
}
