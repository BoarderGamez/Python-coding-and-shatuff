// src/app/page.tsx

import Scene from '../components/Scene'
import Forecast from '../components/Forecast'
import Finance from '../components/Finance'


export default function Home() {
  return (
    <main className="min-h-screen p-6 bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Welcome to Your Dashboard</h1>
      <Scene />
      <Forecast />
      <Finance />
    </main>
  )
}
