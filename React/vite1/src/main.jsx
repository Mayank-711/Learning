import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import names from './App'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <names />
  </StrictMode>,
)
