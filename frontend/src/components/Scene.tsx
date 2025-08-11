import Image from 'next/image'

export default function Scene() {
  return (
    <section className="mb-6 text-center">
      <h2 className="text-2xl font-bold mb-2">Aircraft Wing</h2>
      <p className="text-gray-600 mb-4">Deth</p>

      <div className="space-y-4">
        <Image
          src="/sky_with_wing.jpg"
          alt="Person standing on aircraft wing"
          width={800}
          height={500}
          className="rounded shadow mx-auto"
        />
        <Image
          src="/man-standing-wing-young-businessman-airplane-33016692.png"
          alt="Person sitting on aircraft wing"
          width={800}
          height={500}
          className="rounded shadow mx-auto"
        />
      </div>

      <p className="mt-4 text-gray-500">Quite Breezy, H: 50°, L: 30°</p>
    </section>
  )
}
