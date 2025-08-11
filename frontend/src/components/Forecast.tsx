'use client'

import { useState } from 'react'
import { ForecastData } from '@/types'

const hourly: ForecastData[] = [
  { time: '12 AM', temperature: 50, condition: '100% Rain' },
  { time: 'Now', temperature: -50, condition: 'Freezing' },
]

const weekly: ForecastData[] = [
  { time: 'Mon', temperature: 45, condition: 'Cloudy' },
  { time: 'Tue', temperature: 48, condition: 'Sunny' },
  { time: 'Wed', temperature: 42, condition: 'Rain' },
]

export default function Forecast() {
  const [activeTab, setActiveTab] = useState<'hourly' | 'weekly'>('hourly')
  const data = activeTab === 'hourly' ? hourly : weekly

  return (
    <section className="mb-6 text-center">
      <h2 className="text-2xl font-bold mb-4">Forecast</h2>

      <div className="flex justify-center gap-4 mb-4">
        <button
          className={`px-4 py-2 rounded ${
            activeTab === 'hourly' ? 'bg-blue-500 text-white' : 'bg-gray-200'
          }`}
          onClick={() => setActiveTab('hourly')}
        >
          Hourly Forecast
        </button>
        <button
          className={`px-4 py-2 rounded ${
            activeTab === 'weekly' ? 'bg-blue-500 text-white' : 'bg-gray-200'
          }`}
          onClick={() => setActiveTab('weekly')}
        >
          Weekly Forecast
        </button>
      </div>

      <ul className="space-y-2">
        {data.map((item, index) => (
          <li key={index}>
            <strong>{item.time}</strong>: {item.temperature}° – {item.condition}
          </li>
        ))}
      </ul>
    </section>
  )
}
