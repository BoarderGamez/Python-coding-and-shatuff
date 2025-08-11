const BASE_URL = "http://localhost:8000"

export async function getFinance() {
  const res = await fetch(`${BASE_URL}/api/finance`)
  return res.json()
}
