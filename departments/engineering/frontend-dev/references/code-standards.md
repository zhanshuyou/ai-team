# Frontend Code Standards

## Component Structure

```tsx
// 1. Imports (external → internal → types → styles)
import { useState } from 'react'
import { Button } from '@/components/ui'
import type { UserProps } from './types'

// 2. Type definitions
interface Props {
  name: string
  onSubmit: (value: string) => void
}

// 3. Component (named export preferred)
export function UserCard({ name, onSubmit }: Props) {
  // Hooks first
  const [value, setValue] = useState('')

  // Handlers
  const handleSubmit = () => {
    onSubmit(value)
  }

  // Render
  return (
    <div className="rounded-lg border p-4">
      <h2 className="text-lg font-semibold">{name}</h2>
      <button onClick={handleSubmit}>Submit</button>
    </div>
  )
}
```

## Rules

1. **No `any` types** — Use `unknown` if the type is truly unknown
2. **No inline styles** — Use Tailwind classes
3. **No magic numbers** — Extract constants
4. **No nested ternaries** — Use early returns or helper functions
5. **No barrel exports** unless needed — Import directly from the module

## State Management

- Local UI state → `useState` / `useReducer`
- Server state → React Query (`useQuery`, `useMutation`)
- Global client state → Zustand (keep stores small and focused)

## Error Handling

- Use Error Boundaries for component-level errors
- Use React Query's `onError` for API errors
- Always show user-friendly error messages

## Performance

- Use `React.memo` only when profiling shows a need
- Use `useMemo` / `useCallback` for expensive computations or stable references
- Lazy load routes with `React.lazy` + `Suspense`
- Avoid unnecessary re-renders by keeping state close to where it's used
