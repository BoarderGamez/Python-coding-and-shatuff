// src/types/index.ts

export interface ForecastData {
  time: string
  temperature: number
  condition: string
}

export interface FinanceData {
  name: string
  value: number
  change: number
}

export interface SceneData {
  imageUrl: string
  description: string
}
