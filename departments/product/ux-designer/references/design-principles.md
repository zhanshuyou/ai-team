# Design Principles

## Core Principles

### 1. User-Centered Design
- Understand user needs before designing solutions
- Validate assumptions with user research
- Design for real use cases, not edge cases first

### 2. Visual Hierarchy
- Use size, color, and spacing to guide attention
- Primary actions should be visually prominent
- Group related elements together (Gestalt principles)

### 3. Consistency
- Use the same patterns for the same actions
- Maintain consistent spacing, typography, and color usage
- Follow platform conventions where appropriate

### 4. Accessibility (WCAG 2.1 AA)
- Color contrast ratio: minimum 4.5:1 for text
- All interactive elements must be keyboard accessible
- Provide text alternatives for non-text content
- Support screen readers with proper ARIA labels

## Layout Guidelines

- Use an 8px grid system
- Maximum content width: 1200px
- Minimum touch target size: 44x44px
- Responsive breakpoints: 320px, 768px, 1024px, 1440px

## Typography Scale

| Level | Size | Weight | Use Case |
|-------|------|--------|----------|
| H1 | 32px | Bold | Page titles |
| H2 | 24px | Semi-bold | Section headers |
| H3 | 20px | Semi-bold | Subsection headers |
| Body | 16px | Regular | Body text |
| Small | 14px | Regular | Captions, labels |
| Tiny | 12px | Regular | Helper text |

## Spacing Scale

4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px

## Interaction States

Every interactive element should define:
1. **Default** — Resting state
2. **Hover** — Mouse over (desktop)
3. **Focus** — Keyboard focus (visible outline)
4. **Active** — Being pressed
5. **Disabled** — Not available
6. **Loading** — Processing
7. **Error** — Invalid state
